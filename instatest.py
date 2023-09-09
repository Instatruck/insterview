import collections.abc
import shutil
import tempfile
import unittest

from moto import mock_sts

from instatest_utils.environment_mock import EnvironmentMock
from instatest_utils.wrapper import Wrapper

collections.Callable = collections.abc.Callable

_mock_sts = mock_sts()
_mock_sts.start()


class TestWrapper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a temporary directory for test cache files
        cls.temp_cache_dir = tempfile.mkdtemp()

    @classmethod
    def tearDownClass(cls):
        # Clean up the temporary directory
        shutil.rmtree(cls.temp_cache_dir)

    def setUp(self):
        # Initialize the environment with a unique name for each test
        self.test_env = EnvironmentMock()

    def test_get_session(self):
        # Test that two calls to get_session return the same credentials token
        session1 = Wrapper.get_session(self.test_env)
        session2 = Wrapper.get_session(self.test_env)
        self.assertEqual(session1.get_credentials().token,
                         session2.get_credentials().token)

    def test_get_session_with_mfa(self):
        session = Wrapper.get_session(self.test_env)
        self.assertIsNotNone(session)

    def test_save_session_to_disk_cache(self):
        # Test saving a session to the disk cache and then reading it back
        session_data = {
            'AccessKeyId': 'test_access_key',
            'SecretAccessKey': 'test_secret_key',
            'SessionToken': 'test_session_token',
            'Expiration': '2030-01-01T00:00:00Z',
        }
        Wrapper._save_session_to_disk_cache(session_data)
        loaded_session = Wrapper._get_user_session_from_disk_cache(
            self.test_env)
        self.assertIsNotNone(loaded_session)
        self.assertEqual(
            loaded_session.get_credentials().access_key, 'test_access_key')
        self.assertEqual(
            loaded_session.get_credentials().secret_key, 'test_secret_key')
        self.assertEqual(loaded_session.get_credentials().token,
                         'test_session_token')

    def test_get_user_role(self):
        # Test setting and getting the user's role
        role_to_set = 'test_role'
        Wrapper._save_user_role(self.test_env, role_to_set)
        retrieved_role = Wrapper._get_user_role(self.test_env)
        self.assertEqual(retrieved_role, role_to_set)



if __name__ == "__main__":
    unittest.main()
