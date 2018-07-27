import unittest
from YunluFramework.public.common.log import Log
from YunluFramework.public.common.datainfo import DataInfo
from YunluFramework.public.common.datainfo import DataMysql
from time import sleep
import ddt
from YunluFramework.public.common.Connect import Connect
from YunluFramework.public.common.publicfunction import Tools
from YunluFramework.config.globalparam import GlobalParam
from YunluFramework.public.handle.space.SPACEHANDLE5 import SPACEHANDLE5
from YunluFramework.testcase.空间.common.Space import CommonSpace
from YunluFramework.public.handle.setting.SETTINGHANDLE4 import SETTINGHANDLE4
from YunluFramework.public.handle.login.LOGINHANDLE2 import LOGINHANDLE2
from YunluFramework.testcase.登录.test1_1登录.LoginA import LoginA
from YunluFramework.public.handle.yunshi.YUNSHIHANDLE1 import YUNSHIHANDLE1