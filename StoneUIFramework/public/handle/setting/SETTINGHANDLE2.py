__author__ = 'xiaoj'
from StoneUIFramework.public.handle.setting.SETTINGHANDLE1 import SETTINGHANDLE1

class SETTINGHANDLE2(SETTINGHANDLE1):
# ******************************************************【PAGE1】头像Setting_portrait******************************************************
    #设置:设置-头像-返回
    def Setting_portrait_back_click(self):
        return self.p.click(self.Setting_portrait_back)

    #设置:设置-头像-头像
    def Setting_portrait_headpic_click(self):
        return self.p.click(self.Setting_portrait_headpic)

    #设置:设置-头像-头像-相册
    def Setting_portrait_headpic_ByAlbum_click(self):
        return self.p.click(self.Setting_portrait_headpic_ByAlbum)

    #设置:设置-头像-头像-拍照
    def Setting_portrait_headpic_ByTakepic_click(self):
        return self.p.click(self.Setting_portrait_headpic_ByTakepic)

    #设置:设置-头像-头像-取消
    def Setting_portrait_headpic_cancel_click(self):
        return self.p.click(self.Setting_portrait_headpic_cancel)

# ******************************************************【PAGE1】基本资料Setting_userinfo******************************************************
    #设置:设置-基本资料-返回
    def Setting_userinfo_back_click(self):
        return self.p.click(self.Setting_userinfo_back)

    #设置:设置-基本资料-主菜单
    def Setting_userinfo_menu_click(self):
        return self.p.click(self.Setting_userinfo_menu)

    #设置:设置-基本资料-主菜单-编辑资料
    def Setting_userinfo_menu_eidt_click(self):
        return self.p.click(self.Setting_userinfo_menu_eidt)

    #设置:设置-基本资料-主菜单-通道设置
    def Setting_userinfo_menu_channel_click(self):
        return self.p.click(self.Setting_userinfo_menu_channel)

    #设置:设置-基本资料-主菜单-导购机会
    def Setting_userinfo_menu_shopping_click(self):
        return self.p.click(self.Setting_userinfo_menu_shopping)

     #设置:设置-基本资料-主菜单-热度设置
    def Setting_userinfo_menu_hot_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot)

    #设置:设置-基本资料-主菜单-手机
    def Setting_userinfo_menu_phone_click(self):
        return self.p.click(self.Setting_userinfo_menu_phone)

    #设置:设置-基本资料-主菜单-位置
    def Setting_userinfo_menu_position_click(self):
        return self.p.click(self.Setting_userinfo_menu_position)

    #设置:设置-基本资料-主菜单-邮箱
    def Setting_userinfo_menu_email_click(self):
        return self.p.clicks(self.Setting_userinfo_menu_email,0)

    #设置:设置-基本资料-主菜单-QQ
    def Setting_userinfo_menu_QQ_click(self):
        return self.p.clicks(self.Setting_userinfo_menu_QQ,1)

# ******************************************************【PAGE1】系统设置Setting_system******************************************************
    #设置:设置-系统设置-返回
    def Setting_system_back_click(self):
        return self.p.click(self.Setting_system_back)

    #设置:设置-系统设置-wifi同步
    def Setting_system_wifi_click(self):
        return self.p.click(self.Setting_system_wifi)

    #设置:设置-系统设置-徐改密码
    def Setting_system_editpsw_click(self):
        return self.p.click(self.Setting_system_editpsw)

    #设置:设置-系统设置-清理缓存
    def Setting_system_cleandata_click(self):
        return self.p.click(self.Setting_system_editpsw)

    #设置:设置-系统设置-退出
    def Setting_system_loginout_click(self):
        return self.p.click(self.Setting_system_loginout)

# ******************************************************【PAGE1】关于我Setting_aboutus******************************************************
    #设置:设置-关于我们-返回
    def Setting_aboutus_back_click(self):
        return self.p.click(self.Setting_aboutus_back)

    #设置:设置-关于我们-帮助中心
    def Setting_aboutus_help_click(self):
        return self.p.click(self.Setting_aboutus_help)

    #设置:设置-关于我们-手机
    def Setting_aboutus_phone_click(self):
        return self.p.click(self.Setting_aboutus_phone)

    #设置:设置-关于我们-QQ
    def Setting_aboutus_QQ_click(self):
        return self.p.click(self.Setting_aboutus_QQ)

    #设置:设置-关于我们-使用条款和隐私政策
    def Setting_aboutus_law_click(self):
        return self.p.click(self.Setting_aboutus_law)