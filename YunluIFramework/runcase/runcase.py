__author__ = 'xiaoj'
import unittest
import time
import sys

# sys.path.append("C:\\Users\\xiaoj\PycharmProjects\Appium")
sys.path.append("C:\Program Files (x86)\Jenkins\workspace\jenkins_github_test1\\")

# sys.path.append('/usr/local/StoneUIFramework')1
# sys.path.append("/usr/local/Appium")

from StoneUIFramework.public.common.HTMLTestRunner import HTMLTestRunner
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.common.sendmail import SendMail

# 以下导入各模块测试用例
# @机构空间-测试用例
from StoneUIFramework.testcase.空间.机构空间.test1_1创建机构空间.CreateOrgSpace001_1 import space_CreateO
from StoneUIFramework.testcase.空间.机构空间.test2_1上下架产品.CreateProduct002_1 import space_ProductO
from StoneUIFramework.testcase.空间.机构空间.test3_1团队人事任免.TeamAssignJob003_1 import team_AssignO
from StoneUIFramework.testcase.空间.机构空间.test4_1资讯.Archivies004_1 import space_ArchiviesO
from StoneUIFramework.testcase.空间.机构空间.test5_1企业名片.BusinessCard005_1 import space_BusinessCardO

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

# 控制用例跑的次数，死循环，可人工干预退出
if __name__ == '__main__':
    a = 1
    while a != 5:
        # a = a + 1
        suite = unittest.TestSuite()  # 创建一个测试集，把所有要跑的测试用例跑动起来

        # ----------------------------------【云库-测试用例】----------------------------------
        suite.addTest(yunku_UploadPic("test_uploadpic"))                      # 云库上传图片
        suite.addTest(yunku_EditPic("test_editpic"))                          # 云库编辑图片

        # suite.addTest(yunku_FenLei("test_fenlei"))#云库分类到产品库
        # suite.addTest(yunku_GongSi("test_gongsi"))#云库分类到公司档
        # suite.addTest(yunku_Edit("test_edit"))#云库编辑图片信息

        # ----------------------------------【人脉-测试用例】----------------------------------
        # suite.addTest(contact_Add("test_addContact"))                         #人脉添加
        # suite.addTest(contact_Browse("test_borwseContact"))                   #人脉浏览
        # suite.addTest(contact_Del("test_delContact"))                         #人脉删除——— 需要手动从黑名单中删除
        # suite.addTest(contact_Exc("test_excContact"))                         #人脉换名片
        # suite.addTest(contact_Label("test_labelContact"))                     #打标签

        # ----------------------------------【空间-测试用例】----------------------------------
        # @机构空间
        # suite.addTest(space_CreateO("test_spacecreate"))                     # test1_1 创建机构空间
        # suite.addTest(space_ProductO("test_spaceproduct"))                   # test2_1 上下架产品
        # suite.addTest(team_AssignO("test_teamassign"))                       # test3_1 团队认识任免
        # suite.addTest(space_ArchiviesO("test_archivies"))                    # test4_1 资讯发布
        # suite.addTest(space_BusinessCardO("test_businesscard"))              # test5_1 编辑企业名片

        # @私人空间
        # suite.addTest(perspace_CreateP("test_perspacecreate"))               #test1_1 创建私人空间
        # suite.addTest(perspace_NewFloderP("test_pernewfolder"))              #test1_2 创建私人空间文件夹

        # @协会空间
        # suite.addTest(ascspace_CreateA("test_ascspacecreate"))               #test1_1 创建协会空间
        # suite.addTest(space_EditA("test_edit"))                              #test2_1 编辑
        # suite.addTest(team_AssignA("test_teamassign"))                       #test3_1 团队人事任免
        # suite.addTest(AddAtoPRefuseA("test_addAtoPRefuse"))                  #test5_1 加会员_管理员_个人_拒绝
        # suite.addTest(AddPtoPRefuseA("test_addPtoPRefuse"))                  #test5_2 加会员_个人_个人_拒绝
        # suite.addTest(AddAtoPAgreeA("test_addAtoPAgree"))                    #test5_3 加会员_管理员_个人_同意
        # suite.addTest(AddPtoPAgreeA("test_addPtoPAgree"))                    #test5_4 加会员_个人_个人_同意
        # suite.addTest(AddAtoORefuseA("test_addAtoORefuse"))                  #test5_5 加会员_管理员_企业_拒绝
        # suite.addTest(AddPtoORefuseA("test_addPtoORefuse"))                  #test5_6 加会员_个人_企业_拒绝
        # suite.addTest(AddAtoOAgreeA("test_addAtoORefuse"))                   #test5_6 加会员_管理员_企业_同意
        # suite.addTest(AddPtoOAgreeA("test_addAtoOAgree"))                    #test5_6 加会员_管理员_企业_同意
        # suite.addTest(space_ArchiviesA("test_archivies"))                    #test6_1 资讯发布

        # ------------------------------测试报告----------------------------------
        cf = GlobalParam("config", "report.conf")
        path = cf.getParam("report", "path")  # 报告存储路径
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))  # 获取时间戳
        filename = path + timestr + ".html"  # 测试报告命名
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(
            stream=fp,
            title='测试结果',
            description='测试报告'
        )
        runner.run(suite)
        fp.close()  # 测试报告关闭
        # runner = unittest.TextTestRunner()
        # runner.run(suite)
        # 发送邮件
        time.sleep(5)
        sendMail = SendMail()
        sendMail.send()
        break
