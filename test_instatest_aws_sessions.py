import pytest
from instatest_aws_sessions import Environment, Wrapper
@pytest.fixture
def environment():
    return Environment()

def test_get_session(environment):
    session1 = Wrapper.get_session(environment)
    session2 = Wrapper.get_session(environment)
    assert session1.get_credentials().token == session2.get_credentials().token

def test_get_session_with_role(environment):
    environment.role = 'dev'
    session1 = Wrapper.get_session(environment)
    session2 = Wrapper.get_session(environment)
    assert session1.get_credentials().token == session2.get_credentials().token

def test_get_session_with_mfa(environment):
    environment.role = 'admin'
    session1 = Wrapper.get_session(environment)
    session2 = Wrapper.get_session(environment)
    assert session1.get_credentials().token == session2.get_credentials().token

