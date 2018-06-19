import json

from instatest import EnvironmentMock,Wrapper
import pytest
import boto3
from moto import mock_s3
import hashlib
import os
import logging
#Utility file hash
#https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
def md5_file_hash(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class TestWrapper():

#    @classmethod
#    def setup_test(cls):
#        cls.env = EnvironmentMock()


    def test_get_session(cls):
        env = EnvironmentMock()
        s1 = Wrapper.get_session(env)
        assert s1.__class__ ==  boto3.session.Session
        assert s1.profile_name == 'default'
        assert s1.get_credentials().access_key != ''
        #todo: Write some tests to stress locking


    def test_get_mfa_serial(cls):
        logging.warn("Skipping TEST_GET_MFA_SERIAL, because it assumes working AWS Setip")
        assert True==False #For now.


    def test_get_user_session(cls):
        env = EnvironmentMock()
        s1= Wrapper._get_user_session(env,3600)
        assert s1.__class__ == boto3.session.Session
        assert s1.profile_name == 'default'
        assert s1.get_credentials().token != ''


    def test_get_session_for_assumed_role(cls):
        env = EnvironmentMock()
        s1 = Wrapper.get_session(env)
        s2 = Wrapper._get_session_for_assumed_role(env,s1,'dev')
        assert s2.__class__ == boto3.session.Session
        assert s2.profile_name == 'default'
        assert s2.get_credentials().token != ''



    def test_get_cached_role_session(cls):
        env = EnvironmentMock()
        s1 = Wrapper._get_cached_role_session(env)

        assert s1.__class__ == boto3.session.Session
        assert s1.profile_name == 'default'
        assert s1.get_credentials().token != ''


    def test_get_user_session_from_disk_cache(cls):
        return
        env = EnvironmentMock()
        s1 = Wrapper.get_session(env)
        s2 = Wrapper._get_user_session_from_disk_cache(env)
        assert s1 == s2

    def test_save_session_from_disk_cache(cls):
        env = EnvironmentMock()
        s1 = Wrapper.get_session(env)
        c1 = s1.get_credentials()
        json_c1 = json.dumps(Wrapper._response)
        hash1 = hashlib.md5(json_c1.encode('utf8')).hexdigest()
        Wrapper._save_session_to_disk_cache(Wrapper._response)

        fn = Wrapper._get_cached_token_file_name()
        hash2 = md5_file_hash(fn)
        assert hash1 == hash2

    def test_get_cached_token_file_name(cls):
        env = EnvironmentMock()
        s1 = Wrapper.get_session(env)
        fn = Wrapper._get_cached_token_file_name()
        assert os.path.exists(fn)

    def test_set_user_role(cls):
        env = EnvironmentMock()
        s1 = Wrapper.get_session(env)
        assert Wrapper._set_user_role(env,s1)

    def test_save_user_role(cls):
        env = EnvironmentMock()
        env.set_role('test')
        fn = os.path.expanduser('~/insterview/{}.role'.format(
            env.get_account_number()
        ))
        hash1 = hashlib.md5(env.get_role().encode('utf8')).hexdigest()
        Wrapper._save_user_role(env,env.get_role())
        hash2 = md5_file_hash(fn)
        assert hash1 == hash2

    def test_get_user_role(cls):
        env = EnvironmentMock()
        env.set_role('test2') #Yes I know this is invalid, but it should still work for the purposes of this test
        role1 = env.get_role()
        fn = os.path.expanduser('~/insterview/{}.role'.format(
            env.get_account_number()
        ))
        Wrapper._save_user_role(env, env.get_role())
        role2 = Wrapper._get_user_role(env)
        assert role1 == role2

if __name__ == "main":
    pass