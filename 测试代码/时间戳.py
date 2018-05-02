# Author:Xiaojingyuan
import time
print(time.time())

t1 = time.time()
t1 = str(t1)
print(type(t1))

t1 = t1.replace('.','')
print(t1)
t1 = t1[0:13]
print(t1)

a = '1521010252351'
a = '1521013440934'

import leancloud
leancloud.init("3BXiD9Fga5RtswdyrJSFQ3h3-gzGzoHsz", master_key="71Rc2gx6qoLBM3geWOQUhLDD")

from leancloud import Message

me = Message()

messages = me.find_by_client(from_client='system',limit=1)
# messages = Message.find_by_conversation(conversation_id='8b3ab185492e461c1eb76b1998e5473b')
print(messages)