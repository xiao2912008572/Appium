__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.RENMAIPAGE1 import RENMAIPAGE1

class RENMAIPAGE2(RENMAIPAGE1):
#*********************************【PAGE1】+同步通讯录：RMSY_syscontacts*********************************
    #定位：人脉首页-同步通讯录-返回
         RMSY_syscontacts_back = ("id->com.yunlu6.stone:id/iv_back", "人脉首页-同步通讯录-返回")

    #定位：人脉首页-同步通讯录-立即同步
         RMSY_syncContacts_confirm = ("id->com.yunlu6.stone:id/btn_synchro", "人脉首页-同步通讯录-立即同步")

#*********************************【PAGE1】+主菜单++人脉：RMSY_menu_add*********************************
    #定位：人脉首页-主菜单-+人脉-返回
         RMSY_menu_add_back = ("id->com.yunlu6.stone:id/title_main_more_back", "人脉首页-主菜单-+人脉-返回")

    #定位：人脉首页-主菜单-+人脉-清空
         RMSY_menu_add_clear = ("id->com.yunlu6.stone:id/title_main_tv_more_tv", "人脉首页-主菜单-+人脉-清空")

    #定位：人脉首页-主菜单-+人脉-输入姓名
         RMSY_menu_add_nameinput = ("id->com.yunlu6.stone:id/contact_name", "人脉首页-主菜单-+人脉-输入姓名")

    #定位：人脉首页-主菜单-+人脉-输入手机号
         RMSY_menu_add_telinput = ("id->com.yunlu6.stone:id/contact_mobile", "人脉首页-主菜单-+人脉-输入手机号")

    #定位：人脉首页-主菜单-+人脉-同步手机通讯录
         RMSY_menu_add_syscontacts = ("id->com.yunlu6.stone:id/btn_top", "人脉首页-主菜单-+人脉-同步手机通讯录")

    #定位：人脉首页-主菜单-+人脉-名片夹选择加入
         RMSY_menu_add_addbycard = ("id->com.yunlu6.stone:id/btn_card_add", "人脉首页-主菜单-+人脉-名片夹选择加入")

    #定位：人脉首页-主菜单-+人脉-添加
         RMSY_menu_add_add = ("id->com.yunlu6.stone:id/btn_add", "人脉首页-主菜单-+人脉-添加")

#*********************************【PAGE1】点击联系人：RMSY_clickcontacts*********************************
    #定位：人脉首页-点击联系人-返回
         RMSY_contacts_back = ("id->com.yunlu6.stone:id/iv_back", "人脉首页-点击联系人-返回")

    #定位：人脉首页-点击联系人-打开主菜单
         RMSY_contacts_menu = ("id->com.yunlu6.stone:id/iv_more", "人脉首页-点击联系人-打开主菜单")

    #定位：人脉首页-点击联系人-打开主菜单-名片设置
         RMSY_contacts_menu_cardsetting = ("id->com.yunlu6.stone:id/card_exchange", "人脉首页-点击联系人-打开主菜单-名片设置")

    #定位：人脉首页-点击联系人-打开主菜单-热度设置
         RMSY_contacts_menu_heatsetting = ("id->com.yunlu6.stone:id/anti", "人脉首页-点击联系人-打开主菜单-热度设置")

    #定位：人脉首页-点击联系人-打开主菜单-标签
         RMSY_contacts_menu_tag = ("id->com.yunlu6.stone:id/label", "人脉首页-点击联系人-打开主菜单-标签")

    #定位：人脉首页-点击联系人-打开主菜单-备忘
         RMSY_contacts_menu_memo = ("id->com.yunlu6.stone:id/memorandum", "人脉首页-点击联系人-打开主菜单-备忘")

    #定位;人脉首页-点击联系人-联系方式列表
         RMSY_contacts_contactiontype = ("id->com.yunlu6.stone:id/iv_contact", "人脉首页-点击联系人-选择联系方式")

    #定位;人脉首页-点击联系人-消息按钮
         RMSY_contacts_messagebtn = ("id->com.yunlu6.stone:id/iv_to_message", "人脉首页-点击联系人-消息按钮")

    #定位;人脉首页-点击联系人-消息输入框
         RMSY_contacts_message = ("id->com.yunlu6.stone:id/iv_to_message", "人脉首页-点击联系人-消息按钮")

    #定位;人脉首页-点击联系人-删除
         RMSY_Contacts_delete = ("id->com.yunlu6.stone:id/ll_blacklist", "人脉首页-点击联系人-删除")

    #定位;人脉首页-点击联系人-邀请方式
         RMSY_contacts_invatationtype = ("id->com.yunlu6.stone:id/iv_item_share", "人脉首页-点击联系人-邀请方式")

#*********************************【PAGE1】+搜索输入框：RMST_searchinput*********************************
    #定位：人脉首页-搜索-返回按钮
         RMSY_search_back = ("id->com.yunlu6.stone:id/iv_back", "人脉首页-搜索-返回")

    #定位：人脉首页-搜索-搜索输入框
         RMSY_search_searchinput = ("id->com.yunlu6.stone:id/img_btn_search", "人脉首页-搜索-搜索输入框")

    #定位：人脉首页-搜索-搜索按钮
         RMSY_search_searchbtn = ("id->com.yunlu6.stone:id/iv", "人脉首页-搜索-搜索按钮")

    #定位：人脉首页-搜索-标签列表
         RMSY_search_label = ("id->com.yunlu6.stone:id/tag_id", "人脉首页-搜索-标签列表")

    #定位：人脉首页-搜索-集合列表
         RMSY_search_list = ("id->com.yunlu6.stone:id/iv_arrow", "人脉首页-搜索-集合列表")