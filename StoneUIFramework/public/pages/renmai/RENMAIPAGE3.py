__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.RENMAIPAGE2 import _RENMAIPAGE2

class _RENMAIPAGE3(_RENMAIPAGE2):
#*********************************【PAGE2】搜索按钮：RMSY_search_searchbtn*********************************
    #定位：人脉首页-搜索-搜索按钮-返回按钮
    def RMSY_search_searchbtn_back(self):
        self.RMSY_search_searchbtn_backC = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-搜索-搜索按钮-返回按钮")
        return self.RMSY_search_searchbtn_backC

    #定位：人脉首页-搜索-搜索按钮-搜索输入框
    def RMSY_search_searchbtn_searchinput(self):
        self.RMSY_search_searchbtn_searchinputC = self.p.get_element("id->com.yunlu6.stone:id/edit_text", "人脉首页-搜索-搜索按钮-搜索输入框")
        return self.RMSY_search_searchbtn_searchinputC

    #定位：人脉首页-搜索-搜索按钮-搜索按钮
    def RMSY_search_searchbtn_searchbtn(self):
        self.RMSY_search_searchbtn_searchbtnC = self.p.get_element("id->com.yunlu6.stone:id/iv_search", "人脉首页-搜索-搜索按钮-搜索按钮")
        return self.RMSY_search_searchbtn_searchbtnC

    #定位：人脉首页-搜索-搜索按钮-主菜单
    def RMSY_search_searchbtn_menu(self):
        self.RMSY_search_searchbtn_menuC = self.p.get_element("id->com.yunlu6.stone:id/rl_more", "人脉首页-搜索-搜索按钮-主菜单")
        return self.RMSY_search_searchbtn_menuC

    #定位：人脉首页-搜索-搜索按钮-主菜单-批量操作
    def RMSY_search_searchbtn_menu_batchoperate(self):
        self.RMSY_search_searchbtn_menu_batchoperateC = self.p.get_element("id->com.yunlu6.stone:id/batch_operate", "人脉首页-搜索-搜索按钮-主菜单-批量操作")
        return self.RMSY_search_searchbtn_menu_batchoperateC

