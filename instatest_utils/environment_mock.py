class EnvironmentMock():
    roles = ['dev', 'test', 'admin']

    def __init__(self, name='instatruck', region='Australia'):
        # Defaults to name=instatruck and region=Australia unless specified
        self._role = EnvironmentMock.get_roles()[0]
        self._name = name

        # public property
        self.region = region

    @staticmethod
    def get_account_number():
        return '13579'

    def get_name(self):
        return self._name

    @staticmethod
    def get_roles():
        return EnvironmentMock.roles

    def get_role(self):
        return self._role

    def set_role(self, role):
        self._role = role
