import pandas as pd
import json
from pandas import json_normalize

# with open('data/orders.json', 'r') as file:
#     api_response = json.load(file)


# print(api_response)

# Pandas ka built-in flattener — nested keys ko '.' se join karta hai
# df = json_normalize(
#     api_response['orders'],
#     record_path='items',        # items list ko rows mein expand karo
#     meta=['order_id', 'total',  # ye fields har row mein repeat honge
#           ['customer', 'name'],
#           ['customer', 'city']],
#     meta_prefix='',
#     errors='ignore'
# )
# print(df)