#*********************************【PAGE2】标签列表：RMSY_search_label*********************************
    #定位：人脉首页-搜索-标签列表-返回
    def RMSY_search_label_back(self):
        self.RMSY_search_label_backC = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-搜索-标签列表-返回")
        return self.RMSY_search_label_backC

    #定位：人脉首页-搜索-标签列表-搜索框
    def RMSY_search_label_searchinput(self):
        self.RMSY_search_label_searchinputC = self.p.get_element("id->com.yunlu6.stone:id/edit_text", "人脉首页-搜索-标签列表-搜索框")
        return self.RMSY_search_label_searchinputC

    #定位：人脉首页-搜索-标签列表-搜索按钮
    def RMSY_search_label_searchbtn(self):
        self.RMSY_search_label_searchbtnC = self.p.get_element("id->com.yunlu6.stone:id/iv_search", "人脉首页-搜索-标签列表-搜索按钮")
        return self.RMSY_search_label_searchbtnC

    #------------------------------人脉首页-搜索-标签列表-主菜单---------------------------
    #定位：人脉首页-搜索-标签列表-主菜单
    def RMSY_search_label_menu(self):
        self.RMSY_search_label_menuC = self.p.get_element("id->com.yunlu6.stone:id/iv_more", "人脉首页-搜索-标签列表-主菜单")
        return self.RMSY_search_label_menuC

    #------------------------------批量操作---------------------------
    #定位：人脉首页-搜索-标签列表-主菜单-批量操作
    def RMSY_search_label_menu_bcp(self):
        self.RMSY_search_label_menu_bcpC = self.p.get_element("id->com.yunlu6.stone:id/batch_operate", "人脉首页-搜索-标签列表-主菜单-批量操作")
        return self.RMSY_search_label_menu_bcpC

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-返回
    def RMSY_search_label_menu_bcp_back(self):
        self.RMSY_search_label_menu_bcp_backC = self.p.get_element("id->com.yunlu6.stone:id/iv_batch_back", "人脉首页-搜索-标签列表-主菜单-批量操作-返回")
        return self.RMSY_search_label_menu_bcp_backC

    #---------------------全选-----------------------
    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选
    def RMSY_search_label_menu_bcp_all(self):
        self.RMSY_search_label_menu_bcp_allC = self.p.get_element("id->com.yunlu6.stone:id/tv_all", "人脉首页-搜索-标签列表-主菜单-批量操作-全选")
        return self.RMSY_search_label_menu_bcp_allC

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-取消
    def RMSY_search_label_menu_bcp_all_all(self):
        self.RMSY_search_label_menu_bcp_all_allC = self.p.get_element("id->com.yunlu6.stone:id/tv_all", "人脉首页-搜索-标签列表-主菜单-批量操作-全选-取消")
        return self.RMSY_search_label_menu_bcp_all_allC

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-打标签

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-黑名单

    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-全选-换名片

    #---------------------------选择联系人---------------------------
    #定位：人脉首页-搜索-标签列表-主菜单-批量操作-选择联系人
    def RMSY_search_label_menu_bcp_selectcontact(self):
        self.RMSY_search_label_menu_bcp_selectcontactC = self.p.get_elements("id->com.yunlu6.stone:id/iv_select", "人脉首页-搜索-标签列表-主菜单-批量操作-选择联系人")
        return self.RMSY_search_label_menu_bcp_selectcontactC

    #------------------------------人脉首页-搜索-标签列表-标签成员列表---------------------------
    #定位：人脉首页-搜索-标签列表-标签成员列表
    def RMSY_search_label_memberlist(self):
        self.RMSY_search_label_memberlistC = self.p.get_elements("id->com.yunlu6.stone:id/item_name", "人脉首页-搜索-标签列表-标签成员列表")
        return self.RMSY_search_label_memberlistC

    #------------------------------人脉首页-搜索-标签列表-点击进入群聊---------------------------
    #定位：人脉首页-搜索-标签列表-点击进入群聊
    def RMSY_search_label_groupchat(self):
        row_x = self.driver.get_window_size()["width"]
        row_y = self.driver.get_window_size()["height"]
        scale_x = 720/ 1080
        scale_y = 1825 / 1920
        adjust_x = row_x * scale_x
        adjust_y = row_y * scale_y
        return self.driver.tap([(adjust_x, adjust_y)], 2)

