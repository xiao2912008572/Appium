__author__ = 'Administrator'
from YunluIFramework.public.pages.renmai.RENMAIPAGE2 import RENMAIPAGE2

class RENMAIPAGE3(RENMAIPAGE2):
#*********************************【PAGE2】搜索按钮：RMSY_search_searchbtn*********************************
    #定位：人脉首页-搜索-搜索按钮-返回按钮
        RMSY_search_searchbtn_back = ("id->com.yunlu6.yunlu:id/iv_back", "人脉首页-搜索-搜索按钮-返回按钮")

    #定位：人脉首页-搜索-搜索按钮-搜索输入框
        RMSY_search_searchbtn_searchinput = ("id->com.yunlu6.yunlu:id/edit_text", "人脉首页-搜索-搜索按钮-搜索输入框")

    #定位：人脉首页-搜索-搜索按钮-搜索按钮
        RMSY_search_searchbtn_searchbtn = ("id->com.yunlu6.yunlu:id/iv_search", "人脉首页-搜索-搜索按钮-搜索按钮")

    #定位：人脉首页-搜索-搜索按钮
        RMSY_search_searchbtn_menu = ("id->com.yunlu6.yunlu:id/rl_more", "人脉首页-搜索-搜索按钮")

    #定位：人脉首页-搜索-搜索按钮-批量操作
        RMSY_search_searchbtn_menu_batchoperate = ("id->com.yunlu6.yunlu:id/batch_operate", "人脉首页-搜索-搜索按钮-批量操作")

