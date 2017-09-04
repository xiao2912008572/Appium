__author__ = 'xiaoj'
#空间首页
from StoneUIFramework.public.pages.space.SPACEPAGE1 import _SPACEPAGE1

class _SPACEPAGE2(_SPACEPAGE1):
#*********************************【PAGE1】+机构空间：Kjlb_mainmenu_newspace*********************************
     # 空间列表-主菜单-'+机构空间'-机构全称
    def Kjlb_mainmenu_newspace_orgname(self):
        self.Kjlb_mainmenu_newspace_orgname = self.p.get_element("id->com.yunlu6.stone:id/ed_organization_name","定位空间列表-主菜单-'+机构空间'-机构全称失败")
        return self.Kjlb_mainmenu_newspace_orgname

    # 空间列表-主菜单-'+机构空间'-机构简称
    def Kjlb_mainmenu_newspace_orgintro(self):
        self.Kjlb_mainmenu_newspace_orgintro = self.p.get_element("id->com.yunlu6.stone:id/ed_organization_intro","定位空间列表-主菜单-'+机构空间'-机构简称失败")
        return self.Kjlb_mainmenu_newspace_orgintro

    # 空间列表-主菜单-'+机构空间'-新建机构空间标题
    def Kjlb_mainmenu_newspace_orgtitle(self):
        self.Kjlb_mainmenu_newspace_orgtitle = self.p.get_element("id->com.yunlu6.stone:id/title_tv_title","定位空间列表-主菜单-'+机构空间'-新建机构空间标题失败")
        return self.Kjlb_mainmenu_newspace_orgtitle

    # 空间列表-主菜单-'+机构空间'-机构类型
    def Kjlb_mainmenu_newspace_orgtype(self):
        self.Kjlb_mainmenu_newspace_orgtype = self.p.get_element("id->com.yunlu6.stone:id/tv_organization_type","定位空间列表-主菜单-'+机构空间'-机构类型失败")
        return self.Kjlb_mainmenu_newspace_orgtype


    # 空间列表-主菜单-'+机构空间'-机构类型-企业
    def Kjlb_mainmenu_newspace_orgtype_company(self):
        self.Kjlb_mainmenu_newspace_orgtype_company = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_company","定位空间列表-主菜单-'+机构空间'-机构类型-企业失败")
        return self.Kjlb_mainmenu_newspace_orgtype_company

    # 空间列表-主菜单-'+机构空间'-机构类型-协会
    def Kjlb_mainmenu_newspace_orgtype_association(self):
        self.Kjlb_mainmenu_newspace_orgtype_association = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_association","定位空间列表-主菜单-'+机构空间'-机构类型-协会失败")
        return self.Kjlb_mainmenu_newspace_orgtype_association

    # 空间列表-主菜单-'+机构空间'-产业角色
    def Kjlb_mainmenu_newspace_industry(self):
        self.Kjlb_mainmenu_newspace_industry = self.p.get_element("id->com.yunlu6.stone:id/rl_organization_industry","定位空间列表-主菜单-'+机构空间'-产业角色失败")
        return self.Kjlb_mainmenu_newspace_industry

    # 空间列表-主菜单-'+机构空间'-产业角色-产业角色标签
    def Kjlb_mainmenu_newspace_industry_tag(self):
        self.Kjlb_mainmenu_newspace_industry_tag = self.p.get_elements("id->com.yunlu6.stone:id/tag_id","定位空间列表-主菜单-'+机构空间'-产业角色-产业角色标签失败")
        return self.Kjlb_mainmenu_newspace_industry_tag

    # 空间列表-主菜单-'+机构空间'-客户类型
    def Kjlb_mainmenu_newspace_customertype(self):
        self.Kjlb_mainmenu_newspace_customertype = self.p.get_element("id->com.yunlu6.stone:id/tv_organization_customer_type","定位空间列表-主菜单-'+机构空间'-客户类型失败")
        return self.Kjlb_mainmenu_newspace_customertype

    # 空间列表-主菜单-'+机构空间'-客户类型-客户类型标签
    def Kjlb_mainmenu_newspace_customertype_tag(self):
        self.Kjlb_mainmenu_newspace_customertype_tag = self.p.get_elements("id->com.yunlu6.stone:id/tag_id","定位空间列表-主菜单-'+机构空间'-客户类型-客户类型标签失败")
        return self.Kjlb_mainmenu_newspace_customertype_tag

    # 空间列表-主菜单-'+机构空间'-客户类型-客户类型确定
    def Kjlb_mainmenu_newspace_customertype_confirm(self):
        self.Kjlb_mainmenu_newspace_customertype_confirm = self.p.get_element("id->com.yunlu6.stone:id/btn_confirm","定位空间列表-主菜单-'+机构空间'-客户类型-客户类型确定失败")
        return self.Kjlb_mainmenu_newspace_customertype_confirm

    # 空间列表-主菜单-'+机构空间'-所在地区
    def Kjlb_mainmenu_newspace_area(self):
        self.Kjlb_mainmenu_newspace_area = self.p.get_element("id->com.yunlu6.stone:id/tv_organization_address","定位空间列表-主菜单-'+机构空间'-所在地区失败")
        return self.Kjlb_mainmenu_newspace_area

    # 空间列表-主菜单-'+机构空间'-所在地区-省市区列表
    def Kjlb_mainmenu_newspace_area_address(self):
        self.Kjlb_mainmenu_newspace_area_address = self.p.get_elements("id->com.yunlu6.stone:id/tv_address","定位空间列表-主菜单-'+机构空间'-所在地区-省市区失败")
        return self.Kjlb_mainmenu_newspace_area_address

    # 空间列表-主菜单-'+机构空间'-详细地址框
    def Kjlb_mainmenu_newspace_addressdetail(self):
        self.Kjlb_mainmenu_newspace_addressdetail = self.p.get_element("id->com.yunlu6.stone:id/tv_organization_detailed","定位空间列表-主菜单-'+机构空间'-详细地址框失败")
        return self.Kjlb_mainmenu_newspace_addressdetail

    # 空间列表-主菜单-'+机构空间'-详细地址按钮
    def Kjlb_mainmenu_newspace_mapdetail(self):
        self.Kjlb_mainmenu_newspace_mapdetail = self.p.get_element("id->com.yunlu6.stone:id/iv_map","定位空间列表-主菜单-'+机构空间'-详细地址失败")
        return self.Kjlb_mainmenu_newspace_mapdetail

    # 空间列表-主菜单-'+机构空间'-提交
    def Kjlb_mainmenu_newspace_affirm(self):
        self.Kjlb_mainmenu_newspace_affirm = self.p.get_element("id->com.yunlu6.stone:id/btn_affirm","定位空间列表-主菜单-'+机构空间'-提交失败")
        return self.Kjlb_mainmenu_newspace_affirm

    #----------------------对公账号验证-----------------------
    # 空间列表-主菜单-'+机构空间'-去验证
    def Kjlb_mainmenu_newspace_verifynow(self):
        self.Kjlb_mainmenu_newspace_verifynow = self.p.get_element("id->com.yunlu6.stone:id/tv_now","定位空间列表-主菜单-'+机构空间'-去验证失败")
        return self.Kjlb_mainmenu_newspace_verifynow

    # 空间列表-主菜单-'+机构空间'-去验证-返回
    def Kjlb_mainmenu_newspace_verifynow_back(self):
        self.Kjlb_mainmenu_newspace_verifynow_back = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","定位空间列表-主菜单-'+机构空间'-去验证-返回失败")
        return self.Kjlb_mainmenu_newspace_verifynow_back

    # 空间列表-主菜单-'+机构空间'-去验证-真实姓名
    def Kjlb_mainmenu_newspace_verifynow_sovereigntyname(self):
        self.Kjlb_mainmenu_newspace_verifynow_sovereigntyname = self.p.get_element("id->com.yunlu6.stone:id/et_sovereignty_name","定位空间列表-主菜单-'+机构空间'-去验证-真实姓名失败")
        return self.Kjlb_mainmenu_newspace_verifynow_sovereigntyname

    # 空间列表-主菜单-'+机构空间'-去验证-身份证号
    def Kjlb_mainmenu_newspace_verifynow_idnumber(self):
        self.Kjlb_mainmenu_newspace_verifynow_idnumber = self.p.get_element("id->com.yunlu6.stone:id/et_sovereignty_id_number","定位空间列表-主菜单-'+机构空间'-去验证-身份证号失败")
        return self.Kjlb_mainmenu_newspace_verifynow_idnumber

    # 空间列表-主菜单-'+机构空间'-去验证-银行开户名
    def Kjlb_mainmenu_newspace_verifynow_bankname(self):
        self.Kjlb_mainmenu_newspace_verifynow_bankname = self.p.get_element("id->com.yunlu6.stone:id/tv_sover_bank_name","定位空间列表-主菜单-'+机构空间'-去验证-银行开户名失败")
        return self.Kjlb_mainmenu_newspace_verifynow_bankname

    # 空间列表-主菜单-'+机构空间'-去验证-开户银行
    def Kjlb_mainmenu_newspace_verifynow_soverbank(self):
        self.Kjlb_mainmenu_newspace_verifynow_soverbank = self.p.get_element("id->com.yunlu6.stone:id/et_sover_bank","定位空间列表-主菜单-'+机构空间'-去验证-开户银行失败")
        return self.Kjlb_mainmenu_newspace_verifynow_soverbank

    # 空间列表-主菜单-'+机构空间'-去验证-所在地区
    def Kjlb_mainmenu_newspace_verifynow_soveraddress(self):
        self.Kjlb_mainmenu_newspace_verifynow_soveraddress = self.p.get_element("id->com.yunlu6.stone:id/tv_sover_address","定位空间列表-主菜单-'+机构空间'-去验证-所在地区失败")
        return self.Kjlb_mainmenu_newspace_verifynow_soveraddress

    # 空间列表-主菜单-'+机构空间'-去验证-所在地区-列表
    def Kjlb_mainmenu_newspace_verifynow_soveraddress_list(self):
        self.Kjlb_mainmenu_newspace_verifynow_soveraddress_list = self.p.get_element("com.yunlu6.stone:id/tv_address","定位空间列表-主菜单-'+机构空间'-去验证-所在地区-列表失败")
        return self.Kjlb_mainmenu_newspace_verifynow_soveraddress_list

    # 空间列表-主菜单-'+机构空间'-去验证-支行
    def Kjlb_mainmenu_newspace_verifynow_sovermybank(self):
        self.Kjlb_mainmenu_newspace_verifynow_sovermybank = self.p.get_element("id->com.yunlu6.stone:id/et_sover_my_bank","定位空间列表-主菜单-'+机构空间'-去验证-支行失败")
        return self.Kjlb_mainmenu_newspace_verifynow_sovermybank

    # 空间列表-主菜单-'+机构空间'-去验证-银行账号
    def Kjlb_mainmenu_newspace_verifynow_soverbanknub(self):
        self.Kjlb_mainmenu_newspace_verifynow_soverbanknub = self.p.get_element("id->com.yunlu6.stone:id/et_sover_bank_nub","定位空间列表-主菜单-'+机构空间'-去验证-银行账号失败")
        return self.Kjlb_mainmenu_newspace_verifynow_soverbanknub

    # 空间列表-主菜单-'+机构空间'-去验证-审核费
    def Kjlb_mainmenu_newspace_verifynow_money(self):
        self.Kjlb_mainmenu_newspace_verifynow_money = self.p.get_element("id->com.yunlu6.stone:id/tv_money","定位空间列表-主菜单-'+机构空间'-去验证-审核费失败")
        return self.Kjlb_mainmenu_newspace_verifynow_money

    # 空间列表-主菜单-'+机构空间'-去验证-确定提交
    def Kjlb_mainmenu_newspace_verifynow_soversave(self):
        self.Kjlb_mainmenu_newspace_verifynow_soversave = self.p.get_element("id->com.yunlu6.stone:id/bt_sover_save","定位空间列表-主菜单-'+机构空间'-去验证-确定提交失败")
        return self.Kjlb_mainmenu_newspace_verifynow_soversave

    # 空间列表-主菜单-'+机构空间'-去验证-确定提交-返回
    def Kjlb_mainmenu_newspace_verifynow_soversave_back(self):
        self.Kjlb_mainmenu_newspace_verifynow_soversave_back = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","定位空间列表-主菜单-'+机构空间'-去验证-确定提交-返回失败")
        return self.Kjlb_mainmenu_newspace_verifynow_soversave_back

