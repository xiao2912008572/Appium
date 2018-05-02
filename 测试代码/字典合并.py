# Author:Xiaojingyuan
dict1 = {1: [1, 11, 111], 2: [2, 22, 222]}
dict2 = {3: [3, 33, 333], 4: [4, 44, 444]}
dict3 = {3: [3, 33, 333], 4: [4, 44, 444]}

dict4 = {**dict1,**dict2,**dict3}
print(dict4)
