import hashlib


# def md5Encode(str):
#     m = hashlib.md5(str.encode("utf8"))
#     m.update(str)
#     return m.hexdigest()


# data = "123456"
# m = hashlib.md5(data.encode("utf8"))
# print(m.hexdigest())

AppId = '3BXiD9Fga5RtswdyrJSFQ3h3-gzGzoHsz'
AppKey = 'qXj3uIf46jB6zlcA1C4IrHSs'
masterKey = '71Rc2gx6qoLBM3geWOQUhLDD'
timestamp = '1517811616666'



time_master = timestamp + masterKey
print(time_master)

# data = "151781161666671Rc2gx6qoLBM3geWOQUhLDD"
# m = hashlib.md5(data.encode("utf8"))
# print(m)

m1= hashlib.md5(time_master.encode('utf8'))
print(m1.hexdigest())

