__author__ = 'xiaoj'
from StoneUIFramework.public.common.basepage import Page

class _SETTINGPAGE1(Page):
    #设置:云视页面-设置
    def Setting1(self):
        self.SettingL1 = self.p.get_element("id->com.yunlu6.stone:id/iv_left","云视页设置")
        return self.SettingL1

    #设置:云库页面-设置
    def Setting2(self):
        self.SettingL2 = self.p.get_element("id->com.yunlu6.stone:id/iv_left_search_cloundlibrary","云库页设置")
        return self.SettingL2

    #设置:人脉页面-设置
    def Setting3(self):
        self.SettingL3 = self.p.get_element("id->com.yunlu6.stone:id/iv_left","人脉页设置")
        return self.SettingL3

    #设置:空间页面-设置
    def Setting4(self):
        self.SettingL4 = self.p.get_element("id->com.yunlu6.stone:id/clondzone_title_back","空间页设置")
        return self.SettingL4

    #设置:设置-头像
    def Setting_portrait(self):
        self.Setting_portraitL = self.p.get_element("id->com.yunlu6.stone:id/main_slid_userimg","设置-头像")
        return self.Setting_portraitL

    #设置:设置-基本资料
    def Setting_userinfo(self):
        self.Setting_userinfoL = self.p.get_element("id->com.yunlu6.stone:id/main_slid_ll_userinfo","设置-基本资料")
        return self.Setting_userinfoL

    #设置:设置-系统设置
    def Setting_system(self):
        self.Setting_systemL = self.p.get_element("id->com.yunlu6.stone:id/main_slid_ll_safe","设置-系统设置")
        return self.Setting_systemL

    #设置:设置-关于我们
    def Setting_aboutus(self):
        self.Setting_aboutusL = self.p.get_element("id->com.yunlu6.stone:id/main_slid_ll_aboutus","设置-关于我们")
        return self.Setting_aboutusL


















