#*********************************【PAGE1】+私人空间空间：Kjlb_mainmenu_newpersonspace*********************************
    # 空间列表-主菜单-'+私人空间'-返回
    def Kjlb_mainmenu_newpersonspace_back(self):
        self.Kjlb_mainmenu_newpersonspace_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-主菜单-'+私人空间'")
        return self.Kjlb_mainmenu_newpersonspace_backP

    # 空间列表-主菜单-'+私人空间'-选择空间类型列表
    def Kjlb_mainmenu_newpersonspace_choosespacetype(self):
        self.Kjlb_mainmenu_newpersonspace_choosespacetypeP = self.p.get_elements("id->com.yunlu6.stone:id/item_zone_type_im","空间列表-主菜单-'+私人空间'-选择空间类型")
        return self.Kjlb_mainmenu_newpersonspace_choosespacetypeP

    # 空间列表-主菜单-'+私人空间-空间名称
    def Kjlb_mainmenu_newpersonspace_spacename(self):
        self.Kjlb_mainmenu_newpersonspace_spacenameP = self.p.get_element("id->com.yunlu6.stone:id/create_et_spacename","空间列表-主菜单-'+私人空间'-空间名称")
        return self.Kjlb_mainmenu_newpersonspace_spacenameP

    # 空间列表-主菜单-'+私人空间'-切换空间类型
    def Kjlb_mainmenu_newpersonspace_changespacetype(self):
        self.Kjlb_mainmenu_newpersonspace_changespacetypeP = self.p.get_element("id->com.yunlu6.stone:id/create_img_type","空间列表-主菜单-'+私人空间'-切换空间类型")
        return self.Kjlb_mainmenu_newpersonspace_changespacetypeP

    # 空间列表-主菜单-'+私人空间'-文件夹名称
    def Kjlb_mainmenu_newpersonspace_foldername(self):
        self.Kjlb_mainmenu_newpersonspace_foldernameP = self.p.get_element("id->com.yunlu6.stone:id/create_folder_name","空间列表-主菜单-'+私人空间'-文件名称")
        return self.Kjlb_mainmenu_newpersonspace_foldernameP

    # 空间列- 主菜单-'+私人空间'-推荐空间名标签
    def Kjlb_mainmenu_newpersonspace_suggestspacenametag(self):
        self.Kjlb_mainmenu_newpersonspace_suggestspacenametagP = self.p.get_elements("id->com.yunlu6.stone:id/tag_id","空间列表-主菜单-'+私人空间'-推荐空间名标签")
        return self.Kjlb_mainmenu_newpersonspace_suggestspacenametagP

    # 空间列表-主菜单-'+私人空间'-保存
    def Kjlb_mainmenu_newpersonspace_save(self):
        self.Kjlb_mainmenu_newpersonspace_saveP = self.p.get_element("id->com.yunlu6.stone:id/create_btn_save","空间列表-主菜单-'+私人空间'-保存")
        return self.Kjlb_mainmenu_newpersonspace_saveP

    # 空间列表-主菜单-'+私人空间'-主页面返回
    def Kjlb_mainmenu_newpersonspace_mainback(self):
        self.Kjlb_mainmenu_newpersonspace_mainbackP = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-主菜单-'+私人空间'-主页面返回")
        return self.Kjlb_mainmenu_newpersonspace_mainbackP

