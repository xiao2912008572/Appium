__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.RENMAIPAGE7 import _RENMAIPAGE7

class _RENMAIHANDLE1(_RENMAIPAGE7):
#******************************************************【HANDLE1】******************************************************
    #定位：人脉首页：点击
    def RMSY_click(self):
        return self.p.click(self.RMSY())

    #定位：人脉首页-搜索输入框：点击
    def RMST_searchinput_click(self):
        return self.p.click(self.RMST_searchinput())

    #定位：人脉首页-搜索按钮：点击
    def RMSY_searchbtn_click(self):
        return self.p.click(self.RMSY_searchbtn())

    #定位：人脉首页-联系人列表：点击
    def RMSY_clickcontacts_click(self, n):
        return self.p.click(self.RMSY_clickcontacts()[n])

    #定位：人脉首页-同步通讯录：点击
    def RMSY_syscontacts_click(self):
        return self.p.click(self.RMSY_syscontacts())

    #定位：人脉首页-主菜单：点击
    def RMSY_menu_click(self):
        return self.p.click(self.RMSY_menu())

    #定位：人脉首页-主菜单-+人脉：点击
    def RMSY_menu_add_click(self):
        return self.p.click(self.RMSY_menu_add())

    #定位：人脉首页-主菜单-批量操作：点击
    def RMSY_menu_bcp_click(self):
        return self.p.click(self.RMSY_menu_bcp())

    #定位：人脉首页-主菜单-批量操作-返回：点击
    def RMSY_menu_bcp_back_click(self):
        return self.p.click(self.RMSY_menu_bcp_back())

    #定位：人脉首页-主菜单-批量操作-全选：点击
    def RMSY_menu_bcp_all_click(self):
        return self.p.click(self.RMSY_menu_bcp_all())

    #定位：人脉首页-主菜单-批量操作-全选-返回：点击
    def RMSY_menu_bcp_all_back_click(self):
        return self.p.click(self.RMSY_menu_bcp_all_back())

    #定位：人脉首页-主菜单-批量操作-全选-取消：点击
    def RMSY_menu_bcp_all_cancel_click(self):
        return self.p.click(self.RMSY_menu_bcp_all_cancel())

    #定位：人脉首页-主菜单-批量操作-全选-选择联系人：点击
    def RMSY_menu_bcp_all_select_click(self, n):
        return self.p.click(self.RMSY_menu_bcp_all_select()[n])

    #---------------------黑名单-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-黑名单

    #---------------------打标签-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-打标签

    #---------------------换名片-----------------------
    #定位：人脉首页-主菜单-批量操作-全选-换名片
