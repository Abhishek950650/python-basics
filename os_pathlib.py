import os

# Current directory kahan ho?
# print(os.getcwd())
# /home/abhishek/projects

# Directory change karo
# os.chdir('/home/abhishek/data')

# Naya folder banao
# os.mkdir('output')              # ek folder
# os.makedirs('data/raw/2024')    # nested folders ek saath

# Folder ka content dekho
# print(os.listdir('.'))

# Folder/file exist karta hai?
# print(os.path.exists('data/sales.csv'))   # True/False
# print(os.path.isfile('data/sales.csv'))   # File hai?
# print(os.path.isdir('data/output'))       # Directory hai?


# File rename karo
# os.rename('data/sales_data.xlsx', 'data/new_sales_data.xlsx')

# File delete karo
# os.remove('data/temp_file.csv')

# Empty folder delete karo
# os.rmdir('empty_folder')

# File ka size dekho (bytes mein)
# size = os.path.getsize('data/sales_data.csv')
# print(f"File size: {size/1024:.2f} KB")

# Path join karo — Windows/Linux dono pe kaam karta hai
# path = os.path.join('pipeline','input' ,'sales_data.csv')
# print(path)
# Linux:   data/raw/sales.csv
# Windows: data\raw\sales.csv


# Environment variable set karo (current session ke liye)
# os.environ['DB_PASSWORD'] = 'mypassword'
# os.environ['API_KEY']     = 'abc123'

# Environment variable padhna
# db_password = os.environ.get('DB_PASSWORD')        # None agar nahi mila
# api_key     = os.environ['API_KEY']                # KeyError agar nahi mila

# print(db_password, api_key)
# Default value ke saath — production standard
# db_host = os.environ.get('DB_HOST', 'localhost')   # agar nahi mila toh 'localhost'
# db_port = int(os.environ.get('DB_PORT', '5432'))   # string → int convert karo

# print(f"Connecting to {db_host}:{db_port}")

import os

# Poora folder structure traverse karo
for root, dirs, files in os.walk('pipeline/'):
    print(f"📁 Folder: {root}")
    print(f"   Subfolders: {dirs}")
    print(f"   Files: {files}")

# Output:
# 📁 Folder: data/
#    Subfolders: ['raw', 'processed']
#    Files: ['readme.txt']
# 📁 Folder: data/raw
#    Subfolders: []
#    Files: ['sales.csv', 'orders.json']