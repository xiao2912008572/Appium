__author__ = 'xiaoj'
from StoneUIFramework.public.pages.setting.SETTINGPAGE2 import _SETTINGPAGE2

class _SETTINGPAGE3(_SETTINGPAGE2):
# ******************************************************【PAGE2】主菜单-编辑资料Setting_userinfo_menu_eidt******************************************************
    #设置:设置-基本资料-主菜单-编辑资料-返回
    def Setting_userinfo_menu_eidt_back(self):
        self.Setting_userinfo_menu_eidt_backS = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","设置-基本资料-主菜单-编辑资料-返回")
        return self.Setting_userinfo_menu_eidt_backS

    #设置:设置-基本资料-主菜单-编辑资料-用户名
    def Setting_userinfo_menu_eidt_username(self):
        self.Setting_userinfo_menu_eidt_usernameS = self.p.get_element("id->com.yunlu6.stone:id/userinfo_nickname","设置-基本资料-主菜单-编辑资料-返回")
        return self.Setting_userinfo_menu_eidt_usernameS

    #设置:设置-基本资料-主菜单-编辑资料-邮箱
    def Setting_userinfo_menu_eidt_email(self):
        self.Setting_userinfo_menu_eidt_emailS = self.p.get_element("id->com.yunlu6.stone:id/userinfo_email","设置-基本资料-主菜单-编辑资料-邮箱")
        return self.Setting_userinfo_menu_eidt_emailS

    #设置:设置-基本资料-主菜单-编辑资料-QQ
    def Setting_userinfo_menu_eidt_QQ(self):
        self.Setting_userinfo_menu_eidt_emailS = self.p.get_element("id->com.yunlu6.stone:id/userinfo_qqnum","设置-基本资料-主菜单-编辑资料-QQ")
        return self.Setting_userinfo_menu_eidt_emailS

    #设置:设置-基本资料-主菜单-编辑资料-微信
    def Setting_userinfo_menu_eidt_wechat(self):
        self.Setting_userinfo_menu_eidt_wechatS = self.p.get_element("id->com.yunlu6.stone:id/userinfo_wechat","设置-基本资料-主菜单-编辑资料-微信")
        return self.Setting_userinfo_menu_eidt_wechatS

    #设置:设置-基本资料-主菜单-编辑资料-住址
    def Setting_userinfo_menu_eidt_address(self):
        self.Setting_userinfo_menu_eidt_addressS = self.p.get_element("id->com.yunlu6.stone:id/userinfo_address","设置-基本资料-主菜单-编辑资料-住址")
        return self.Setting_userinfo_menu_eidt_addressS

    #设置:设置-基本资料-主菜单-编辑资料-出生日期
    def Setting_userinfo_menu_eidt_birthday(self):
        self.Setting_userinfo_menu_eidt_birthdayS = self.p.get_element("id-> com.yunlu6.stone:id/userinfo_birthday","设置-基本资料-主菜单-编辑资料-住址")
        return self.Setting_userinfo_menu_eidt_birthdayS

    #设置:设置-基本资料-主菜单-编辑资料-男
    def Setting_userinfo_menu_eidt_male(self):
        self.Setting_userinfo_menu_eidt_maleS = self.p.get_element("id->com.yunlu6.stone:id/userinfo_sexmale","设置-基本资料-主菜单-编辑资料-男")
        return self.Setting_userinfo_menu_eidt_maleS

    #设置:设置-基本资料-主菜单-编辑资料-女
    def Setting_userinfo_menu_eidt_female(self):
        self.Setting_userinfo_menu_eidt_femaleS = self.p.get_element("id->com.yunlu6.stone:id/userinfo_sexfemale","设置-基本资料-主菜单-编辑资料-女")
        return self.Setting_userinfo_menu_eidt_femaleS

    #设置:设置-基本资料-主菜单-编辑资料-确定
    def Setting_userinfo_menu_eidt_commit(self):
        self.Setting_userinfo_menu_eidt_commitS = self.p.get_element("id->com.yunlu6.stone:id/userinfo_commitedit","设置-基本资料-主菜单-编辑资料-确定")
        return self.Setting_userinfo_menu_eidt_commitS

