__author__ = 'Administrator'
from StoneUIFramework.public.common.basepage import Page

class _RENMAIPAGE1(Page):
    #定位：人脉首页
    def RMSY(self):
        self.RMSYC = self.p.get_element("id->com.yunlu6.stone:id/navi_item_connection", "人脉首页")
        return self.RMSYC

    #定位：人脉首页-搜索输入框
    def RMST_searchinput(self):
        self.RMST_searchinputC = self.p.get_element("id->com.yunlu6.stone:id/img_btn_search", "人脉首页-搜索输入框")
        return self.RMST_searchinputC

    #定位：人脉首页-搜索按钮
    def RMSY_searchbtn(self):
        self.RMSY_searchbtnC = self.p.get_element("id->com.yunlu6.stone:id/iv", "人脉首页-搜索输入框")
        return self.RMSY_searchbtnC

    #定位：人脉首页-联系人列表
    def RMSY_clickcontacts(self):
        self.RMSY_clickcontactsC = self.p.get_elements("id->com.yunlu6.stone:id/iv_arrow", "人脉首页-点击联系人")
        return self.RMSY_clickcontactsC

    #定位：人脉首页-同步通讯录
    def RMSY_syscontacts(self):
        self.RMSY_syscontactsC = self.p.get_element("id->com.yunlu6.stone:id/bt_start_mailer", "人脉首页-同步通讯录")
        return self.RMSY_syscontactsC

    #定位：人脉首页-主菜单
    def RMSY_menu(self):
        self.RMSY_menuC = self.p.get_elements("id->com.yunlu6.stone:id/iv_right", "人脉首页-主菜单")
        return self.RMSY_menuC

    #定位：人脉首页-主菜单-+人脉
    def RMSY_menu_add(self):
        self.RMSY_menu_addC = self.p.get_element("id->com.yunlu6.stone:id/contacts_expand", "人脉首页-主菜单-+人脉")
        return self.RMSY_menu_addC

    #定位：人脉首页-主菜单-批量操作
    def RMSY_menu_bcp(self):
        self.RMSY_menu_bcpC = self.p.get_element("id->com.yunlu6.stone:id/batch_operate", "人脉首页-主菜单-批量操作")
        return self.RMSY_menu_bcpC

    #定位：人脉首页-主菜单-批量操作-返回
    def RMSY_menu_bcp_back(self):
        self.RMSY_menu_bcp_backC = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-主菜单-批量操作-返回")
        return self.RMSY_menu_bcp_backC

    #定位：人脉首页-主菜单-批量操作-全选
    def RMSY_menu_bcp_all(self):
        self.RMSY_menu_bcp_allC = self.p.get_element("id->com.yunlu6.stone:id/tv_all", "人脉首页-主菜单-批量操作-全选")
        return self.RMSY_menu_bcp_allC

    #定位：人脉首页-主菜单-批量操作-全选-返回
    def RMSY_menu_bcp_all_back(self):
        self.RMSY_menu_bcp_all_backC = self.p.get_element("id->com.yunlu6.stone:id/title_back", "人脉首页-主菜单-批量操作-全选-返回")
        return self.RMSY_menu_bcp_all_backC

    #定位：人脉首页-主菜单-批量操作-全选-取消
    def RMSY_menu_bcp_all_cancel(self):
        self.RMSY_menu_bcp_all_cancelC = self.p.get_element("id->com.yunlu6.stone:id/tv_all", "人脉首页-主菜单-批量操作-全选-取消")
        return self.RMSY_menu_bcp_all_cancelC

    #定位：人脉首页-主菜单-批量操作-全选-选择联系人
    def RMSY_menu_bcp_all_select(self):
        self.RMSY_menu_bcp_all_selectC = self.p.get_elements("id->com.yunlu6.stone:id/tv_all", "人脉首页-主菜单-批量操作-全选-选择联系人")
        return self.RMSY_menu_bcp_all_selectC

    #---------------------黑名单-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-黑名单

    #---------------------打标签-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-打标签

    #---------------------换名片-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-换名片
