import datetime
import getpass
import json
import logging
import os
import random
import string
from os.path import expanduser, exists
import configparser
from threading import Lock
import boto3
import dateutil.parser
from moto import mock_sts

# Start mock STS for testing
mock_sts().start()
aws_config_data = {
    'default': {
        'region': 'us-east-1',
        'output': 'json'
    },
    'dev': {
        'region': 'us-west-2',
        'output': 'json',
        'mfa_serial': 'arn:aws:iam::123456789012:mfa/user'
    },
    'test': {
        'region': 'us-west-2',
        'output': 'json',
        'mfa_serial': 'arn:aws:iam::123456789012:mfa/user'
    },
    'admin': {
        'region': 'us-west-2',
        'output': 'json',
        'mfa_serial': 'arn:aws:iam::123456789012:mfa/user'
    }
}
class Environment:
    roles = ['dev', 'test', 'admin']

    def __init__(self, name='instatruck', region='Australia'):
        self.role = self.roles[0]
        self.name = name
        self.region = region

    @staticmethod
    def get_account_number():
        return '13579'

class Wrapper:
    _role_session_cache = {}
    _locks = {'all': Lock()}
    _console_available = True
    _profile_env_var = 'Wrapper_PROFILE'
    _cache_dir = '~/insterview/cache'

    @classmethod
    def get_session(cls, environment, duration_seconds=86400):
        with cls._lock_for_environment(environment):
            session = cls._get_cached_role_session(environment) or cls._get_user_session_from_disk_cache(environment)
            if session:
                return session
            if environment.role:
                session = cls._get_or_create_user_session(environment, duration_seconds)
                if session:
                    return cls._assume_role_if_needed(environment, session)
                else:
                    print("Error: User session creation failed.")
                    return None
            else:
                return boto3.Session(region_name=environment.region, profile_name=os.getenv(cls._profile_env_var, 'default'))

    @classmethod
    def _lock_for_environment(cls, environment):
        account_lock = cls._locks.setdefault(environment.get_account_number(), Lock())
        return account_lock

    @classmethod
    def _get_or_create_user_session(cls, environment, duration_seconds):
        session = cls._get_user_session_from_disk_cache(environment)
        if not session:
            session = cls._create_user_session(environment, duration_seconds)
        return session

    @classmethod
    def _create_user_session(cls, environment, duration_seconds):
        log = logging.getLogger(__name__)
        if not cls._console_available:
            raise Exception('Not authenticated to Wrapper. Run authenticate command.')
        log.debug(f'Creating user session for {environment.name}')
        mfa_serial = cls._get_mfa_serial()
        if mfa_serial:
            token = getpass.getpass('Enter MFA Token: ')
            sts_client = boto3.client('sts')
            response = sts_client.get_session_token(DurationSeconds=duration_seconds, SerialNumber=mfa_serial, TokenCode=token)
        else:
            log.debug('MFA serial not found, getting session without MFA')
            sts_client = boto3.client('sts')
            response = sts_client.get_session_token(DurationSeconds=duration_seconds)
        data = response['Credentials']
        data['Expiration'] = data['Expiration'].isoformat()
        cls._save_session_to_disk_cache(data)
        return cls._get_user_session_from_disk_cache(environment)

    @classmethod
    def _get_mfa_serial(cls):
        aws_profile = os.getenv(cls._profile_env_var)
        config_file = expanduser('~/.aws/config')
        config = configparser.ConfigParser()
        config.read(config_file)
        if aws_profile and config.has_section(f'profile {aws_profile}'):
            return config.get(f'profile {aws_profile}', 'mfa_serial', fallback=None)
        return None

    @classmethod
    def _assume_role_if_needed(cls, environment, session):
        if environment.role:
            return cls._get_session_for_assumed_role(environment, session)
        return session

    @classmethod
    def _get_session_for_assumed_role(cls, environment, session):
        log = logging.getLogger(__name__)
        role = environment.role
        role_arn = f'arn:aws:iam::{environment.get_account_number()}:role/{role}'
        log.info(f'Assuming role {role_arn}')
        sts_client = session.client('sts')
        response = sts_client.assume_role(RoleArn=role_arn, RoleSessionName=''.join(random.choices(string.ascii_uppercase + string.digits, k=8)))
        data = response['Credentials']
        assumed_session = boto3.Session(aws_access_key_id=data['AccessKeyId'], aws_secret_access_key=data['SecretAccessKey'], aws_session_token=data['SessionToken'], region_name=environment.region)
        cls._role_session_cache[environment.get_account_number()] = (assumed_session, data)
        return assumed_session

    @classmethod
    def _get_cached_role_session(cls, environment):
        session_info = cls._role_session_cache.get(environment.get_account_number())
        if session_info:
            session, data = session_info
            expiration = dateutil.parser.parse(data['Expiration'])
            if expiration > datetime.datetime.now(datetime.timezone.utc):
                return session
        return None

    @classmethod
    def _get_user_session_from_disk_cache(cls, environment):
        file_name = cls._get_cached_token_file_name()
        if not exists(file_name):
            return None
        with open(file_name, 'r') as token_file:
            data = json.load(token_file)
        expiration = dateutil.parser.parse(data['Expiration'])
        if expiration <= datetime.datetime.now(datetime.timezone.utc):
            return None
        return boto3.Session(aws_access_key_id=data['AccessKeyId'], aws_secret_access_key=data['SecretAccessKey'], aws_session_token=data['SessionToken'], region_name=environment.region)

    @classmethod
    def _save_session_to_disk_cache(cls, session_data):
        file_name = cls._get_cached_token_file_name()
        with open(file_name, 'w') as token_file:
            json.dump(session_data, token_file)

    @staticmethod
    def _get_cached_token_file_name():
        profile = os.getenv("Wrapper_PROFILE", 'default')
        file_name = f'cached-session-token-{profile}.json'
        directory = expanduser(Wrapper._cache_dir)
        os.makedirs(directory, exist_ok=True)
        return os.path.join(directory, file_name)

if __name__ == "__main__":
    env = Environment()
    session1 = Wrapper.get_session(env)
    session2 = Wrapper.get_session(env)
    print(session1, session2)
    assert session1.get_credentials().token == session2.get_credentials().token
    # Additional tests and validations
