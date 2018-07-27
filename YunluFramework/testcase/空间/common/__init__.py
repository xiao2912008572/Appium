import unittest
from YunluFramework.public.common.log import Log
from YunluFramework.public.common.datainfo import DataInfo
from YunluFramework.public.common.datainfo import DataMysql
from time import sleep
import ddt
from YunluFramework.public.common.Connect import Connect
from YunluFramework.public.common.publicfunction import Tools
from YunluFramework.config.globalparam import GlobalParam
from YunluFramework.public.handle.space.SPACEHANDLE6 import SPACEHANDLE6
from YunluFramework.public.handle.login.LOGINHANDLE2 import LOGINHANDLE2
from YunluFramework.testcase.登录.test1_1登录.LoginA import LoginA
from YunluFramework.public.handle.space.SPACEHANDLE5 import SPACEHANDLE5