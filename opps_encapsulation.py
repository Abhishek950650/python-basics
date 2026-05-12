class DataPipeline:
    
    def __init__(self, source:str, destination:str):
        #__init__ is a constructor ye object banate time execute hota hai

        self.source = source
        self.destination = destination
        self._status = 'idle' #private
        self.__secret = 'db_pass'#strictyly private

    def start(self):
        self._status = 'running'
        print(f'pipeline started status: {self.source} to destination: {self.destination}')

    def stop(self):
        self._status = 'stopped'
        print(f'pipeline stopped status: {self._status}')

    def get_status(self):
        return self._status

#object banao
pipeline = DataPipeline(
    source='mysql_orders',
    destination='data_warehouse'
)

# pipeline.start()
print(pipeline.get_status())

