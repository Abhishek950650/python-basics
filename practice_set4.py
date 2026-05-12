class FileProcessor:

    def __init__(self, file_path: str, file_type: str):
        self.file_path = file_path
        self.file_type = file_type
    

    def process(self):
        
        if self.file_type.lower() == 'csv':
            print(f'Proccessing CSV file : {self.file_path}')
        elif self.file_type.lower() == 'json':
            print(f'Process JSON file : {self.file_path}')
        else :
            print(f'Unknow file : {self.file_path}')


# processor =  FileProcessor('data/salary_data.csv', 'CSV')
# processor.process()
