__author__ = 'Administrator'
from StoneUIFramework.public.handle.renmai.RENMAIHANDLE2 import _RENMAIHANDLE2

class _RENMAIHANDLE3(_RENMAIHANDLE2):
#******************************************************【HANDLE3】******************************************************
#*********************************【PAGE2】搜索按钮：RMSY_search_searchbtn*********************************
    #定位：人脉首页-搜索-搜索按钮-返回按钮：点击
    def RMSY_search_searchbtn_back_click(self):
        return self.p.click(self.RMSY_search_searchbtn_back())

    #定位：人脉首页-搜索-搜索按钮-搜索输入框：输入
    def RMSY_search_searchbtn_searchinput_sendkeys(self, keys):
        return self.p.send_keys(self.RMSY_search_searchbtn_searchinput(), keys)

    #定位：人脉首页-搜索-搜索按钮-搜索按钮：点击
    def RMSY_search_searchbtn_searchbtn_click(self):
        return self.p.click(self.RMSY_search_searchbtn_searchbtn())

    #定位：人脉首页-搜索-搜索按钮-主菜单：点击
    def RMSY_search_searchbtn_menu_click(self):
        return self.p.click(self.RMSY_search_searchbtn_menu())

    #定位：人脉首页-搜索-搜索按钮-主菜单-批量操作：点击
    def RMSY_search_searchbtn_menu_batchoperate_click(self):
        return self.p.click(self.RMSY_search_searchbtn_menu_batchoperate())

#*********************************【PAGE2】标签列表：RMSY_search_label*********************************
    #定位：人脉首页-搜索-标签列表-返回：点击
    def RMSY_search_label_back_click(self):
        return self.p.click(self.RMSY_search_label_back())

    #定位：人脉首页-搜索-标签列表-搜索框：输入
    def RMSY_search_label_searchinput_sendkeys(self, keys):
        return self.p.send_keys(self.RMSY_search_label_searchinput(), keys)

    #定位：人脉首页-搜索-标签列表-搜索按钮：点击
    def RMSY_search_label_searchbtn_click(self):
        return self.p.click(self.RMSY_search_label_searchbtn())

    #------------------------------人脉首页-搜索-标签列表-主菜单---------------------------
    #定位：人脉首页-搜索-标签列表-主菜单：点击
    def RMSY_search_label_menu_click(self):
        return self.p.click(self.RMSY_search_label_menu())

    #------------------------------批量操作---------------------------
    #定位：人脉首页-搜索-标签列表-主菜单-批量操作：点击
    def RMSY_search_label_menu_bcp_click(self):
        return self.p.click(self.RMSY_search_label_menu_bcp())

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-返回：点击
    def RMSY_search_label_menu_bcp_back_click(self):
        return self.p.click(self.RMSY_search_label_menu_bcp_back())

    #---------------------全选-----------------------
    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选：点击
    def RMSY_search_label_menu_bcp_all_click(self):
        return self.p.click(self.RMSY_search_label_menu_bcp_all())

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-取消：点击
    def RMSY_search_label_menu_bcp_all_cancel(self):
        return self.p.click(self.RMSY_search_label_menu_bcp_all_all())

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-打标签

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-黑名单

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-换名片

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-选择联系人：点击
    def RMSY_search_label_menu_bcp_selectcontact_click(self, n):
        return self.p.click(self.RMSY_search_label_menu_bcp_selectcontact()[n])

    #定位：人脉首页-搜索-标签列表-标签成员列表：点击
    def RMSY_search_label_memberlist_click(self, n):
        return self.p.click(self.RMSY_search_label_memberlist()[n])

    #定位：人脉首页-搜索-标签列表-点击进入群聊：点击
    def RMSY_search_label_groupchat_click(self):
        return self.RMSY_search_label_groupchat()

