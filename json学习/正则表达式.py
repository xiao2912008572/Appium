import re
import json学习
'''
^  以某字符开头 例： ^a  以a开头的字符串
$  以某字符结尾 例： 3%  以3结尾的字符串
.  匹配任意字符
*  乘以0或多个
() 取括号中的东西      .*(b.*b).*
贪婪匹配： 从左边开始匹配，遇到最后一个匹配的，因为很贪婪
非贪婪匹配：从左边开始匹配 ，只匹配第一个遇到的，贪婪模式下会匹配到最后一个: ?
+  至少匹配一次
{2}     限定前面字符出现的次数
{2,}    最小两次
{2,5}   2-5次

'''

'''
1. |   :或
'''
# 待匹配字符串
line = "boobby123"
# 模式
regex_str = "((bobby|boobby)123)"
match_obj = re.match(regex_str, line)
# 模式匹配
if match_obj:
    print(match_obj.group(2))

'''
2. [] :匹配任意字符,进入中括号的字符，不再有特殊含义
'''
# 待匹配字符串
line = "boobby123"
# 模式
regex_str = "([abcd]oobby123)"
match_obj = re.match(regex_str, line)
# 模式匹配
if match_obj:
    print(match_obj.group(1))

line = '13027104206'
regex_str = '(1[3875][0-9]{9})'
match_obj = re.match(regex_str,line)
if match_obj:
    print(match_obj.group(1))