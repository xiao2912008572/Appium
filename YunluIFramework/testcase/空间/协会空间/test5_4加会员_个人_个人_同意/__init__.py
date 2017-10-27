import unittest
from time import sleep

from YunluIFramework.public.common.Connect import Connect
from YunluIFramework.public.common.publicfunction import Tools
from YunluIFramework.config.globalparam import GlobalParam
from YunluIFramework.public.handle.space.SPACEHANDLE5 import SPACEHANDLE5
from YunluIFramework.public.handle.login.LOGINHANDLE2 import LOGINHANDLE2
from YunluIFramework.testcase.空间.协会空间.test5_4加会员_个人_个人_同意.AddPerVip import AddPerVip
from YunluIFramework.testcase.空间.协会空间.test4_1会员_个人_移除.DeletePerVip import DeletePerVip
from YunluIFramework.testcase.登录.test1_1登录.LoginA import LoginA
from YunluIFramework.testcase.登录.test2_1退出登录.LoginoutA import LoginoutA
from YunluIFramework.public.common.datainfo import DataInfo
from YunluIFramework.public.common.log import Log
import ddt

from YunluIFramework.testcase.登录.test2_1退出登录.Loginout002_1 import Loginout