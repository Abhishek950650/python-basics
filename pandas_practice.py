import pandas as pd

# Sample dirty data
df = pd.DataFrame({
    'order_id' : ['ORD001', 'ORD002', None,     'ORD004'],
    'customer' : ['Rahul',  'priya',  'AMIT',    ' Neha '],
    'city'     : ['Delhi',  'Mumbai', 'delhi',   None],
    'amount'   : [700,      None,     320,        -50],
    'phone'    : ['9876543210', '1234', '9999999999', '8888888888']
})

# 1. Null values check karo

# print(df.isnull().sum())

# 2. Null values handle karo

df['amount'] = df['amount'].fillna(round(df['amount'].mean(), 2), inplace=True) #mean se fill
df['city']= df['city'].fillna('Unknown', inplace=True) #default se fill
df.dropna(subset=['order_id'], inplace=True) #order_id null -> drop row

# print(df)
# 3. String clean karo

df['customer'] = df['customer'].str.strip() #spaces hatao
df['customer'] = df['customer'].str.title() #title case
df['city']     = df['city'].str.lower()   
# print(df)

# 4. Invalid values handle karo
df = df[df['amount'] > 0] #negative amount drop

# 5. Phone validation
df['valid_phone'] = df['phone'].str.len() == 10

# print(df)

# df['revenue'] = df['amount'] * df['quantity']
# df['tax'] = df['revenue'] * 0.18
# df['total'] = df['revenue'] + df['tax']

# print(df)

# Apply — custom function har row pe

def categroize_order(amount):
    if amount > 500:
        return 'High'
    elif amount > 200:
        return 'Mid'
    else:
        return 'Low'

df['category'] = df['amount'].apply(categroize_order)

# Lambda — short functions
df['city_upper'] =  df['city'].apply(lambda x: x.upper())

# print(df)

# City wise total revenue
city_revenue = df.groupby('city')['revenue'].sum()
# print(city_revenue)

# Multiple aggregations
summary = df.groupby('city').agg(
    total_revenue = ('revenue', 'sum'),
    avg_amount    = ('amount',  'mean'),
    order_count   = ('order_id','count'),
    max_amount    = ('amount',  'max')
).reset_index()

# print(summary)

# Orders DataFrame
orders = pd.DataFrame({
    'order_id'   : ['ORD001', 'ORD002', 'ORD003'],
    'customer_id': [1, 2, 1],
    'amount'     : [700, 150, 320]
})

# Customers DataFrame
customers = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'name'       : ['Rahul', 'Priya', 'Amit'],
    'city'       : ['Delhi', 'Mumbai', 'Pune']
})

# Inner Join — dono mein match ho
inner = pd.merge(orders, customers, on='customer_id', how='inner')

# Left Join — orders sab aayenge
left  = pd.merge(orders, customers, on='customer_id', how='left')

# Right Join — customers sab aayenge
right = pd.merge(orders, customers, on='customer_id', how='right')

# Outer Join — sab aayenge
outer = pd.merge(orders, customers, on='customer_id', how='outer')

print(inner)
#   order_id  customer_id  amount   name    city
# 0   ORD001            1     700  Rahul   Delhi
# 1   ORD003            1     320  Rahul   Delhi
# 2   ORD002            2     150  Priya  Mumbai