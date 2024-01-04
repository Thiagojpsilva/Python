# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    # setter
    def set_user(self, user):
        """_summary_

        Args:
            user (_type_): _description_
        """
        self.user = user

    def set_password(self, pwd):
        """_summary_

        Args:
            pwd (_type_): _description_
        """
        self.password = pwd

    @classmethod
    def create_with_auth(cls, user, password):
        """_summary_

        Args:
            user (_type_): _description_
            password (_type_): _description_

        Returns:
            _type_: _description_
        """
        con1 = cls()
        con1.user = user
        con1.password = password
        return con1

    @staticmethod
    def soma(x, y):
        return x + y


# c1=Connection()
c1 = Connection.create_with_auth('Thiago', '1234')
print(Connection.soma(1, 2))
# print(c1.user)
# c1.set_user('Thiago')
# c1.set_password('12345')
print(c1.user)
print(c1.password)
