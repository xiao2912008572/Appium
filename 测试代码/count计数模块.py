# Author:Xiaojingyuan
from collections import Counter
list1 = [1,2,1,3,4,4,3]
a = Counter(list1)
print(a)


# print(len(a))


for k,v in a.items():
    print(k,v)