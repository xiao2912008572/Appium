__author__ = 'xiaoj'
from YunluIFramework.public.pages.login.LOGINPAGE2 import LOGINPAGE2

class LOGINHANDLE1(LOGINPAGE2):
#******************************************************【HANDLE1】******************************************************
    # 登录：点击
    def Login_click(self):
        return self.p.click(self.LoginL)