#*********************************【PAGE2】集合列表：RMSY_search_list*********************************
    #定位：人脉首页-搜索-集合列表-返回
    def RMSY_search_list_back(self):
        self.RMSY_search_list_backC = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-搜索-集合列表-返回")
        return self.RMSY_search_list_backC

    #定位：人脉首页-搜索-集合列表-搜索输入框
    def RMSY_search_list_searchinput(self):
        self.RMSY_search_list_searchinputC = self.p.get_element("id->com.yunlu6.stone:id/edit_text", "人脉首页-搜索-集合列表-搜索输入框")
        return self.RMSY_search_list_searchinputC

    #定位：人脉首页-搜索-集合列表-搜索按钮
    def RMSY_search_list_searchbtn(self):
        self.RMSY_search_list_searchbtnC = self.p.get_element("id->com.yunlu6.stone:id/iv_search", "人脉首页-搜索-集合列表-搜索按钮")
        return self.RMSY_search_list_searchbtnC

    #定位：人脉首页-搜索-集合列表-搜索按钮-搜索匹配成员列表
    def RMSY_search_list_searchbtn_matchlist(self):
        self.RMSY_search_list_searchbtn_matchlistC = self.p.get_elements("id->com.yunlu6.stone:id/iv_arrow", "人脉首页-搜索-集合列表-搜索按钮-搜索匹配成员列表")
        return self.RMSY_search_list_searchbtn_matchlistC

    #---------------------------------------------------编辑所有元素定位------------------------------------------------------
    #定位：人脉首页-搜索-集合列表-编辑
    def RMSY_search_list_edit(self):
        self.RMSY_search_list_editC = self.p.get_element("id->com.yunlu6.stone:id/tv_edit", "人脉首页-搜索-集合列表-编辑")
        return self.RMSY_search_list_editC

    #定位：人脉首页-搜索-集合列表-编辑-返回
    def RMSY_search_list_edit_back(self):
        self.RMSY_search_list_edit_back = self.p.get_element("id->com.yunlu6.stone:id/iv_batch_back", "人脉首页-搜索-集合列表-编辑-返回")
        return self.RMSY_search_list_edit_back

    #定位：人脉首页-搜索-集合列表-编辑-全选
    def RMSY_search_list_edit_all(self):
        self.RMSY_search_list_edit_allC = self.p.get_element("id->com.yunlu6.stone:id/tv_all", "人脉首页-搜索-集合列表-编辑-全选")
        return self.RMSY_search_list_edit_allC

    #定位：人脉首页-搜索-集合列表-编辑-全选-取消
    def RMSY_search_list_edit_all_cancel(self):
        self.RMSY_search_list_edit_all_cancelC = self.p.get_element("id->com.yunlu6.stone:id/tv_all", "人脉首页-搜索-集合列表-编辑-全选-取消")
        return self.RMSY_search_list_edit_all_cancelC

    #定位：人脉首页-搜索-集合列表-编辑-选择成员
    def RMSY_search_list_edit_selectmember(self):
        self.RMSY_search_list_edit_selectmemberC = self.p.get_elements("id->com.yunlu6.stone:id/iv_select", "人脉首页-搜索-集合列表-编辑-选择成员")
        return self.RMSY_search_list_edit_selectmemberC

    #定位：人脉首页-搜索-集合列表-编辑-删除和还原

    #---------------------------------------------------成员列表所有元素定位------------------------------------------------------
    #定位：人脉首页-搜索-集合列表-成员列表
    def RMSY_search_list_memberlist(self):
        self.RMSY_search_list_memberlistC = self.p.get_elements("id->com.yunlu6.stone:id/iv_arrow", "人脉首页-搜索-集合列表-成员列表")
        return self.RMSY_search_list_memberlistC

