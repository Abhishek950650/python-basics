class CSVExtractor:
    def extract(self, path: str):
        import pandas as pd
        print(f'extract CSV from path : {path}')
        return pd.read_csv(path)
    
class JSONExtractor:
    def extract(self, path: str):
        import pandas as pd
        print(f'extract JSON from path : {path}')
        return pd.read_json(path)
    
class APIExtractor:
    def extract(self, path: str):
        import requests
        print(f'extract API from path : {path}')
        response = requests.get(path)
        return response.json()


extractors = [CSVExtractor(), JSONExtractor(), APIExtractor()]

sources = ["data/salary_data.csv", "data/orders.json", "https://api.example.com/data"]

for extracotr, source in zip(extractors, sources):
    data = extracotr.extract(source)
    print(data)