#*********************************【PAGE1】+分享名片：Kjlb_mainmenu_sharecard*********************************
    # 空间列表-主菜单-分享名片
    def Kjlb_mainmenu_sharecard(self):
        self.Kjlb_mainmenu_sharecard = self.p.get_element("id->com.yunlu6.stone:id/btn_share_space","空间列表-主菜单-分享名片")
        return self.Kjlb_mainmenu_sharecard

    # 空间列表-主菜单-分享名片-返回
    def Kjlb_mainmenu_sharecard_back(self):
        self.Kjlb_mainmenu_sharecard_back = self.p.get_element("id->com.yunlu6.stone:id/title_back_edit_icon","空间列表-主菜单-分享名片-返回")
        return self.Kjlb_mainmenu_sharecard_back

    # 空间列表-主菜单-分享名片-分享
    def Kjlb_mainmenu_sharecard_share(self):
        _share = self.p.get_element("id->com.yunlu6.stone:id/title_tv_edit_menu_tv","空间列表-主菜单-分享名片-分享")
        return self.Kjlb_mainmenu_sharecard_share

    # 空间列表-主菜单-分享名片-手机
    def Kjlb_mainmenu_sharecard_phone(self):
        self.Kjlb_mainmenu_sharecard_phone = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_phone_cb","空间列表-主菜单-分享名片-手机")
        return self.Kjlb_mainmenu_sharecard_phone

    # 空间列表-主菜单-分享名片-邮箱
    def Kjlb_mainmenu_sharecard_email(self):
        self.Kjlb_mainmenu_sharecard_email = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_email_cb","空间列表-主菜单-分享名片-邮箱")
        return self.Kjlb_mainmenu_sharecard_email

    # 空间列表-主菜单-分享名片-地址
    def Kjlb_mainmenu_sharecard_address(self):
        self.Kjlb_mainmenu_sharecard_address = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_address_cb","空间列表-主菜单-分享名片-地址")
        return self.Kjlb_mainmenu_sharecard_address

    # 空间列表-主菜单-分享名片-QQ
    def Kjlb_mainmenu_sharecard_qq(self):
        self.Kjlb_mainmenu_sharecard_qq = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_qq_cb","空间列表-主菜单-分享名片-QQ")
        return self.Kjlb_mainmenu_sharecard_qq

    # 空间列表-主菜单-分享名片-空间按钮
    def Kjlb_mainmenu_sharecard_spacebutton(self):
        self.Kjlb_mainmenu_sharecard_spacebutton = self.p.get_elements("id->com.yunlu6.stone:id/user_card_team_item_cb","空间列表-主菜单-分享名片-空间按钮")
        return self.Kjlb_mainmenu_sharecard_spacebutton