#*********************************【PAGE2】名片设置：RMSY_contacts_menu_cardsetting*********************************
    #定位：人脉首页-点击联系人-打开主菜单-名片设置-返回
    def RMSY_contacts_menu_cardsetting_back(self):
        self.RMSY_contacts_menu_cardsetting_backC = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-点击联系人-打开主菜单-名片设置-返回")
        return self.RMSY_contacts_menu_cardsetting_backC

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-全部屏蔽
    def RMSY_contacts_menu_cardsetting_sheildall(self):
        self.RMSY_contacts_menu_cardsetting_sheildallC = self.p.get_element("id->com.yunlu6.stone:id/vsb_link", "人脉首页-点击联系人-打开主菜单-名片设置-全部屏蔽")
        return self.RMSY_contacts_menu_cardsetting_sheildallC

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-一对一会话
    def RMSY_contacts_menu_cardsetting_o2o(self):
        self.RMSY_contacts_menu_cardsetting_o2oC = self.p.get_element("id->com.yunlu6.stone:id/vsb_one_one", "人脉首页-点击联系人-打开主菜单-名片设置-一对一会话")
        return self.RMSY_contacts_menu_cardsetting_o2oC

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-姓名
    def RMSY_contacts_menu_cardsetting_name(self):
        self.RMSY_contacts_menu_cardsetting_nameC = self.p.get_element("id->com.yunlu6.stone:id/sb_name_bt", "人脉首页-点击联系人-打开主菜单-名片设置-姓名")
        return self.RMSY_contacts_menu_cardsetting_nameC

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-手机
    def RMSY_contacts_menu_cardsetting_tel(self):
        self.RMSY_contacts_menu_cardsetting_telC = self.p.get_element("id->com.yunlu6.stone:id/sb_nub_bt", "人脉首页-点击联系人-打开主菜单-名片设置-手机")
        return self.RMSY_contacts_menu_cardsetting_telC

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-邮箱
    def RMSY_contacts_menu_cardsetting_mail(self):
        self.RMSY_contacts_menu_cardsetting_mail = self.p.get_element("id->com.yunlu6.stone:id/sb_em_bt", "人脉首页-点击联系人-打开主菜单-名片设置-邮箱")
        return self.RMSY_contacts_menu_cardsetting_mail

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-QQ
    def RMSY_contacts_menu_cardsetting_qq(self):
        self.RMSY_contacts_menu_cardsetting_qqC = self.p.get_element("id->com.yunlu6.stone:id/sb_qq_bt", "人脉首页-点击联系人-打开主菜单-名片设置-QQ")
        return self.RMSY_contacts_menu_cardsetting_qqC

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-开放名片列表
    def RMSY_contacts_menu_cardsetting_cardlist(self):
        self.RMSY_contacts_menu_cardsetting_cardlistC = self.p.get_elements("id->com.yunlu6.stone:id/toggle_button", "人脉首页-点击联系人-打开主菜单-名片设置-开放名片列表")
        return self.RMSY_contacts_menu_cardsetting_cardlistC

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览
    def RMSY_contacts_menu_cardsetting_preview(self):
        self.RMSY_contacts_menu_cardsetting_previewC = self.p.get_element("id->com.yunlu6.stone:id/btn_exchange", "人脉首页-点击联系人-打开主菜单-名片设置-预览")
        return self.RMSY_contacts_menu_cardsetting_previewC

