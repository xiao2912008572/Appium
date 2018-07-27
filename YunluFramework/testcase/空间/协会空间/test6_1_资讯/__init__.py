import unittest
from time import sleep

from YunluFramework.public.common.Connect import Connect
from YunluFramework.public.common.publicfunction import Tools
from YunluFramework.config.globalparam import GlobalParam
from YunluFramework.public.handle.space.SPACEHANDLE5 import SPACEHANDLE5
from YunluFramework.testcase.空间.协会空间.test6_1_资讯.NewArchivies import NewArchivies
from YunluFramework.testcase.空间.协会空间.test6_1_资讯.DeleteArchivies import DeleteArchivies
from YunluFramework.public.common.datainfo import DataInfo
from YunluFramework.public.common.log import Log
import ddt
