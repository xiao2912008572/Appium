__author__ = 'xiaoj'
from YunluIFramework.public.handle.setting.SETTINGHANDLE2 import SETTINGHANDLE2

class SETTINGHANDLE3(SETTINGHANDLE2):
# ******************************************************【PAGE2】主菜单-编辑资料Setting_userinfo_menu_eidt******************************************************
    #设置:设置-基本资料-主菜单-编辑资料-返回
    def Setting_userinfo_menu_eidt_back_click(self):
        return self.p.click(self.Setting_userinfo_menu_eidt_back)

    #设置:设置-基本资料-主菜单-编辑资料-用户名
    def Setting_userinfo_menu_eidt_username_click(self):
        return self.p.click(self.Setting_userinfo_menu_eidt_username)

    #设置:设置-基本资料-主菜单-编辑资料-邮箱
    def Setting_userinfo_menu_eidt_email_click(self):
        return self.p.click(self.Setting_userinfo_menu_eidt_email)

    #设置:设置-基本资料-主菜单-编辑资料-QQ
    def Setting_userinfo_menu_eidt_QQ_click(self):
        return self.p.click(self.Setting_userinfo_menu_eidt_QQ)

    #设置:设置-基本资料-主菜单-编辑资料-微信
    def Setting_userinfo_menu_eidt_wechat_click(self):
        return self.p.click(self.Setting_userinfo_menu_eidt_wechat)

    #设置:设置-基本资料-主菜单-编辑资料-住址
    def Setting_userinfo_menu_eidt_address_click(self):
        return self.p.click(self.Setting_userinfo_menu_eidt_address)

    #设置:设置-基本资料-主菜单-编辑资料-出生日期
    def Setting_userinfo_menu_eidt_birthday_click(self):
        return self.p.click(self.Setting_userinfo_menu_eidt_birthday)

    #设置:设置-基本资料-主菜单-编辑资料-男
    def Setting_userinfo_menu_eidt_male_click(self):
        return self.p.click(self.Setting_userinfo_menu_eidt_male)

    #设置:设置-基本资料-主菜单-编辑资料-女
    def Setting_userinfo_menu_eidt_female_click(self):
        return self.p.click(self.Setting_userinfo_menu_eidt_female)

    #设置:设置-基本资料-主菜单-编辑资料-确定
    def Setting_userinfo_menu_eidt_commit_click(self):
        return self.p.click(self.Setting_userinfo_menu_eidt_commit)

# ******************************************************【PAGE2】主菜单-通道设置Setting_userinfo_menu_channel******************************************************
    #设置:设置-基本资料-主菜单-通道设置-空间列表
    def Setting_userinfo_menu_channel_slist_click(self,n):
        return self.p.clicks(self.Setting_userinfo_menu_channel_slist,n)

    #设置:设置-基本资料-主菜单-通道设置-住址
    def Setting_userinfo_menu_channel_address_click(self):
        return self.p.click(self.Setting_userinfo_menu_channel_address)

     #设置:设置-基本资料-主菜单-通道设置-QQ
    def Setting_userinfo_menu_channel_QQ_click(self):
        return self.p.click(self.Setting_userinfo_menu_channel_QQ)

    #设置:设置-基本资料-主菜单-通道设置-邮箱
    def Setting_userinfo_menu_channel_email_click(self):
        return self.p.click(self.Setting_userinfo_menu_channel_email)

    #设置:设置-基本资料-主菜单-通道设置-手机号
    def Setting_userinfo_menu_channel_phone_click(self):
        return self.p.click(self.Setting_userinfo_menu_channel_phone)

    #设置:设置-基本资料-主菜单-通道设置-姓名
    def Setting_userinfo_menu_channel_name_click(self):
        return self.p.click(self.Setting_userinfo_menu_channel_name)

    #设置:设置-基本资料-主菜单-通道设置-返回
    def Setting_userinfo_menu_channel_back_click(self):
        return self.p.click(self.Setting_userinfo_menu_channel_back)

