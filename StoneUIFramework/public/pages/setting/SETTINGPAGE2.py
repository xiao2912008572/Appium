__author__ = 'xiaoj'
from StoneUIFramework.public.pages.setting.SETTINGPAGE1 import _SETTINGPAGE1

class _SETTINGPAGE2(_SETTINGPAGE1):
# ******************************************************【PAGE1】头像Setting_portrait******************************************************
    #设置:设置-头像-返回
    def Setting_portrait_back(self):
        self.Setting_portrait_backS = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","设置-头像-返回")
        return self.Setting_portrait_backS

    #设置:设置-头像-头像
    def Setting_portrait_headpic(self):
        self.Setting_portrait_headpicS = self.p.get_element("id->com.yunlu6.stone:id/replace_userimg","设置-头像-头像")
        return self.Setting_portrait_headpicS

    #设置:设置-头像-头像-相册
    def Setting_portrait_headpic_ByAlbum(self):
        self.Setting_portrait_headpic_ByAlbumS = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_album","设置-头像-头像-相册")
        return self.Setting_portrait_headpic_ByAlbumS

    #设置:设置-头像-头像-拍照
    def Setting_portrait_headpic_ByTakepic(self):
        self.Setting_portrait_headpic_ByTakepicS = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_take_pictures","设置-头像-头像-拍照")
        return self.Setting_portrait_headpic_ByTakepicS

    #设置:设置-头像-头像-取消
    def Setting_portrait_headpic_cancel(self):
        self.Setting_portrait_headpic_cancelS = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_cancel","设置-头像-头像-取消")
        return self.Setting_portrait_headpic_cancelS

# ******************************************************【PAGE1】基本资料Setting_userinfo******************************************************
    #设置:设置-基本资料-返回
    def Setting_userinfo_back(self):
        self.Setting_userinfo_backS = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","设置-基本资料-返回")
        return self.Setting_userinfo_backS

    #设置:设置-基本资料-主菜单
    def Setting_userinfo_menu(self):
        self.Setting_userinfo_menuS = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","设置-基本资料-主菜单")
        return self.Setting_userinfo_menuS

    #设置:设置-基本资料-主菜单-编辑资料
    def Setting_userinfo_menu_eidt(self):
        self.Setting_userinfo_menu_eidtS = self.p.get_element("id->com.yunlu6.stone:id/anti","设置-基本资料-主菜单-编辑资料")
        return self.Setting_userinfo_menu_eidtS

    #设置:设置-基本资料-主菜单-通道设置
    def Setting_userinfo_menu_channel(self):
        self.Setting_userinfo_menu_channelS = self.p.get_element("id->com.yunlu6.stone:id/rl_4","设置-基本资料-主菜单-通道设置")
        return self.Setting_userinfo_menu_channelS

    #设置:设置-基本资料-主菜单-导购机会
    def Setting_userinfo_menu_shopping (self):
        self.Setting_userinfo_menu_shoppingS = self.p.get_element("id->ccom.yunlu6.stone:id/label","设置-基本资料-主菜单-导购机会")
        return self.Setting_userinfo_menu_shoppingS

     #设置:设置-基本资料-主菜单-热度设置
    def Setting_userinfo_menu_hot(self):
        self.Setting_userinfo_menu_hotS = self.p.get_element("id->com.yunlu6.stone:id/rl_msgsetting","设置-基本资料-主菜单-热度设置")
        return self.Setting_userinfo_menu_hotS

    #设置:设置-基本资料-主菜单-手机
    def Setting_userinfo_menu_phone(self):
        self.Setting_userinfo_menu_phoneS = self.p.get_element("id->com.yunlu6.stone:id/iv_top_call","设置-基本资料-主菜单-手机")
        return self.Setting_userinfo_menu_phoneS

    #设置:设置-基本资料-主菜单-位置
    def Setting_userinfo_menu_position(self):
        self.Setting_userinfo_menu_positionS = self.p.get_element("id->com.yunlu6.stone:id/iv_top_position","设置-基本资料-主菜单-位置")
        return self.Setting_userinfo_menu_positionS

    #设置:设置-基本资料-主菜单-邮箱
    def Setting_userinfo_menu_email(self):
        self.Setting_userinfo_menu_emailS = self.p.get_elements("id->com.yunlu6.stone:id/iv_contact","设置-基本资料-主菜单-邮箱")
        return self.Setting_userinfo_menu_emailS

    #设置:设置-基本资料-主菜单-QQ
    def Setting_userinfo_menu_QQ(self):
        self.Setting_userinfo_menu_QQS = self.p.get_elements("id->com.yunlu6.stone:id/iv_contact","设置-基本资料-主菜单-邮箱")
        return self.Setting_userinfo_menu_QQS

# ******************************************************【PAGE1】系统设置Setting_system******************************************************
    #设置:设置-系统设置-返回
    def Setting_system_back(self):
        self.Setting_system_backS = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","设置-系统设置-返回")
        return self.Setting_system_backS

    #设置:设置-系统设置-wifi同步
    def Setting_system_wifi(self):
        self.Setting_system_wifiS = self.p.get_element("id->com.yunlu6.stone:id/aboutus_wifibtn","设置-系统设置-wifi同步")
        return self.Setting_system_wifiS

    #设置:设置-系统设置-修改密码
    def Setting_system_editpsw(self):
        self.Setting_system_editpswS = self.p.get_element("id->com.yunlu6.stone:id/sliding_safe_editpsw","设置-系统设置-修改密码")
        return self.Setting_system_editpswS

    #设置:设置-系统设置-清理缓存
    def Setting_system_cleandata(self):
        self.Setting_system_cleandataS = self.p.get_element("id->com.yunlu6.stone:id/aboutus_cleandata","设置-系统设置-清理缓存")
        return self.Setting_system_cleandataS

    #设置:设置-系统设置-退出
    def Setting_system_loginout(self):
        self.Setting_system_loginoutS = self.p.get_element("id->com.yunlu6.stone:id/aboutus_loginout","设置-系统设置-退出")
        return self.Setting_system_loginoutS

# ******************************************************【PAGE1】关于我Setting_aboutus******************************************************
    #设置:设置-关于我们-返回
    def Setting_aboutus_back(self):
        self.Setting_aboutus_backS = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","设置-关于我们-返回")
        return self.Setting_aboutus_backS

    #设置:设置-关于我们-帮助中心
    def Setting_aboutus_help(self):
        self.Setting_aboutus_helpS = self.p.get_element("id->com.yunlu6.stone:id/aboutus_help","设置-关于我们-帮助中心")
        return self.Setting_aboutus_helpS

    #设置:设置-关于我们-手机
    def Setting_aboutus_phone(self):
        self.Setting_aboutus_phoneS = self.p.get_element("id->com.yunlu6.stone:id/aboutus_phone","设置-关于我们-手机")
        return self.Setting_aboutus_phoneS

    #设置:设置-关于我们-QQ
    def Setting_aboutus_QQ(self):
        self.Setting_aboutus_QQS = self.p.get_element("id->com.yunlu6.stone:id/aboutus_qq","设置-关于我们-QQ")
        return self.Setting_aboutus_QQS

    #设置:设置-关于我们-使用条款和隐私政策
    def Setting_aboutus_law(self):
        self.Setting_aboutus_lawS = self.p.get_element("id-> com.yunlu6.stone:id/abouts_yunlu_law","设置-关于我们-使用条款和隐私政策")
        return self.Setting_aboutus_lawS