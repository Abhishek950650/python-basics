import numpy as np

list1 = [1,2,3,4,5]

# print(list1 * 2) # list repeat ho gya  # har element ko 2 se multiply NAHI kiya!

#numpy array 

numpy_arr = np.array(list1)

# print(numpy_arr * 2) # <- har element 2 se multiply ho gya

#Python list -> slow aur jyada memory
#NumPy Array -> C level par fast , kam memory, maths operations built in

#NumPy Basics

arr1 = np.array([1,2,3,4,5])  #1D array
arr2 = np.array([[1,2,3],[4,5,6]]) #2D array (matrix)
arr3 = np.zeros((3, 4))                        # 3x4 zeros
arr4 = np.ones((2, 3))                         # 2x3 ones
arr5 = np.arange(0, 10, 2)                     # [0,2,4,6,8]
arr6 = np.linspace(0, 1, 5)                   # [0, 0.25, 0.5, 0.75, 1.0]
arr7 = np.random.randint(0, 100, size=(3, 3)) # random integers

# Array info

# print(arr2.shape)    # (2, 3) — 2 rows, 3 columns
# print(arr2.ndim)     # 2 — dimensions
# print(arr2.dtype)    # int64 — data type
# print(arr2.size)     # 6 — total elements


prices    = np.array([100, 200, 300, 400, 500])
quantities= np.array([2, 3, 1, 5, 2])

revenue = prices * quantities
tax  =  revenue * 0.18
discounted = prices * 0.9
sum = revenue.sum()
# print(sum)

# Comparison
expensive = prices > 300                 # [False, False, False, True, True]
high_rev  = revenue[revenue > 500]       # filter — [600, 2000, 1000]

# print(expensive)
# print(high_rev)
# Math operations
# print(np.sum(revenue))                   # total
# print(np.mean(revenue))                  # average
# print(np.max(revenue))                   # maximum
# print(np.min(revenue))                   # minimum
# print(np.std(revenue))                   # standard deviation
# print(np.median(revenue))               # median


data = np.arange(10)

# print(data.shape)
matrix  = data.reshape(2,5)
print(matrix.shape)

#flatten 
# flat = matrix.flatten()
# flat = matrix.ravel()  # same but memory efficient

# print(flat)

a = np.array([1,2,3])
b = np.array([4,5,6])

vertical   = np.vstack([a, b])   # [[1,2,3],[4,5,6]]  — rows ke neeche
horizontal = np.hstack([a, b])   # [1,2,3,4,5,6]      — side by side
# print(horizontal)
# print(vertical)

arr = np.array([1, 2, 3])
arr2 = np.array([1, 2])
# result = arr + arr2

# print(result)

sales = np.array([
    [700, 500, 300],  # Delhi
    [150, 450, 200],  # Mumbai
    [320, 280, 600]   # Pune
])
# 1. Har city ka total revenue nikalo
# 2. Har month ka average nikalo

city_total = np.sum(sales, axis=1)
month_avg = np.average(sales, axis=0)

# print(f'city ka total revenue : {city_total }')
# print(f'month ka average : {month_avg}')

amounts = np.array([700, 150, 320, 890, 50])
# 500 se upar → 'High'
# 200 se upar → 'Medium'  
# baaki → 'Low'
# Hint: nested np.where use karo

data = np.where(amounts > 500 , 'High', np.where(amounts > 200, 'Medium', 'Low'))
print(data)