#*********************************【PAGE2】标签列表：RMSY_search_label*********************************
    #定位：人脉首页-搜索-标签列表-返回
        RMSY_search_label_back = ("id->com.yunlu6.yunlu:id/iv_back", "人脉首页-搜索-标签列表-返回")

    #定位：人脉首页-搜索-标签列表-搜索框
        RMSY_search_label_searchinput = ("id->com.yunlu6.yunlu:id/edit_text", "人脉首页-搜索-标签列表-搜索框")

    #定位：人脉首页-搜索-标签列表-搜索按钮
        RMSY_search_label_searchbtn = ("id->com.yunlu6.yunlu:id/iv_search", "人脉首页-搜索-标签列表-搜索按钮")

    #------------------------------人脉首页-搜索-标签列表---------------------------
    #定位：人脉首页-搜索-标签列表
        RMSY_search_label_menu = ("id->com.yunlu6.yunlu:id/iv_more", "人脉首页-搜索-标签列表")

    #------------------------------批量操作---------------------------
    #定位：人脉首页-搜索-标签列表-批量操作
        RMSY_search_label_menu_bcp = ("id->com.yunlu6.yunlu:id/batch_operate", "人脉首页-搜索-标签列表-批量操作")

    #定位：人脉首页-搜索-标签列表-批量操作-返回
        RMSY_search_label_menu_bcp_back = ("id->com.yunlu6.yunlu:id/iv_batch_back", "人脉首页-搜索-标签列表-批量操作-返回")

    #---------------------全选-----------------------
    #定位：人脉首页-搜索-标签列表-批量操作-全选
        RMSY_search_label_menu_bcp_all = ("id->com.yunlu6.yunlu:id/tv_all", "人脉首页-搜索-标签列表-批量操作-全选")

    #定位：人脉首页-搜索-标签列表-批量操作-全选-取消
        RMSY_search_label_menu_bcp_all_all = ("id->com.yunlu6.yunlu:id/tv_all", "人脉首页-搜索-标签列表-批量操作-全选-取消")

    #定位：人脉首页-搜索-标签列表-批量操作-全选-打标签

    #定位：人脉首页-搜索-标签列表-批量操作-全选-黑名单

    #定位：人脉首页-搜索-标签列表-批量操作-全选-换名片

    #---------------------------选择联系人---------------------------
    #定位：人脉首页-搜索-标签列表-批量操作-选择联系人
        RMSY_search_label_menu_bcp_selectcontact = ("id->com.yunlu6.yunlu:id/iv_select", "人脉首页-搜索-标签列表-批量操作-选择联系人")

    #------------------------------人脉首页-搜索-标签列表-标签成员列表---------------------------
    #定位：人脉首页-搜索-标签列表-标签成员列表
        RMSY_search_label_memberlist = ("id->com.yunlu6.yunlu:id/item_name", "人脉首页-搜索-标签列表-标签成员列表")

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
        RMSY_search_list_back = ("id->com.yunlu6.yunlu:id/iv_back", "人脉首页-搜索-集合列表-返回")

    #定位：人脉首页-搜索-集合列表-搜索输入框
        RMSY_search_list_searchinput = ("id->com.yunlu6.yunlu:id/edit_text", "人脉首页-搜索-集合列表-搜索输入框")

    #定位：人脉首页-搜索-集合列表-搜索按钮
        RMSY_search_list_searchbtn = ("id->com.yunlu6.yunlu:id/iv_search", "人脉首页-搜索-集合列表-搜索按钮")

    #定位：人脉首页-搜索-集合列表-搜索按钮-搜索匹配成员列表
        RMSY_search_list_searchbtn_matchlist = ("id->com.yunlu6.yunlu:id/iv_arrow", "人脉首页-搜索-集合列表-搜索按钮-搜索匹配成员列表")

    #---------------------------------------------------编辑所有元素定位------------------------------------------------------
    #定位：人脉首页-搜索-集合列表-编辑
        RMSY_search_list_edit = ("id->com.yunlu6.yunlu:id/tv_edit", "人脉首页-搜索-集合列表-编辑")

    #定位：人脉首页-搜索-集合列表-编辑-返回
        RMSY_search_list_edit_back = ("id->com.yunlu6.yunlu:id/iv_batch_back", "人脉首页-搜索-集合列表-编辑-返回")

    #定位：人脉首页-搜索-集合列表-编辑-全选
        RMSY_search_list_edit_all = ("id->com.yunlu6.yunlu:id/tv_all", "人脉首页-搜索-集合列表-编辑-全选")

    #定位：人脉首页-搜索-集合列表-编辑-全选-取消
        RMSY_search_list_edit_all_cancel = ("id->com.yunlu6.yunlu:id/tv_all", "人脉首页-搜索-集合列表-编辑-全选-取消")

    #定位：人脉首页-搜索-集合列表-编辑-选择成员
        RMSY_search_list_edit_selectmember = ("id->com.yunlu6.yunlu:id/iv_select", "人脉首页-搜索-集合列表-编辑-选择成员")

    #定位：人脉首页-搜索-集合列表-编辑-删除和还原

    #---------------------------------------------------成员列表所有元素定位------------------------------------------------------
    #定位：人脉首页-搜索-集合列表-成员列表
        RMSY_search_list_memberlist = ("id->com.yunlu6.yunlu:id/iv_arrow", "人脉首页-搜索-集合列表-成员列表")

