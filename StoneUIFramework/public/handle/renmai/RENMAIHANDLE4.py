__author__ = 'Administrator'
from StoneUIFramework.public.handle.renmai.RENMAIHANDLE3 import _RENMAIHANDLE3

class _RENMAIHANDLE4(_RENMAIHANDLE3):
#*********************************【PAGE3】点击进入群聊：RMSY_search_label_groupchat*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-返回：点击
    def RMSY_search_label_groupchat_back_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_back())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-消息输入框：输入
    def RMSY_search_label_groupchat_msginput_sendkeys(self, keys):
        return self.p.send_keys(self.RMSY_search_label_groupchat_msginput(), keys)

    #定位：人脉首页-搜索-标签列表-点击进入群聊-发送：点击
    def RMSY_search_label_groupchat_send_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_send())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-表情：点击
    def RMSY_search_label_groupchat_emoji_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_emoji())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-表情-表情列表：点击
    def RMSY_search_label_groupchat_emoji_emojilist_click(self, n):
        return self.p.click(self.RMSY_search_label_groupchat_emoji_emojilist()[n])

    #定位：人脉首页-搜索-标签列表-点击进入群聊-功能按钮：点击
    def RMSY_search_label_groupchat_func_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_func())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-功能按钮-功能列表：点击
    def RMSY_search_label_groupchat_func_funclist_click(self, n):
        return self.p.click(self.RMSY_search_label_groupchat_func_funclist()[n])

    #----------------------------设置所有元素定位------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单：点击
    def RMSY_search_label_groupchat_menu_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置：点击
    def RMSY_search_label_groupchat_menu_setting_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置：点击
    def RMSY_search_label_groupchat_menu_heatsetting_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_heatsetting())

    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮：点击
    def RMSY_search_label_groupchat_groupbtn_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_memberbtn())

#*********************************【PAGE3】预览：RMSY_contacts_menu_cardsetting_preview*********************************
    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-返回：点击
    def RMSY_contacts_menu_cardsetting_preview_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_preview_back())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-电话：点击
    def RMSY_contacts_menu_cardsetting_preview_tel_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_preview_tel())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-联系方式列表
    def RMSY_contacts_menu_cardsetting_preview_contacttypes_click(self, n):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_preview_contacttypes()[n])

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-发送名片：点击
    def RMSY_contacts_menu_cardsetting_preview_sendcard_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_preview_sendcard)

#*********************************【PAGE3】一对一会话：RMSY_contacts_menu_heatsetting_p2pconversation*********************************
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-返回：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_back())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-消息：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_msg_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_msg())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-飘泡：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_bubble_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_bubble())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-震动：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_shock_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_shock())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-铃声：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_bell_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_bell())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-确定：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_confirm_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_confirm())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_period_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_period())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_time_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation_time())

#*********************************【PAGE3】自定义标签：RMSY_contacts_menu_tag_customtag*********************************
    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签-返回：点击
    def RMSY_contacts_menu_tag_customtag_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_tag_customtag_back())

    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签-输入标签名：输入
    def RMSY_contacts_menu_tag_customtag_taginput_sendkeys(self, name):
        return self.p.send_keys(self.RMSY_contacts_menu_tag_customtag_taginput(), name)

    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签-添加：点击
    def RMSY_contacts_menu_tag_customtag_add_click(self):
        return self.p.click(self.RMSY_contacts_menu_tag_customtag_add())

#*********************************【PAGE3】修改备注：RMSY_contacts_menu_memo_changenotename*********************************
    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注-输入备注名：输入
    def RMSY_contacts_menu_memo_changenotename_notenameinput_sendkeys(self, name):
        return self.p.send_keys(self.RMSY_contacts_menu_memo_changenotename_notenameinput(), name)

    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注-确定：点击
    def RMSY_contacts_menu_memo_changenotename_confirm_click(self):
        return self.p.click(self.RMSY_contacts_menu_memo_changenotename_confirm())

    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注-取消：点击
    def RMSY_contacts_menu_memo_changenotename_cancel_click(self):
        return self.p.click(self.RMSY_contacts_menu_memo_changenotename_cancel())

#*********************************【PAGE3】热度设置：RMSY_contacts_menu_memo_changenotename*********************************
    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-返回：点击
    def RMSY_contacts_msg_menu_heatsetting_back_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_back())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-消息：点击
    def RMSY_contacts_msg_menu_heatsetting_msg_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_msg())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-飘泡：点击
    def RMSY_contacts_msg_menu_heatsetting_bubble_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_bubble())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-震动：点击
    def RMSY_contacts_msg_menu_heatsetting_shock_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_shock())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-铃声：点击
    def RMSY_contacts_msg_menu_heatsetting_bell_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_bell())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-确定：点击
    def RMSY_contacts_msg_menu_heatsetting_confirm_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_confirm())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期：点击
    def RMSY_contacts_msg_menu_heatsetting_period_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_period())

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-时段：点击
    def RMSY_contacts_msg_menu_heatsetting_time_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting_time())