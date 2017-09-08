__author__ = 'xiaoj'
from StoneUIFramework.public.common.basepage import Page

class _SPACEPAGE1(Page):
    #定位:空间列表
    def Kjlb(self):
        self.KjlbA = self.p.get_element("id->com.yunlu6.stone:id/navi_item_zone","空间列表")
        return self.KjlbA

    # # 空间列表-主菜单
    # def Kjlb_mainmenu(self):
    #     self.Kjlb_mainmenuA = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-主菜单")
    #     return self.Kjlb_mainmenuA

    # 空间列表-主菜单(加号按钮)
    def Kjlb_mainmenu(self):
        self.Kjlb_mainmenuA = self.p.get_element("id->com.yunlu6.stone:id/cloundzone_bottom_more","空间列表-主菜单")
        return self.Kjlb_mainmenuA

    # 空间列表-浏览空间列表(通过ID查找)
    def Kjlb_browseorgspaceByID(self):
        self.Kjlb_browseorgspaceByIDS = self.p.get_elements("id->com.yunlu6.stone:id/zone_company_title","空间列表-浏览企业空间(通过ID查找)")
        return self.Kjlb_browseorgspaceByIDS

    # 空间列表-浏览空间(通过name查找)
    def Kjlb_browseorgspaceByName(self,name):
        self.Kjlb_browseorgspaceByNameA = self.p.get_element("name->%s"%name,"定位空间列表-浏览企业空间(通过Name查找)失败")
        return self.Kjlb_browseorgspaceByNameA

    # 空间列表-搜索按钮
    def Kjlb_searchbutton(self):
        self.Kjlb_searchbuttonA = self.p.get_element("id->com.yunlu6.stone:id/navi_item_zone","空间列表-搜索按钮")
        return self.Kjlb_searchbuttonA

    # 空间列表-搜索框
    def Kjlb_searchspace(self):
        self.Kjlb_searchspaceA = self.p.get_element("id->com.yunlu6.stone:id/edit_text","空间列表-搜索框")
        return self.Kjlb_searchspaceA

    # 空间列表-主菜单-'+机构空间'
    def Kjlb_mainmenu_newspace(self):
        self.Kjlb_mainmenu_newspaceA = self.p.get_element("id->com.yunlu6.stone:id/cloundzone_bottom_companyzone","定位空间列表-主菜单-'+机构空间'失败")
        return self.Kjlb_mainmenu_newspaceA

    # 空间列表-主菜单-'+私人空间'
    def Kjlb_mainmenu_newpersonspace(self):
        self.Kjlb_mainmenu_newpersonspaceP = self.p.get_element("id->com.yunlu6.stone:id/cloundzone_bottom_personzone","空间列表-主菜单-'+私人空间'")
        return self.Kjlb_mainmenu_newpersonspaceP

    # 空间列表-主菜单-分享名片
    def Kjlb_mainmenu_sharecard(self):
        self.Kjlb_mainmenu_sharecardA = self.p.get_element("id->com.yunlu6.stone:id/btn_share_space","空间列表-主菜单-分享名片")
        return self.Kjlb_mainmenu_sharecardA