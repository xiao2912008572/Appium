# Author:Xiaojingyuan

from B import BBBB

x = BBBB()
x.b()

# flag =0
# for i in range(1,101):
#     for j in range(2,i):
#         # print('j =',j)
#         if i % j ==0:
#             flag = 1
#             break
#         else:
#             flag = 0
#     if flag==0 and i!=1:
#         print(i)


for i in range(1,4):
    print('i = ',i)
    for j in range(2,i):
        print('j = ',j)