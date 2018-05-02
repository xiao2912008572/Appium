import unittest
from time import sleep

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import SPACEHANDLE5
from StoneUIFramework.public.handle.login.LOGINHANDLE2 import LOGINHANDLE2
from StoneUIFramework.testcase.空间.协会空间.test5_4加会员_个人_个人_同意.AddPerVip import AddPerVip
from StoneUIFramework.testcase.空间.协会空间.test4_1会员_个人_移除.DeletePerVip import DeletePerVip
from StoneUIFramework.testcase.登录.test1_1登录.LoginA import LoginA
from StoneUIFramework.testcase.登录.test2_1退出登录.LoginoutA import LoginoutA
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log
import ddt

from StoneUIFramework.testcase.登录.test2_1退出登录.Loginout002_1 import Loginout