#*********************************【PAGE1】【机构空间】浏览空间列表：Kjlb_browseorgspaceByID*********************************
    # 空间列表-浏览企业空间-返回
    def Kjlb_browseorgspace_back(self):
        self.Kjlb_browseorgspace_back = self.p.get_element("com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览企业空间-返回失败")
        return self.Kjlb_browseorgspace_back

    # 空间列表-浏览企业空间-菜单栏
    def Kjlb_browseorgspace_menu(self):
        self.Kjlb_browseorgspace_menu = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览企业空间-菜单栏")
        return self.Kjlb_browseorgspace_menu

    # 空间列表-浏览企业空间-菜单栏-业务升级
    def Kjlb_browseorgspace_menu_upgrade(self):
        self.Kjlb_browseorgspace_menu_upgrade = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_company_upgrade","空间列表-浏览企业空间-菜单栏-业务升级")
        return self.Kjlb_browseorgspace_menu_upgrade

    #  空间列表-浏览企业空间-菜单栏-产品
    def Kjlb_browseorgspace_menu_product(self):
        self.Kjlb_browseorgspace_menu_productP = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_company_product","空间列表-浏览企业空间-菜单栏-产品")
        return self.Kjlb_browseorgspace_menu_productP

    # 空间列表-浏览企业空间-菜单栏-企业名片
    def Kjlb_browseorgspace_menu_bcard(self):
        self.Kjlb_browseorgspace_menu_bcard = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_company_info","空间列表-浏览企业空间-菜单栏-企业名片")
        return self.Kjlb_browseorgspace_menu_bcard

    # 空间列表-浏览企业空间-菜单栏-团队
    def Kjlb_browseorgspace_menu_team(self):
        self.Kjlb_browseorgspace_menu_team = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_company_team","空间列表-浏览企业空间-菜单栏-团队")
        return self.Kjlb_browseorgspace_menu_team

    # 空间列表-浏览企业空间-菜单栏-客户
    def Kjlb_browseorgspace_menu_customer(self):
        self.Kjlb_browseorgspace_menu_customer = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_company_customer","空间列表-浏览企业空间-菜单栏-客户")
        return self.Kjlb_browseorgspace_menu_customer

    # 空间列表-浏览企业空间-菜单栏-访客
    def Kjlb_browseorgspace_menu_visitor(self):
        self.Kjlb_browseorgspace_menu_visitor = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_company_fangke","空间列表-浏览企业空间-菜单栏-访客")
        return self.Kjlb_browseorgspace_menu_visitor

    # 空间列表-浏览企业空间-菜单栏-资讯
    def Kjlb_browseorgspace_menu_archivies(self):
        self.Kjlb_browseorgspace_menu_archivies = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_company_archivies","空间列表-浏览企业空间-菜单栏-资讯")
        return self.Kjlb_browseorgspace_menu_archivies

