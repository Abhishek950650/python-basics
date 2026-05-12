import pandas as pd

data = [
['Rahul','IT',40000],
['Ankit','HR',50000],
['Neha','IT',60000],
['Pooja','HR',55000],
['Rohit','IT',45000]
]


df = pd.DataFrame(data, columns=['Name', 'Department', 'Salary'])

# print(df)

# print(df[:3])
# print(df['Salary'])
# print(df[df['Salary'] > 50000])
# df['Bonous'] = df['Salary'] * 0.1

# print(df.isnull().sum())

# print(df.head(3))
# print(df.info())
# print(df.tail(1))
# print(df.describe)

# print(df.isnull().sum().sort_values(ascending=False))
# print(df.dropna())
# print(df.fillna(0))

# print(df.isnull())
# print(df['Age'].fillna(df['Age'].mean()))

# df['Age'] = df['Age'].fillna(df['Age'].mean())
# df['Age'] = df['Age'].fillna(df['Age'].mean(), inplace=True)
# print(df.groupby('Department')['Salary'].mean())
# print(df.groupby('Department')['Salary'].max())

