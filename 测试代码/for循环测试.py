# -*- coding: utf-8 -*-
# Author:Xiaojingyuan

for i in range(10):
    print(i)
    if i == 5:
        print('i = 5')
        assert i == 5, 'i 不等于5'

# a = input('输入数字A：')
# a = int(a)
# if a%3==0 and a%5==0:
#     print('找到了')

for i in "erqerq adf":
    print(i)
    print(id(i))