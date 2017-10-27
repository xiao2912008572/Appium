__author__ = 'xiaoj'
from YunluIFramework.public.pages.yunku.YUNKUPAGE3 import YUNKUPAGE3
from YunluIFramework.public.common.publicfunction import Tools


class YUNKUHANDLE1(YUNKUPAGE3):
    # ******************************************************【HANDLE1】******************************************************
    # 云库：点击
    def Yk_click(self):
        return self.p.click(self.Yk)

    # 云库-照片列表：点击
    def Yk_piclist_click(self, n):
        return self.p.clicks(self.Yk_piclist, n)
        # 云库-照片列表：点击

    def Yk_piclist_getElements(self):
        return self.p.get_elements(self.Yk_piclist[0],self.Yk_piclist[1])

    # 云库-添加：点击
    def Yk_add_click(self):
        return self.p.click(self.Yk_add)

    # 云库-添加-相册：点击
    def Yk_add_ByAlbum_click(self):
        return self.p.click(self.YK_add_byAlbum)

    # 云库-添加-拍照：点击
    def Yk_add_ByCamera_click(self):
        return self.p.click(self.YK_add_byCamera)

    # 云库-添加-拍照：点击
    def Yk_add_ByWifi_click(self):
        return self.p.click(self.YK_add_byWifi)

    # 云库-添加-取消：点击
    def Yk_add_cancel_click(self):
        return self.p.click(self.YK_add_cancel)

    # 云库-搜索栏：发送文本
    def Yk_search_sendkeys(self, text):
        return self.p.send_keys(self.YK_search, text)

    # 云库-搜索栏：点击
    def Yk_search_click(self):
        return self.p.click(self.YK_search)

    # 云库-搜索按钮：点击
    def Yk_searchbtn_click(self):
        return self.p.click(self.YK_searchbtn)

    # 云库-菜单栏：点击
    def Yk_menu_click(self):
        return self.p.click(self.YK_menu)

    # 云库-菜单栏-返回：点击
    def Yk_menu_back_click(self):
        return self.p.click(self.YK_menu_back)

    # 云库-菜单栏-取消：点击
    def Yk_menu_cancel_click(self):
        return self.p.click(self.YK_menu_cancel)

    # 云库-菜单栏-全选：点击
    def Yk_menu_all_click(self):
        return self.p.click(self.YK_menu_all)

    # 云库-菜单栏-照片列表：点击
    def Yk_menu_piclist_click(self, n):
        return self.p.clicks(self.YK_menu_all, n)

    # 云库-菜单栏-照片列表-分类到：点击
    def Yk_menu_piclist_classify_click(self):
        t = Tools(self.driver)
        t.click_element_by_coordinate(self.YK_menu_piclist_classify_x, self.YK_menu_piclist_classify_y)

    # 云库-菜单栏-照片列表-删除：点击
    def Yk_menu_piclist_delete_click(self):
        t = Tools(self.driver)
        t.click_element_by_coordinate(self.YK_menu_piclist_delete_x, self.YK_menu_piclist_delete_y)

    # 云库-菜单栏-照片列表-删除-是：点击
    def Yk_menu_piclist_delete_yes_click(self):
        return self.p.click(self.YK_menu_piclist_delete_yes)

    # 云库-菜单栏-照片列表-删除-否：点击
    def Yk_menu_piclist_delete_no_click(self):
        return self.p.click(self.YK_menu_piclist_delete_no)
