__author__ = 'xiaoj'
from StoneUIFramework.public.pages.login.LOGINPAGE2 import _LOGINPAGE2

class _LOGINHANDLE1(_LOGINPAGE2):
#******************************************************【HANDLE1】******************************************************
    # 登录：点击
    def Login_click(self):
        return self.p.click(self.Login())

