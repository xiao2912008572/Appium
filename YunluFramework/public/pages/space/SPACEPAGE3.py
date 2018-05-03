__author__ = 'xiaoj'
# 空间首页
from YunluFramework.public.pages.space.SPACEPAGE2 import SPACEPAGE2


class SPACEPAGE3(SPACEPAGE2):
    # ***************************************【PAGE2】产品Kjlb_browseorgspace_menu_product***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-返回
    Kjlb_browseorgspace_menu_product_back = ("id->com.yunlu6.yunlu:id/title_back_icon", "空间列表-浏览企业空间-菜单栏-产品-返回")

    #  空间列表-浏览企业空间-菜单栏-产品-新建
    Kjlb_browseorgspace_menu_product_new = ("id->com.yunlu6.yunlu:id/title_tv_menu", "空间列表-浏览企业空间-菜单栏-产品-新建")

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表
    Kjlb_browseorgspace_menu_product_unlock_list = ("id->com.yunlu6.yunlu:id/tv_productr_name", "空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表")

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-产品名查找
    def Kjlb_browseorgspace_menu_product_unlock_list_byname(self, name):
        return ("name->%s" % name, "空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-产品名查找")

    #  空间列表-浏览企业空间-菜单栏-产品-未发布
    Kjlb_browseorgspace_menu_product_unlock = ("id->com.yunlu6.yunlu:id/tv_unlock", "空间列表-浏览企业空间-菜单栏-产品-未发布")

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-产品名查找
    def Kjlb_browseorgspace_menu_product_lock_list_byname(self, name):
        return ("name->%s" % name, "空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-产品名查找")

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表
    Kjlb_browseorgspace_menu_product_lock_list = ("id->com.yunlu6.yunlu:id/iv_productr", "空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表")

    #  空间列表-浏览企业空间-菜单栏-产品-已发布
    Kjlb_browseorgspace_menu_product_lock = ("id->com.yunlu6.yunlu:id/tv_lock", "空间列表-浏览企业空间-菜单栏-产品-已发布")

    # 空间列表-浏览企业空间-菜单栏-产品-收款账号
    Kjlb_browseorgspace_menu_product_account = ("name->%s" % "为保障交易安全顺畅，需验证贵司收款银行账户", "空间列表-浏览企业空间-菜单栏-产品-收款账号")

    # 空间列表-浏览企业空间-菜单栏-产品-搜索
    Kjlb_browseorgspace_menu_product_seek = ("id->com.yunlu6.yunlu:id/et_seek", "空间列表-浏览企业空间-菜单栏-产品-搜索")

    # ***************************************【PAGE2】团队Kjlb_browseorgspace_menu_team***************************************
    # 空间列表-浏览企业空间-菜单栏-团队-返回
    Kjlb_browseorgspace_menu_team_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon", "空间列表-浏览企业空间-菜单栏-团队-返回")

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏
    Kjlb_browseorgspace_menu_team_menu = ("id->com.yunlu6.yunlu:id/title_main_tv_more_menu", "空间列表-浏览企业空间-菜单栏-团队-菜单栏")

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免
    Kjlb_browseorgspace_menu_team_menu_assignjob = ("id->com.yunlu6.yunlu:id/pop_teamedit_personnel", "空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免")

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门
    Kjlb_browseorgspace_menu_team_menu_mydepartment = ("id->com.yunlu6.yunlu:id/pop_teamedit_mydepartment", "空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门")

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-返回
    Kjlb_browseorgspace_menu_team_menu_mydepartment_back = ("id->com.yunlu6.yunlu:id/title_main_more_back", "空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-返回")

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-搜索
    Kjlb_browseorgspace_menu_team_menu_mydepartment_seek = ("id->com.yunlu6.yunlu:id/et_seek", "空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-搜索")

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑
    Kjlb_browseorgspace_menu_team_teamedit = ("id->com.yunlu6.yunlu:id/companyteam_btn_edit", "空间列表-浏览企业空间-菜单栏-团队-团队编辑")

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮列表
    Kjlb_browseorgspace_menu_team_teamedit_numeidt = ("id->com.yunlu6.yunlu:id/companyteam_item_edit", "空间列表-浏览企业空间-菜单栏-团队-团队编辑-编辑人数按钮列表")

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-职位人数
    Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit = ("id->com.yunlu6.yunlu:id/teamedit_jobs_editnum", "空间列表-浏览企业空间-菜单栏-团队-团队编辑-编辑人数按钮-职位人数按钮")

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-否
    Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancel = ("id->com.yunlu6.yunlu:id/teamedit_cancleedit", "空间列表-浏览企业空间-菜单栏-团队-团队编辑-编辑人数按钮-职位人数按钮-否")

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-是
    Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirm = ("id->com.yunlu6.yunlu:id/teamedit_commitedit", "空间列表-浏览企业空间-菜单栏-团队-团队编辑-编辑人数-职位人数按钮-是")

    # ***************************************【PAGE2】资讯Kjlb_browseorgspace_menu_archivies***************************************
    # 空间列表-浏览企业空间-菜单栏-资讯-返回
    Kjlb_browseorgspace_menu_archivies_back = ("id->com.yunlu6.yunlu:id/ivBack", "空间列表-浏览企业空间-菜单栏-资讯-返回")

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮
    Kjlb_browseorgspace_menu_archivies_new = ("id->com.yunlu6.yunlu:id/titleMenu", "空间列表-浏览企业空间-菜单栏-资讯-新增按钮")

    # 空间列表-浏览企业空间-菜单栏-资讯-搜索栏
    Kjlb_browseorgspace_menu_archivies_search = ("id->com.yunlu6.yunlu:id/etKey","空间列表-浏览企业空间-菜单栏-资讯-搜索栏")

    # 空间列表-浏览企业空间-菜单栏-资讯-搜索按钮
    Kjlb_browseorgspace_menu_archivies_searchbutton = ("id->com.yunlu6.yunlu:id/ivSearch","空间列表-浏览企业空间-菜单栏-资讯-搜索按钮")

    # 空间列表-浏览企业空间-菜单栏-资讯-全部
    Kjlb_browseorgspace_menu_archivies_all = ("name->全部","空间列表-浏览企业空间-菜单栏-资讯-全部")

    # 空间列表-浏览企业空间-菜单栏-资讯-待发布
    Kjlb_browseorgspace_menu_archivies_dafabu = ("name->待发布","空间列表-浏览企业空间-菜单栏-资讯-待发布")

    # 空间列表-浏览企业空间-菜单栏-资讯-已发布
    Kjlb_browseorgspace_menu_archivies_yifabu = ("name->已发布","空间列表-浏览企业空间-菜单栏-资讯-已发布")

    # 空间列表-浏览企业空间-菜单栏-资讯-全部类型
    Kjlb_browseorgspace_menu_archivies_tvclass = ("id->com.yunlu6.yunlu:id/tvClass","空间列表-浏览企业空间-菜单栏-资讯-全部类型")

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片
    Kjlb_browseorgspace_menu_archivies_new_addpic = ("id->com.yunlu6.yunlu:id/iv_add_photo","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片")

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片切换封面
    Kjlb_browseorgspace_menu_archivies_new_cover = ("id->com.yunlu6.yunlu:id/ll_cover","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片切换封面")

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-标题
    Kjlb_browseorgspace_menu_archivies_new_title = ("id->com.yunlu6.yunlu:id/archiveName","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-标题")

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-类型选择
    Kjlb_browseorgspace_menu_archivies_new_type = ("id->com.yunlu6.yunlu:id/llTypesOf","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-类型选择")

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-保存按钮
    Kjlb_browseorgspace_menu_archivies_new_save = ("id->com.yunlu6.yunlu:id/product_save","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-保存")

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-发布按钮
    Kjlb_browseorgspace_menu_archivies_new_issue = ("id->com.yunlu6.yunlu:id/product_issue","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-发布按钮")

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-相册
    Kjlb_browseorgspace_menu_archivies_new_addpic_Allbum = ("id->com.yunlu6.yunlu:id/iv_cloundlibrary_alumm","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-相册")

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-拍照
    Kjlb_browseorgspace_menu_archivies_new_addpic_photograph = ("id->com.yunlu6.yunlu:id/iv_cloundlibrary_camera","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-拍照")

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-产品库
    Kjlb_browseorgspace_menu_archivies_new_addpic_library = ("id->com.yunlu6.yunlu:id/iv_cloundlibrary_yun","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-产品库")


    '''
        20180320资讯模块更新，此处代码已注释，start
    '''
    # # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-资讯
    # Kjlb_browseorgspace_menu_archivies_new_archivies = ("id->com.yunlu6.yunlu:id/add_zixun", "空间列表-浏览企业空间-菜单栏-资讯-新增按钮-资讯")
    #
    # # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-章程
    # Kjlb_browseorgspace_menu_archivies_new_constitution = ("id->com.yunlu6.yunlu:id/to_rule", "空间列表-浏览企业空间-菜单栏-资讯-新增按钮-章程")
    #
    # # 空间列表-浏览企业空间-菜单栏-资讯-图片新增
    # Kjlb_browseorgspace_menu_archivies_picadd = ("id->com.yunlu6.yunlu:id/rl_add", "空间列表-浏览企业空间-菜单栏-资讯-图片新增")
    #
    # # 空间列表-浏览企业空间-菜单栏-资讯-图片列表
    # Kjlb_browseorgspace_menu_archivies_pic = ("id->com.yunlu6.yunlu:id/iv_profile", "空间列表-浏览企业空间-菜单栏-资讯-图片列表")
    #
    # # 空间列表-浏览企业空间-菜单栏-资讯-图片列表
    # def Kjlb_browseorgspace_menu_archivies_pic_element(self):
    #     return self.p.get_elements(self.Kjlb_browseorgspace_menu_archivies_pic[0])


    # 空间列表-浏览企业空间-菜单栏-资讯-图片列表
    # def Kjlb_browseorgspace_menu_archivies_pics(self):
    #     self.Kjlb_browseorgspace_menu_archivies_picA = self.p.get_elements("id->com.yunlu6.yunlu:id/iv_profile",
    #                                                                            "空间列表-浏览企业空间-菜单栏-资讯-图片列表")
    #     return self.Kjlb_browseorgspace_menu_archivies_picA

    # # 空间列表-浏览企业空间-菜单栏-资讯-图片-标题
    # Kjlb_browseorgspace_menu_archivies_pic_title = ("id->com.yunlu6.yunlu:id/title_main_tv_more_title", "空间列表-浏览企业空间-菜单栏-资讯-图片-标题")
    #
    # # 空间列表-浏览企业空间-菜单栏-资讯-图片-类型
    # Kjlb_browseorgspace_menu_archivies_pic_type = ("id->com.yunlu6.yunlu:id/tv_profile", "空间列表-浏览企业空间-菜单栏-资讯-图片-类型")
    '''
        20180320，end
    '''

    # ***************************************【PAGE2】编辑Kjlb_browseorgspace_menu_edit***************************************
    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-返回
    Kjlb_browseorgspace_menu_edit_back = ("id->com.yunlu6.yunlu:id/title_back_icon", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-返回")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-Logo
    Kjlb_browseorgspace_menu_edit_logo = ("id->com.yunlu6.yunlu:id/iv_open_logo", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-Logo")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-Logo-相册
    Kjlb_browseorgspace_menu_edit_logo_album = ("id->com.yunlu6.yunlu:id/iv_cloundlibrary_alumm", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-Logo-相册")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-Logo-拍照
    Kjlb_browseorgspace_menu_edit_logo_takepic = ("id->com.yunlu6.yunlu:id/iv_cloundlibrary_cameras", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-Logo-拍照")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-Logo-取消
    Kjlb_browseorgspace_menu_edit_logo_cancel = ("id->com.yunlu6.yunlu:id/pop_cloundlibrary_tv_cancel", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-Logo-取消")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-企业全称
    Kjlb_browseorgspace_menu_edit_fullname = ("id->com.yunlu6.yunlu:id/company_name", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-企业全称")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-企业简称
    Kjlb_browseorgspace_menu_edit_simplename = ("id->com.yunlu6.yunlu:id/company_introduce", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-企业简称")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-所在地区
    Kjlb_browseorgspace_menu_edit_address = ("id->com.yunlu6.yunlu:id/company_address", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-所在地区")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-所在地区-所在地区列表
    Kjlb_browseorgspace_menu_edit_address_list = ("id->com.yunlu6.yunlu:id/tv_address", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-所在地区")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-详细地址
    Kjlb_browseorgspace_menu_edit_detailaddress = ("id->com.yunlu6.yunlu:id/company_address_det", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-详细地址")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-联系人
    Kjlb_browseorgspace_menu_edit_contact = ("id->com.yunlu6.yunlu:id/people_name", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-联系人")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-手机号
    Kjlb_browseorgspace_menu_edit_phone = ("id->com.yunlu6.yunlu:id/mobile_phone", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-手机号")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-座机号
    Kjlb_browseorgspace_menu_edit_landline = ("id->com.yunlu6.yunlu:id/phone", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-座机号")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-邮箱
    Kjlb_browseorgspace_menu_edit_email = ("id->com.yunlu6.yunlu:id/email", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-邮箱")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-QQ
    Kjlb_browseorgspace_menu_edit_QQ = ("id->com.yunlu6.yunlu:id/qq", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-QQ")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-网站
    Kjlb_browseorgspace_menu_edit_website = ("id->com.yunlu6.yunlu:id/website", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-网站")

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-勾选
    Kjlb_browseorgspace_menu_edit_confirm = ("id->com.yunlu6.yunlu:id/title_tv_menu", "空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑-勾选")

    # ***************************************【PAGE2】订单Kjlb_browseorgspace_menu_order***************************************
    # 空间列表-浏览企业空间-菜单栏-订单-返回
    Kjlb_browseorgspace_menu_order_back = ("id->com.yunlu6.yunlu:id/clondzone_title_back", "空间列表-浏览企业空间-菜单栏-订单-返回")

    # 空间列表-浏览企业空间-菜单栏-订单-搜索栏
    Kjlb_browseorgspace_menu_order_search = ("id->com.yunlu6.yunlu:id/edit_text", "空间列表-浏览企业空间-菜单栏-订单-搜索栏")

    # 空间列表-浏览企业空间-菜单栏-订单-搜索按钮
    Kjlb_browseorgspace_menu_order_searchbtn = ("id->com.yunlu6.yunlu:id/iv_search_zone", "空间列表-浏览企业空间-菜单栏-订单-搜索按钮")

    # 空间列表-浏览企业空间-菜单栏-订单-空白页
    Kjlb_browseorgspace_menu_order_nonepage = ("id->com.yunlu6.yunlu:id/companyorder_commen_nodata", "空间列表-浏览企业空间-菜单栏-订单-空白页")

    # 空间列表-浏览企业空间-菜单栏-订单-全部
    Kjlb_browseorgspace_menu_order_all = ("name->全部", "空间列表-浏览企业空间-菜单栏-订单-全部")

    # 空间列表-浏览企业空间-菜单栏-订单-全部元素
    Kjlb_browseorgspace_menu_order_allE = ["name->全部", "空间列表-浏览企业空间-菜单栏-订单-全部元素"]

    # 空间列表-浏览企业空间-菜单栏-订单-待付款
    Kjlb_browseorgspace_menu_order_waitforpay = ("name->待付款", "空间列表-浏览企业空间-菜单栏-订单-待付款")

    # 空间列表-浏览企业空间-菜单栏-订单-待付款元素
    Kjlb_browseorgspace_menu_order_waitforpayE = ["name->待付款", "空间列表-浏览企业空间-菜单栏-订单-待付款元素"]

    # 空间列表-浏览企业空间-菜单栏-订单-待发货
    Kjlb_browseorgspace_menu_order_waitforsend = ("name->待发货", "空间列表-浏览企业空间-菜单栏-订单-待发货")

    # 空间列表-浏览企业空间-菜单栏-订单-待发货元素
    Kjlb_browseorgspace_menu_order_waitforsendE = ["name->待发货", "空间列表-浏览企业空间-菜单栏-订单-待发货元素"]

    # 空间列表-浏览企业空间-菜单栏-订单-已发货
    Kjlb_browseorgspace_menu_order_alreadysend = ("name->已发货", "空间列表-浏览企业空间-菜单栏-订单-已发货")

    # 空间列表-浏览企业空间-菜单栏-订单-已发货元素
    Kjlb_browseorgspace_menu_order_alreadysendE = ["name->已发货", "空间列表-浏览企业空间-菜单栏-订单-已发货元素"]

    # 空间列表-浏览企业空间-菜单栏-订单-退款中
    Kjlb_browseorgspace_menu_order_refund = ("name->退款中", "空间列表-浏览企业空间-菜单栏-订单-退款中")

    # 空间列表-浏览企业空间-菜单栏-订单-退款中元素
    Kjlb_browseorgspace_menu_order_refundE = ["name->退款中", "空间列表-浏览企业空间-菜单栏-订单-退款中元素"]

    # 空间列表-浏览企业空间-菜单栏-订单-待评价
    Kjlb_browseorgspace_menu_order_evaluate = ("name->待评价", "空间列表-浏览企业空间-菜单栏-订单-待评价")

    # 空间列表-浏览企业空间-菜单栏-订单-待评价元素
    Kjlb_browseorgspace_menu_order_evaluateE = ["name->待评价", "空间列表-浏览企业空间-菜单栏-订单-待评价元素"]

    # 空间列表-浏览企业空间-菜单栏-订单-商品名列表(卖家）
    Kjlb_browseorgspace_menu_order_prolistS = ("id->com.yunlu6.yunlu:id/tv_dingdan_name", "空间列表-浏览企业空间-菜单栏-订单-商品名列表")

    # 空间列表-浏览企业空间-菜单栏-订单-商品名列表-商品名
    Kjlb_browseorgspace_menu_order_prolist_proname = ("id->com.yunlu6.yunlu:id/shop_item_name", "空间列表-浏览企业空间-菜单栏-订单-商品名列表-商品名")

    # 空间列表-浏览企业空间-菜单栏-订单-订单编号列表
    Kjlb_browseorgspace_menu_order_no = ("id->com.yunlu6.yunlu:id/tv_dingdan_num", "空间列表-浏览企业空间-菜单栏-订单-订单编号列表")

    # 空间列表-浏览企业空间-菜单栏-订单-价格列表
    Kjlb_browseorgspace_menu_order_price = ("id->com.yunlu6.yunlu:id/tv_dingdan_price", "空间列表-浏览企业空间-菜单栏-订单-价格列表")

    # 空间列表-浏览企业空间-菜单栏-订单-数量列表
    Kjlb_browseorgspace_menu_order_amount = ("id->com.yunlu6.yunlu:id/tv_dingdan_amount_one", "空间列表-浏览企业空间-菜单栏-订单-数量列表")

    # 空间列表-浏览企业空间-菜单栏-订单-合计列表
    Kjlb_browseorgspace_menu_order_total = ("id->com.yunlu6.yunlu:id/tv_dingdan_total_price", "空间列表-浏览企业空间-菜单栏-订单-合计列表")






    # 空间列表-浏览企业空间-菜单栏-订单-确认发货
    Kjlb_browseorgspace_menu_order_confirm = ("name->确认发货", "空间列表-浏览企业空间-菜单栏-订单-确认发货")

    # 空间列表-浏览企业空间-菜单栏-订单-查看物流
    Kjlb_browseorgspace_menu_order_logistics = ("name->查看物流", "空间列表-浏览企业空间-菜单栏-订单-查看物流")

    # ***************************************【PAGE2】访客Kjlb_browseorgspace_menu_visitor***************************************
    # 空间列表-浏览企业空间-菜单栏-访客-访客列表
    Kjlb_browseorgspace_menu_visitor_list = ("id->com.yunlu6.yunlu:id/visitor_name", "空间列表-浏览企业空间-菜单栏-访客-访客列表")

    # 空间列表-浏览企业空间-菜单栏-访客-访客列表-返回
    Kjlb_browseorgspace_menu_visitor_list_back = ("id->com.yunlu6.yunlu:id/iv_back", "空间列表-浏览企业空间-菜单栏-访客-访客列表")

    # ***************************************【PAGE2】客户Kjlb_browseorgspace_menu_customer***************************************
    # 空间列表-浏览企业空间-菜单栏-客户-返回
    Kjlb_browseorgspace_menu_customer_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon", "空间列表-浏览企业空间-菜单栏-客户-返回")

    # 空间列表-浏览企业空间-菜单栏-客户-搜索框
    Kjlb_browseorgspace_menu_customer_search = ("id->com.yunlu6.yunlu:id/et_search", "空间列表-浏览企业空间-菜单栏-客户-搜索框")

    # 空间列表-浏览企业空间-菜单栏-客户-搜索
    Kjlb_browseorgspace_menu_customer_seek = ("id->com.yunlu6.yunlu:id/iv_search", "空间列表-浏览企业空间-菜单栏-客户-搜索")

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏
    Kjlb_browseorgspace_menu_customer_menu = ("id->com.yunlu6.yunlu:id/title_main_tv_more_menu", "空间列表-浏览企业空间-菜单栏-客户-菜单栏")

    # 空间列表-浏览企业空间-菜单栏-客户-客户列表
    Kjlb_browseorgspace_menu_customer_clist = ("id->com.yunlu6.yunlu:id/rl_out", "空间列表-浏览企业空间-菜单栏-客户-客户列表")

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏+客户
    Kjlb_browseorgspace_menu_customer_menu_add = ("id->com.yunlu6.yunlu:id/btn_new_space", "空间列表-浏览企业空间-菜单栏-客户-菜单栏+客户")

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作
    Kjlb_browseorgspace_menu_customer_menu_batch = ("id->com.yunlu6.yunlu:id/btn_share_space", "空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作")

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-返回
    Kjlb_browseorgspace_menu_customer_menu_batch_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon", "空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-返回")

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-全选
    Kjlb_browseorgspace_menu_customer_menu_batch_all = ("id->com.yunlu6.yunlu:id/title_main_tv_more_tv", "空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-全选")

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-圆圈勾选
    Kjlb_browseorgspace_menu_customer_menu_batch_choose = ("id->com.yunlu6.yunlu:id/iv_select", "空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-全选")

    # ***************************************【PAGE2】业务升级Kjlb_browseorgspace_menu_upgrade***************************************
    # 空间列表-浏览企业空间-菜单栏-业务升级-开启
    Kjlb_browseorgspace_menu_upgrade_open = ("id->com.yunlu6.yunlu:id/upgrade_open", "空间列表-浏览企业空间-菜单栏-业务升级-开启")

    # 空间列表-浏览企业空间-菜单栏-业务升级-返回
    Kjlb_browseorgspace_menu_upgrade_back = ("id->com.yunlu6.yunlu:id/companyupgrade_backe", "空间列表-浏览企业空间-菜单栏-业务升级-返回")

    # ***************************************【PAGE2】流程Kjlb_browseorgspace_menu_flow_click***************************************
    # 空间列表-浏览企业空间-菜单栏-流程-返回
    Kjlb_browseorgspace_menu_flow_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon","空间列表-浏览企业空间-菜单栏-流程-返回")

    # 空间列表-浏览企业空间-菜单栏-流程-菜单栏
    Kjlb_browseorgspace_menu_flow_menu = ("id->com.yunlu6.yunlu:id/title_main_tv_more_menu","空间列表-浏览企业空间-菜单栏-流程-菜单栏")

    # 空间列表-浏览企业空间-菜单栏-流程-我审批的
    Kjlb_browseorgspace_menu_flow_approve = ("id->com.yunlu6.yunlu:id/rb_approve","空间列表-浏览企业空间-菜单栏-流程-我审批的")

    # 空间列表-浏览企业空间-菜单栏-流程-我发起的
    Kjlb_browseorgspace_menu_flow_create = ("id->com.yunlu6.yunlu:id/rb_create","空间列表-浏览企业空间-菜单栏-流程-我发起的")

    # 空间列表-浏览企业空间-菜单栏-流程-抄送我的
    Kjlb_browseorgspace_menu_flow_copy = ("id->com.yunlu6.yunlu:id/rb_copy","空间列表-浏览企业空间-菜单栏-流程-抄送我的")

    # 空间列表-浏览企业空间-菜单栏-流程-待处理
    Kjlb_browseorgspace_menu_flow_wait = ("id->com.yunlu6.yunlu:id/rb_wait","空间列表-浏览企业空间-菜单栏-流程-待处理")

    # 空间列表-浏览企业空间-菜单栏-流程-已处理
    Kjlb_browseorgspace_menu_flow_already = ("id->com.yunlu6.yunlu:id/rb_already","空间列表-浏览企业空间-菜单栏-流程-已处理")

    # 空间列表-浏览企业空间-菜单栏-流程-菜单栏-新申请
    Kjlb_browseorgspace_menu_flow_menu_new = ("id->com.yunlu6.yunlu:id/btn_apply","空间列表-浏览企业空间-菜单栏-流程-菜单栏-新申请")

    # 空间列表-浏览企业空间-菜单栏-流程-菜单栏-新申请-请假
    Kjlb_browseorgspace_menu_flow_menu_new_leave = ("id->com.yunlu6.yunlu:id/bt_leave","空间列表-浏览企业空间-菜单栏-流程-菜单栏-新申请-请假")

    # 空间列表-浏览企业空间-菜单栏-流程-菜单栏-新申请-加班
    Kjlb_browseorgspace_menu_flow_menu_new_overtime = ("id->com.yunlu6.yunlu:id/bt_overtime","空间列表-浏览企业空间-菜单栏-流程-菜单栏-新申请-加班")

    # 空间列表-浏览企业空间-菜单栏-流程-菜单栏-新申请-方案审批
    Kjlb_browseorgspace_menu_flow_menu_new_scheme = ("id->com.yunlu6.yunlu:id/bt_scheme","空间列表-浏览企业空间-菜单栏-流程-菜单栏-新申请-方案审批")

    # ***************************************【PAGE2】照片列表(包括点击照片加数据)Kjlb_browseperspace_piclist***************************************
    # 空间列表-浏览私人空间-照片列表-菜单栏
    Kjlb_browseperspace_piclist_menu = ("id->com.yunlu6.yunlu:id/title_main_tv_more_menu", "空间列表-浏览私人空间-照片列表-菜单栏")

    # 空间列表-浏览私人空间-照片列表-分类到
    Kjlb_browseperspace_piclist_classify = ("id->com.yunlu6.yunlu:id/btn_new_space", "空间列表-浏览私人空间-照片列表-分类到")

    # 空间列表-浏览私人空间-照片列表-编辑
    Kjlb_browseperspace_piclist_edit = ("id->com.yunlu6.yunlu:id/btn_share_space", "空间列表-浏览私人空间-照片列表-编辑")

    # 空间列表-浏览私人空间-照片列表-返回
    Kjlb_browseperspace_piclist_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon", "空间列表-浏览私人空间-照片列表-返回")

    # 空间列表-浏览私人空间-照片列表-照片本身
    Kjlb_browseperspace_piclist_itself = ("id->com.yunlu6.yunlu:id/image", "空间列表-浏览私人空间-照片列表-照片本身")

    # 空间列表-浏览私人空间-文件夹名称列表
    Kjlb_browseperspace_foldername = ("id->com.yunlu6.yunlu:id/personzone_item_foldername", "空间列表-浏览私人空间-文件夹名称列表")

    # 空间列表-浏览私人空间-加数据-相册
    Kjlb_browseperspace_addData_ByAlbum = ("id->com.yunlu6.yunlu:id/iv_cloundlibrary_alumm", "空间列表-浏览私人空间--加数据-相册")

    # ***************************************【PAGE2】菜单栏-名片Kjlb_browseperspace_menu_card***************************************
    # 空间列表-浏览私人空间-菜单栏-名片-返回
    Kjlb_browseperspace_menu_card_back = ("id->com.yunlu6.yunlu:id/title_back_edit_icon", "空间列表-浏览私人空间-菜单栏-名片-返回")

    # 空间列表-浏览私人空间-菜单栏-名片-分享
    Kjlb_browseperspace_menu_card_share = ("id->com.yunlu6.yunlu:id/title_tv_edit_menu_tv", "空间列表-浏览私人空间-菜单栏-名片-分享")

    # 空间列表-浏览私人空间-菜单栏-名片-分享-微信
    Kjlb_browseperspace_menu_card_share_wechat = ("id->com.yunlu6.yunlu:id/iv_cloundlibrary_alumm", "空间列表-浏览私人空间-菜单栏-名片-分享-微信")

    # 空间列表-浏览私人空间-菜单栏-名片-分享-微信朋友圈
    Kjlb_browseperspace_menu_card_share_circle = ("id->com.yunlu6.yunlu:id/iv_cloundlibrary_cameras", "空间列表-浏览私人空间-菜单栏-名片-分享-微信朋友圈")

    # 空间列表-浏览私人空间-菜单栏-名片-分享-QQ空间
    Kjlb_browseperspace_menu_card_share_qqzone = ("id->com.yunlu6.yunlu:id/pop_cloundlibrary_tv_wifi_sync", "空间列表-浏览私人空间-菜单栏-名片-分享-QQ空间")

    # 空间列表-浏览私人空间-菜单栏-名片-分享-QQ
    Kjlb_browseperspace_menu_card_share_qq = ("id->com.yunlu6.yunlu:id/pop_cloundlibrary_tv_qq", "空间列表-浏览私人空间-菜单栏-名片-分享-QQ")

    # 空间列表-浏览私人空间-菜单栏-名片-分享-新浪微博
    Kjlb_browseperspace_menu_card_share_sina = ("id->com.yunlu6.yunlu:id/pop_cloundlibrary_tv_weibo", "空间列表-浏览私人空间-菜单栏-名片-分享-微博")

    # 空间列表-浏览私人空间-菜单栏-名片-分享-取消
    Kjlb_browseperspace_menu_card_share_cancel = ("id->com.yunlu6.yunlu:id/pop_cloundlibrary_tv_cancel", "空间列表-浏览私人空间-菜单栏-名片-分享-取消")

    # 空间列表-浏览私人空间-菜单栏-名片-手机
    Kjlb_browseperspace_menu_card_phone = ("id->com.yunlu6.yunlu:id/user_card_team_phone_cb", "空间列表-浏览私人空间-菜单栏-名片-手机")

    # 空间列表-浏览私人空间-菜单栏-名片-邮箱
    Kjlb_browseperspace_menu_card_email = ("id->com.yunlu6.yunlu:id/user_card_team_email_cb", "空间列表-浏览私人空间-菜单栏-名片-邮箱")

    # 空间列表-浏览私人空间-菜单栏-名片-地址
    Kjlb_browseperspace_menu_card_address = ("id->com.yunlu6.yunlu:id/user_card_team_address_cb", "空间列表-浏览私人空间-菜单栏-名片-地址")

    # 空间列表-浏览私人空间-菜单栏-名片-QQ
    Kjlb_browseperspace_menu_card_QQ = ("id->com.yunlu6.yunlu:id/user_card_team_qq_cb", "空间列表-浏览私人空间-菜单栏-名片-QQ")

    # 空间列表-浏览私人空间-菜单栏-名片-有效期
    Kjlb_browseperspace_menu_card_limit = ("id->com.yunlu6.yunlu:id/user_card_team_userlife_tv", "空间列表-浏览私人空间-菜单栏-名片-有效期")

    # 空间列表-浏览私人空间-菜单栏-编辑-删除文件夹列表
    Kjlb_browseperspace_menu_edit_deletefolder = ("id->com.yunlu6.yunlu:id/editlayout_folder_dele", "空间列表-浏览私人空间-菜单栏-编辑-删除文件夹名称")

    # 空间列表-浏览私人空间-菜单栏-编辑-修改文件夹图标
    Kjlb_browseperspace_menu_edit_editfolder = ("id->com.yunlu6.yunlu:id/editlayout_folder_edite", "空间列表-浏览私人空间-菜单栏-编辑-修改文件夹名称")

    # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称
    Kjlb_browseperspace_menu_edit_editfolder_fname = ("id->com.yunlu6.yunlu:id/edit_folder_name", "空间列表-浏览私人空间-菜单栏-编辑-修改文件夹名称-名称列表")

    # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-是
    Kjlb_browseperspace_menu_edit_editfolder_spaceEdit_OK = ("id->com.yunlu6.yunlu:id/edit_folder_ok", "空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-是")

    # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-否
    Kjlb_browseperspace_menu_edit_editfolder_spaceEdit_NO = ("id->com.yunlu6.yunlu:id/edit_folder_no", "空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-否")

    # 空间列表-浏览私人空间-菜单栏-编辑-+数据
    Kjlb_browseperspace_menu_edit_adddata = ("name->＋ 数据", "空间列表-浏览私人空间-菜单栏-编辑-+数据")

    # 空间列表-浏览私人空间-菜单栏-编辑-空间类型
    Kjlb_browseperspace_menu_edit_spacetype = ("id->com.yunlu6.yunlu:id/create_img_type", "空间列表-浏览私人空间-菜单栏-编辑-空间类型")

    # 空间列表-浏览私人空间-菜单栏-编辑-删除空间
    Kjlb_browseperspace_menu_edit_deletespace = ("id->com.yunlu6.yunlu:id/space_dele_icon", "空间列表-浏览私人空间-菜单栏-编辑-删除空间")

    # 空间列表-浏览私人空间-菜单栏-编辑-删除空间-是
    Kjlb_browseperspace_menu_edit_deletespace_OK = ("id->com.yunlu6.yunlu:id/edit_folder_ok", "空间列表-浏览私人空间-菜单栏-编辑-删除空间-是")

    # 空间列表-浏览私人空间-菜单栏-编辑-删除空间-否
    Kjlb_browseperspace_menu_edit_deletespace_NO = ("id->com.yunlu6.yunlu:id/edit_folder_no", "空间列表-浏览私人空间-菜单栏-编辑-删除空间-否")

    # 空间列表-浏览私人空间-菜单栏-编辑-返回
    Kjlb_browseperspace_menu_edit_back = ("id->com.yunlu6.yunlu:id/title_back_icon", "空间列表-浏览私人空间-菜单栏-编辑-返回")

    # 空间列表-浏览私人空间-菜单栏-编辑-空间名
    Kjlb_browseperspace_menu_edit_spacename = ("id->com.yunlu6.yunlu:id/space_name_edit", "空间列表-浏览私人空间-菜单栏-编辑-空间名")

    # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称列表(0)
    Kjlb_browseperspace_menu_edit_spacename_spaceEdit = ("id->com.yunlu6.yunlu:id/edit_folder_name", "空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称")

    # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-是
    Kjlb_browseperspace_menu_edit_spacename_spaceEdit_OK = ("id->com.yunlu6.yunlu:id/edit_folder_ok", "空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-是")

    # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-否
    Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NO = ("id->com.yunlu6.yunlu:id/edit_folder_no", "空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-否")

    # ***************************************【PAGE2】菜单栏-客户Kjlb_browseperspace_menu_customer***************************************
    # 空间列表-浏览私人空间-菜单栏-客户-返回
    Kjlb_browseperspace_menu_customer_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon", "空间列表-浏览私人空间-菜单栏-客户-返回")

    # 空间列表-浏览私人空间-菜单栏-客户-搜索栏
    Kjlb_browseperspace_menu_customer_search = ("id->com.yunlu6.yunlu:id/et_search", "空间列表-浏览私人空间-菜单栏-客户-搜索栏")

    # 空间列表-浏览私人空间-菜单栏-客户-搜索按钮
    Kjlb_browseperspace_menu_customer_searchbtn = ("id->com.yunlu6.yunlu:id/iv_search", "空间列表-浏览私人空间-菜单栏-客户-搜索栏")

    # 空间列表-浏览私人空间-菜单栏-客户-菜单
    Kjlb_browseperspace_menu_customer_menu = ("id->com.yunlu6.yunlu:id/title_main_tv_more_menu", "空间列表-浏览私人空间-菜单栏-客户-菜单")

    # 空间列表-浏览私人空间-菜单栏-客户-菜单-+客户
    Kjlb_browseperspace_menu_customer_menu_addcus = ("id->com.yunlu6.yunlu:id/btn_new_space", "空间列表-浏览私人空间-菜单栏-客户-菜单-+客户")

    # 空间列表-浏览私人空间-菜单栏-客户-客户列表
    Kjlb_browseperspace_menu_customer_clist = ("id->com.yunlu6.yunlu:id/rl_out", "空间列表-浏览私人空间-菜单栏-客户-客户列表")

    # 空间列表-浏览私人空间-菜单栏-客户-群聊
    Kjlb_browseperspace_menu_customer_gchat = ("id->com.yunlu6.yunlu:id/rl_bottom", "空间列表-浏览私人空间-菜单栏-客户-群聊")

    # 空间列表-浏览私人空间-菜单栏-+文件夹-文件夹名称-确定
    Kjlb_browseperspace_menu_addfolder_confirm = ("id->com.yunlu6.yunlu:id/zone_add_commit", "空间列表-浏览私人空间-菜单栏-+文件夹-确定")

    # 空间列表-浏览私人空间-菜单栏-+文件夹-文件夹名称
    Kjlb_browseperspace_menu_addfolder_foldername = ("id->com.yunlu6.yunlu:id/zone_add_gallery_et", "空间列表-浏览私人空间-菜单栏-+文件夹-文件夹名称")

    # 空间列表-浏览私人空间-菜单栏-+文件夹-返回
    Kjlb_browseperspace_menu_addfolder_back = ("id->com.yunlu6.yunlu:id/title_back_icon", "空间列表-浏览私人空间-菜单栏-+文件夹-返回")

    # ***************************************【PAGE2】+数据Kjlb_browseperspace_adata***************************************
    # 空间列表-浏览私人空间-加数据-相册
    Kjlb_browseperspace_adata_ByAlbum = ("id->com.yunlu6.yunlu:id/iv_cloundlibrary_alumm", "空间列表-浏览私人空间-加数据-相册")

    # 空间列表-浏览私人空间-加数据-拍照
    Kjlb_browseperspace_adata_ByTakepic = ("id->com.yunlu6.yunlu:id/iv_cloundlibrary_camera", "空间列表-浏览私人空间-加数据-拍照")

    # 空间列表-浏览私人空间-加数据-取消
    Kjlb_browseperspace_adata_cancel = ("id->com.yunlu6.yunlu:id/pop_cloundlibrary_tv_cancel", "空间列表-浏览私人空间-加数据-取消")

    # ***************************************【PAGE2】更多Kjlb_browseperspace_more***************************************
    # 空间列表-浏览私人空间-更多-照片列表
    Kjlb_browseperspace_more_piclist = ("id->com.yunlu6.yunlu:id/presonzone_gridview_iv", "空间列表-浏览私人空间-更多-照片列表")

    # 空间列表-浏览私人空间-更多-返回
    Kjlb_browseperspace_more_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon", "空间列表-浏览私人空间-更多-照片列表-照片本身")

    # 空间列表-浏览私人空间-更多-菜单栏
    Kjlb_browseperspace_more_menu = ("id->com.yunlu6.yunlu:id/title_main_tv_more_menu", "空间列表-浏览私人空间-更多-菜单栏")

    # 空间列表-浏览私人空间-更多-菜单栏-上传
    Kjlb_browseperspace_more_menu_upload = ("id->com.yunlu6.yunlu:id/pop_gallery_photoes_btn_uploade", "空间列表-浏览私人空间-更多-菜单栏-上传")

    # 空间列表-浏览私人空间-更多-菜单栏-上传-相册
    Kjlb_browseperspace_more_menu_upload_ByAlbum = ("id->com.yunlu6.yunlu:id/iv_cloundlibrary_alumm", "空间列表-浏览私人空间-更多-菜单栏-上传-相册")

    # 空间列表-浏览私人空间-更多-菜单栏-上传-拍照
    Kjlb_browseperspace_more_menu_upload_ByTakepic = ("id->com.yunlu6.yunlu:id/iv_cloundlibrary_cameras", "空间列表-浏览私人空间-更多-菜单栏-上传-拍照")

    # 空间列表-浏览私人空间-更多-菜单栏-上传-取消
    Kjlb_browseperspace_more_menu_upload_cancel = ("id->com.yunlu6.yunlu:id/pop_cloundlibrary_tv_cancel", "空间列表-浏览私人空间-更多-菜单栏-上传-取消")

    # 空间列表-浏览私人空间-更多-菜单栏-编辑
    Kjlb_browseperspace_more_menu_edit = ("id->com.yunlu6.yunlu:id/pop_gallery_photoes_btn_edit", "空间列表-浏览私人空间-更多-菜单栏-编辑")

    # 空间列表-浏览私人空间-更多-菜单栏-排序
    Kjlb_browseperspace_more_menu_sort = ("id->com.yunlu6.yunlu:id/pop_gallery_photoes_btn_sort", "空间列表-浏览私人空间-更多-菜单栏-排序")

    # ***************************************【PAGE2】企业会员Kjlb_browseascspace_ovip***************************************
    # 空间列表-协会空间-企业会员-返回
    Kjlb_browseascspace_ovip_back = ("id->com.yunlu6.yunlu:id/title_main_more_back", "空间列表-协会空间-企业会员-返回")

    # 空间列表-协会空间-企业会员-搜索栏
    Kjlb_browseascspace_ovip_search = ("id->com.yunlu6.yunlu:id/companyclient_search_keyword", "空间列表-协会空间-企业会员-搜索栏")

    # 空间列表-协会空间-企业会员-搜索按钮
    Kjlb_browseascspace_ovip_searchbtn = ("id->com.yunlu6.yunlu:id/companyclient_search_search", "空间列表-协会空间-企业会员-搜索按钮")

    # 空间列表-协会空间-企业会员-企业列表
    Kjlb_browseascspace_ovip_olist = ("id->com.yunlu6.yunlu:id/ass_company_name", "空间列表-协会空间-企业会员-企业列表")

    # ***************************************【PAGE2】个人会员Kjlb_browseascspace_ovip***************************************
    # 空间列表-协会空间-个人会员-返回
    Kjlb_browseascspace_pvip_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon", "空间列表-协会空间-个人会员-返回")

    # 空间列表-协会空间-个人会员-搜索栏
    Kjlb_browseascspace_pvip_search = ("id->com.yunlu6.yunlu:id/companyclient_search_keyword", "空间列表-协会空间-个人会员-搜索栏")

    # 空间列表-协会空间-个人会员-搜索按钮
    Kjlb_browseascspace_pvip_searchbtn = ("id->com.yunlu6.yunlu:id/companyclient_search_search", "空间列表-协会空间-个人会员-搜索按钮")

    # 空间列表-协会空间-个人会员-人脉列表
    Kjlb_browseascspace_pvip_olist = ("id->com.yunlu6.yunlu:id/vip_name", "空间列表-协会空间-个人会员-人脉列表")

    # ***************************************【PAGE2】资讯Kjlb_browseascspace_arch***************************************
    # 空间列表-协会空间-资讯-返回
    Kjlb_browseascspace_arch_back = ("id->com.yunlu6.yunlu:id/title_back_icon", "空间列表-协会空间-资讯-返回")

    # 空间列表-协会空间-资讯-资讯文件列表
    Kjlb_browseascspace_arch_alist = ("id->com.yunlu6.yunlu:id/iv_profile", "空间列表-协会空间-资讯-资讯文件列表")

    # ***************************************【PAGE2】协会资信信息Kjlb_browseascspace_credit***************************************
    # 空间列表-协会空间-资信-返回
    Kjlb_browseascspace_credit_back = ("id->com.yunlu6.yunlu:id/title_back_icone", "空间列表-协会空间-资信-返回")

    # ***************************************【PAGE2】菜单栏-编辑Kjlb_browseascspace_menu_edit***************************************
    # 空间列表-浏览协会空间-菜单栏-编辑-返回
    Kjlb_browseascspace_menu_edit_back = ("id->com.yunlu6.yunlu:id/title_back_icon", "空间列表-浏览协会空间-菜单栏-编辑-返回")

    # 空间列表-浏览协会空间-菜单栏-编辑-Logo
    Kjlb_browseascspace_menu_edit_logo = ("id->com.yunlu6.yunlu:id/iv_open_logo", "空间列表-浏览协会空间-菜单栏-编辑-Logo")

    # 空间列表-浏览协会空间-菜单栏-编辑-企业全称
    Kjlb_browseascspace_menu_edit_fullname = ("id->com.yunlu6.yunlu:id/company_name", "空间列表-浏览协会空间-菜单栏-编辑-企业全称")

    # 空间列表-浏览协会空间-菜单栏-编辑-企业简称
    Kjlb_browseascspace_menu_edit_simplename = ("id->com.yunlu6.yunlu:id/company_introduce", "空间列表-浏览协会空间-菜单栏-编辑-企业简称")

    # 空间列表-浏览协会空间-菜单栏-编辑-所在地区
    Kjlb_browseascspace_menu_edit_address = ("id->com.yunlu6.yunlu:id/company_address", "空间列表-浏览协会空间-菜单栏-编辑-所在地区")

    # 空间列表-浏览协会空间-菜单栏-编辑-所在地区-所在地区列表
    Kjlb_browseascspace_menu_edit_address_list = ("id->com.yunlu6.yunlu:id/tv_address", "空间列表-浏览协会空间-菜单栏-编辑-所在地区")

    # 空间列表-浏览协会空间-菜单栏-编辑-详细地址
    Kjlb_browseascspace_menu_edit_detailaddress = ("id->com.yunlu6.yunlu:id/company_address_det", "空间列表-浏览协会空间-菜单栏-编辑-详细地址")

    # 空间列表-浏览协会空间-菜单栏-编辑-联系人
    Kjlb_browseascspace_menu_edit_contact = ("id->com.yunlu6.yunlu:id/people_name", "空间列表-浏览协会空间-菜单栏-编辑-联系人")

    # 空间列表-浏览协会空间-菜单栏-编辑-手机号
    Kjlb_browseascspace_menu_edit_phone = ("id->com.yunlu6.yunlu:id/mobile_phone", "空间列表-浏览协会空间-菜单栏-编辑-手机号")

    # 空间列表-浏览协会空间-菜单栏-编辑-座机号
    Kjlb_browseascspace_menu_edit_landline = ("id->com.yunlu6.yunlu:id/phone", "空间列表-浏览协会空间-菜单栏-编辑-座机号")

    # 空间列表-浏览协会空间-菜单栏-编辑-邮箱
    Kjlb_browseascspace_menu_edit_email = ("id->com.yunlu6.yunlu:id/email", "空间列表-浏览协会空间-菜单栏-编辑-邮箱")

    # 空间列表-浏览协会空间-菜单栏-编辑-QQ
    Kjlb_browseascspace_menu_edit_QQ = ("id->com.yunlu6.yunlu:id/qq", "空间列表-浏览协会空间-菜单栏-编辑-QQ")

    # 空间列表-浏览协会空间-菜单栏-编辑-网站
    Kjlb_browseascspace_menu_edit_website = ("id->com.yunlu6.yunlu:id/website", "空间列表-浏览协会空间-菜单栏-编辑-网站")

    # 空间列表-浏览协会空间-菜单栏-编辑-勾选
    Kjlb_browseascspace_menu_edit_confirm = ("id->com.yunlu6.yunlu:id/title_tv_menu", "空间列表-浏览协会空间-菜单栏-编辑-勾选")

    # ***************************************【PAGE2】菜单栏-团队Kjlb_browseascspace_menu_team***************************************
    # 空间列表-浏览协会空间-菜单栏-团队-返回
    Kjlb_browseascspace_menu_team_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon", "空间列表-浏览协会空间-菜单栏-团队-返回")

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏
    Kjlb_browseascspace_menu_team_menu = ("id->com.yunlu6.yunlu:id/title_main_tv_more_menu", "空间列表-浏览协会空间-菜单栏-团队-菜单栏")

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免
    Kjlb_browseascspace_menu_team_menu_assignjob = ("id->com.yunlu6.yunlu:id/pop_teamedit_personnel", "空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免")

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门
    Kjlb_browseascspace_menu_team_menu_mydepartment = ("id->com.yunlu6.yunlu:id/pop_teamedit_personnel", "空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门")

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑
    Kjlb_browseascspace_menu_team_teamedit = ("id->com.yunlu6.yunlu:id/companyteam_btn_edit", "空间列表-浏览协会空间-菜单栏-团队-团队编辑")

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮
    Kjlb_browseascspace_menu_team_teamedit_numeidt = ("id->com.yunlu6.yunlu:id/companyteam_item_edit", "空间列表-浏览协会空间-菜单栏-团队-团队编辑-编辑人数按钮")

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-职位人数
    Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit = ("id->com.yunlu6.yunlu:id/teamedit_jobs_editnum", "空间列表-浏览协会空间-菜单栏-团队-团队编辑-编辑人数按钮-职位人数按钮")

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-否
    Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel = ("id->com.yunlu6.yunlu:id/teamedit_cancleedit", "空间列表-浏览协会空间-菜单栏-团队-团队编辑-编辑人数按钮-职位人数按钮-否")

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-是
    Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm = ("id->com.yunlu6.yunlu:id/teamedit_commitedit", "空间列表-浏览协会空间-菜单栏-团队-团队编辑-编辑人数-职位人数按钮-是")

    # ***************************************【PAGE2】菜单栏-会员Kjlb_browseascspace_menu_vip***************************************
    # 空间列表-浏览协会空间-菜单栏-会员-企业名录
    Kjlb_browseascspace_menu_vip_companylist = ("id->com.yunlu6.yunlu:id/ass_select_companylist", "空间列表-浏览协会空间-菜单栏-会员-企业名录")

    # 空间列表-浏览协会空间-菜单栏-会员-企业名录-企业名列表
    Kjlb_browseascspace_menu_vip_companylist_companyname = ("id->com.yunlu6.yunlu:id/ass_company_name", "空间列表-浏览协会空间-菜单栏-会员-企业名录-企业名列表")

    # 空间列表-浏览协会空间-菜单栏-会员-搜索按钮
    Kjlb_browseascspace_menu_vip_searchbtn = ("id->com.yunlu6.yunlu:id/companyclient_search_search", "空间列表-浏览协会空间-菜单栏-会员-搜索按钮")

    # 空间列表-浏览协会空间-菜单栏-会员-个人名录
    Kjlb_browseascspace_menu_vip_personlist = ("id->com.yunlu6.yunlu:id/ass_select_personlist", "空间列表-浏览协会空间-菜单栏-会员-个人名录")

    # 空间列表-浏览协会空间-菜单栏-会员-个人名录-个人名列表
    Kjlb_browseascspace_menu_vip_personlist_personname = ("id->com.yunlu6.yunlu:id/vip_name", "空间列表-浏览协会空间-菜单栏-会员-个人名录-个人名列表")

    # 空间列表-浏览协会空间-菜单栏-会员-搜索栏
    Kjlb_browseascspace_menu_vip_search = ("id->com.yunlu6.yunlu:id/companyclient_search_keyword", "空间列表-浏览协会空间-菜单栏-会员-搜索栏")

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏
    Kjlb_browseascspace_menu_vip_menu = ("id->com.yunlu6.yunlu:id/title_main_tv_more_menu", "空间列表-浏览协会空间-菜单栏-会员-菜单栏")

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员
    Kjlb_browseascspace_menu_vip_menu_addvip = ("id->com.yunlu6.yunlu:id/btn_add_vip", "空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员")

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理
    Kjlb_browseascspace_menu_vip_menu_manage = ("id->com.yunlu6.yunlu:id/btn_add_manage", "空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理")

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-返回
    Kjlb_browseascspace_menu_vip_menu_manage_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon", "空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-返回")

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索栏
    Kjlb_browseascspace_menu_vip_menu_manage_search = ("id->com.yunlu6.yunlu:id/companyclient_search_keyword", "空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索栏")

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索按钮
    Kjlb_browseascspace_menu_vip_menu_manage_searchbtn = ("id->com.yunlu6.yunlu:id/companyclient_search_search", "空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索按钮")

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑
    Kjlb_browseascspace_menu_vip_menu_manage_edit = ("id->com.yunlu6.yunlu:id/title_main_tv_more_tv", "空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑")

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业
    Kjlb_browseascspace_menu_vip_menu_manage_companyname = ("id->com.yunlu6.yunlu:id/ass_company_name", "空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业")

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业-返回
    Kjlb_browseascspace_menu_vip_menu_manage_companyname_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon", "空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业-返回")

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人
    Kjlb_browseascspace_menu_vip_menu_manage_personname = ("id->com.yunlu6.yunlu:id/vip_name", "空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人")

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人-返回
    Kjlb_browseascspace_menu_vip_menu_manage_personname_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon", "空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人-返回")

    # 空间列表-浏览协会空间-菜单栏-会员-返回
    Kjlb_browseascspace_menu_vip_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon", "空间列表-浏览协会空间-菜单栏-会员-返回")

    # ***************************************【PAGE2】菜单栏-+会员-个人会员Kjlb_browseascspace_menu_addvip_addperson***************************************
    # 定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-添加
    Kjlb_browseascspace_menu_addvip_addperson_confirm = ("id->com.yunlu6.yunlu:id/btn_pop_client_operate", "空间列表-浏览协会空间-菜单栏-会员-个人会员-添加失败")

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-圆圈勾选列表
    Kjlb_browseascspace_menu_addvip_addperson_choose = ("id->com.yunlu6.yunlu:id/item_client_tv_checked", "空间列表-浏览协会空间-菜单栏-会员-个人会员-圆圈勾选失败")

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-全选
    Kjlb_browseascspace_menu_addvip_addperson_all = ("id->com.yunlu6.yunlu:id/title_main_tv_more_tv", "空间列表-浏览协会空间-菜单栏-会员-个人会员-全选失败")

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-搜索按钮
    Kjlb_browseascspace_menu_addvip_addperson_searchbtn = ("id->com.yunlu6.yunlu:id/iv_search", "空间列表-浏览协会空间-菜单栏-会员-个人会员-搜索按钮失败")

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-搜索栏
    Kjlb_browseascspace_menu_addvip_addperson_search = ("id->com.yunlu6.yunlu:id/et_search", "空间列表-浏览协会空间-菜单栏-会员-个人会员-搜索栏失败")

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-返回
    Kjlb_browseascspace_menu_addvip_addperson_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon", "空间列表-浏览协会空间-菜单栏-会员-个人会员-返回失败")

    '''
        20180322，添加企业会员此处代码已过期，注释，start
    '''

    # ***************************************【PAGE2】菜单栏-+会员-企业会员Kjlb_browseascspace_menu_addvip_addcompany***************************************
    # # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-返回
    # Kjlb_browseascspace_menu_addvip_addcompany_back = ("id->com.yunlu6.yunlu:id/title_main_back_more_icon", "空间列表-浏览协会空间-菜单栏-会员-企业会员-返回失败")
    #
    # # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索栏
    # Kjlb_browseascspace_menu_addvip_addcompany_search = ("id->com.yunlu6.yunlu:id/buildyunlu_search_key", "空间列表-浏览协会空间-菜单栏-会员-企业会员-搜索栏失败")
    #
    # # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索栏-搜索栏
    # Kjlb_browseascspace_menu_addvip_addcompany_search_search = ("id->com.yunlu6.yunlu:id/et_search_key", "空间列表-浏览协会空间-菜单栏-会员-企业会员-搜索栏-搜索栏失败")
    #
    # # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索按钮
    # Kjlb_browseascspace_menu_addvip_addcompany_searchbtn = ("id->com.yunlu6.yunlu:id/iv_search", "空间列表-浏览协会空间-菜单栏-会员-企业会员-搜索按钮失败")
    #
    # # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-菜单栏
    # Kjlb_browseascspace_menu_addvip_addcompany_menu = ("id->com.yunlu6.yunlu:id/iv_more", "空间列表-浏览协会空间-菜单栏-会员-企业会员-菜单栏失败")
    #
    # # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近
    # Kjlb_browseascspace_menu_addvip_addcompany_nearby = ("id->com.yunlu6.yunlu:id/ll_recover", "空间列表-浏览协会空间-菜单栏-会员-企业会员-我的附近失败")
    #
    # # 定位:空间列表-浏览协会空间-菜单栏-浏览记录
    # Kjlb_browseascspace_menu_history = ("id->com.yunlu6.yunlu:id/anti", "空间列表-浏览协会空间-菜单栏-浏览记录")
    #
    # # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-圆圈勾选列表
    # Kjlb_browseascspace_menu_addvip_addcompany_choose = ("id->com.yunlu6.yunlu:id/assadd_select_icon", "空间列表-浏览协会空间-菜单栏-会员-企业会员-圆圈勾选失败")
    #
    '''
        20180322,end
    '''

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索栏
    Kjlb_browseascspace_menu_addvip_addcompany_search = ("id->com.yunlu6.yunlu:id/buildstone_search_key", "空间列表-浏览协会空间-菜单栏-会员-企业会员-搜索栏失败")

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索按钮
    Kjlb_browseascspace_menu_addvip_addcompany_searchbtn = ("id->com.yunlu6.yunlu:id/iv_search", "空间列表-浏览协会空间-菜单栏-会员-企业会员-搜索按钮失败")

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索栏-搜索栏
    Kjlb_browseascspace_menu_addvip_addcompany_search_search = ("id->com.yunlu6.yunlu:id/et_search_key", "空间列表-浏览协会空间-菜单栏-会员-企业会员-搜索栏-搜索栏失败")

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-圆圈勾选列表
    Kjlb_browseascspace_menu_addvip_addcompany_choose = ("id->com.yunlu6.yunlu:id/assadd_select_icon", "空间列表-浏览协会空间-菜单栏-会员-企业会员-圆圈勾选失败")

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-确定
    Kjlb_browseascspace_menu_addvip_addcompany_confirm = (
    "id->com.yunlu6.yunlu:id/company_search_assadd", "空间列表-浏览协会空间-菜单栏-会员-企业会员-确定失败")

    # ***************************************【PAGE2】菜单栏-搜附近Kjlb_browseascspace_menu_nearby***************************************
    # 【PAGE3】路线Kjlb_browseascspace_menu_addvip_addcompany_nearby_route
    # 【PAGE3】路线-返回Kjlb_browseascspace_menu_addvip_addcompany_nearby_route_back
    # 【PAGE3】确定Kjlb_browseascspace_menu_addvip_addcompany_nearby_confirm
    # 【PAGE3】搜索栏Kjlb_browseascspace_menu_addvip_addcompany_nearby_search
    # 【PAGE3】搜索按钮Kjlb_browseascspace_menu_addvip_addcompany_nearby_searchbtn
    # 【PAGE3】返回Kjlb_browseascspace_menu_addvip_addcompany_nearby_back