#*********************************【PAGE1】【私人空间】浏览空间列表：Kjlb_browseorgspaceByID*********************************
    # 空间列表-浏览私人空间-返回
    def Kjlb_browseperspace_back(self):
        self.Kjlb_browseascspace_backP = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览私人空间-返回")
        return self.Kjlb_browseascspace_backP

    # 空间列表-浏览私人空间-照片列表
    def Kjlb_browseperspace_piclist(self):
        self.Kjlb_browseperspace_piclistP = self.p.get_elements("id->com.yunlu6.stone:id/presonzone_gridview_iv","空间列表-浏览私人空间-照片列表")
        return self.Kjlb_browseperspace_piclistP

    # 空间列表-浏览私人空间-菜单栏
    def Kjlb_browseperspace_menu(self):
        self.Kjlb_browseperspace_menuP = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览私人空间-菜单栏")
        return self.Kjlb_browseperspace_menuP

    # 空间列表-浏览私人空间-菜单栏-名片
    def Kjlb_browseperspace_menu_card(self):
        self.Kjlb_browseperspace_menu_cardP = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_gallery_card","空间列表-浏览私人空间-菜单栏-名片")
        return self.Kjlb_browseperspace_menu_cardP

    # 空间列表-浏览私人空间-菜单栏-编辑
    def Kjlb_browseperspace_menu_edit(self):
        self.Kjlb_browseperspace_menu_editP = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_gallery_edit","空间列表-浏览私人空间-菜单栏-编辑")
        return self.Kjlb_browseperspace_menu_editP

    # 空间列表-浏览私人空间-菜单栏-客户
    def Kjlb_browseperspace_menu_customer(self):
        self.Kjlb_browseperspace_menu_customerP = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_gallery_client","空间列表-浏览私人空间-菜单栏-客户")
        return self.Kjlb_browseperspace_menu_customerP

     # 空间列表-浏览私人空间-菜单栏-+文件夹
    def Kjlb_browseperspace_menu_addfolder(self):
        self.Kjlb_browseperspace_menu_addfolderP = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_gallery_add","空间列表-浏览私人空间-菜单栏-+文件夹")
        return self.Kjlb_browseperspace_menu_addfolderP

    # 空间列表-浏览私人空间-加数据
    def Kjlb_browseperspace_adata(self):
        self.Kjlb_browseperspace_adataP = self.p.get_element("id->com.yunlu6.stone:id/personzone_grid_itemup","空间列表-浏览私人空间-加数据")
        return self.Kjlb_browseperspace_adataP

    # 空间列表-浏览私人空间-更多
    def Kjlb_browseperspace_more(self):
        self.Kjlb_browseperspace_moreP = self.p.get_element("id->com.yunlu6.stone:id/personzone_grid_itemdown","空间列表-浏览私人空间-更多")
        return self.Kjlb_browseperspace_moreP

