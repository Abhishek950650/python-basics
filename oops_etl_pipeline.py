# Scenario: Ek reusable ETL framework banao jisme Extract → Transform → Load sab OOP se handle ho.

from abc import ABC, abstractmethod
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')

class ETLPipeline:

    def __init__(self, pipeline_name: str):
        self.pipline_name = pipeline_name
        self.data = None
    
    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

    @abstractmethod
    def load(self, df: pd.DataFrame):
        pass

    # template method - order is fix, child nhi badal skta

    def run(self):
        # logging.info(f'Pipeline {self.pipeline_name} started')
        print(f'Pipeline {self.pipline_name} started')

        df = self.extract()
        # logging.info(f'Extracted {len(df)} rows')
        print(f'Extracted {len(df)} rows')

        df = self.transform(df)
        # logging.info(f'Transform. Shape : {df.shape}')
        print(f'Transform. Shape : {df.shape}')

        self.load(df)
        # logging.info(f'Pipeline {self.pipline_name} is Completed')
        print(f'Pipeline {self.pipline_name} is Completed')


# Concrete implementation — Sales pipeline
class SalesETLPipeline(ETLPipeline):

    def __init__(self, source_file: str, dest_file: str):
        super().__init__('Sales Daily Pipeline')
        self.source_file = source_file
        self.dest_file = dest_file
    
    def extract(self) -> pd.DataFrame:
        return pd.read_csv(self.source_file)
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df['revenue']    = df['price'] * df['quantity']
        df['city']       = df['city'].str.upper()
        df.dropna(inplace=True)
        return df

    def load(self, df: pd.DataFrame):
        df.to_parquet(self.dest_file, index=False)
        print(f'Saved to {self.dest_file}')



pipeline = SalesETLPipeline('/data/sales_data.csv', 'data/sales_processed.parquet')
pipeline.run()
        
    