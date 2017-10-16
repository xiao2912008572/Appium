__author__ = 'xiaoj'
from StoneUIFramework.public.pages.yunku.YUNKUPAGE3 import _YUNKUPAGE3


class _SPACEHANDLE2(_YUNKUPAGE3):
    # *********************************【HADNLE1】云库-照片列表：YK_piclist_click*********************************
    # 云库-照片列表-返回：点击
    def Yk_piclist_back_click(self):
        return self.p.click(self.Yk_piclist_back)

    # 云库-照片列表-照片名称：获取文本
    def Yk_piclist_picanme_text(self):
        return self.p.get_text(self.Yk_piclist_picname)

    # 云库-照片列表-照片本身：点击
    def Yk_piclist_picself_click(self):
        return self.p.click(self.Yk_piclist_picself)

    # 云库-照片列表-照片本身-备注名：获取文本
    def Yk_piclist_picself_reamark_text(self):
        return self.p.get_text(self.Yk_piclist_picself_reamark)

    # 云库-照片列表-照片本身-照片总数：获取文本
    def Yk_piclist_picself_total_text(self):
        return self.p.get_text(self.Yk_piclist_picself_pictotal)

    # 云库-照片列表-菜单栏：点击
    def Yk_piclist_menu_click(self):
        return self.p.click(self.Yk_piclist_menu)

    # 云库-照片列表-菜单栏-分类：点击
    def Yk_piclist_menu_classify_click(self):
        return self.p.click(self.Yk_piclist_menu_classify)

        # 云库-照片列表-菜单栏-编辑：点击

    def Yk_piclist_menu_edit_click(self):
        return self.p.click(self.Yk_piclist_menu_edit)

    # *********************************【HANDLE1】云库-添加-相册Yk_add_ByAlbum_click*********************************
    # 云库-添加-相册-返回：点击
    def Yk_add_ByAlbum_back_click(self):
        return self.p.click(self.Yk_add_ByAlbum_back)

    # 云库-添加-相册-照片列表：点击
    def Yk_add_ByAlbum_piclist_click(self, n):
        return self.p.clicks(self.Yk_add_ByAlbum_piclist, n)

    # 云库-添加-相册-完成：点击
    def Yk_add_ByAlbum_confirm_click(self):
        return self.p.click(self.Yk_add_ByAlbum_piclist)

    # *********************************【HANDLE1】云库-搜索栏发送文本Yk_search_sendkeys*********************************
    # 云库-搜索栏-搜索按钮：点击
    def Yk_search_searchbtn_click(self):
        return self.p.click(self.Yk_search_searchbtn)

    # 云库-搜索栏-空间列表：点击
    def Yk_search_spacelist_click(self, n):
        return self.p.clicks(self.Yk_search_searchbtn, n)

    # 云库-搜索栏-空间列表-返回：点击
    def Yk_search_spacelist_back_click(self):
        return self.p.click(self.Yk_search_spacelist_back_click)

    # 云库-搜索栏-返回：点击
    def Yk_search_back(self):
        return self.p.click(self.Yk_search_back)

    # *********************************【HANDLE1】云库-菜单栏-照片列表-分类到Yk_menu_piclist_classify_click*********************************
    # 云库-菜单栏-照片列表-分类到-返回：点击
    def Yk_menu_piclist_classify_back_click(self):
        return self.p.click(self.Yk_menu_piclist_classify_back)

    # 云库-菜单栏-照片列表-分类到-确认：点击
    def Yk_menu_piclist_classify_confirm_click(self):
        return self.p.click(self.Yk_menu_piclist_classify_confirm)

    # 云库-菜单栏-照片列表-分类到-空间列表：点击
    def Yk_menu_piclist_classify_piclist_click(self, n):
        return self.p.clicks(self.Yk_menu_piclist_classify_piclist, n)

    # 云库-菜单栏-照片列表-分类到-空间列表-文件夹列表：点击
    def Yk_menu_piclist_classify_piclist_folder_click(self, n):
        return self.p.clicks(self.Yk_menu_piclist_classify_piclist_folder, n)

    # 云库-菜单栏-照片列表-分类到-空间列表-产品：点击
    def Yk_menu_piclist_classify_piclist_product_click(self):
        return self.p.clicks(self.Yk_menu_piclist_classify_piclist_folder, 0)

    # 云库-菜单栏-照片列表-分类到-空间列表-资讯：点击
    def Yk_menu_piclist_classify_piclist_archivies_click(self):
        return self.p.clicks(self.Yk_menu_piclist_classify_piclist_folder, 1)
