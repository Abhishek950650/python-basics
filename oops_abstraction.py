from abc import ABC, abstractmethod

class DataLoader:

    @abstractmethod
    def validate(self, data) -> bool:
        pass

    @abstractmethod
    def load(self, data, destination: str):
        pass

    def run(self, data, destination: str):
        print('Starting load Process')
        if self.validate(data):
            self.load(data, destination)
            print('Data Sucessfully load !')
        else:
            print('Data no loaded !')


class WareHouseLoader(DataLoader):
    
    def validate(self, data):
        return len(data) > 0
    
    def load(self, data, destination: str):
        print(f'loading {len(data)} for records {destination}')

# loader = DataLoader() # it give TypeError abastract class directly use nhi hoti

loader = WareHouseLoader()

loader.run([1,2,3,4], 'sales_warehouse')