#*********************************【PAGE2】集合列表：RMSY_search_list*********************************
    #定位：人脉首页-搜索-集合列表-返回：点击
    def RMSY_search_list_back_click(self):
        return self.p.click(self.RMSY_search_list_back())

    #定位：人脉首页-搜索-集合列表-搜索输入框：输入
    def RMSY_search_list_searchinput_sendkeys(self, keys):
        return self.p.send_keys(self.RMSY_search_list_searchinput(), keys)

    #定位：人脉首页-搜索-集合列表-搜索按钮：点击
    def RMSY_search_list_searchbtn_click(self):
        return self.p.click(self.RMSY_search_list_searchbtn())

    #定位：人脉首页-搜索-集合列表-搜索按钮-搜索匹配成员列表
    def RMSY_search_list_searchbtn_matchlist_click(self, n):
        return self.p.click(self.RMSY_search_list_searchbtn_matchlist()[n])

    #---------------------------------------------------编辑所有元素定位------------------------------------------------------
    #定位：人脉首页-搜索-集合列表-编辑
    def RMSY_search_list_edit_click(self):
        return self.p.click(self.RMSY_search_list_edit())

    #定位：人脉首页-搜索-集合列表-编辑-返回
    def RMSY_search_list_edit_back_click(self):
        return self.p.click(self.RMSY_search_list_edit_back())

    #定位：人脉首页-搜索-集合列表-编辑-全选：点击
    def RMSY_search_list_edit_all_click(self):
        return self.p.click(self.RMSY_search_list_edit_all())

    #定位：人脉首页-搜索-集合列表-编辑-全选-取消：点击
    def RMSY_search_list_edit_all_cancel_click(self):
        return self.p.click(self.RMSY_search_list_edit_all_cancel())

    #定位：人脉首页-搜索-集合列表-编辑-选择成员：点击
    def RMSY_search_list_edit_selectmember_click(self, n):
        return self.p.click(self.RMSY_search_list_edit_selectmember()[n])

    #定位：人脉首页-搜索-集合列表-编辑-删除和还原
    #---------------------------------------------------成员列表所有元素定位------------------------------------------------------
    #定位：人脉首页-搜索-集合列表-成员列表：点击
    def RMSY_search_list_memberlist_click(self, n):
        return self.p.click(self.RMSY_search_list_memberlist()[n])

#*********************************【PAGE2】名片设置：RMSY_contacts_menu_cardsetting*********************************
    #定位：人脉首页-点击联系人-打开主菜单-名片设置-返回：点击
    def RMSY_contacts_menu_cardsetting_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-全部屏蔽：点击
    def RMSY_contacts_menu_cardsetting_sheildall_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_sheildall())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-一对一会话：点击
    def RMSY_contacts_menu_cardsetting_o2o_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_o2o())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-姓名：点击
    def RMSY_contacts_menu_cardsetting_name_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_name())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-手机：点击
    def RMSY_contacts_menu_cardsetting_tel_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_tel())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-邮箱：点击
    def RMSY_contacts_menu_cardsetting_mail_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_mail())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-QQ：点击
    def RMSY_contacts_menu_cardsetting_qq_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_qq())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-开放名片列表：点击
    def RMSY_contacts_menu_cardsetting_cardlist_click(self, n):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_cardlist()[n])

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览：点击
    def RMSY_contacts_menu_cardsetting_preview_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting_preview())

#*********************************【PAGE2】热度设置：RMSY_contacts_menu_heatsetting*********************************
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-返回按钮：点击
    def RMSY_contacts_menu_heatsetting_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_back())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-全部打开：点击
    def RMSY_contacts_menu_heatsetting_openall_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_openall())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-响铃图形：点击
    def RMSY_contacts_menu_heatsetting_bellgraph_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_bellgraph())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话：点击
    def RMSY_contacts_menu_heatsetting_p2pconversation_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting_p2pconversation())

#*********************************【PAGE2】标签：RMSY_contacts_menu_tag*********************************
    #定位：人脉首页-点击联系人-打开主菜单-标签-返回：点击
    def RMSY_contacts_menu_tag_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_tag_back())

    #定位：人脉首页-点击联系人-打开主菜单-标签-保存：点击
    def RMSY_contacts_menu_tag_save_click(self):
        return self.p.click(self.RMSY_contacts_menu_tag_save())

    #定位：人脉首页-点击联系人-打开主菜单-标签-选择标签类型：点击
    def RMSY_contacts_menu_tag_tagtype_click(self, n):
        return self.p.click(self.RMSY_contacts_menu_tag_tags()[n])

    #定位：人脉首页-点击联系人-打开主菜单-标签-选择标签：点击
    def RMSY_contacts_menu_tag_tags_click(self, n):
        return self.p.click(self.RMSY_contacts_menu_tag_tags()[n])

    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签：点击
    def RMSY_contacts_menu_tag_customtag_click(self):
        return self.p.click(self.RMSY_contacts_menu_tag_customtag())

