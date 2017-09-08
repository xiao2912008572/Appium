__author__ = 'xiaoj'
from StoneUIFramework.public.pages.login.LOGINPAGE1 import _LOGINPAGE1

class _LOGINPAGE2(_LOGINPAGE1):
#******************************************************【PAGE1】登录Login******************************************************
    #定位:登录-返回
    def Login_back(self):
        self.Login_backL = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","登录-返回")
        return self.Login_backL

    #定位:登录-手机号
    def Login_phone(self):
        self.Login_phoneL = self.p.get_element("id->com.yunlu6.stone:id/login_et_photo","登录-手机号")
        return self.Login_phoneL

    #定位:登录-密码
    def Login_password(self):
        self.Login_passwordL = self.p.get_element("id->com.yunlu6.stone:id/login_et_password","登录-密码")
        return self.Login_passwordL

    #定位:登录-登录按钮
    def Login_loginbtn(self):
        self.Login_loginbtnL = self.p.get_element("id->com.yunlu6.stone:id/login_btn","登录-密码")
        return self.Login_loginbtnL























