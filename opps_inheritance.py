#implement inheritance
# parent class for common features
class BaseConnector: 
    def __init__(self, host: str, port: int, database: str):
        self.host = host
        self.port = port
        self.database = database
        self.connection = None
    
    def connect(self):
        return NotImplementedError('ye function child class implement karega')

    def disconnect(self):
        self.connection = None
        print(f'Disconnected from : {self.database}')
    
    def test_connection(self):
        print(f'Testing Connection to : {self.host}:{self.port}/{self.database}')
        return self.connection is not None
    
# specefic mySql Connection class
class MySqlConnector(BaseConnector):

    def __init__(self, host, port, database, username: str):
        super().__init__(host, port, database)
        self.username = username
    
    def connect(self):
        # conncetion for mysql.connect(...)
        self.connection = f'mysql://{self.username}@{self.host}:{self.port}/{self.database}'
        print(f'connect to database : {self.connection}')

# specefic postgres Connection class
class PostgressConnector(BaseConnector):

    def __init__(self, host, port, database, schema: str):
        super().__init__(host, port, database)
        self.schema = schema

    def connect(self):
        self.connection = f'postgres://{self.host}/{self.database}/{self.schema}'      
        print(f'connect to database : {self.connection}')
    

#use karo

mysql = MySqlConnector('localhost', 4200, 'orders_db', 'admin')

mysql.connect()
mysql.test_connection()

pssql = PostgressConnector('prod-server', 8100, 'warehouse', 'public')

pssql.connect()
pssql.test_connection()