__author__ = 'xiaoj'
from StoneUIFramework.public.common.basepage import Page

class _LOGINPAGE1(Page):
    #定位:登录
    def Login(self):
        self.LoginL = self.p.get_element("id->com.yunlu6.stone:id/main_login","登录")
        return self.LoginL