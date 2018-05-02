import datetime

'''
y = int(input('请输入4位数字的年份：'))  # 获取年份
m = int(input('请输入月份：'))  # 获取月份
d = int(input('请输入是哪一天：'))  # 获取“日”

targetDay = datetime.date(y, m, d)  # 将输入的日期格式化成标准的日期

print(targetDay)
print(datetime.date(targetDay.year-1,12,31))

print(targetDay - datetime.date(targetDay.year - 1, 12, 31))
'''

for month in range(1, 501):
    if month < 10:
        month = '00{}'.format(month)
    elif month>=10 and month<100:
        month = '0{}'.format(month)
    print(month)