# ******************************************************【PAGE2】主菜单-通道设置Setting_userinfo_menu_channel******************************************************
    #设置:设置-基本资料-主菜单-通道设置-空间列表
    def Setting_userinfo_menu_channel_slist(self):
        self.Setting_userinfo_menu_channel_slistS = self.p.get_elements("id->com.yunlu6.stone:id/sb_cluster","设置-基本资料-主菜单-通道设置-空间列表")
        return self.Setting_userinfo_menu_channel_slistS

    #设置:设置-基本资料-主菜单-通道设置-住址
    def Setting_userinfo_menu_channel_address(self):
        self.Setting_userinfo_menu_channel_addressS = self.p.get_element("id->com.yunlu6.stone:id/sb_address_bt","设置-基本资料-主菜单-通道设置-住址")
        return self.Setting_userinfo_menu_channel_addressS

     #设置:设置-基本资料-主菜单-通道设置-QQ
    def Setting_userinfo_menu_channel_QQ(self):
        self.Setting_userinfo_menu_channel_QQS = self.p.get_element("id->com.yunlu6.stone:id/sb_qq_bt","设置-基本资料-主菜单-通道设置-QQ")
        return self.Setting_userinfo_menu_channel_QQS

    #设置:设置-基本资料-主菜单-通道设置-邮箱
    def Setting_userinfo_menu_channel_email(self):
        self.Setting_userinfo_menu_channel_emailS = self.p.get_element("id->com.yunlu6.stone:id/sb_em_bt","设置-基本资料-主菜单-通道设置-邮箱")
        return self.Setting_userinfo_menu_channel_emailS

    #设置:设置-基本资料-主菜单-通道设置-手机号
    def Setting_userinfo_menu_channel_phone(self):
        self.Setting_userinfo_menu_channel_phoneS = self.p.get_element("id->com.yunlu6.stone:id/sb_nub_bt","设置-基本资料-主菜单-通道设置-手机号")
        return self.Setting_userinfo_menu_channel_phoneS

    #设置:设置-基本资料-主菜单-通道设置-姓名
    def Setting_userinfo_menu_channel_name(self):
        self.Setting_userinfo_menu_channel_phoneS = self.p.get_element("id->com.yunlu6.stone:id/sb_name_bt","设置-基本资料-主菜单-通道设置-姓名")
        return self.Setting_userinfo_menu_channel_phoneS

    #设置:设置-基本资料-主菜单-通道设置-返回
    def Setting_userinfo_menu_channel_back(self):
        self.Setting_userinfo_menu_channel_backS = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","设置-基本资料-主菜单-通道设置-返回")
        return self.Setting_userinfo_menu_channel_backS

# ******************************************************【PAGE2】主菜单-导购机会Setting_userinfo_menu_shopping******************************************************
    #设置:设置-基本资料-主菜单-导购机会-返回
    def Setting_userinfo_menu_shopping_back(self):
        self.Setting_userinfo_menu_shopping_backS = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","设置-基本资料-主菜单-导购机会-返回")
        return self.Setting_userinfo_menu_shopping_backS

    #设置:设置-基本资料-主菜单-导购机会-开启机会
    def Setting_userinfo_menu_shopping_toggle(self):
        self.Setting_userinfo_menu_shopping_toggleS = self.p.get_element("id->com.yunlu6.stone:id/toggle_button","设置-基本资料-主菜单-导购机会-开启机会")
        return self.Setting_userinfo_menu_shopping_toggleS

    #设置:设置-基本资料-主菜单-导购机会-行业意向
    def Setting_userinfo_menu_shopping_intention(self):
        self.Setting_userinfo_menu_shopping_intentionS = self.p.get_element("id->com.yunlu6.stone:id/rl_service","设置-基本资料-主菜单-导购机会-意向行业")
        return self.Setting_userinfo_menu_shopping_intentionS

    #设置:设置-基本资料-主菜单-导购机会-提成点数
    def Setting_userinfo_menu_shopping_point(self):
        self.Setting_userinfo_menu_shopping_pointS = self.p.get_element("id->com.yunlu6.stone:id/et_order","设置-基本资料-主菜单-导购机会-提成点数")
        return self.Setting_userinfo_menu_shopping_pointS

    #设置:设置-基本资料-主菜单-导购机会-意向地区
    def Setting_userinfo_menu_shopping_address(self):
        self.Setting_userinfo_menu_shopping_addressS = self.p.get_element("id->com.yunlu6.stone:id/tv_address","设置-基本资料-主菜单-导购机会-意向地区")
        return self.Setting_userinfo_menu_shopping_addressS

    #设置:设置-基本资料-主菜单-导购机会-确认
    def Setting_userinfo_menu_shopping_confirm(self):
        self.Setting_userinfo_menu_shopping_confirmS = self.p.get_element("id->com.yunlu6.stone:id/btn","设置-基本资料-主菜单-导购机会-确认")
        return self.Setting_userinfo_menu_shopping_confirmS

