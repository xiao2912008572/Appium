__author__ = 'xiaoj'
from YunluFramework.public.common.basepage import Page


class SPACEPAGE1(Page):
    # 定位:空间列表
    Kjlb = ('id->com.yunlu6.yunlu:id/navi_item_zone', '空间列表')

    # 空间列表-主菜单(加号按钮)
    Kjlb_mainmenu = ("id->com.yunlu6.yunlu:id/main_bottom_iv_addpuls", "空间列表-+按钮")

    # 空间列表-浏览空间列表(通过ID查找)
    Kjlb_browseorgspaceByID = ("id->com.yunlu6.yunlu:id/zone_company_title", "空间列表-浏览企业空间(通过ID查找)")

    # 空间列表-浏览空间列表(通过ID查找)
    def Kjlb_browseorgspaceByIDS(self):
        self.Kjlb_browseorgspaceByIDS = self.p.get_elements("id->com.yunlu6.yunlu:id/zone_company_title",
                                                            "空间列表-浏览企业空间(通过ID查找)")
        return self.Kjlb_browseorgspaceByIDS

    # 空间列表-浏览空间(通过name查找)
    def Kjlb_browseorgspaceByName(self, name):
        Kjlb_browseorgspaceByName = ("name->%s" % name, "定位空间列表-浏览企业空间(通过Name查找)失败")
        return Kjlb_browseorgspaceByName

    # 空间列表-搜索按钮
    Kjlb_searchbutton = ("id->com.yunlu6.yunlu:id/navi_item_zone", "空间列表-搜索按钮")

    # 空间列表-搜索框
    Kjlb_searchspace = ("id->com.yunlu6.yunlu:id/edit_text", "空间列表-搜索框")

    # 空间列表-主菜单-'+机构空间'
    Kjlb_mainmenu_newspace = ("id->com.yunlu6.yunlu:id/cloundzone_bottom_companyzone", "定位空间列表-主菜单-'+机构空间'失败")

    # 空间列表-主菜单-'+私人空间'
    Kjlb_mainmenu_newpersonspace = ("id->com.yunlu6.yunlu:id/cloundzone_bottom_personzone", "空间列表-主菜单-'+私人空间'")

    # 空间列表-主菜单-分享名片
    Kjlb_mainmenu_sharecard = ("id->com.yunlu6.yunlu:id/btn_share_space", "空间列表-主菜单-分享名片")
