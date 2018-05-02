__author__ = 'xiaoj'
from StoneUIFramework.public.handle.yunku.YUNKUHANDLE2 import YUNKUHANDLE2


class YUNKUHANDLE3(YUNKUHANDLE2):
    # *********************************【HANDLE2】云库-照片列表-菜单栏-分类Yk_piclist_menu_classify*********************************
    # 云库-照片列表-菜单栏-分类-返回：点击
    def Yk_piclist_back_click(self):
        return self.p.click(self.Yk_piclist_menu_classify_back)

    # 云库-照片列表-菜单栏-分类-确认：点击
    def Yk_piclist_menu_confirm_click(self):
        return self.p.click(self.Yk_piclist_menu_classify_confirm)

    # 云库-照片列表-菜单栏-分类-空间列表：点击
    def Yk_piclist_menu_classify_spacelist(self, n):
        return self.p.clicks(self.Yk_piclist_menu_classify_spacelist, n)

    # 云库-照片列表-菜单栏-分类-空间列表-文件夹：点击
    def Yk_piclist_menu_classify_spacelist_folder_click(self, n):
        return self.p.clicks(self.Yk_piclist_menu_classify_spacelist_folder, n)

    # 云库-照片列表-菜单栏-分类-空间列表-产品：点击
    def Yk_piclist_menu_classify_spacelist_product_click(self):
        return self.p.clicks(self.Yk_piclist_menu_classify_spacelist_product, 0)

    # 云库-照片列表-菜单栏-分类-空间列表-产品：点击
    def Yk_piclist_menu_classify_spacelist_archivies_click(self):
        return self.p.clicks(self.Yk_piclist_menu_classify_spacelist_archivies, 1)

    # *********************************【HANDLE3】云库-照片列表-菜单栏-编辑Yk_piclist_menu_edit_click*********************************
    # 云库-照片列表-菜单栏-编辑-返回：点击
    def Yk_piclist_menu_edit_back_click(self):
        return self.p.click(self.Yk_piclist_menu_edit_back)

    # 云库-照片列表-菜单栏-编辑-删除：点击
    def Yk_piclist_menu_edit_delete_click(self):
        return self.p.click(self.Yk_piclist_menu_edit_delete)

    # 云库-照片列表-菜单栏-编辑-删除-是：点击
    def Yk_piclist_menu_edit_delete_yes_click(self):
        return self.p.click(self.Yk_piclist_menu_edit_delete_yes)

    # 云库-照片列表-菜单栏-编辑-删除-否：点击
    def Yk_piclist_menu_edit_delete_no_click(self):
        return self.p.click(self.Yk_piclist_menu_edit_delete_no)

    # 云库-照片列表-菜单栏-编辑-名称：发送文本
    def Yk_piclist_menu_edit_name_sendkeys(self, text):
        return self.p.send_keys(self.Yk_piclist_menu_edit_name, text)

    # 云库-照片列表-菜单栏-编辑-备注：发送文本
    def Yk_piclist_menu_edit_remark_sendkeys(self, text):
        return self.p.send_keys(self.Yk_piclist_menu_edit_remark, text)

    # 云库-照片列表-菜单栏-编辑-保存：点击
    def Yk_piclist_menu_edit_save_click(self):
        return self.p.click(self.Yk_piclist_menu_edit_save)

    # *********************************【HANDLE2】云库-搜索栏-搜索按钮Yk_search_searchbtn*********************************
    # 云库-搜索栏-搜索按钮-返回：点击
    def Yk_search_searchbtn_back_click(self):
        return self.p.click(self.Yk_search_searchbtn_back)

    # 云库-搜索栏-搜索按钮-返回：点击
    def Yk_search_searchbtn_piclist_click(self, n):
        return self.p.clicks(self.Yk_search_searchbtn_piclist, n)