#*********************************【PAGE2】名片设置：RMSY_contacts_menu_cardsetting*********************************
    #定位：人脉首页-点击联系人-打开主菜单-名片设置-返回
        RMSY_contacts_menu_cardsetting_back = ("id->com.yunlu6.yunlu:id/iv_back", "人脉首页-点击联系人-打开主菜单-名片设置-返回")

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-全部屏蔽
        RMSY_contacts_menu_cardsetting_sheildall = ("id->com.yunlu6.yunlu:id/vsb_link", "人脉首页-点击联系人-打开主菜单-名片设置-全部屏蔽")

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-一对一会话
        RMSY_contacts_menu_cardsetting_o2o = ("id->com.yunlu6.yunlu:id/vsb_one_one", "人脉首页-点击联系人-打开主菜单-名片设置-一对一会话")

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-姓名
        RMSY_contacts_menu_cardsetting_name = ("id->com.yunlu6.yunlu:id/sb_name_bt", "人脉首页-点击联系人-打开主菜单-名片设置-姓名")

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-手机
        RMSY_contacts_menu_cardsetting_tel = ("id->com.yunlu6.yunlu:id/sb_nub_bt", "人脉首页-点击联系人-打开主菜单-名片设置-手机")

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-邮箱
        RMSY_contacts_menu_cardsetting_mail = ("id->com.yunlu6.yunlu:id/sb_em_bt", "人脉首页-点击联系人-打开主菜单-名片设置-邮箱")

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-QQ
        RMSY_contacts_menu_cardsetting_qq = ("id->com.yunlu6.yunlu:id/sb_qq_bt", "人脉首页-点击联系人-打开主菜单-名片设置-QQ")

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-开放名片列表
        RMSY_contacts_menu_cardsetting_cardlist = ("id->com.yunlu6.yunlu:id/toggle_button", "人脉首页-点击联系人-打开主菜单-名片设置-开放名片列表")

    #定位：人脉首页-点击联系人-打开主菜单-名片设置-预览
        RMSY_contacts_menu_cardsetting_preview = ("id->com.yunlu6.yunlu:id/btn_exchange", "人脉首页-点击联系人-打开主菜单-名片设置-预览")

#*********************************【PAGE2】热度设置：RMSY_contacts_menu_heatsetting*********************************
    #定位：人脉首页-点击联系人-打开主菜单-热度设置-返回按钮
        RMSY_contacts_menu_heatsetting_back = ("id->com.yunlu6.yunlu:id/title_back", "人脉首页-点击联系人-打开主菜单-热度设置-返回按钮")

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-全部打开
        RMSY_contacts_menu_heatsetting_openall = ("id->com.yunlu6.yunlu:id/sb_all", "人脉首页-点击联系人-打开主菜单-热度设置-全部打开")

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-响铃图形
        RMSY_contacts_menu_heatsetting_bellgraph = ("id->com.yunlu6.yunlu:id/sb_conversation", "人脉首页-点击联系人-打开主菜单-热度设置-响铃图形")

    #定位：人脉首页-点击联系人-打开主菜单-热度设置-一对一会话
        RMSY_contacts_menu_heatsetting_p2pconversation = ("id->com.yunlu6.yunlu:id/rl_conversation", "人脉首页-点击联系人-打开主菜单-热度设置-一对一会话")

#*********************************【PAGE2】标签：RMSY_contacts_menu_tag*********************************
    #定位：人脉首页-点击联系人-打开主菜单-标签-返回
        RMSY_contacts_menu_tag_back = ("id->com.yunlu6.yunlu:id/iv_back", "人脉首页-点击联系人-打开主菜单-标签-返回")

    #定位：人脉首页-点击联系人-打开主菜单-标签-保存
        RMSY_contacts_menu_tag_save = ("id->com.yunlu6.yunlu:id/iv_confirm", "人脉首页-点击联系人-打开主菜单-标签-返回")

    #定位：人脉首页-点击联系人-打开主菜单-标签-选择标签类型
        RMSY_contacts_menu_tag_tagtype = ("id->com.yunlu6.yunlu:id/tv_name", "人脉首页-点击联系人-打开主菜单-标签-选择标签类型")

    #定位：人脉首页-点击联系人-打开主菜单-标签-选择标签
        RMSY_contacts_menu_tag_tags = ("id->com.yunlu6.yunlu:id/tag_id", "人脉首页-点击联系人-打开主菜单-标签-选择标签")

    #定位：人脉首页-点击联系人-打开主菜单-标签-自定义标签
        RMSY_contacts_menu_tag_customtag = ("id->com.yunlu6.yunlu:id/iv_add", "人脉首页-点击联系人-打开主菜单-标签-自定义标签")

