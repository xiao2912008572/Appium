__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.RENMAIPAGE3 import _RENMAIPAGE3

class _RENMAIPAGE4(_RENMAIPAGE3):
#*********************************【PAGE3】点击进入群聊：RMSY_search_label_groupchat*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-返回
    def RMSY_search_label_groupchat_back(self):
        self.RMSY_search_label_groupchat_backC = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-搜索-标签列表-点击进入群聊-返回")
        return self.RMSY_search_label_groupchat_backC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-消息输入框
    def RMSY_search_label_groupchat_msginput(self):
        self.RMSY_search_label_groupchat_msginputC = self.p.get_element("id->com.yunlu6.stone:id/message_content_msgcontent", "人脉首页-搜索-标签列表-点击进入群聊-消息输入框")
        return self.RMSY_search_label_groupchat_msginputC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-发送
    def RMSY_search_label_groupchat_send(self):
        self.RMSY_search_label_groupchat_sendC = self.p.get_element("id->com.yunlu6.stone:id/message_content_send", "人脉首页-搜索-标签列表-点击进入群聊-发送")
        return self.RMSY_search_label_groupchat_sendC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-表情
    def RMSY_search_label_groupchat_emoji(self):
        self.RMSY_search_label_groupchat_emojiC = self.p.get_element("id->com.yunlu6.stone:id/iv_emoji", "人脉首页-搜索-标签列表-点击进入群聊-表情")
        return self.RMSY_search_label_groupchat_emojiC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-表情-表情列表
    def RMSY_search_label_groupchat_emoji_emojilist(self):
        self.RMSY_search_label_groupchat_emoji_emojilistC = self.p.get_elements("id->com.yunlu6.stone:id/item_iv_face", "人脉首页-搜索-标签列表-点击进入群聊-表情-表情列表")
        return self.RMSY_search_label_groupchat_emoji_emojilistC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-功能按钮
    def RMSY_search_label_groupchat_func(self):
        self.RMSY_search_label_groupchat_funcC = self.p.get_element("id->com.yunlu6.stone:id/iv_send", "人脉首页-搜索-标签列表-点击进入群聊-功能按钮")
        return self.RMSY_search_label_groupchat_funcC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-功能按钮-功能列表
    def RMSY_search_label_groupchat_func_funclist(self):
        self.RMSY_search_label_groupchat_func_funclistC = self.p.get_elements("id->com.yunlu6.stone:id/iv", "人脉首页-搜索-标签列表-点击进入群聊-功能按钮-功能列表")
        return self.RMSY_search_label_groupchat_func_funclistC

    #----------------------------设置所有元素定位------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单
    def RMSY_search_label_groupchat_menu(self):
        self.RMSY_search_label_groupchat_menuC = self.p.get_element("id->com.yunlu6.stone:id/title_main_fl_more_menu", "人脉首页-搜索-标签列表-点击进入群聊-主菜单")
        return self.RMSY_search_label_groupchat_menuC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置
    def RMSY_search_label_groupchat_menu_setting(self):
        self.RMSY_search_label_groupchat_menu_settingC = self.p.get_element("id->com.yunlu6.stone:id/anti", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置")
        return self.RMSY_search_label_groupchat_menu_settingC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置
    def RMSY_search_label_groupchat_menu_heatsetting(self):
        self.RMSY_search_label_groupchat_menu_heatsettingC = self.p.get_element("id->com.yunlu6.stone:id/rl_msgsetting", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-热度设置")
        return self.RMSY_search_label_groupchat_menu_heatsettingC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-人群按钮
    def RMSY_search_label_groupchat_groupbtn(self):
        self.RMSY_search_label_groupchat_memberbtnC = self.p.get_element("id->com.yunlu6.stone:id/iv_to_message", "人脉首页-搜索-标签列表-点击进入群聊-人群按钮")
        return self.RMSY_search_label_groupchat_memberbtnC

#*********************************【PAGE3】预览：RMSY_contacts_menu_cardsetting_preview*********************************
    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-返回
    def RMSY_contacts_menu_cardsetting_preview_back(self):
        self.RMSY_contacts_menu_cardsetting_preview_backC = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-点击联系人-打开主菜单-名片设置-预览-返回")
        return self.RMSY_contacts_menu_cardsetting_preview_backC

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-电话
    def RMSY_contacts_menu_cardsetting_preview_tel(self):
        self.RMSY_contacts_menu_cardsetting_preview_telC = self.p.get_element("id->com.yunlu6.stone:id/iv_top_call", "人脉首页-点击联系人-打开主菜单-名片设置-预览-电话")
        return self.RMSY_contacts_menu_cardsetting_preview_telC

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-联系方式列表
    def RMSY_contacts_menu_cardsetting_preview_contacttypes(self):
        self.RMSY_contacts_menu_cardsetting_preview_contacttypesC = self.p.get_elements("id->com.yunlu6.stone:id/iv_contact", "人脉首页-点击联系人-打开主菜单-名片设置-预览-联系方式列表")
        return self.RMSY_contacts_menu_cardsetting_preview_contacttypesC

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览-发送名片
    def RMSY_contacts_menu_cardsetting_preview_sendcard(self):
        self.RMSY_contacts_menu_cardsetting_preview_sendcardC = self.p.get_element("id->com.yunlu6.stone:id/btn_exchange", "人脉首页-点击联系人-打开主菜单-名片设置-预览-发送名片")
        return self.RMSY_contacts_menu_cardsetting_preview_sendcardC

#*********************************【PAGE3】一对一会话：RMSY_contacts_menu_heatsetting_p2pconversation*********************************
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-返回
    def RMSY_contacts_menu_heatsetting_p2pconversation_back(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_backC = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-返回")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_backC

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-消息
    def RMSY_contacts_menu_heatsetting_p2pconversation_msg(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_msgC = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_msg", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-消息")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_msgC

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-飘泡
    def RMSY_contacts_menu_heatsetting_p2pconversation_bubble(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_bubbleC = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_pop", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-飘泡")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_bubbleC

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-震动
    def RMSY_contacts_menu_heatsetting_p2pconversation_shock(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_shockC = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_shock", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-震动")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_shockC

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-铃声
    def RMSY_contacts_menu_heatsetting_p2pconversation_bell(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_bellC = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_bell", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-铃声")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_bellC

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-确定
    def RMSY_contacts_menu_heatsetting_p2pconversation_confirm(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_confirmC = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_ok", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-确定")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_confirmC

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期
    def RMSY_contacts_menu_heatsetting_p2pconversation_period(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_periodC = self.p.get_element("id->android.widget.ImageView", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-周期")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_periodC

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段
    def RMSY_contacts_menu_heatsetting_p2pconversation_time(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversation_timeC = self.p.get_element("id->com.yunlu6.stone:id/im_add_time", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话-时段")
        return self.RMSY_contacts_menu_heatsetting_p2pconversation_timeC

#*********************************【PAGE3】自定义标签：RMSY_contacts_menu_tag_customtag*********************************
    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签-返回
    def RMSY_contacts_menu_tag_customtag_back(self):
        self.RMSY_contacts_menu_tag_customtag_backC = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-点击联系人-打开主菜单-标签-自定义标签-返回")
        return self.RMSY_contacts_menu_tag_customtag_backC

    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签-输入标签名
    def RMSY_contacts_menu_tag_customtag_taginput(self):
        self.RMSY_contacts_menu_tag_customtag_taginputC = self.p.get_element("id->com.yunlu6.stone:id/edit_text", "人脉首页-点击联系人-打开主菜单-标签-自定义标签-输入标签名")
        return self.RMSY_contacts_menu_tag_customtag_taginputC

    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签-添加
    def RMSY_contacts_menu_tag_customtag_add(self):
        self.RMSY_contacts_menu_tag_customtag_addC = self.p.get_element("id->com.yunlu6.stone:id/btn_add", "人脉首页-点击联系人-打开主菜单-标签-自定义标签-输入标签名")
        return self.RMSY_contacts_menu_tag_customtag_addC

#*********************************【PAGE3】修改备注：RMSY_contacts_menu_memo_changenotename*********************************
    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注-输入备注名
    def RMSY_contacts_menu_memo_changenotename_notenameinput(self):
        self.RMSY_contacts_menu_memo_changenotename_notenameinputC = self.p.get_element("id->com.yunlu6.stone:id/et_remark_name", "人脉首页-点击联系人-打开主菜单-备忘--输入备注名")
        return self.RMSY_contacts_menu_memo_changenotename_notenameinputC

    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注-确定
    def RMSY_contacts_menu_memo_changenotename_confirm(self):
        self.RMSY_contacts_menu_memo_changenotename_confirmC = self.p.get_element("id->com.yunlu6.stone:id/dialog_remark_sure", "人脉首页-点击联系人-打开主菜单-备忘-修改备注-确定")
        return self.RMSY_contacts_menu_memo_changenotename_confirmC

    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注-取消
    def RMSY_contacts_menu_memo_changenotename_cancel(self):
        self.RMSY_contacts_menu_memo_changenotename_cancelC = self.p.get_element("id->com.yunlu6.stone:id/dialog_remark_no", "人脉首页-点击联系人-打开主菜单-备忘-修改备注-取消")
        return self.RMSY_contacts_menu_memo_changenotename_cancelC

#*********************************【PAGE3】热度设置：RMSY_contacts_menu_memo_changenotename*********************************
    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-返回
    def RMSY_contacts_msg_menu_heatsetting_back(self):
        self.RMSY_contacts_msg_menu_heatsetting_backC = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-点击联系人-消息-主菜单-热度设置-返回")
        return self.RMSY_contacts_msg_menu_heatsetting_backC

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-消息
    def RMSY_contacts_msg_menu_heatsetting_msg(self):
        self.RMSY_contacts_msg_menu_heatsetting_msgC = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_msg", "人脉首页-点击联系人-消息-主菜单-热度设置-消息")
        return self.RMSY_contacts_msg_menu_heatsetting_msgC

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-飘泡
    def RMSY_contacts_msg_menu_heatsetting_bubble(self):
        self.RMSY_contacts_msg_menu_heatsetting_bubbleC = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_pop", "人脉首页-点击联系人-消息-主菜单-热度设置-飘泡")
        return self.RMSY_contacts_msg_menu_heatsetting_bubbleC

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-震动
    def RMSY_contacts_msg_menu_heatsetting_shock(self):
        self.RMSY_contacts_msg_menu_heatsetting_shockC = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_shock", "人脉首页-点击联系人-消息-主菜单-热度设置-震动")
        return self.RMSY_contacts_msg_menu_heatsetting_shockC

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-铃声
    def RMSY_contacts_msg_menu_heatsetting_bell(self):
        self.RMSY_contacts_msg_menu_heatsetting_bellC = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_bell", "人脉首页-点击联系人-消息-主菜单-热度设置-铃声")
        return self.RMSY_contacts_msg_menu_heatsetting_bellC

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-确定
    def RMSY_contacts_msg_menu_heatsetting_confirm(self):
        self.RMSY_contacts_msg_menu_heatsetting_confirmC = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_ok", "人脉首页-点击联系人-消息-主菜单-热度设置-确定")
        return self.RMSY_contacts_msg_menu_heatsetting_confirmC

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-周期
    def RMSY_contacts_msg_menu_heatsetting_period(self):
        self.RMSY_contacts_msg_menu_heatsetting_periodC = self.p.get_element("id->android.widget.ImageView", "人脉首页-点击联系人-消息-主菜单-热度设置-周期")
        return self.RMSY_contacts_msg_menu_heatsetting_periodC

    #定位：人脉首页-点击联系人-消息-主菜单-热度设置-时段
    def RMSY_contacts_msg_menu_heatsetting_time(self):
        self.RMSY_contacts_msg_menu_heatsetting_timeC = self.p.get_element("id->com.yunlu6.stone:id/im_add_time", "人脉首页-点击联系人-消息-主菜单-热度设置-时段")
        return self.RMSY_contacts_msg_menu_heatsetting_timeC