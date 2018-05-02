__author__ = 'xiaoj'
from YunluFramework.public.common.basepage import Page


class SPACEPAGE1(Page):
    # 定位:空间列表
    Kjlb = ('id->com.yunlu6.yunlu:id/navi_item_zone', '空间列表')

    # 空间列表-主菜单
    Kjlb_mainmenu = ("id->com.yunlu6.yunlu:id/title_main_tv_more_menu", "空间列表-主菜单")

    # +按钮
    Add_btn = ("id->com.yunlu6.yunlu:id/main_bottom_iv_addpuls", "空间列表-+按钮")

    # 空间列表-浏览空间列表(通过ID查找)
    Kjlb_browseorgspaceByID = ("id->com.yunlu6.yunlu:id/tvCompanyTitle", "空间列表-浏览企业空间(通过ID查找)")

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
    Kjlb_searchbutton = ("id->com.yunlu6.yunlu:id/iv_search_zone", "空间列表-搜索按钮")

    # 空间列表-搜索框
    Kjlb_searchspace = ("id->com.yunlu6.yunlu:id/edit_text", "空间列表-搜索框")

    # 空间列表-搜索-返回
    Kjlb_search_back = ("id->com.yunlu6.yunlu:id/clondzone_search_back", "空间列表-搜索-返回")

    # 空间列表-主菜单-'+机构空间'
    # Kjlb_mainmenu_newspace = ("name->机构空间", "定位空间列表-主菜单-'+机构空间'")
    # Kjlb_mainmenu_newspace = ("name->企业", "定位空间列表-主菜单-'+机构空间'")
    Kjlb_mainmenu_newspace = ("id->com.yunlu6.yunlu:id/tv_name", "定位空间列表-主菜单-'+机构空间'")

    # 空间列表-主菜单-'+私人空间'
    Kjlb_mainmenu_newpersonspace = ("name->私人空间", "空间列表-主菜单-'+私人空间'")

    # 空间列表-主菜单-分享名片
    Kjlb_mainmenu_sharecard = ("name->分析", "空间列表-主菜单-分享")
