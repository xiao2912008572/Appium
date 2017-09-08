__author__ = 'Administrator'
from StoneUIFramework.public.handle.renmai.RENMAIHANDLE4 import _RENMAIHANDLE4

class _RENMAIHANDLE5(_RENMAIHANDLE4):
#*********************************【PAGE4】人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置：RMSY_search_label_groupchat_menu_setting*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像：点击
    def RMSY_search_label_groupchat_menu_setting_grouphead_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_grouphead())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-返回：点击
    def RMSY_search_label_groupchat_menu_setting_back_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_back())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群名称：点击
    def RMSY_search_label_groupchat_menu_setting_groupname_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_groupname())

#*********************************【PAGE4】人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置：RMSY_search_label_groupchat_menu_heatsetting*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-返回：点击
    def RMSY_search_label_groupchat_menu_heatsetting_back_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_back())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-消息：点击
    def RMSY_search_label_groupchat_menu_heatsetting_msg_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_msg())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-飘泡：点击
    def RMSY_search_label_groupchat_menu_heatsetting_bubble_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_bubble())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-震动：点击
    def RMSY_search_label_groupchat_menu_heatsetting_shock_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_shock())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-铃声：点击
    def RMSY_search_label_groupchat_menu_heatsetting_bell_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_bell())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-确定：点击
    def RMSY_search_label_groupchat_menu_heatsetting_confirm_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_confirm())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-周期：点击
    def RMSY_search_label_groupchat_menu_heatsetting_period_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_period())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置-时段：点击
    def RMSY_search_label_groupchat_menu_heatsetting_time_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu__heatsetting_time())

#*********************************【PAGE4】人脉首页-搜索-标签列表-点击进入群聊-人群按钮：RMSY_search_label_groupchat_groupbtn*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮-返回：点击
    def RMSY_search_label_groupchat_groupbtn_back_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_groupbtn_back())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮-联系人列表：点击
    def RMSY_search_label_groupchat_groupbtn_Contacts_click(self, n):
        return self.p.click(self.RMSY_search_label_groupchat_groupbtn_Contacts()[n])

    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮-消息输入框：输入
    def RMSY_search_label_groupchat_groupbtn_msginput_sendkeys(self, msg):
        return self.p.send_keys(self.RMSY_search_label_groupchat_groupbtn_msginput(), msg)

    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮-消息按钮：点击
    def RMSY_search_label_groupchat_groupbtn_msgbtn_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_groupbtn_msgbtn())

#*********************************【PAGE3】人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期：RMSY_contacts_menu_heatsetting_p2pconversation_period*********************************
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-返回：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_period_back())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-每天：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_everyday_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_period_everyday())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-工昨日：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_workday_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_period_workday())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-节假日：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_holiday_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_period_holiday())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-择日：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_selectday_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_period_selectday())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期-保存：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_save_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_period_save())

#*********************************【PAGE3】人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段：RMSY_contacts_menu_heatsetting_p2pconversation_time*********************************
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段-确定：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_time_confirm_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_time_confirm())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段-取消：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_time_cancel_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_time_cancel())

#*********************************【PAGE3】人脉首页-点击联系人-消息-主菜单-热度设置-周期：RMSY_contacts_msg_menu_heatsetting_period*********************************
    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-返回：点击
    def RMSY_contacts_msg_menu_heatsetting_period_back_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_period_back())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-每天：点击
    def RMSY_contacts_msg_menu_heatsetting_period_everyday_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_period_everyday())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-工昨日：点击
    def RMSY_contacts_msg_menu_heatsetting_period_workday_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_period_workday())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-节假日：点击
    def RMSY_contacts_msg_menu_heatsetting_period_holiday_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_period_holiday())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-择日：点击
    def RMSY_contacts_msg_menu_heatsetting_period_selectday_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_period_selectday())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期-保存：点击
    def RMSY_contacts_msg_menu_heatsetting_period_save_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_period_save())

#*********************************【PAGE4】人脉首页-点击联系人-消息-主菜单-热度设置-时段：RMSY_contacts_msg_menu_heatsetting_time*********************************
    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-时段-确定：点击
    def RMSY_contacts_msg_menu_heatsetting_time_confirm_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_time_confirm())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-时段-取消：点击
    def RMSY_contacts_msg_menu_heatsetting_time_cancel_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_time_cancel())