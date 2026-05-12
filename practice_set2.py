import pandas as pd
from dataclasses import dataclass
from typing import List


def process_large_csv(file_path: str, chunk_size: int=1000):
    total_revenue = 0
    processed_rows = 0

    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        chunk['revenue'] = chunk['price'] * chunk['quantity']
        total_revenue += chunk['revenue'].sum()
        processed_rows += len(chunk)
        print(f'Processed {processed_rows} rows so far')
    
    print(f'\n Total rows {processed_rows}')
    print(f'Total Revenue in Rs: {total_revenue:.2f}')

@dataclass
class SalesRecord:
    """Data class — schema define karta hai"""
    order_id: str
    product: str
    price: float
    quantity: int
    city: str

def validate_and_load(file_path: str) -> List[SalesRecord]:
    """
    Schema validation ke saath CSV load karna.
    Production pipelines mein bad data ko early reject karte hain.
    """
    df = pd.read_csv(file_path)
    
    # Required columns check
    required_cols = {'order_id', 'product', 'price', 'quantity', 'city'}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
    # Type validation
    df['price'] = df['price'].astype(float)
    df['quantity'] = df['quantity'].astype(int)
    
    # Convert to dataclass objects
    records = [SalesRecord(**row) for row in df.to_dict('records')]
    print(f"✅ {len(records)} valid records loaded")
    return records

def load_huge_csv(file_path: str, chunk_size: int = 1000):
    # using chunk process to read 50GB of csv file 
    firstChunk = True
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        filtered_city = chunk[chunk['city'] == 'Delhi']
        filtered_city.to_csv('./data/filtered_city.csv', mode='a', header=firstChunk, index=False)
        print(f'chunks of csv data {len(chunk)}')

    print('Done')

# process_large_csv('./data/sales_data.csv')
# validate_and_load('./data/sales_data.csv')
load_huge_csv('./data/sales_data.csv') # large data 