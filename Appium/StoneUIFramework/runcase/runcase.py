__author__ = 'xiaoj'
import unittest
import time

import sys
sys.path.append("C:\\Users\\xiaoj\PycharmProjects\Appium")
# sys.path.append('/usr/local/StoneUIFramework')
# sys.path.append("/usr/local/Appium")

from StoneUIFramework.public.common.HTMLTestRunner import HTMLTestRunner
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.common.sendmail import SendMail

#以下导入各模块测试用例
from StoneUIFramework.testcase.空间.机构空间.test1_1创建机构空间.CreateOrgSpace001_1 import space_Create
from StoneUIFramework.testcase.空间.机构空间.test2_1上下架产品.CreateProduct002_1 import space_Product
from StoneUIFramework.testcase.空间.机构空间.test3_1团队人事任免.TeamAssignJob003_1 import team_Assign
from StoneUIFramework.testcase.空间.机构空间.test5_1企业名片.BusinessCard005_1 import space_BusinessCard
from StoneUIFramework.testcase.空间.私人空间.test1_1创建私人空间.CreatePersongSpace001_1 import perspace_Create
from StoneUIFramework.testcase.空间.私人空间.test2_1私人空间加文件夹.CreatePerSFolder002_1 import perspace_NewFloder

from StoneUIFramework.testcase.空间.协会空间.test1_1创建协会空间.CreateAscSpace001_1 import ascspace_Create
from StoneUIFramework.testcase.空间.协会空间.test2_1编辑.Edit002_1 import space_Edit
from StoneUIFramework.testcase.空间.协会空间.test3_1团队人事任免.TeamAssignJob003_1 import team_Assign
from StoneUIFramework.testcase.空间.协会空间.test5_1加会员_管理员_个人_拒绝.Add_AtoP_Refuse005_1 import AddAtoPRefuse
from StoneUIFramework.testcase.空间.协会空间.test5_2加会员_个人_个人_拒绝.Add_PtoP_Refuse005_2 import AddPtoPRefuse
from StoneUIFramework.testcase.空间.协会空间.test5_3加会员_管理员_个人_同意.Add_AtoP_Agree005_3 import AddAtoPAgree
from StoneUIFramework.testcase.空间.协会空间.test5_4加会员_个人_个人_同意.Add_PtoP_Agree005_4 import AddPtoPAgree
from StoneUIFramework.testcase.空间.协会空间.test5_5加会员_管理员_企业_拒绝.Add_AtoO_Refuse005_5 import AddAtoORefuse
from StoneUIFramework.testcase.空间.协会空间.test5_6加会员_个人_企业_拒绝.Add_PtoO_Refuse005_6 import AddPtoORefuse
from StoneUIFramework.testcase.空间.协会空间.test5_7加会员_管理员_企业_同意.Add_AtoO_Agree005_7 import AddAtoOAgree
from StoneUIFramework.testcase.空间.协会空间.test5_8加会员_个人_企业_同意.Add_PtoO_Agree005_8 import AddPtoOAgree
from StoneUIFramework.testcase.空间.协会空间.test6_1_资讯.Archivies006_1 import space_Archivies

#控制用例跑的次数，死循环，可人工干预退出
if __name__ == '__main__':
    a = 1
    while a != 5:
        # a = a + 1
        suite = unittest.TestSuite()#创建一个测试集，把所有要跑的测试用例跑动起来

        #----------------------------------【云库-测试用例】----------------------------------
        # suite.addTest(yunku_ShangChuan("test_shangchuan"))#云库上传
        # suite.addTest(yunku_ShangChuan("test_shangchuan"))#云库上传

        # suite.addTest(yunku_FenLei("test_fenlei"))#云库分类到产品库
        # suite.addTest(yunku_GongSi("test_gongsi"))#云库分类到公司档
        # suite.addTest(yunku_Edit("test_edit"))#云库编辑图片信息

        #----------------------------------【人脉-测试用例】----------------------------------
        # suite.addTest(contact_Add("test_addContact"))#人脉添加
        # suite.addTest(contact_Browse("test_borwseContact"))#人脉浏览
        # suite.addTest(contact_Del("test_delContact"))#人脉删除——— 需要手动从黑名单中删除
        # suite.addTest(contact_Exc("test_excContact"))#人脉换名片
        # suite.addTest(contact_Label("test_labelContact"))#打标签

        #----------------------------------【空间-测试用例】----------------------------------
        # @机构空间
        suite.addTest(space_Create("test_spacecreate"))                     #test1_1 创建机构空间
        # suite.addTest(space_Product("test_spaceproduct"))                   #test2_1 上下架产品
        # suite.addTest(team_Assign("test_teamassign"))                       #test3_1 团队认识任免

        # suite.addTest(space_Archivies("test_archivies"))                    #test4_1 资讯发布

        # suite.addTest(space_BusinessCard("test_businesscard"))              #test5_1 编辑企业名片

        # @私人空间
        # suite.addTest(perspace_Create("test_perspacecreate"))               #test1_1 创建私人空间
        # suite.addTest(perspace_NewFloder("test_pernewfolder"))              #test1_2 创建私人空间文件夹

        # @协会空间
        # suite.addTest(ascspace_Create("test_ascspacecreate"))               #test1_1 创建协会空间
        '''
        suite.addTest(space_Edit("test_edit"))                              #test2_1 编辑
        suite.addTest(team_Assign("test_teamassign"))                       #test3_1 团队人事任免
        suite.addTest(AddAtoPRefuse("test_addAtoPRefuse"))                  #test5_1 加会员_管理员_个人_拒绝
        suite.addTest(AddPtoPRefuse("test_addPtoPRefuse"))                  #test5_2 加会员_个人_个人_拒绝
        suite.addTest(AddAtoPAgree("test_addAtoPAgree"))                    #test5_3 加会员_管理员_个人_同意
        suite.addTest(AddPtoPAgree("test_addPtoPAgree"))                    #test5_4 加会员_个人_个人_同意
        suite.addTest(AddAtoORefuse("test_addAtoORefuse"))                  #test5_5 加会员_管理员_企业_拒绝
        suite.addTest(AddPtoORefuse("test_addPtoORefuse"))                  #test5_6 加会员_个人_企业_拒绝
        suite.addTest(AddAtoOAgree("test_addAtoORefuse"))                   #test5_6 加会员_管理员_企业_同意
        suite.addTest(AddPtoOAgree("test_addAtoOAgree"))                    #test5_6 加会员_管理员_企业_同意
        '''
        # suite.addTest(space_Archivies("test_archivies"))                    #test6_1 资讯发布

        #------------------------------测试报告----------------------------------
        cf = GlobalParam("config","report.conf")
        path = cf.getParam("report","path")#报告存储路径
        timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))#获取时间戳
        filename = path + timestr + ".html"#测试报告命名
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(
                    stream=fp,
                    title='测试结果',
                    description='测试报告'
                    )
        runner.run(suite)
        fp.close() #测试报告关闭
        # runner = unittest.TextTestRunner()
        # runner.run(suite)
        #发送邮件
        time.sleep(5)
        sendMail = SendMail()
        sendMail.send()
        break
