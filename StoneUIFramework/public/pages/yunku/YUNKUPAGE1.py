__author__ = 'xiaoj'
from StoneUIFramework.public.common.basepage import Page


class YUNKUPAGE1(Page):
    # 定位:云库
    Yk = ('id->com.yunlu6.stone:id/navi_item_work_cloundlibrary', '云库')

    # 云库-照片列表
    Yk_piclist = ('id->com.yunlu6.stone:id/cloudlibrary_image_item', '云库-照片列表')

    # 云库-添加
    Yk_add = ('id->com.yunlu6.stone:id/cloundlibrary_bottom_more', '云库-添加')

    # 云库-添加-相册
    YK_add_byAlbum = ("id->com.yunlu6.stone:id/iv_cloundlibrary_alumm", "云库-添加-相册")

    # 云库-添加-拍照
    YK_add_byCamera = ("id->com.yunlu6.stone:id/iv_cloundlibrary_camera", "云库-添加-拍照")

    # 云库-添加-wifi
    YK_add_byWifi = ("id->com.yunlu6.stone:id/iv_cloundlibrary_yun", "云库-添加-wifi同步")

    # 云库-添加-取消
    YK_add_cancel = ("id->com.yunlu6.stone:id/bt_commen_cancel", "云库-添加-取消")

    # 云库-搜索栏
    YK_search = ("id->com.yunlu6.stone:id/img_btn_search_search_cloundlibrary", "云库-搜索栏")

    # 云库-搜索按钮
    YK_searchbtn = ("id->com.yunlu6.stone:id/search_tv_search", "云库-搜索按钮")

    # 云库-菜单栏
    YK_menu = ("id->com.yunlu6.stone:id/iv_right_cloundlibrary_menu", "云库-菜单栏")

    # 云库-菜单栏-返回
    YK_menu_back = ("id->com.yunlu6.stone:id/iv_batch_back_selected_cloundlibrary", "云库-菜单栏-返回")

    # 云库-菜单栏-取消
    YK_menu_cancel = ("id->com.yunlu6.stone:id/tv_cancel_selected_cloundlibrary", "云库-菜单栏-取消")

    # 云库-菜单栏-全选
    YK_menu_all = ("id->com.yunlu6.stone:id/tv_cancel_selected_cloundlibrary", "云库-菜单栏-全选")

    # 云库-菜单栏-照片列表
    YK_menu_piclist = ("id->com.yunlu6.stone:id/item_cloudlibrary_ll_checked", "云库-菜单栏-照片列表")

    # 云库-菜单栏-照片列表-分类到
    YK_menu_piclist_classify_x = 269
    YK_menu_piclist_classify_y = 1820

    # 云库-菜单栏-照片列表-删除
    YK_menu_piclist_delete_x = 800
    YK_menu_piclist_delete_y = 1816

    # 云库-菜单栏-照片列表-删除-是
    YK_menu_piclist_delete_yes = ("id->com.yunlu6.stone:id/bt_affirm", "云库-菜单栏-照片列表-删除-是")

    # 云库-菜单栏-照片列表-删除-否
    YK_menu_piclist_delete_no = ("id->com.yunlu6.stone:id/bt_cancel", "云库-菜单栏-照片列表-删除-否")
