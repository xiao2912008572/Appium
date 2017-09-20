__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo

#创建机构空间
class CreatePersonSpace:
    def __init__(self):#初始化测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        #1.空间类型
        self.clothes = int(d.cell("test006-私人空间",2,1))#衣0
        self.food = int(d.cell("test006-私人空间",2,2))#食1
        self.live = int(d.cell("test006-私人空间",2,3))#住2
        self.walk = int(d.cell("test006-私人空间",2,4))#行3
        self.study = int(d.cell("test006-私人空间",2,5))#学习4
        self.health = int(d.cell("test006-私人空间",2,6))#健康5
        self.social = int(d.cell("test006-私人空间",2,7))#社交6
        self.work = int(d.cell("test006-私人空间",2,8))#工作7
        self.literature = int(d.cell("test006-私人空间",2,9))#文艺8
        self.entertainment = int(d.cell("test006-私人空间",2,10))#娱乐9
        self.beauty = int(d.cell("test006-私人空间",2,11))#美护10
        self.other = int(d.cell("test006-私人空间",2,12))#其它11
        #2.各空间类型下热门空间名第1个标签
        self.clothesT = (d.cell("test006-私人空间",3,1))#我的衣柜0
        self.foodT = (d.cell("test006-私人空间",3,2))#舌尖上的中国1
        self.liveT = (d.cell("test006-私人空间",3,3))#我爱我家2
        self.walkT = (d.cell("test006-私人空间",3,4))#旅游照片3
        self.studyT = (d.cell("test006-私人空间",3,5))#互联网十4
        self.healthT = (d.cell("test006-私人空间",3,6))#强身健体5
        self.socialT = (d.cell("test006-私人空间",3,7))#同学们6
        self.workT = (d.cell("test006-私人空间",3,8))#办公场所7
        self.literatureT = (d.cell("test006-私人空间",3,9))#文娱空间8
        self.entertainmentT = (d.cell("test006-私人空间",3,10))#电影放映室9
        self.beautyT = (d.cell("test006-私人空间",3,11))#Onlyyou10
        self.otherT = (d.cell("test006-私人空间",3,12))#摄影11
    def createPersonSpace(self,driver,spacename,foldername1 = None,foldername2 = None,foldername3 = None):#最多三个文件夹
        #创建工具类
        tools = Tools(driver)#tools工具
        #创建_SPACEHANDLE5公有定位控件对象
        space = _SPACEHANDLE5(driver)
        sleep(1)
        try:
        # #1.空间首页
        #     space.Kjlb_click()
        #2.右上角主菜单
            space.Kjlb_mainmenu_click()
        #3.+私人空间
            space.Kjlb_mainmenu_newpersonspace_click()
        #4.选择空间类型-检查类型和推荐名对应
            AllLabel = []#把各标签下的推荐列表，存到AllLabel列表里面
            for a in range(12):#循环12次
                space.Kjlb_mainmenu_newpersonspace_choosespacetype_click(a)#选择列表中第a个标签
                # sleep(1)
                #把该标签下的推荐空间名存到一个列表中
                EveryLabel = []
                for i in space.Kjlb_mainmenu_newpersonspace_suggestspacenametag():
                    text = i.text
                    EveryLabel.append(text)
                AllLabel.append(EveryLabel)
                # print("A",A)
                space.Kjlb_mainmenu_newpersonspace_changespacetype_click()#切换类型
            # print("AllLabel",AllLabel)
            #4.1衣
            assert self.clothesT in AllLabel[0],"Clothes : The recommended name does not conform to type"
            #4.2食
            assert self.foodT in AllLabel[1],"Food : The recommended name does not conform to type"
            #4.3住
            assert self.liveT in AllLabel[2],"Live : The recommended name does not conform to type"
            #4.4行
            assert self.walkT in AllLabel[3],"Walk : The recommended name does not conform to type"
            #4.5学习
            assert self.studyT in AllLabel[4],"StudyT : The recommended name does not conform to type"
            #4.6健康
            assert self.healthT in AllLabel[5],"HealthT : The recommended name does not conform to type"
            #4.7社交
            assert self.socialT in AllLabel[6],"Social : The recommended name does not conform to type"
            #4.8工作
            assert self.workT in AllLabel[7],"Work : The recommended name does not conform to type"
            #4.9文艺
            assert self.literatureT in AllLabel[8],"LiteratureT : The recommended name does not conform to type"
            #4.10娱乐
            assert self.entertainmentT in AllLabel[9],"Entertainment : The recommended name does not conform to type"
            #4.11美护
            assert self.beautyT in AllLabel[10],"Beauty : The recommended name does not conform to type"
            #4.12其它
            assert self.otherT in AllLabel[11],"Other : The recommended name does not conform to type"
        #5.输入空间名称、文件夹名-保存
            space.Kjlb_mainmenu_newpersonspace_choosespacetype_click(0)#选择衣服类型空间
            space.Kjlb_mainmenu_newpersonspace_spacename_sendkeys(spacename)#appium私人空间
            # space.Kjlb_mainmenu_newpersonspace_foldername_sendkeys(foldername1)#appium文件夹
            space.Kjlb_mainmenu_newpersonspace_save_click()#保存
        #6.返回到空间列表
            space.Kjlb_mainmenu_newpersonspace_mainback_click()

            #临时方案,点击取消
            driver.find_element_by_id("com.yunlu6.stone:id/cloundviewbottom_cancle").click()

        except Exception as err:
            logging.error("Error Information CreatePersonSpace Inside : %s"%err)
            raise err