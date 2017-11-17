import unittest
from time import sleep

from YunluFramework.public.common.Connect import Connect
from YunluFramework.public.common.publicfunction import Tools
from YunluFramework.config.globalparam import GlobalParam
from YunluFramework.public.handle.space.SPACEHANDLE5 import SPACEHANDLE5
from YunluFramework.public.handle.login.LOGINHANDLE2 import LOGINHANDLE2
from YunluFramework.testcase.空间.协会空间.test5_2加会员_个人_个人_拒绝.AddPerVip import AddPerVip
from YunluFramework.testcase.登录.test1_1登录.LoginA import LoginA
from YunluFramework.testcase.登录.test2_1退出登录.LoginoutA import LoginoutA
from YunluFramework.public.common.datainfo import DataInfo
from YunluFramework.public.common.log import Log
import ddt

from YunluFramework.testcase.登录.test2_1退出登录.Loginout002_1 import Loginout