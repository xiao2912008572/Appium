__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.RENMAIPAGE5 import _RENMAIPAGE5

class _RENMAIPAGE6(_RENMAIPAGE5):
#*********************************【PAGE5】人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像：RMSY_search_label_groupchat_menu_setting_grouphead*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-返回
    def RMSY_search_label_groupchat_menu_setting_grouphead_back(self):
        self.RMSY_search_label_groupchat_menu_setting_grouphead_backC = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-返回")
        return self.RMSY_search_label_groupchat_menu_setting_grouphead_backC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像
    def RMSY_search_label_groupchat_menu_setting_grouphead_head(self):
        self.RMSY_search_label_groupchat_menu_setting_grouphead_headC = self.p.get_element("id->com.yunlu6.stone:id/iv_logo", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像")
        return self.RMSY_search_label_groupchat_menu_setting_grouphead_headC

#*********************************【PAGE5】人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称：RMSY_search_label_groupchat_menu_setting_groupname*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-返回
    def RMSY_search_label_groupchat_menu_setting_groupname_back(self):
        self.RMSY_search_label_groupchat_menu_setting_groupname_backC = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-返回")
        return self.RMSY_search_label_groupchat_menu_setting_groupname_backC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-名称输入框
    def RMSY_search_label_groupchat_menu_setting_groupname_nameinput(self):
        self.RMSY_search_label_groupchat_menu_setting_groupname_nameinputC = self.p.get_element("id->com.yunlu6.stone:id/et_name", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-名称输入框")
        return self.RMSY_search_label_groupchat_menu_setting_groupname_nameinputC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-备注名输入框
    def RMSY_search_label_groupchat_menu_setting_groupname_remarknameinput(self):
        self.RMSY_search_label_groupchat_menu_setting_groupname_remarknameinputC = self.p.get_element("id->com.yunlu6.stone:id/rl_group_name", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-备注名输入框")
        return self.RMSY_search_label_groupchat_menu_setting_groupname_remarknameinputC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-保存
    def RMSY_search_label_groupchat_menu_setting_groupname_save(self):
        self.RMSY_search_label_groupchat_menu_setting_groupname_saveC = self.p.get_element("id->com.yunlu6.stone:id/btn_save", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-保存")
        return self.RMSY_search_label_groupchat_menu_setting_groupname_saveC

#*********************************【PAGE5】人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期：RMSY_search_label_groupchat_menu__heatsetting_period*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-返回
    def RMSY_search_label_groupchat_menu__heatsetting_period_back(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_period_backC = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-返回")
        return self.RMSY_search_label_groupchat_menu__heatsetting_period_backC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-每天
    def RMSY_search_label_groupchat_menu__heatsetting_period_everyday(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_period_everydayC = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_allday", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-每天")
        return self.RMSY_search_label_groupchat_menu__heatsetting_period_everydayC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-工昨日
    def RMSY_search_label_groupchat_menu__heatsetting_period_workday(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_period_workdayC = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_workday", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-工昨日")
        return self.RMSY_search_label_groupchat_menu__heatsetting_period_workdayC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-节假日
    def RMSY_search_label_groupchat_menu__heatsetting_period_holiday(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_period_holidayC = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_holiday", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-节假日")
        return self.RMSY_search_label_groupchat_menu__heatsetting_period_holidayC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-择日
    def RMSY_search_label_groupchat_menu__heatsetting_period_selectday(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_period_selectdayC = self.p.get_element("id->com.yunlu6.stone:id/im_add_days", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-择日")
        return self.RMSY_search_label_groupchat_menu__heatsetting_period_selectdayC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-保存
    def RMSY_search_label_groupchat_menu__heatsetting_period_save(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_period_saveC = self.p.get_element("id->com.yunlu6.stone:id/btn_messagetime_save", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-保存")
        return self.RMSY_search_label_groupchat_menu__heatsetting_period_saveC

#*********************************【PAGE5】人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段：RMSY_search_label_groupchat_menu__heatsetting_time*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段-确定
    def RMSY_search_label_groupchat_menu__heatsetting_time_confirm(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_time_confirmC = self.p.get_element("id->com.yunlu6.stone:id/tv_dialog_ok", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段-确定")
        return self.RMSY_search_label_groupchat_menu__heatsetting_time_confirmC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段-取消
    def RMSY_search_label_groupchat_menu__heatsetting_time_cancel(self):
        self.RMSY_search_label_groupchat_menu__heatsetting_time_cancelC = self.p.get_element("id->com.yunlu6.stone:id/tv_dialog_cancel", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段-确定")
        return self.RMSY_search_label_groupchat_menu__heatsetting_time_cancelC