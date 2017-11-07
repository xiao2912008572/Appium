import unittest

# 以下导入各模块测试用例
# @机构空间-测试用例
from StoneUIFramework.testcase.空间.机构空间.test1_1创建机构空间.CreateOrgSpace001_1 import space_CreateO
from StoneUIFramework.testcase.空间.机构空间.test2_1上下架产品.CreateProduct002_1 import space_ProductO
from StoneUIFramework.testcase.空间.机构空间.test3_1团队人事任免.TeamAssignJob003_1 import team_AssignO
from StoneUIFramework.testcase.空间.机构空间.test4_1资讯.Archivies004_1 import space_ArchiviesO
from StoneUIFramework.testcase.空间.机构空间.test5_1编辑.BusinessCard005_1 import space_BusinessCardO

# @私人空间-测试用例
from StoneUIFramework.testcase.空间.私人空间.test1_1创建私人空间.CreatePersonSpace001_1 import perspace_CreateP
from StoneUIFramework.testcase.空间.私人空间.test2_1私人空间加文件夹.CreatePerSFolder002_1 import perspace_NewFloderP

# @协会空间-测试用例
from StoneUIFramework.testcase.空间.协会空间.test1_1创建协会空间.CreateAscSpace001_1 import ascspace_CreateA
from StoneUIFramework.testcase.空间.协会空间.test2_1编辑.Edit002_1 import space_EditA
from StoneUIFramework.testcase.空间.协会空间.test3_1团队人事任免.TeamAssignJob003_1 import team_AssignA
from StoneUIFramework.testcase.空间.协会空间.test5_1加会员_管理员_个人_拒绝.Add_AtoP_Refuse005_1 import AddAtoPRefuseA
from StoneUIFramework.testcase.空间.协会空间.test5_2加会员_个人_个人_拒绝.Add_PtoP_Refuse005_2 import AddPtoPRefuseA
from StoneUIFramework.testcase.空间.协会空间.test5_3加会员_管理员_个人_同意.Add_AtoP_Agree005_3 import AddAtoPAgreeA
from StoneUIFramework.testcase.空间.协会空间.test5_4加会员_个人_个人_同意.Add_PtoP_Agree005_4 import AddPtoPAgreeA
from StoneUIFramework.testcase.空间.协会空间.test5_5加会员_管理员_企业_拒绝.Add_AtoO_Refuse005_5 import AddAtoORefuseA
from StoneUIFramework.testcase.空间.协会空间.test5_6加会员_个人_企业_拒绝.Add_PtoO_Refuse005_6 import AddPtoORefuseA
from StoneUIFramework.testcase.空间.协会空间.test5_7加会员_管理员_企业_同意.Add_AtoO_Agree005_7 import AddAtoOAgreeA
from StoneUIFramework.testcase.空间.协会空间.test5_8加会员_个人_企业_同意.Add_PtoO_Agree005_8 import AddPtoOAgreeA
from StoneUIFramework.testcase.空间.协会空间.test6_1_资讯.Archivies006_1 import space_ArchiviesA

# @云库-测试用例
from StoneUIFramework.testcase.云库.test1_1上传图片.UploadPic001_1 import yunku_UploadPic
from StoneUIFramework.testcase.云库.test2_1编辑图片.EditPic002_1 import yunku_EditPic


class SuiteController():
    def __suiteLoader(self):
        suite1 = 1
        suite2 = 2
        self.suite = [suite1, suite2]
        return self.suite

    # def chooseSuite(self, index=None, all=None):
    #     # 1.跑全部测试用例
    #     if all == "ALL" and index == None:
    #         return unittest.TestSuite(self.__suiteLoader())
    #     # 2.跑指定的某个测试用例
    #     else:
    #         return self.__suiteLoader()[index - 1]

    def chooseSuite(self, index_F=None, index_S=None, all=None):
        # 1.跑全部测试用例
        if all == "ALL" and index_F == None and index_S == None:
            return print(self.__suiteLoader())
        # 2.跑指定的某个测试用例
        else:
            return print(self.__suiteLoader()[index_F-1:index_S])


if __name__ == "__main__":
    SC = SuiteController()
    suiteA = SC.chooseSuite(None,None, 'ALL')  # 所有用例
    # unittest.TextTestRunner(verbosity=2).run(suiteA)
