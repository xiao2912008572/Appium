import unittest
from time import sleep
from YunluIFramework.testcase.登录.test1_1登录.LoginA import LoginA
from YunluIFramework.testcase.登录.test2_1退出登录.LoginoutA import LoginoutA
from YunluIFramework.public.common.datainfo import DataInfo
from YunluIFramework.public.common.log import Log
import ddt
from YunluIFramework.public.common.Connect import Connect
from YunluIFramework.public.common.publicfunction import Tools
from YunluIFramework.config.globalparam import GlobalParam
from YunluIFramework.public.handle.space.SPACEHANDLE5 import SPACEHANDLE5
from YunluIFramework.public.handle.login.LOGINHANDLE2 import LOGINHANDLE2
from YunluIFramework.testcase.空间.协会空间.test5_1加会员_管理员_个人_拒绝.AddPerVip import AddPerVip