#*********************************【PAGE2】备忘：RMSY_contacts_menu_memo*********************************
    #定位：人脉首页-点击联系人-打开主菜单-备忘-返回
        RMSY_contacts_menu_memo_back = ("id->com.yunlu6.yunlu:id/iv_back", "人脉首页-点击联系人-打开主菜单-备忘-返回")

    #定位：人脉首页-点击联系人-打开主菜单-备忘-修改备注
        RMSY_contacts_menu_memo_changenotename = ("id->com.yunlu6.yunlu:id/bt_edit", "人脉首页-点击联系人-打开主菜单-备忘-修改备注")

    #定位：人脉首页-点击联系人-打开主菜单-备忘-备忘内容
        RMSY_contacts_menu_memo_memocontent = ("id->com.yunlu6.yunlu:id/et_memo_info", "人脉首页-点击联系人-打开主菜单-备忘-备忘内容")

    #定位：人脉首页-点击联系人-打开主菜单-备忘-备忘内容-确定
        RMSY_contacts_menu_memo_memocontent_confirm = ("id->com.yunlu6.yunlu:id/bt_confirm", "人脉首页-点击联系人-打开主菜单-备忘-备忘内容-确定")

#*********************************【PAGE2】消息输入框：RMSY_contacts_message*********************************
    #定位：人脉首页-点击联系人-消息-返回
        RMSY_contacts_msg_back = ("id->com.yunlu6.yunlu:id/title_main_more_back", "人脉首页-点击联系人-消息-返回")

    #定位：人脉首页-点击联系人-消息
        RMSY_contacts_msg_menu = ("id->com.yunlu6.yunlu:id/title_main_fl_more_menu", "人脉首页-点击联系人-消息")

    #--------------------------所有元素定位--------------------
    #定位：人脉首页-点击联系人-消息-热度设置
        RMSY_contacts_msg_menu_heatsetting = ("id->com.yunlu6.yunlu:id/rl_msgsetting", "人脉首页-点击联系人-消息-热度设置")

    #定位：人脉首页-点击联系人-消息-人形按钮
        RMSY_contacts_msg_humanbtn = ("id->com.yunlu6.yunlu:id/iv_to_message", "人脉首页-点击联系人-消息-人形按钮")

    #定位：人脉首页-点击联系人-消息-消息输入框
        RMSY_contacts_msg_msginput = ("id->com.yunlu6.yunlu:id/message_content_msgcontent", "人脉首页-点击联系人-消息-消息输入框")

    #定位：人脉首页-点击联系人-消息-发送消息
        RMSY_contacts_msg_msgsend = ("id->com.yunlu6.yunlu:id/message_content_send", "人脉首页-点击联系人-消息-发送消息")

    #定位：人脉首页-点击联系人-消息-表情按钮
        RMSY_contacts_msg_emoji = ("id->com.yunlu6.yunlu:id/iv_emoji", "人脉首页-点击联系人-消息-表情按钮")

    #定位：人脉首页-点击联系人-消息-表情按钮-表情列表
        RMSY_contacts_msg_emoji_emojilist = ("id->com.yunlu6.yunlu:id/item_iv_face", "人脉首页-点击联系人-消息-表情按钮-表情列表")

    #定位：人脉首页-点击联系人-消息-功能按钮
        RMSY_contacts_msg_func = ("id->com.yunlu6.yunlu:id/iv_send", "人脉首页-点击联系人-消息-功能按钮")

    #定位：人脉首页-点击联系人-消息-功能按钮-功能列表
        RMSY_contacts_msg_func_funclist = ("id->com.yunlu6.yunlu:id/iv", "人脉首页-点击联系人-消息-功能按钮-功能列表")

#*********************************【PAGE2】删除：RMSY_Contacts_delete*********************************
    #定位：人脉首页-点击联系人-删除-取消
        RMSY_Contacts_delete_cancel = ("id->com.yunlu6.yunlu:id/bt_cancel", "人脉首页-点击联系人-删除-取消")

    #定位：人脉首页-点击联系人-删除-确认
        RMSY_Contacts_delete_confirm = ("id->com.yunlu6.yunlu:id/bt_affirm", "人脉首页-点击联系人-删除-确认")