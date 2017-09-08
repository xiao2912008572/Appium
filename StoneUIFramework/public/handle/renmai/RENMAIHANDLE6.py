__author__ = 'Administrator'
from StoneUIFramework.public.handle.renmai.RENMAIHANDLE5 import _RENMAIHANDLE5

class _RENMAIHANDLE6(_RENMAIHANDLE5):
#*********************************【PAGE5】人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像：RMSY_search_label_groupchat_menu_setting_grouphead*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-返回：点击
    def RMSY_search_label_groupchat_menu_setting_grouphead_back_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_grouphead_back())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像：点击
    def RMSY_search_label_groupchat_menu_setting_grouphead_head_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_grouphead_head())

#*********************************【PAGE5】人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称：RMSY_search_label_groupchat_menu_setting_groupname*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-返回：点击
    def RMSY_search_label_groupchat_menu_setting_groupname_back_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_groupname_back())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-名称输入框：输入
    def RMSY_search_label_groupchat_menu_setting_groupname_nameinput_sendkeys(self, name):
        return self.p.send_keys(self.RMSY_search_label_groupchat_menu_setting_groupname_nameinput(), name)

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-备注名输入框：输入
    def RMSY_search_label_groupchat_menu_setting_groupname_remarknameinput_sendkeys(self, remarkname):
        return self.p.send_keys(self.RMSY_search_label_groupchat_menu_setting_groupname_remarknameinput(), remarkname)

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称-保存：点击
    def RMSY_search_label_groupchat_menu_setting_groupname_save_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_groupname_save())

#*********************************【PAGE5】人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期：RMSY_search_label_groupchat_menu__heatsetting_period*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-返回：点击
    def RMSY_search_label_groupchat_menu_heatsetting_period_back_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_period_back())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-每天：点击
    def RMSY_search_label_groupchat_menu_heatsetting_period_everyday_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_period_everyday())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-工昨日：点击
    def RMSY_search_label_groupchat_menu_heatsetting_period_workday_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_period_workday())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-节假日：点击
    def RMSY_search_label_groupchat_menu_heatsetting_period_holiday_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_period_holiday())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-择日：点击
    def RMSY_search_label_groupchat_menu_heatsetting_period_selectday_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_period_selectday())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期-保存：点击
    def RMSY_search_label_groupchat_menu_heatsetting_period_save_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_period_save())

#*********************************【PAGE5】人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段：RMSY_search_label_groupchat_menu__heatsetting_time*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段-确定：点击
    def RMSY_search_label_groupchat_menu_heatsetting_time_confirm_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_time_confirm())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段-取消：点击
    def RMSY_search_label_groupchat_menu_heatsetting_time_cancel_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_time_cancel())