# ******************************************************【PAGE2】主菜单-热度设置Setting_userinfo_menu_hot******************************************************
    #设置:设置-基本资料-主菜单-热度设置-返回
    def Setting_userinfo_menu_hot_back(self):
        self.Setting_userinfo_menu_hot_backS = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","设置-基本资料-主菜单-热度设置-返回")
        return self.Setting_userinfo_menu_hotS

    #设置:设置-基本资料-主菜单-热度设置-消息
    def Setting_userinfo_menu_hot_message(self):
        self.Setting_userinfo_menu_hot_messageS = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_msg","设置-基本资料-主菜单-热度设置-消息")
        return self.Setting_userinfo_menu_hot_messageS

     #设置:设置-基本资料-主菜单-热度设置-飘泡
    def Setting_userinfo_menu_hot_pop(self):
        self.Setting_userinfo_menu_hot_popS = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_pop","设置-基本资料-主菜单-热度设置-飘泡")
        return self.Setting_userinfo_menu_hot_popS

    #设置:设置-基本资料-主菜单-热度设置-振动
    def Setting_userinfo_menu_hot_shock(self):
        self.Setting_userinfo_menu_hot_shockS = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_shock","设置-基本资料-主菜单-热度设置-振动")
        return self.Setting_userinfo_menu_hot_shockS

    #设置:设置-基本资料-主菜单-热度设置-铃声
    def Setting_userinfo_menu_hot_bell(self):
        self.Setting_userinfo_menu_hot_bellS = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_bell","设置-基本资料-主菜单-热度设置-铃声")
        return self.Setting_userinfo_menu_hot_bellS

    #设置:设置-基本资料-主菜单-热度设置-周期
    def Setting_userinfo_menu_hot_cycle(self):
        self.Setting_userinfo_menu_hot_cycleS = self.p.get_element("id->com.yunlu6.stone:id/tv_cycle","设置-基本资料-主菜单-热度设置-周期")
        return self.Setting_userinfo_menu_hot_cycleS

     #设置:设置-基本资料-主菜单-热度设置-+时段
    def Setting_userinfo_menu_hot_addtime(self):
        self.Setting_userinfo_menu_hot_addtimeS = self.p.get_element("id->com.yunlu6.stone:id/im_add_time","设置-基本资料-主菜单-热度设置-+时段")
        return self.Setting_userinfo_menu_hot_addtimeS

    #设置:设置-基本资料-主菜单-热度设置-确定
    def Setting_userinfo_menu_hot_confirm(self):
        self.Setting_userinfo_menu_hot_confirmS = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_ok","设置-基本资料-主菜单-热度设置-确定")
        return self.Setting_userinfo_menu_hot_confirmS

# ******************************************************【PAGE2】修改密码Setting_system_editpsw******************************************************
    #设置:设置-系统设置-修改密码-返回
    def Setting_system_editpsw_back(self):
        self.Setting_system_editpsw_backS = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","设置-系统设置-修改密码-返回")
        return self.Setting_system_editpsw_backS

    #设置:设置-系统设置-修改密码-输入密码
    def Setting_system_editpsw_newpsw(self):
        self.Setting_system_editpsw_newpswS = self.p.get_element("id->com.yunlu6.stone:id/edit_newpsw","设置-系统设置-修改密码-输入密码")
        return self.Setting_system_editpsw_newpswS

     #设置:设置-系统设置-修改密码-确认密码
    def Setting_system_editpsw_rnewpsw(self):
        self.Setting_system_editpsw_rnewpswS = self.p.get_element("id->com.yunlu6.stone:id/edit_renewpsw","设置-系统设置-修改密码-确认密码")
        return self.Setting_system_editpsw_rnewpswS

     #设置:设置-系统设置-修改密码-完成
    def Setting_system_editpsw_confirm(self):
        self.Setting_system_editpsw_confirmS = self.p.get_element("id->com.yunlu6.stone:id/edit_commit","设置-系统设置-修改密码-完成")
        return self.Setting_system_editpsw_confirmS

# ******************************************************【PAGE2】清理缓存Setting_system_cleandata******************************************************
    #设置:设置-系统设置-清理缓存-确定
    def Setting_system_cleandata_confirm(self):
        self.Setting_system_cleandata_confirmS = self.p.get_element("id->android:id/button1","设置-系统设置-清理缓存-确定")
        return self.Setting_system_cleandata_confirmS

    #设置:设置-系统设置-清理缓存-取消
    def Setting_system_cleandata_cancel(self):
        self.Setting_system_cleandata_cancelS = self.p.get_element("id->android:id/button2","设置-系统设置-清理缓存-取消")
        return self.Setting_system_cleandata_cancelS

# ******************************************************【PAGE2】退出Setting_system_loginout******************************************************
    #设置:设置-系统设置-退出-确定
    def Setting_system_loginout_confirm(self):
        self.Setting_system_loginout_confirmS = self.p.get_element("id->android:id/button1","设置-系统设置-退出-确定")
        return self.Setting_system_loginout_confirmS

    #设置:设置-系统设置-退出-取消
    def Setting_system_loginout_cancel(self):
        self.Setting_system_loginout_cancelS = self.p.get_element("id->android:id/button2","设置-系统设置-退出-取消")
        return self.Setting_system_loginout_cancelS

# ******************************************************【PAGE2】帮助中心Setting_aboutus_help******************************************************
    #设置:设置-关于我们-帮助中心-返回
    def Setting_aboutus_help_back(self):
        self.Setting_aboutus_help_backS = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","设置-关于我们-帮助中心-返回")
        return self.Setting_aboutus_help_backS

# ******************************************************【PAGE2】使用条款和隐私政策Setting_aboutus_law******************************************************
    #设置:设置-关于我们-使用条款和隐私政策-返回
    def Setting_aboutus_law_back(self):
        self.Setting_aboutus_law_backS = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","设置-关于我们-使用条款和隐私政策-返回")
        return self.Setting_aboutus_law_backS

















































