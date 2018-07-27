__author__ = 'xiaoj'
from YunluFramework.public.pages.login.LOGINPAGE1 import LOGINPAGE1


class LOGINPAGE2(LOGINPAGE1):
    # ******************************************************【PAGE1】登录Login******************************************************
    # 定位:登录-返回
    Login_back = ("id->com.yunlu6.yunlu:id/title_back_icon", "登录-返回")

    # 定位：登录-账号密码登录
    Login_byAccount = ("id->com.yunlu6.yunlu:id/rb_account_login","登录-账号密码登录")

    # 定位:登录-手机号
    Login_phone = ("id->com.yunlu6.yunlu:id/et_phone", "登录-手机号")

    # 定位:登录-密码
    Login_password = ("id->com.yunlu6.yunlu:id/et_code", "登录-密码")

    # 定位:登录-登录按钮
    Login_loginbtn = ("id->com.yunlu6.yunlu:id/btn_login", "登录-密码")
