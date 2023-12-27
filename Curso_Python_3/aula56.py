# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self,host='localhost'):
        self.host = host
        self.user = None
        self.password = None
        
    #setter    
    def set_user(self, user):
        self.user = user
    
    def set_password(self, pwd):
        self.password = pwd

    @classmethod
    def create_with_auth(cls,user,password):
        Connection = cls()
        Connection.user = user
        Connection.password = password
        return Connection
    
    @staticmethod
    def soma (x, y):
        return x + y

#c1=Connection()
c1 = Connection.create_with_auth('Thiago','1234')
print(Connection.soma(1,2))
#print(c1.user)
#c1.set_user('Thiago')
#c1.set_password('12345')
print(c1.user)
print(c1.password)          