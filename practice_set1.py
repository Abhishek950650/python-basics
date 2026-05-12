# print('hello');
import pandas as pd;
from sklearn.preprocessing import StandardScaler, MinMaxScaler

csv = pd.read_csv('./data/salary_data.csv')

# print(csv)

csv['Age'] = csv['Age'].fillna(csv['Age'].mean(), inplace=True)

csv['Gender'] = csv['Gender'].fillna(csv['Gender'].mode()[0], inplace=True)

csv['Education'] = csv['Education'].fillna(csv['Education'].mode()[0], inplace=True)

# print(csv.tail());

# Encoding
csv = pd.get_dummies(csv, columns=['Gender'], drop_first=True)


#ordinal encoding
education_map = {'School': 1, 'Graduate':2, 'Postgraduate':3}

csv['Education'] = csv['Education'].map(education_map)

#frequency encoding
city_freq =  csv['City'].value_counts()
# print(city_freq)
csv['City'] = csv['City'].map(city_freq)


#feature scaling apply standard scalar on Age, Experience
# ss = StandardScaler()
# csv[['Age', 'Experience']] = ss.fit_transform(csv[['Age', 'Experience']])


#minmax scalar
mm = MinMaxScaler()

csv[['Age', 'Experience']] = mm.fit_transform(csv[['Age', 'Experience']])
print(csv.head())