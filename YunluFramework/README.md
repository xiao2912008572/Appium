# 欢迎使用UI框架设计文档
@[云庐|UI自动化|python|appium]
**UI自动化** 本框架主要针对于安卓UI层面设计的，利用了python的简单、易用的特性，并且加入了appium最新版本的封装。
- **python** 需要使用者有良好的python基础，至少掌握类、对象、循环、判断、方法等基本语法，适当了解logging、mysql-connector、xlwt、xlrd、unittest等模块。
- **appium** 需要使用者掌握基本的Webdriver库方法，掌握UIAutomator等元素定位基本方法，掌握appium自带的例如点击、滑动、发送文本等方法。
- **unittest** python自带的单元测试框架，此处用它的目的在于加载测试用例。

----
[TOC]
##整体框架简介
整体框架结构如下：

    YunluFramework/
	|—— config/
	|   |—— connect.conf
	|	|—— globalparam.py
	|   |—— path_file.conf
	|   |—— report.conf
	|   |—— sqlserver.conf
	|
	|—— data/
	|   |—— login.xls
	|   |—— order.xls
	|   |—— space.xls
	|   |—— yunku.xls
	|
	|—— public/
	|	|—— common/
	|	|   |—— basepage.py
	|	|   |—— choosesuite.py
	|	|   |—— Connect.py
	|	|   |—— datainfo.py
	|	|   |—— HTMLTestRunner.py
	|	|   |—— HTMLTestRunner1.py
	|	|   |—— log.py
	|	|   |—— mytest.py
	|	|   |—— publicfunction.py
	|	|   |—— pyappium.py
	|	|   |—— readconfig.py
	|	|   |—— sendmail.py
	|   |
	|   |—— handle/
	|   |   |—— login/
	|   |   |    |—— LOGINHANDLE1.py
	|   |   |    |—— LOGINHANDLE2.py
	|   |   |
	|   |   |—— renmai/
	|   |   |    |—— RENMAIHANDLE1.py
	|   |   |    |—— RENMAIHANDLE2.py
	|   |   |    |—— RENMAIHANDLE3.py
	|   |   |    |—— RENMAIHANDLE4.py
	|   |   |    |—— RENMAIHANDLE5.py
	|   |   |    |—— RENMAIHANDLE6.py
	|   |   |    |—— RENMAIHANDLE7.py
	|   |   |
	|   |   |—— setting/
	|   |   |    |—— SETTINGHANDLE1.py
	|   |   |    |—— SETTINGHANDLE2.py
	|   |   |    |—— SETTINGHANDLE3.py
	|   |   |    |—— SETTINGHANDLE4.py
	|   |   |
	|   |   |—— space/
	|   |   |    |—— SPACEHANDLE1.py
	|   |   |    |—— SPACEHANDLE2.py
	|   |   |    |—— SPACEHANDLE3.py
	|   |   |    |—— SPACEHANDLE4.py
	|   |   |    |—— SPACEHANDLE5.py
	|   |   |    |—— SPACEHANDLE6.py
	|   |   |
	|   |   |—— yunku/
	|   |   |    |—— YUNKUHANDLE1.py
	|   |   |    |—— YUNKUHANDLE2.py
	|   |   |    |—— YUNKUHANDLE3.py
	|   |   |
	|   |   |—— yunshi/
	|   |        |—— YUNSHIHANDLE1.py
	|   |        |—— YUNSHIHANDLE2.py
	|   |        |—— YUNSHIHANDLE3.py
	|   |
	|   |—— pages/
	|       |—— login/
	|       |    |—— LOGINPAGE1.py
	|       |    |—— LOGINPAGE2.py
	|       |
	|       |—— renmai/
	|       |    |—— RENMAIPAGE1.py
	|       |    |—— RENMAIPAGE2.py
	|       |    |—— RENMAIPAGE3.py
	|       |    |—— RENMAIPAGE4.py
	|       |    |—— RENMAIPAGE5.py
	|       |    |—— RENMAIPAGE6.py
	|       |    |—— RENMAIPAGE7.py
	|       |
	|       |—— setting/
	|       |    |—— SETTINGPAGE1.py
	|       |    |—— SETTINGPAGE2.py
	|       |    |—— SETTINGPAGE3.py
	|       |    |—— SETTINGPAGE4.py
	|       |
	|       |—— space/
	|       |    |—— SPACEPAGE1.py
	|       |    |—— SPACEPAGE2.py
	|       |    |—— SPACEPAGE3.py
	|       |    |—— SPACEPAGE4.py
	|       |    |—— SPACEPAGE5.py
	|       |    |—— SPACEPAGE6.py
	|       |
	|       |—— yunku/
	|       |    |—— YUNKUPAGE1.py
	|       |    |—— YUNKUPAGE2.py
	|       |    |—— YUNKUPAGE3.py
	|       |
	|       |—— yunshi/
	|           |—— YUNSHIPAGE1.py
	|           |—— YUNSHIPAGE2.py
	|           |—— YUNSHIPAGE3.py
	|—— report
	|   |—— log
	|   |   |—— log.log
	|
	|


###1. config
>####--- connect.onf
> 连接信息配置文件，主要编写desired_cpas信息，格式如下：

```
desired_caps1 = {
        'platformName' : 'Android',
        'platformVersion' : '6.0.1',
        'appPackage' : 'com.yunlu6.yunlu',
        'appActivity' : '.WelcomeActivity',
        'deviceName' : 'ef8bde8a',
        'noReset':'True',
        'sessionOverride':'True',
        'unicodeKeyboard' : 'True',
        'resetKeyboard' : True
        }
```

>####--- globalparam.py
> 用于读取配置文件信息

```
import os
from YunluFramework_API.public.common.readconfig import Config


class GlobalParam():
    def __init__(self, folder, file):
# 获取当前文件夹的父目录绝对路径
        self.BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 获取config文件夹中的的path_file.conf文件————截图和日志配置文件路径
        self.file_path = os.path.join(self.BASE_DIR, folder, file)

   def getParam(self, path_Section, path_NO):
        # 创建读取配置文件的对象:
        cf1 = Config(self.file_path)
        path = cf1.get_PATH(path_Section, path_NO)

        # 将父目录和配置文件读取的相对路径拼接
        path = self.BASE_DIR + path
        return path
```

>#### --- path_flie.conf
>日志和截图文件的路径配置文件

```
[log]
logfile = /report/log/log.log

[login]
login_path_001_1 = /report/screenshot/login/login/test1_1/
login_path_001_2 = /report/screenshot/login/login/test1_2/
```

>#### --- report.conf
>测试报告的路径配置文件

```
[report]
path = /report/testreport/
```
>#### --- sqlserver.conf
>mysql数据库连接信息

```
[MYSQL]
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123456',
    'port': '3306',
    'database': 'YunluFramework',
    'charset': 'utf8'
    }
```

###2. data
>**注意：**data主要用于存放测试数据，依赖于excel文档存储，当前版本已经弃用该方式存储数据，改用mysql数据库存取数据了。

例如：
| phone1       | password1 |
| :--------:   | :--------:|
| 13027104206  | 12345678  |

###3. public
####--- common
>common主要用于存放一些共有方法，结构如下：
##### --- --- public