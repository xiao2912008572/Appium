import unittest
from time import sleep
from YunluFramework.public.common.log import Log
from YunluFramework.testcase.登录.test1_1登录.LoginA import LoginA
from YunluFramework.public.common.Connect import Connect
from YunluFramework.public.common.publicfunction import Tools
from YunluFramework.config.globalparam import GlobalParam
from YunluFramework.public.handle.space.SPACEHANDLE5 import SPACEHANDLE5
from YunluFramework.public.handle.login.LOGINHANDLE2 import LOGINHANDLE2
from YunluFramework.testcase.空间.协会空间.test4_1会员_个人_移除.DeletePerVip import DeletePerVip
from YunluFramework.testcase.登录.test2_1退出登录.LoginoutA import LoginoutA
from YunluFramework.public.common.datainfo import DataInfo
import ddt
from YunluFramework.testcase.空间.common.AddPerVip import *
# from YunluFramework.testcase.登录.test2_1退出登录.Loginout002_1 import Loginout