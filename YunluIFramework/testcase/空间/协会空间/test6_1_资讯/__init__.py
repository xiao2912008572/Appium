import unittest
from time import sleep

from YunluIFramework.public.common.Connect import Connect
from YunluIFramework.public.common.publicfunction import Tools
from YunluIFramework.config.globalparam import GlobalParam
from YunluIFramework.public.handle.space.SPACEHANDLE5 import SPACEHANDLE5
from YunluIFramework.testcase.空间.协会空间.test6_1_资讯.NewArchivies import NewArchivies
from YunluIFramework.testcase.空间.协会空间.test6_1_资讯.DeleteArchivies import DeleteArchivies
from YunluIFramework.public.common.datainfo import DataInfo
from YunluIFramework.public.common.log import Log
import ddt