# ******************************************************【PAGE2】主菜单-导购机会Setting_userinfo_menu_shopping******************************************************
    #设置:设置-基本资料-主菜单-导购机会-返回
    def Setting_userinfo_menu_shopping_back_click(self):
        return self.p.click(self.Setting_userinfo_menu_shopping_back)

    #设置:设置-基本资料-主菜单-导购机会-开启机会
    def Setting_userinfo_menu_shopping_toggle_click(self):
        return self.p.click(self.Setting_userinfo_menu_shopping_toggle)

    #设置:设置-基本资料-主菜单-导购机会-行业意向
    def Setting_userinfo_menu_shopping_intention_click(self):
        return self.p.click(self.Setting_userinfo_menu_shopping_intention)

    #设置:设置-基本资料-主菜单-导购机会-提成点数
    def Setting_userinfo_menu_shopping_point_click(self):
        return self.p.click(self.Setting_userinfo_menu_shopping_point)

    #设置:设置-基本资料-主菜单-导购机会-意向地区
    def Setting_userinfo_menu_shopping_address_click(self):
        return self.p.click(self.Setting_userinfo_menu_shopping_address)

    #设置:设置-基本资料-主菜单-导购机会-确认
    def Setting_userinfo_menu_shopping_confirm_click(self):
        return self.p.click(self.Setting_userinfo_menu_shopping_confirm)

# ******************************************************【PAGE2】主菜单-热度设置Setting_userinfo_menu_hot******************************************************
    #设置:设置-基本资料-主菜单-热度设置-返回
    def Setting_userinfo_menu_hot_back_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot)

    #设置:设置-基本资料-主菜单-热度设置-消息
    def Setting_userinfo_menu_hot_message_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_message)

     #设置:设置-基本资料-主菜单-热度设置-飘泡
    def Setting_userinfo_menu_hot_pop_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_pop)

    #设置:设置-基本资料-主菜单-热度设置-振动
    def Setting_userinfo_menu_hot_shock_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_shock)

    #设置:设置-基本资料-主菜单-热度设置-铃声
    def Setting_userinfo_menu_hot_bell_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_bell)

    #设置:设置-基本资料-主菜单-热度设置-周期
    def Setting_userinfo_menu_hot_cycle_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_cycle)

     #设置:设置-基本资料-主菜单-热度设置-+时段
    def Setting_userinfo_menu_hot_addtime_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_addtime)

    #设置:设置-基本资料-主菜单-热度设置-确定
    def Setting_userinfo_menu_hot_confirm_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_confirm)

# ******************************************************【PAGE2】修改密码Setting_system_editpsw******************************************************
    #设置:设置-系统设置-修改密码-返回
    def Setting_system_editpsw_back_click(self):
        return self.p.click(self.Setting_system_editpsw_back)

    #设置:设置-系统设置-修改密码-输入密码
    def Setting_system_editpsw_newpsw_click(self):
        return self.p.click(self.Setting_system_editpsw_newpsw)

     #设置:设置-系统设置-修改密码-确认密码
    def Setting_system_editpsw_rnewpsw_click(self):
        return self.p.click(self.Setting_system_editpsw_rnewpsw)

     #设置:设置-系统设置-修改密码-完成
    def Setting_system_editpsw_confirm_click(self):
        return self.p.click(self.Setting_system_editpsw_confirm)

# ******************************************************【PAGE2】清理缓存Setting_system_cleandata******************************************************
    #设置:设置-系统设置-清理缓存-确定
    def Setting_system_cleandata_confirm_click(self):
        return self.p.click(self.Setting_system_cleandata_confirm)

    #设置:设置-系统设置-清理缓存-取消
    def Setting_system_cleandata_cancel_click(self):
        return self.p.click(self.Setting_system_cleandata_cancel)

# ******************************************************【PAGE2】退出Setting_about_loginout******************************************************
    #设置:设置-系统设置-退出-确定
    def Setting_aboutus_loginout_confirm_click(self):
        return self.p.click(self.Setting_aboutus_loginout_confirm)

    #设置:设置-系统设置-退出-取消
    def Setting_aboutus_loginout_cancel_click(self):
        return self.p.click(self.Setting_aboutus_loginout_confirm_loginout_cancel)

# ******************************************************【PAGE2】帮助中心Setting_aboutus_help******************************************************
    #设置:设置-关于我们-帮助中心-返回
    def Setting_aboutus_help_back_click(self):
        return self.p.click(self.Setting_aboutus_help_back)

# ******************************************************【PAGE2】使用条款和隐私政策Setting_aboutus_law******************************************************
    #设置:设置-关于我们-使用条款和隐私政策-返回
    def Setting_aboutus_law_back_click(self):
        return self.p.click(self.Setting_aboutus_law_back)