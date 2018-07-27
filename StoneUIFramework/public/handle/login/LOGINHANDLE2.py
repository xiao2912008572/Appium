__author__ = 'xiaoj'
from StoneUIFramework.public.handle.login.LOGINHANDLE1 import LOGINHANDLE1

class LOGINHANDLE2(LOGINHANDLE1):
#******************************************************【PAGE1】登录Login******************************************************
    #定位:登录-返回
    def Login_back_click(self):
        return self.p.click(self.Login_back)

    #定位:登录-手机号
    def Login_phone_sendkeys(self,text):
        return self.p.send_keys(self.Login_phone,text)

    #定位:登录-密码
    def Login_password_sendkeys(self,text):
        return self.p.send_keys(self.Login_password,text)

    #定位:登录-登录按钮
    def Login_loginbtn_click(self):
        return self.p.click(self.Login_loginbtn)
























