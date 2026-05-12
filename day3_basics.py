numbers = [10, 20, 30, 40, 50, 100, 99, 10, 30]
# character = ['10', '20', '30', '40', '50']

# print(numbers)
# print(character)

# largest = max(numbers)
# numbers.remove(largest)
# second_largest = max(numbers)
# print(second_largest)

# unique_arr = []
# for x in numbers:
#     if x not in unique_arr:
#         unique_arr.append(x)
# # or
# unique = set(numbers)
# print(unique, unique_arr)
# print(list(dict.fromkeys(numbers)))


# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]

# for x in list2:
#     list1.append(x)
# print(list1)
# honestly i don't know how to merge to list in javascript i know using concat or using rest operator in array

# lst = [[1,2],[3,4],[5,6]]

# flatten_arr = []

# for x in lst:
#     for y in x:
#         flatten_arr.append(y)

# flatten = [y for x in lst for y in x]

# print(flatten_arr)

word_freq = {
    "spam": 15,
    "offer": 8,
    "free": 22,
    "win": 5
}
# top_frequent_word = {}
# for (key, value) in word_freq.items():
#     # print(len(key))
#     lst_arr = []
#     for x in range(len(key)):
#         # print(key[x])
#         lst_arr.append(key[x])
#     # print(lst_arr)
#     # print(sorted(lst_arr))
#     for x in range(len(lst_arr)-1):
#         # print(lst_arr[x], lst_arr[x+1])
#         if(lst_arr[x] == lst_arr[x+1]):
#             # print(key)
#             top_frequent_word[key]=value
        

# print(top_frequent_word)

# arr = []
# obj = {}
# for (key, value) in word_freq.items():
#     arr.append(value)
#     obj[value] = key

# ind = sorted(arr)
# # print(ind[-1], ind[-2])
# lst = [obj[ind[-1]], obj[ind[-2]]]
# print(lst)