#*********************************【PAGE2】备忘：RMSY_contacts_menu_memo*********************************
    #定位：人脉首页-点击联系人-打开主菜单-备忘-返回：点击
    def RMSY_contacts_menu_memo_back_click(self):
        return self.p.click(self.RMSY_contacts_menu_memo_back())

    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注：点击
    def RMSY_contacts_menu_memo_changenotename_click(self):
        return self.p.click(self.RMSY_contacts_menu_memo_changenotename())

    #定位：人脉首页-点击联系人-打开主菜单-备忘-备忘内容：输入
    def RMSY_contacts_menu_memo_memocontent_sendkeys(self, content):
        return self.p.send_keys(self.RMSY_contacts_menu_memo_memocontent(), content)

    #定位：人脉首页-点击联系人-打开主菜单-备忘-备忘内容-确定：点击
    def RMSY_contacts_menu_memo_memocontent_confirm_click(self):
        return self.p.click(self.RMSY_contacts_menu_memo_memocontent_confirm())

#*********************************【PAGE2】消息输入框：RMSY_contacts_message*********************************
    #定位：人脉首页-点击联系人-消息-返回：点击
    def RMSY_contacts_msg_back_click(self):
        return self.p.click(self.RMSY_contacts_msg_back())

    #定位：人脉首页-点击联系人-消息-主菜单：点击
    def RMSY_contacts_msg_menu_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu())

    #---------------------------主菜单所有元素定位--------------------
    #定位：人脉首页-点击联系人-消息-主菜单-热度设置：点击
    def RMSY_contacts_msg_menu_heatsetting_click(self):
        return self.p.click(self.RMSY_contacts_msg_menu_heatsetting())

    #定位：人脉首页-点击联系人-消息-人形按钮：点击
    def RMSY_contacts_msg_humanbtn_click(self):
        return self.p.click(self.RMSY_contacts_msg_humanbtn())

    #定位：人脉首页-点击联系人-消息-消息输入框：输入
    def RMSY_contacts_msg_msginput_sendkeys(self, msg):
        return self.p.click(self.RMSY_contacts_msg_msginput(), msg)

    #定位：人脉首页-点击联系人-消息-发送消息：点击
    def RMSY_contacts_msg_msgsend_click(self):
        return self.p.click(self.RMSY_contacts_msg_msgsend())

    #定位：人脉首页-点击联系人-消息-表情按钮：点击
    def RMSY_contacts_msg_emoji_click(self):
        return self.p.click(self.RMSY_contacts_msg_emoji())

    #定位：人脉首页-点击联系人-消息-表情按钮-表情列表：点击
    def RMSY_contacts_msg_emoji_emojilist_click(self, n):
        return self.p.click(self.RMSY_contacts_msg_emoji_emojilist()[n])

    #定位：人脉首页-点击联系人-消息-功能按钮：点击
    def RMSY_contacts_msg_func_click(self):
        return self.p.click(self.RMSY_contacts_msg_func())

    #定位：人脉首页-点击联系人-消息-功能按钮-功能列表：点击
    def RMSY_contacts_msg_func_funclist_click(self, n):
        return self.p.click(self.RMSY_contacts_msg_func_funclist()[n])

#*********************************【PAGE2】删除：RMSY_Contacts_delete*********************************
    #定位：人脉首页-点击联系人-删除-取消：点击
    def RMSY_Contacts_delete_cancel_click(self):
        return self.p.click(self.RMSY_Contacts_delete_cancel())

    #定位：人脉首页-点击联系人-删除-确认：点击
    def RMSY_Contacts_delete_confirm_click(self):
        return self.p.click(self.RMSY_Contacts_delete_confirm())
