__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.空间.私人空间.test1_1创建私人空间 import *


# 创建机构空间
class CreatePersonSpace:
    # 1.初始化
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)

    # 2.创建私人空间-公用方法
    def createPersonSpace(self, driver, spacename, clothesT, foodT, liveT, walkT, studyT,
                          healthT, socialT, workT, literatureT, entertainmentT,
                          beautyT, otherT, foldername1=None, foldername2=None, foldername3=None
                          ):  # 最多三个文件夹
        # 创建_SPACEHANDLE5公有定位控件对象
        space = SPACEHANDLE5(driver)
        sleep(1)
        try:
            self.log.info("------START:test1_1创建私人空间CreatePersonSpace.py------")
            # # #1.空间首页
            # #     space.Kjlb_click()
            # # 2.右上角主菜单
            # space.Kjlb_mainmenu_click()
            # self.log.info('点击右上角主菜单')
            # # 3.+私人空间
            # space.Kjlb_mainmenu_newpersonspace_click()
            # self.log.info('点击+私人空间')


            # 4.选择空间类型-检查类型和推荐名对应
            AllLabel = []  # 把各标签下的推荐列表，存到AllLabel列表里面
            for a in range(12):  # 循环12次
                space.Kjlb_mainmenu_newpersonspace_choosespacetype_click(a)  # 选择列表中第a个标签
                self.log.info('选择列表中的第{0}个标签'.format(a + 1))
                # sleep(1)
                # 把该标签下的推荐空间名存到一个列表中
                EveryLabel = []
                for i in space.Kjlb_mainmenu_newpersonspace_suggestspacenametag_get():
                    text = i.text
                    EveryLabel.append(text)
                AllLabel.append(EveryLabel)
                space.Kjlb_mainmenu_newpersonspace_changespacetype_click()  # 切换类型
            # print("AllLabel",AllLabel)
            # 4.1衣
            self.log.info("判断'衣'下的推荐标签")
            assert clothesT in AllLabel[0], "Clothes : The recommended name does not conform to type"
            # 4.2食
            self.log.info("判断'食'下的推荐标签")
            assert foodT in AllLabel[1], "Food : The recommended name does not conform to type"
            # 4.3住
            self.log.info("判断'住'下的推荐标签")
            assert liveT in AllLabel[2], "Live : The recommended name does not conform to type"
            # 4.4行
            self.log.info("判断'行'下的推荐标签")
            assert walkT in AllLabel[3], "Walk : The recommended name does not conform to type"
            # 4.5学习
            self.log.info("判断'学习'下的推荐标签")
            assert studyT in AllLabel[4], "StudyT : The recommended name does not conform to type"
            # 4.6健康
            self.log.info("判断'健康'下的推荐标签")
            assert healthT in AllLabel[5], "HealthT : The recommended name does not conform to type"
            # 4.7社交
            self.log.info("判断'社交'下的推荐标签")
            assert socialT in AllLabel[6], "Social : The recommended name does not conform to type"
            # 4.8工作
            self.log.info("判断'工作'下的推荐标签")
            assert workT in AllLabel[7], "Work : The recommended name does not conform to type"
            # 4.9文艺
            self.log.info("判断'文艺'下的推荐标签")
            assert literatureT in AllLabel[8], "LiteratureT : The recommended name does not conform to type"
            # 4.10娱乐
            self.log.info("判断'娱乐'下的推荐标签")
            assert entertainmentT in AllLabel[9], "Entertainment : The recommended name does not conform to type"
            # 4.11美护
            self.log.info("判断'美护'下的推荐标签")
            assert beautyT in AllLabel[10], "Beauty : The recommended name does not conform to type"
            # 4.12其它
            self.log.info("判断'其它'下的推荐标签")
            assert otherT in AllLabel[11], "Other : The recommended name does not conform to type"
            # 5.输入空间名称、文件夹名-保存
            space.Kjlb_mainmenu_newpersonspace_choosespacetype_click(0)  # 选择衣服类型空间
            self.log.info('选择衣服类型空间')
            space.Kjlb_mainmenu_newpersonspace_spacename_sendkeys(spacename)  # appium私人空间
            self.log.info('创建{0}空间'.format(spacename))
            space.Kjlb_mainmenu_newpersonspace_save_click()  # 保存
            self.log.info('点击保存')
            # 6.返回到空间列表
            space.Kjlb_mainmenu_newpersonspace_mainback_click()
            self.log.info('点击保存')
            self.log.info('------END:test1_1创建机构空间.CreatePersonSpace.py------')
        except Exception as err:
            self.log.error("CreatePersonSpace Inside : %s" % err)
            raise err