#*********************************【PAGE2】热度设置：RMSY_contacts_menu_heatsetting*********************************
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-返回按钮
    def RMSY_contacts_menu_heatsetting_back(self):
        self.RMSY_contacts_menu_heatsetting_backC = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-点击联系人-打开主菜单-热度设置-返回按钮")
        return self.RMSY_contacts_menu_heatsetting_backC

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-全部打开
    def RMSY_contacts_menu_heatsetting_openall(self):
        self.RMSY_contacts_menu_heatsetting_openallC = self.p.get_element("id->com.yunlu6.stone:id/sb_all", "人脉首页-点击联系人-打开主菜单-热度设置-全部打开")
        return self.RMSY_contacts_menu_heatsetting_openallC

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-响铃图形
    def RMSY_contacts_menu_heatsetting_bellgraph(self):
        self.RMSY_contacts_menu_heatsetting_bellgraphC = self.p.get_element("id->com.yunlu6.stone:id/sb_conversation", "人脉首页-点击联系人-打开主菜单-热度设置-响铃图形")
        return self.RMSY_contacts_menu_heatsetting_bellgraphC

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话
    def RMSY_contacts_menu_heatsetting_p2pconversation(self):
        self.RMSY_contacts_menu_heatsetting_p2pconversationC = self.p.get_element("id->com.yunlu6.stone:id/rl_conversation", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话")
        return self.RMSY_contacts_menu_heatsetting_p2pconversationC

#*********************************【PAGE2】标签：RMSY_contacts_menu_tag*********************************
    #定位：人脉首页-点击联系人-打开主菜单-标签-返回
    def RMSY_contacts_menu_tag_back(self):
        self.RMSY_contacts_menu_tag_backC = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-点击联系人-打开主菜单-标签-返回")
        return self.RMSY_contacts_menu_tag_backC

    #定位：人脉首页-点击联系人-打开主菜单-标签-保存
    def RMSY_contacts_menu_tag_save(self):
        self.RMSY_contacts_menu_tag_saveC = self.p.get_element("id->com.yunlu6.stone:id/iv_confirm", "人脉首页-点击联系人-打开主菜单-标签-返回")
        return self.RMSY_contacts_menu_tag_saveC

    #定位：人脉首页-点击联系人-打开主菜单-标签-选择标签类型
    def RMSY_contacts_menu_tag_tagtype(self):
        self.RMSY_contacts_menu_tag_tagtypeC = self.p.get_elements("id->com.yunlu6.stone:id/tv_name", "人脉首页-点击联系人-打开主菜单-标签-选择标签类型")
        return self.RMSY_contacts_menu_tag_tagtypeC

    #定位：人脉首页-点击联系人-打开主菜单-标签-选择标签
    def RMSY_contacts_menu_tag_tags(self):
        self.RMSY_contacts_menu_tag_tagsC = self.p.get_elements("id->com.yunlu6.stone:id/tag_id", "人脉首页-点击联系人-打开主菜单-标签-选择标签")
        return self.RMSY_contacts_menu_tag_tagsC

    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签
    def RMSY_contacts_menu_tag_customtag(self):
        self.RMSY_contacts_menu_tag_customtagC = self.p.get_element("id->com.yunlu6.stone:id/iv_add", "人脉首页-点击联系人-打开主菜单-标签-自定义标签")
        return self.RMSY_contacts_menu_tag_customtagC

#*********************************【PAGE2】备忘：RMSY_contacts_menu_memo*********************************
    #定位：人脉首页-点击联系人-打开主菜单-备忘-返回
    def RMSY_contacts_menu_memo_back(self):
        self.RMSY_contacts_menu_memo_backC = self.p.get_element("id->com.yunlu6.stone:id/iv_back", "人脉首页-点击联系人-打开主菜单-备忘-返回")
        return self.RMSY_contacts_menu_memo_backC

    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注
    def RMSY_contacts_menu_memo_changenotename(self):
        self.RMSY_contacts_menu_memo_changenotenameC = self.p.get_element("id->com.yunlu6.stone:id/bt_edit", "人脉首页-点击联系人-打开主菜单-备忘-修改备注")
        return self.RMSY_contacts_menu_memo_changenotenameC

    #定位：人脉首页-点击联系人-打开主菜单-备忘-备忘内容
    def RMSY_contacts_menu_memo_memocontent(self):
        self.RMSY_contacts_menu_memo_memocontentC = self.p.get_element("id->com.yunlu6.stone:id/et_memo_info", "人脉首页-点击联系人-打开主菜单-备忘-备忘内容")
        return self.RMSY_contacts_menu_memo_memocontentC

    #定位：人脉首页-点击联系人-打开主菜单-备忘-备忘内容-确定
    def RMSY_contacts_menu_memo_memocontent_confirm(self):
        self.RMSY_contacts_menu_memo_memocontent_confirmC = self.p.get_element("id->com.yunlu6.stone:id/bt_confirm", "人脉首页-点击联系人-打开主菜单-备忘-备忘内容-确定")
        return self.RMSY_contacts_menu_memo_memocontent_confirmC

#*********************************【PAGE2】消息输入框：RMSY_contacts_message*********************************
    #定位：人脉首页-点击联系人-消息-返回
    def RMSY_contacts_msg_back(self):
        self.RMSY_contacts_msg_backC = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-点击联系人-消息-返回")
        return self.RMSY_contacts_msg_backC

    #定位：人脉首页-点击联系人-消息-主菜单
    def RMSY_contacts_msg_menu(self):
        self.RMSY_contacts_msg_menuC = self.p.get_element("id->com.yunlu6.stone:id/title_main_fl_more_menu", "人脉首页-点击联系人-消息-主菜单")
        return self.RMSY_contacts_msg_menuC

    #---------------------------主菜单所有元素定位--------------------
    #定位：人脉首页-点击联系人-消息-主菜单-热度设置
    def RMSY_contacts_msg_menu_heatsetting(self):
        self.RMSY_contacts_msg_menu_heatsettingC = self.p.get_element("id->com.yunlu6.stone:id/rl_msgsetting", "人脉首页-点击联系人-消息-主菜单-热度设置")
        return self.RMSY_contacts_msg_menu_heatsettingC

    #定位：人脉首页-点击联系人-消息-人形按钮
    def RMSY_contacts_msg_humanbtn(self):
        self.RMSY_contacts_msg_humanbtnC = self.p.get_element("id->com.yunlu6.stone:id/iv_to_message", "人脉首页-点击联系人-消息-人形按钮")
        return self.RMSY_contacts_msg_humanbtnC

    #定位：人脉首页-点击联系人-消息-消息输入框
    def RMSY_contacts_msg_msginput(self):
        self.RMSY_contacts_msg_msginputC = self.p.get_element("id->com.yunlu6.stone:id/message_content_msgcontent", "人脉首页-点击联系人-消息-消息输入框")
        return self.RMSY_contacts_msg_msginputC

    #定位：人脉首页-点击联系人-消息-发送消息
    def RMSY_contacts_msg_msgsend(self):
        self.RMSY_contacts_msg_msgsendC = self.p.get_element("id->com.yunlu6.stone:id/message_content_send", "人脉首页-点击联系人-消息-发送消息")
        return self.RMSY_contacts_msg_msgsendC

    #定位：人脉首页-点击联系人-消息-表情按钮
    def RMSY_contacts_msg_emoji(self):
        self.RMSY_contacts_msg_emojiC = self.p.get_element("id->com.yunlu6.stone:id/iv_emoji", "人脉首页-点击联系人-消息-表情按钮")
        return self.RMSY_contacts_msg_emojiC

    #定位：人脉首页-点击联系人-消息-表情按钮-表情列表
    def RMSY_contacts_msg_emoji_emojilist(self):
        self.RMSY_contacts_msg_emoji_emojilistC = self.p.get_elements("id->com.yunlu6.stone:id/item_iv_face", "人脉首页-点击联系人-消息-表情按钮-表情列表")
        return self.RMSY_contacts_msg_emoji_emojilistC

    #定位：人脉首页-点击联系人-消息-功能按钮
    def RMSY_contacts_msg_func(self):
        self.RMSY_contacts_msg_funcC = self.p.get_element("id->com.yunlu6.stone:id/iv_send", "人脉首页-点击联系人-消息-功能按钮")
        return self.RMSY_contacts_msg_funcC

    #定位：人脉首页-点击联系人-消息-功能按钮-功能列表
    def RMSY_contacts_msg_func_funclist(self):
        self.RMSY_contacts_msg_func_funclistC = self.p.get_elements("id->com.yunlu6.stone:id/iv", "人脉首页-点击联系人-消息-功能按钮-功能列表")
        return self.RMSY_contacts_msg_func_funclistC

#*********************************【PAGE2】删除：RMSY_Contacts_delete*********************************
    #定位：人脉首页-点击联系人-删除-取消
    def RMSY_Contacts_delete_cancel(self):
        self.RMSY_Contacts_delete_cancelC = self.p.get_element("id->com.yunlu6.stone:id/bt_cancel", "人脉首页-点击联系人-删除-取消")
        return self.RMSY_Contacts_delete_cancelC

    #定位：人脉首页-点击联系人-删除-确认
    def RMSY_Contacts_delete_confirm(self):
        self.RMSY_Contacts_delete_confirmC = self.p.get_element("id->com.yunlu6.stone:id/bt_affirm", "人脉首页-点击联系人-删除-确认")
        return self.RMSY_Contacts_delete_confirmC