#*********************************【PAGE1】【协会空间】浏览空间列表：Kjlb_browseorgspaceByID*********************************
    # 空间列表-浏览协会空间-添加按钮
    def Kjlb_browseascspace_addbtn(self):
        self.Kjlb_browseascspace_addbtnA = self.p.get_element("id->com.yunlu6.stone:id/companycard_moremenu","空间列表-浏览协会空间-添加按钮")
        return self.Kjlb_browseascspace_addbtnA

    # 空间列表-浏览协会空间-添加按钮-企业会员
    def Kjlb_browseascspace_addbtn_oVip(self):
        self.Kjlb_browseascspace_addbtn_oVipA = self.p.get_element("id->com.yunlu6.stone:id/add_ass_tv","空间列表-浏览协会空间-添加按钮-企业会员")
        return self.Kjlb_browseascspace_addbtn_oVipA

    # 空间列表-浏览协会空间-添加按钮-个人会员
    def Kjlb_browseascspace_addbtn_pVip(self):
        self.Kjlb_browseascspace_addbtn_pVipA = self.p.get_element("id->com.yunlu6.stone:id/add_person_tv","空间列表-浏览协会空间-添加按钮-个人会员")
        return self.Kjlb_browseascspace_addbtn_pVipA

    # 空间列表-浏览协会空间-添加按钮-关注
    def Kjlb_browseascspace_addbtn_concern(self):
        self.Kjlb_browseascspace_addbtn_concernA = self.p.get_element("id->com.yunlu6.stone:id/tv_add_favorites","空间列表-浏览协会空间-添加按钮-关注")
        return self.Kjlb_browseascspace_addbtn_concernA

    # 空间列表-浏览协会空间-添加按钮-取消关注
    def Kjlb_browseascspace_addbtn_concernC(self):
        self.Kjlb_browseascspace_addbtn_concernC = self.p.get_element("id->com.yunlu6.stone:id/tv_add_favorites","空间列表-浏览协会空间-添加按钮-取消关注")
        return self.Kjlb_browseascspace_addbtn_concernC

    # 空间列表-浏览协会空间-添加按钮-申请加入
    def Kjlb_browseascspace_addbtn_apply(self):
        self.Kjlb_browseascspace_addbtn_applyA = self.p.get_element("id->com.yunlu6.stone:id/add_client_tv","空间列表-浏览协会空间-添加按钮-申请加入")
        return self.Kjlb_browseascspace_addbtn_applyA

     # 空间列表-浏览协会空间-企业会员
    def Kjlb_browseascspace_ovip(self):
        self.Kjlb_browseascspace_ovipA = self.p.get_element("id->com.yunlu6.stone:id/btn_company","空间列表-浏览协会空间-企业会员")
        return self.Kjlb_browseascspace_ovipA

     # 空间列表-浏览协会空间-个人会员
    def Kjlb_browseascspace_pvip(self):
        self.Kjlb_browseascspace_pvipA = self.p.get_element("id->com.yunlu6.stone:id/btn_person","空间列表-浏览协会空间-个人会员")
        return self.Kjlb_browseascspace_pvipA

     # 空间列表-浏览协会空间-资讯
    def Kjlb_browseascspace_arch(self):
        self.Kjlb_browseascspace_archA = self.p.get_element("id->com.yunlu6.stone:id/btn_archivie","空间列表-浏览协会空间-资讯")
        return self.Kjlb_browseascspace_archA

     # 空间列表-浏览协会空间-资信
    def Kjlb_browseascspace_credit(self):
        self.Kjlb_browseascspace_creditA = self.p.get_element("id->com.yunlu6.stone:id/ass_companycard_level","空间列表-浏览协会空间-资信")
        return self.Kjlb_browseascspace_creditA

    # 空间列表-浏览协会空间-返回
    def Kjlb_browseascspace_back(self):
        self.Kjlb_browseascspace_backA = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-返回")
        return self.Kjlb_browseascspace_backA

     #定位:空间列表-浏览协会空间-菜单栏
    def Kjlb_browseascspace_menu(self):
        self.Kjlb_browseascspace_menuA = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览协会空间-菜单栏")
        return self.Kjlb_browseascspace_menuA

    # 空间列表-浏览协会空间-菜单栏-编辑
    def Kjlb_browseascspace_menu_edit(self):
        self.Kjlb_browseascspace_menu_editA = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_association_edit","空间列表-浏览协会空间-菜单栏-编辑")
        return self.Kjlb_browseascspace_menu_editA

    # 空间列表-浏览协会空间-菜单栏-团队
    def Kjlb_browseascspace_menu_team(self):
        self.Kjlb_browseascspace_menu_teamA = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_association_member","空间列表-浏览协会空间-菜单栏-团队")
        return self.Kjlb_browseascspace_menu_teamA

     # 空间列表-浏览协会空间-菜单栏-会员
    def Kjlb_browseascspace_menu_vip(self):
        self.Kjlb_browseascspace_menu_vipA = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_association_vip","空间列表-浏览协会空间-菜单栏-会员")
        return self.Kjlb_browseascspace_menu_vipA

    #定位:空间列表-浏览协会空间-菜单栏-加会员
    def Kjlb_browseascspace_menu_addvip(self):
        self.Kjlb_browseascspace_menu_addvipA = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_association_addvip","空间列表-浏览协会空间-菜单栏-会员失败")
        return self.Kjlb_browseascspace_menu_addvipA

     #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员
    def Kjlb_browseascspace_menu_addvip_addperson(self):
        self.Kjlb_browseascspace_menu_addvip_addpersonA = self.p.get_element("id->com.yunlu6.stone:id/pop_assvip_addperson","空间列表-浏览协会空间-菜单栏-会员-个人会员失败")
        return self.Kjlb_browseascspace_menu_addvip_addpersonA

     #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员
    def Kjlb_browseascspace_menu_addvip_addcompany(self):
        self.Kjlb_browseascspace_menu_addvip_addcompanyA = self.p.get_element("id->com.yunlu6.stone:id/pop_assvip_addcompany","空间列表-浏览协会空间-菜单栏-会员-企业会员失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompanyA

     #定位:空间列表-浏览协会空间-菜单栏-加会员-取消
    def Kjlb_browseascspace_menu_addvip_cancel(self):
        self.Kjlb_browseascspace_menu_addvip_cancelA = self.p.get_element("id->com.yunlu6.stone:id/pop_assvip_cancle","空间列表-浏览协会空间-菜单栏-会员-取消失败")
        return self.Kjlb_browseascspace_menu_addvip_cancelA

    #定位:空间列表-浏览协会空间-菜单栏-客户
    def Kjlb_browseascspace_menu_customer(self):
        self.Kjlb_browseascspace_menu_customerA = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_association_customer","空间列表-浏览协会空间-菜单栏-客户")
        return self.Kjlb_browseascspace_menu_addvip_cancelA

     #定位:空间列表-浏览协会空间-菜单栏-资讯
    def Kjlb_browseascspace_menu_arc(self):
        self.Kjlb_browseascspace_menu_arcA = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_association_file","空间列表-浏览协会空间-菜单栏-资讯")
        return self.Kjlb_browseascspace_menu_arcA

     #定位:空间列表-浏览协会空间-菜单栏-搜附近
    def Kjlb_browseascspace_menu_nearby(self):
        self.Kjlb_browseascspace_menu_nearbyA = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_association_nearbusz","空间列表-浏览协会空间-菜单栏-搜附近")
        return self.Kjlb_browseascspace_menu_nearbyA

    #定位:空间列表-浏览协会空间-菜单栏-关闭
    def Kjlb_browseascspace_menu_close(self):
        self.Kjlb_browseascspace_menu_nearbyA = self.p.get_element("id->com.yunlu6.stone:id/bt_close","空间列表-浏览协会空间-菜单栏-关闭")
        return self.Kjlb_browseascspace_menu_nearbyA

     #定位:空间列表-浏览协会空间-菜单栏-关闭-是
    def Kjlb_browseascspace_menu_close_yes(self):
        self.Kjlb_browseascspace_menu_nearbyA = self.p.get_element("id->com.yunlu6.stone:id/bt_affirm","空间列表-浏览协会空间-菜单栏-关闭-是")
        return self.Kjlb_browseascspace_menu_nearbyA

     #定位:空间列表-浏览协会空间-菜单栏-关闭-否
    def Kjlb_browseascspace_menu_close_no(self):
        self.Kjlb_browseascspace_menu_nearbyA = self.p.get_element("id->com.yunlu6.stone:id/bt_cancel","空间列表-浏览协会空间-菜单栏-关闭-否")
        return self.Kjlb_browseascspace_menu_nearbyA

    #定位:空间列表-浏览协会空间-菜单栏-设置
    def Kjlb_browseascspace_menu_setting(self):
        self.Kjlb_browseascspace_menu_settingA = self.p.get_element("id->com.yunlu6.stone:id/bt_setup","空间列表-浏览协会空间-菜单栏-设置")
        return self.Kjlb_browseascspace_menu_settingA

     #定位:空间列表-浏览协会空间-菜单栏-分享
    def Kjlb_browseascspace_menu_share(self):
        self.Kjlb_browseascspace_menu_shareA = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_association_share","空间列表-浏览协会空间-菜单栏-分享")
        return self.Kjlb_browseascspace_menu_shareA













































