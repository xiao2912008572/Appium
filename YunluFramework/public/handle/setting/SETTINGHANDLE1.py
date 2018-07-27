__author__ = 'xiaoj'
from YunluFramework.public.pages.setting.SETTINGPAGE4 import SETTINGPAGE4

class SETTINGHANDLE1(SETTINGPAGE4):
#******************************************************【HANDLE1】******************************************************
    #设置:云视页-设置
    def Setting_click1(self,n):
        if n == 1:
            return self.p.click(self.Setting1)    #云视
        if n ==2 :
            return self.p.click(self.Setting2)    #云库
        if n ==3 :
            return self.p.click(self.Setting3)    #人脉
        if n ==4 :
            return self.p.click(self.Setting4)    #空间

    #设置:设置-头像
    def Setting_portrait_click(self):
        return self.p.click(self.Setting_portrait)

    #设置:设置-基本资料
    def Setting_userinfo_click(self):
        return self.p.click(self.Setting_userinfo)

    #设置:设置-系统设置
    def Setting_system_click(self):
        return self.p.click(self.Setting_system)

     #设置:设置-关于我们
    def Setting_aboutus_click(self):
        return self.p.click(self.Setting_aboutus)