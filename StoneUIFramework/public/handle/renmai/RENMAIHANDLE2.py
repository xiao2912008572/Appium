__author__ = 'Administrator'
from StoneUIFramework.public.handle.renmai.RENMAIHANDLE1 import _RENMAIHANDLE1

class _RENMAIHANDLE2(_RENMAIHANDLE1):
#******************************************************【HANDLE2】******************************************************
#*********************************【PAGE1】+同步通讯录：RMSY_syscontacts*********************************
    #定位：人脉首页-同步通讯录-返回：点击
    def RMSY_syncContacts_back_click(self):
        return self.p.click(self.RMSY_syncContacts_back())

    #定位：人脉首页-同步通讯录-立即同步：点击
    def RMSY_syncContacts_confirm_click(self):
        return self.p.click(self.RMSY_syncContacts_confirm())

#*********************************【PAGE1】+主菜单++人脉：RMSY_menu_add*********************************
    #定位：人脉首页-主菜单-+人脉-返回：点击
    def RMSY_menu_add_back_click(self):
        return self.p.click(self.RMSY_menu_add_back())

    #定位：人脉首页-主菜单-+人脉-清空：点击
    def RMSY_menu_add_clear_click(self):
        return self.p.click(self.RMSY_menu_add_clear())

    #定位：人脉首页-主菜单-+人脉-输入姓名：输入姓名
    def RMSY_menu_add_nameinput_sendkeys(self, name):
        return self.p.send_keys(self.RMSY_menu_add_nameinput(), name)

    #定位：人脉首页-主菜单-+人脉-输入手机号：输入手机号
    def RMSY_menu_add_telinput_sendkeys(self, telphone):
        return self.p.send_keys(self.RMSY_menu_add_telinput(), telphone)

    #定位：人脉首页-主菜单-+人脉-同步手机通讯录：点击
    def RMSY_menu_add_syscontacts_click(self):
        return self.p.click(self.RMSY_menu_add_syscontacts())

    #定位：人脉首页-主菜单-+人脉-名片夹选择加入：点击
    def RMSY_menu_add_addbycard_click(self):
        return self.p.click(self.RMSY_menu_add_addbycard())

    #定位：人脉首页-主菜单-+人脉-添加：点击
    def RMSY_menu_add_add_click(self):
        return self.p.click(self.RMSY_menu_add_add())

#*********************************【PAGE1】点击联系人：RMSY_clickcontacts*********************************
    #定位：人脉首页-点击联系人-返回：点击
    def RMSY_contacts_back_click(self):
        return self.p.click(self.RMSY_contacts_back())

    #定位：人脉首页-点击联系人-打开主菜单：点击
    def RMSY_contacts_menu_click(self):
        return self.p.click(self.RMSY_contacts_menu())

    #定位：人脉首页-点击联系人-打开主菜单-名片设置：点击
    def RMSY_contacts_menu_cardsetting_click(self):
        return self.p.click(self.RMSY_contacts_menu_cardsetting())

    #定位：人脉首页-点击联系人-打开主菜单-热度设置：点击
    def RMSY_contacts_menu_heatsetting_click(self):
        return self.p.click(self.RMSY_contacts_menu_heatsetting())

    #定位：人脉首页-点击联系人-打开主菜单-标签：点击
    def RMSY_contacts_menu_tag_click(self):
        return self.p.click(self.RMSY_contacts_menu_tag())

    #定位：人脉首页-点击联系人-打开主菜单-备忘：点击
    def RMSY_contacts_menu_memo_click(self):
        return self.p.click(self.RMSY_contacts_menu_memo())

    #定位;人脉首页-点击联系人-联系方式列表：点击
    def RMSY_contacts_contactiontype_click(self, n):
        return self.p.click(self.RMSY_contacts_contactiontype()[n])

    #定位;人脉首页-点击联系人-消息按钮：点击
    def RMSY_contacts_messagebtn_click(self):
        return self.p.click(self.RMSY_contacts_messagebtn())

    #定位;人脉首页-点击联系人-消息输入框：输入消息
    def RMSY_contacts_message_sendkeys(self, msg):
        return self.p.send_keys(self.RMSY_contacts_message(), msg)

    #定位;人脉首页-点击联系人-删除：点击
    def RMSY_Contacts_delete_click(self):
        return self.p.click(self.RMSY_Contacts_delete())

    #定位;人脉首页-点击联系人-邀请方式：点击
    def RMSY_contacts_invatationtype_click(self, n):
        return self.p.click(self.RMSY_contacts_invatationtype()[n])

#*********************************【PAGE1】+搜索输入框：RMST_searchinput*********************************
    #定位：人脉首页-搜索-返回按钮：点击
    def RMSY_search_back_click(self):
        return self.p.click(self.RMSY_search_back())

    #定位：人脉首页-搜索-搜索输入框：输入消息
    def RMSY_search_searchinput_sendkeys(self, msg):
        return self.p.send_keys(self.RMSY_search_searchinput(), msg)

    #定位：人脉首页-搜索-搜索按钮：点击
    def RMSY_search_searchbtn_click(self):
        return self.p.click(self.RMSY_search_searchbtn())

    #定位：人脉首页-搜索-标签列表：点击
    def RMSY_search_label_click(self, n):
        return self.p.click(self.RMSY_search_label()[n])

    #定位：人脉首页-搜索-集合列表:点击
    def RMSY_search_list_click(self, n):
        return self.p.click(self.RMSY_search_list()[n])