# Author:Xiaojingyuan
a = '3=[#len#list]'
print(a)
if '#len#' in a:
    print(111)
    b = a.replace('#len#','')
    print(b)