__author__ = 'xiaoj'
# 空间首页
from YunluFramework.public.pages.space.SPACEPAGE6 import SPACEPAGE6

class SPACEHANDLE1(SPACEPAGE6):

    # ******************************************************【HANDLE1】******************************************************
    # 空间列表：点击
    def Kjlb_click(self):
        return self.p.click(self.Kjlb)

    # 空间列表-加号按钮:点击
    def Kjlb_mainmenu_click(self):
        return self.p.click(self.Kjlb_mainmenu)

    # 空间列表-浏览企业空间列表(通过ID查找)：获取空间名
    def Kjlb_browseorgspaceByID_text(self):
        return self.Kjlb_browseorgspaceByIDS().text

    # 空间列表-浏览企业空间列表(通过ID查找)
    def Kjlb_browseorgspaceByID_click(self):
        return self.p.click(self.Kjlb_browseorgspaceByID)  # n代表索引

    # 空间列表-浏览企业空间(通过name查找)
    def Kjlb_browseorgspaceByName_click(self, name):
        return self.p.click(self.Kjlb_browseorgspaceByName(name))

    # 空间列表-获取空间元素列表
    def Kjlb_browseorgspace_getElements(self):
        return self.p.get_elements(self.Kjlb_browseorgspaceByID[0], self.Kjlb_browseorgspaceByID[1])

    # 空间列表-搜索按钮:点击
    def Kjlb_searchbutton_click(self):
        return self.p.click(self.Kjlb_searchbutton)

    # 空间列表-搜索框:发送文本
    def Kjlb_searchspace_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_searchspace, text)

    # 空间列表-搜索-返回：点击
    def Kjlb_search_back_click(self):
        return self.p.click(self.Kjlb_search_back)

    # 空间列表-主菜单-'+机构空间':点击
    def Kjlb_mainmenu_newspace_click(self):
        return self.p.click(self.Kjlb_mainmenu_newspace)

    # 空间列表-主菜单-'+私人空间':点击
    def Kjlb_mainmenu_newpersonspace_click(self):
        return self.p.click(self.Kjlb_mainmenu_newpersonspace)

    # 空间列表-主菜单-分享名片:点击
    def Kjlb_mainmenu_sharecard_click(self):
        return self.p.click(self.Kjlb_mainmenu_sharecard)

    #空间列表-主菜单
