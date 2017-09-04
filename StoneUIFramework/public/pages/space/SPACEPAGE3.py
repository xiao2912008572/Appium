__author__ = 'xiaoj'
#空间首页
from StoneUIFramework.public.pages.space.SPACEPAGE2 import _SPACEPAGE2

class _SPACEPAGE3(_SPACEPAGE2):
#***************************************【PAGE2】产品Kjlb_browseorgspace_menu_product***************************************
#  空间列表-浏览企业空间-菜单栏-产品-返回
    def Kjlb_browseorgspace_menu_product_back(self):
        self.Kjlb_browseorgspace_menu_product_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览企业空间-菜单栏-产品-返回")
        return self.Kjlb_browseorgspace_menu_product_backP

    #  空间列表-浏览企业空间-菜单栏-产品-新建
    def Kjlb_browseorgspace_menu_product_new(self):
        self.Kjlb_browseorgspace_menu_product_newP = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览企业空间-菜单栏-产品-新建")
        return self.Kjlb_browseorgspace_menu_product_newP

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表
    def Kjlb_browseorgspace_menu_product_unlock_list(self):
        self.Kjlb_browseorgspace_menu_product_unlock_list = self.p.get_elements("id->com.yunlu6.stone:id/tv_productr_name","空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表")
        return self.Kjlb_browseorgspace_menu_product_unlock_list

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-产品名查找
    def Kjlb_browseorgspace_menu_product_unlock_list_byname(self,name):
        self.Kjlb_browseorgspace_menu_product_unlock_list_bynameP = self.p.get_elements("name->%s"%name,"空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-产品名查找")
        return self.Kjlb_browseorgspace_menu_product_unlock_list_bynameP

    #  空间列表-浏览企业空间-菜单栏-产品-未发布
    def Kjlb_browseorgspace_menu_product_unlock(self):
        self.Kjlb_browseorgspace_menu_product_unlockP = self.p.get_element("id->com.yunlu6.stone:id/tv_unlock", "空间列表-浏览企业空间-菜单栏-产品-未发布")
        return self.Kjlb_browseorgspace_menu_product_unlockP

     #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-产品名查找
    def Kjlb_browseorgspace_menu_product_lock_list_byname(self,name):
        self.Kjlb_browseorgspace_menu_product_lock_list_bynameP = self.p.get_elements("name->%s"%name,"空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-产品名查找")
        return self.Kjlb_browseorgspace_menu_product_lock_list_bynameP

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表
    def Kjlb_browseorgspace_menu_product_lock_list(self):
        self.Kjlb_browseorgspace_menu_product_lock_listP = self.p.get_element("id->com.yunlu6.stone:id/iv_productr","空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表")
        return self.Kjlb_browseorgspace_menu_product_lock_listP

    #  空间列表-浏览企业空间-菜单栏-产品-已发布
    def Kjlb_browseorgspace_menu_product_lock(self):
        self.Kjlb_browseorgspace_menu_product_lockP = self.p.get_element("id->com.yunlu6.stone:id/tv_lock","空间列表-浏览企业空间-菜单栏-产品-已发布")
        return self.Kjlb_browseorgspace_menu_product_lockP

     # 空间列表-浏览企业空间-菜单栏-产品-收款账号
    def Kjlb_browseorgspace_menu_product_account(self):
        self.Kjlb_browseorgspace_menu_product_accountP = self.p.get_element("name->%s"%"为保障交易安全顺畅，需验证贵司收款银行账户","空间列表-浏览企业空间-菜单栏-产品-收款账号")
        return self.Kjlb_browseorgspace_menu_product_accountP

    # 空间列表-浏览企业空间-菜单栏-产品-搜索
    def Kjlb_browseorgspace_menu_product_seek(self):
        self.Kjlb_browseorgspace_menu_product_seekP = self.p.get_element("id->com.yunlu6.stone:id/et_seek","空间列表-浏览企业空间-菜单栏-产品-搜索")
        return self.Kjlb_browseorgspace_menu_product_seekP

#***************************************【PAGE2】团队Kjlb_browseorgspace_menu_team***************************************
# 空间列表-浏览企业空间-菜单栏-团队-返回
    def Kjlb_browseorgspace_menu_team_back(self):
        self.Kjlb_browseorgspace_menu_team_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览企业空间-菜单栏-团队-返回")
        return self.Kjlb_browseorgspace_menu_team_back

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏
    def Kjlb_browseorgspace_menu_team_menu(self):
        self.Kjlb_browseorgspace_menu_team_menuT = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览企业空间-菜单栏-团队-菜单栏")
        return self.Kjlb_browseorgspace_menu_team_menuT

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免
    def Kjlb_browseorgspace_menu_team_menu_assignjob(self):
        self.Kjlb_browseorgspace_menu_team_menu_assignjobT = self.p.get_element("id->com.yunlu6.stone:id/pop_teamedit_personnel","空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免")
        return self.Kjlb_browseorgspace_menu_team_menu_assignjobT

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门
    def Kjlb_browseorgspace_menu_team_menu_mydepartment(self):
        self.Kjlb_browseorgspace_menu_team_menu_mydepartmentT = self.p.get_element("id->com.yunlu6.stone:id/pop_teamedit_mydepartment","空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门")
        return self.Kjlb_browseorgspace_menu_team_menu_mydepartmentT

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-返回
    def Kjlb_browseorgspace_menu_team_menu_mydepartment_back(self):
        self.Kjlb_browseorgspace_menu_team_menu_mydepartment_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back","空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-返回")
        return self.Kjlb_browseorgspace_menu_team_menu_mydepartment_back

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-搜索
    def Kjlb_browseorgspace_menu_team_menu_mydepartment_seek(self):
        self.Kjlb_browseorgspace_menu_team_menu_mydepartment_seek = self.p.get_element("id->com.yunlu6.stone:id/et_seek","空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-搜索")
        return self.Kjlb_browseorgspace_menu_team_menu_mydepartment_seek

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑
    def Kjlb_browseorgspace_menu_team_teamedit(self):
        self.Kjlb_browseorgspace_menu_team_teameditT = self.p.get_element("id->com.yunlu6.stone:id/companyteam_btn_edit","空间列表-浏览企业空间-菜单栏-团队-团队编辑")
        return self.Kjlb_browseorgspace_menu_team_teameditT

     # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮列表
    def Kjlb_browseorgspace_menu_team_teamedit_numeidtL(self):
        self.Kjlb_browseorgspace_menu_team_teamedit_numeidtT = self.p.get_elements("id->com.yunlu6.stone:id/companyteam_item_edit","空间列表-浏览企业空间-菜单栏-团队-团队编辑-编辑人数按钮列表")
        return self.Kjlb_browseorgspace_menu_team_teamedit_numeidtT

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-职位人数
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit(self):
        self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumeditT = self.p.get_element("id->com.yunlu6.stone:id/teamedit_jobs_editnum","空间列表-浏览企业空间-菜单栏-团队-团队编辑-编辑人数按钮-职位人数按钮")
        return self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumeditT

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-否
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancel(self):
        self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancelT = self.p.get_element("id->com.yunlu6.stone:id/teamedit_cancleedit","空间列表-浏览企业空间-菜单栏-团队-团队编辑-编辑人数按钮-职位人数按钮-否")
        return self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancelT

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-是
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirm(self):
        self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirmT = self.p.get_element("id->com.yunlu6.stone:id/teamedit_commitedit","空间列表-浏览企业空间-菜单栏-团队-团队编辑-编辑人数-职位人数按钮-是")
        return self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirmT

#***************************************【PAGE2】资讯Kjlb_browseorgspace_menu_archivies***************************************
    # 空间列表-浏览企业空间-菜单栏-资讯-返回
    def Kjlb_browseorgspace_menu_archivies_back(self):
        self.Kjlb_browseorgspace_menu_archivies_backT = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览企业空间-菜单栏-资讯-返回")
        return self.Kjlb_browseorgspace_menu_archivies_backT

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮
    def Kjlb_browseorgspace_menu_archivies_new(self):
        self.Kjlb_browseorgspace_menu_archivies_newT = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览企业空间-菜单栏-资讯-新增按钮")
        return self.Kjlb_browseorgspace_menu_archivies_newT

    # 空间列表-浏览企业空间-菜单栏-资讯-图片新增
    def Kjlb_browseorgspace_menu_archivies_picadd(self):
        self.Kjlb_browseorgspace_menu_archivies_picaddA = self.p.get_element("id->com.yunlu6.stone:id/rl_add","空间列表-浏览企业空间-菜单栏-资讯-图片新增")
        return self.Kjlb_browseorgspace_menu_archivies_picaddA

     # 空间列表-浏览企业空间-菜单栏-资讯-图片列表
    def Kjlb_browseorgspace_menu_archivies_pic(self):
        self.Kjlb_browseorgspace_menu_archivies_picA = self.p.get_elements("id->com.yunlu6.stone:id/iv_profile","空间列表-浏览企业空间-菜单栏-资讯-图片列表")
        return self.Kjlb_browseorgspace_menu_archivies_picA

     # 空间列表-浏览企业空间-菜单栏-资讯-图片-标题
    def Kjlb_browseorgspace_menu_archivies_pic_title(self):
        self.Kjlb_browseorgspace_menu_archivies_pic_titleT = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_title","空间列表-浏览企业空间-菜单栏-资讯-图片-标题")
        return self.Kjlb_browseorgspace_menu_archivies_pic_titleT

    # 空间列表-浏览企业空间-菜单栏-资讯-图片-类型
    def Kjlb_browseorgspace_menu_archivies_pic_type(self):
        self.Kjlb_browseorgspace_menu_archivies_pic_typeT = self.p.get_element("id->com.yunlu6.stone:id/tv_profile","空间列表-浏览企业空间-菜单栏-资讯-图片-类型")
        return self.Kjlb_browseorgspace_menu_archivies_pic_typeT

#***************************************【PAGE2】企业名片Kjlb_browseorgspace_menu_bcard***************************************
    # 空间列表-浏览企业空间-菜单栏-企业名片-返回
    def Kjlb_browseorgspace_menu_bcard_back(self):
        self.Kjlb_browseorgspace_menu_bcard_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back","空间列表-浏览企业空间-菜单栏-企业名片-返回")
        return self.Kjlb_browseorgspace_menu_bcard_back

     # 空间列表-浏览企业空间-菜单栏-企业名片-企业资信
    def Kjlb_browseorgspace_menu_bcard_credit(self):
        self.Kjlb_browseorgspace_menu_bcard_credit = self.p.get_element("id->com.yunlu6.stone:id/companycard_level","空间列表-浏览企业空间-菜单栏-企业名片-企业资信")
        return self.Kjlb_browseorgspace_menu_bcard_credit

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏
    def Kjlb_browseorgspace_menu_bcard_menu(self):
        self.Kjlb_browseorgspace_menu_bcard_menuB = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏")
        return self.Kjlb_browseorgspace_menu_bcard_menuB

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队
    def Kjlb_browseorgspace_menu_bcard_menu_quitteam(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_quitteam = self.p.get_element("id->com.yunlu6.stone:id/bt_teamquit","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队")
        return self.Kjlb_browseorgspace_menu_bcard_menu_quitteam

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队-否
    def Kjlb_browseorgspace_menu_bcard_menu_quitteam_cancel(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_quitteam_cancell = self.p.get_element("id->com.yunlu6.stone:id/bt_cancel","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队-否")
        return self.Kjlb_browseorgspace_menu_bcard_menu_quitteam_cancell

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队-是
    def Kjlb_browseorgspace_menu_bcard_menu_quitteam_confirm(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_quitteam_confirm = self.p.get_element("id->com.yunlu6.stone:id/bt_affirm","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-退出团队-是")
        return self.Kjlb_browseorgspace_menu_bcard_menu_quitteam_confirm

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-附近商家
    def Kjlb_browseorgspace_menu_bcard_menu_nearby(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_nearby = self.p.get_element("id->com.yunlu6.stone:id/bt_nearby","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-附近商家")
        return self.Kjlb_browseorgspace_menu_bcard_menu_nearby

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑
    def Kjlb_browseorgspace_menu_bcard_menu_edit(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_editB = self.p.get_element("id->com.yunlu6.stone:id/bt_edit","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-编辑")
        return self.Kjlb_browseorgspace_menu_bcard_menu_editB

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-设置
    def Kjlb_browseorgspace_menu_bcard_menu_setting(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_setting = self.p.get_element("id->com.yunlu6.stone:id/bt_setup","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-设置")
        return self.Kjlb_browseorgspace_menu_bcard_menu_setting

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-关闭
    def Kjlb_browseorgspace_menu_bcard_menu_close(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_close = self.p.get_element("id->com.yunlu6.stone:id/bt_close","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-关闭")
        return self.Kjlb_browseorgspace_menu_bcard_menu_close

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享
    def Kjlb_browseorgspace_menu_bcard_menu_share(self):
        self.Kjlb_browseorgspace_menu_bcard_menu_share = self.p.get_element("id->com.yunlu6.stone:id/bt_share","空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享")
        return self.Kjlb_browseorgspace_menu_bcard_menu_share

    # 空间列表-浏览企业空间-菜单栏-企业名片-联系方式列表
    def Kjlb_browseorgspace_menu_bcard_contactlist(self):
        self.Kjlb_browseorgspace_menu_bcard_contactB = self.p.get_elements("id->com.yunlu6.stone:id/contact_icon","空间列表-浏览企业空间-菜单栏-企业名片-联系方式列表")
        return self.Kjlb_browseorgspace_menu_bcard_contactB

    # 空间列表-浏览企业空间-菜单栏-企业名片-资讯
    def Kjlb_browseorgspace_menu_bcard_archivies(self):
        self.Kjlb_browseorgspace_menu_bcard_archivies = self.p.get_element("id->com.yunlu6.stone:id/btn_archivie","空间列表-浏览企业空间-菜单栏-企业名片-资讯")
        return self.Kjlb_browseorgspace_menu_bcard_archivies

    # 空间列表-浏览企业空间-菜单栏-企业名片-点击创建产品
    def Kjlb_browseorgspace_menu_bcard_newpro(self):
        self.Kjlb_browseorgspace_menu_bcard_newpro = self.p.get_element("id->com.yunlu6.stone:id/iv_crad_build_prod","空间列表-浏览企业空间-菜单栏-企业名片-点击创建产品")
        return self.Kjlb_browseorgspace_menu_bcard_newpro

#***************************************【PAGE2】访客Kjlb_browseorgspace_menu_visitor***************************************
 # 空间列表-浏览企业空间-菜单栏-访客-访客列表
    def Kjlb_browseorgspace_menu_visitor_list(self):
        self.Kjlb_browseorgspace_menu_visitor_list = self.p.get_element("id->com.yunlu6.stone:id/visitor_name","空间列表-浏览企业空间-菜单栏-访客-访客列表")
        return self.Kjlb_browseorgspace_menu_visitor_list

    # 空间列表-浏览企业空间-菜单栏-访客-访客列表-返回
    def Kjlb_browseorgspace_menu_visitor_list_back(self):
        self.Kjlb_browseorgspace_menu_visitor_list_back = self.p.get_element("id->com.yunlu6.stone:id/iv_back","空间列表-浏览企业空间-菜单栏-访客-访客列表")
        return self.Kjlb_browseorgspace_menu_visitor_list_back

#***************************************【PAGE2】客户Kjlb_browseorgspace_menu_customer***************************************
    # 空间列表-浏览企业空间-菜单栏-客户-返回
    def Kjlb_browseorgspace_menu_customer_back(self):
        self.Kjlb_browseorgspace_menu_customer_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览企业空间-菜单栏-客户-返回")
        return self.Kjlb_browseorgspace_menu_customer_back

    # 空间列表-浏览企业空间-菜单栏-客户-搜索框
    def Kjlb_browseorgspace_menu_customer_search(self):
        self.Kjlb_browseorgspace_menu_customer_search = self.p.get_element("id->com.yunlu6.stone:id/et_search","空间列表-浏览企业空间-菜单栏-客户-搜索框")
        return self.Kjlb_browseorgspace_menu_customer_search

    # 空间列表-浏览企业空间-菜单栏-客户-搜索
    def Kjlb_browseorgspace_menu_customer_seek(self):
        self.Kjlb_browseorgspace_menu_customer_seek = self.p.get_element("id->com.yunlu6.stone:id/iv_search","空间列表-浏览企业空间-菜单栏-客户-搜索")
        return self.Kjlb_browseorgspace_menu_customer_seek

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏
    def Kjlb_browseorgspace_menu_customer_menu(self):
        self.Kjlb_browseorgspace_menu_customer_menu = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览企业空间-菜单栏-客户-菜单栏")
        return self.Kjlb_browseorgspace_menu_customer_menu

    # 空间列表-浏览企业空间-菜单栏-客户-客户列表
    def Kjlb_browseorgspace_menu_customer_list(self):
        self.Kjlb_browseorgspace_menu_customer_clist = self.p.get_elements("id->com.yunlu6.stone:id/rl_out","空间列表-浏览企业空间-菜单栏-客户-客户列表")
        return self.Kjlb_browseorgspace_menu_customer_clist

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏+客户
    def Kjlb_browseorgspace_menu_customer_menu_add(self):
        self.Kjlb_browseorgspace_menu_customer_menu_add = self.p.get_element("id->com.yunlu6.stone:id/btn_new_space","空间列表-浏览企业空间-菜单栏-客户-菜单栏+客户")
        return self.Kjlb_browseorgspace_menu_customer_menu_add

     # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作
    def Kjlb_browseorgspace_menu_customer_menu_batch(self):
        self.Kjlb_browseorgspace_menu_customer_menu_batch = self.p.get_elements("id->com.yunlu6.stone:id/btn_share_space","空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作")
        return self.Kjlb_browseorgspace_menu_customer_menu_batch

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-返回
    def Kjlb_browseorgspace_menu_customer_menu_batch_back(self):
        self.Kjlb_browseorgspace_menu_customer_menu_batch_back = self.p.get_elements("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-返回")
        return self.Kjlb_browseorgspace_menu_customer_menu_batch_back

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-全选
    def Kjlb_browseorgspace_menu_customer_menu_batch_all(self):
        self.Kjlb_browseorgspace_menu_customer_menu_batch_all = self.p.get_elements("id->com.yunlu6.stone:id/title_main_tv_more_tv","空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-全选")
        return self.Kjlb_browseorgspace_menu_customer_menu_batch_all

     # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-圆圈勾选
    def Kjlb_browseorgspace_menu_customer_menu_batch_choose(self):
        self.Kjlb_browseorgspace_menu_customer_menu_batch_choose = self.p.get_elements("id->com.yunlu6.stone:id/iv_select","空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-全选")
        return self.Kjlb_browseorgspace_menu_customer_menu_batch_choose

#***************************************【PAGE2】业务升级Kjlb_browseorgspace_menu_upgrade***************************************
     # 空间列表-浏览企业空间-菜单栏-业务升级-开启
    def Kjlb_browseorgspace_menu_upgrade_open(self):
        self.Kjlb_browseorgspace_menu_upgrade_open = self.p.get_elements("id->com.yunlu6.stone:id/upgrade_open","空间列表-浏览企业空间-菜单栏-业务升级-开启")
        return self.Kjlb_browseorgspace_menu_upgrade_open

    # 空间列表-浏览企业空间-菜单栏-业务升级-返回
    def Kjlb_browseorgspace_menu_upgrade_back(self):
        self.Kjlb_browseorgspace_menu_upgrade_back = self.p.get_element("id->com.yunlu6.stone:id/companyupgrade_backe","空间列表-浏览企业空间-菜单栏-业务升级-返回")
        return self.Kjlb_browseorgspace_menu_upgrade_back

#***************************************【PAGE2】照片列表(包括点击照片加数据)Kjlb_browseperspace_piclist***************************************
    # 空间列表-浏览私人空间-照片列表-菜单栏
    def Kjlb_browseperspace_piclist_menu(self):
        self.Kjlb_browseperspace_piclist_menuP = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览私人空间-照片列表-菜单栏")
        return self.Kjlb_browseperspace_piclist_menuP

    # 空间列表-浏览私人空间-照片列表-分类到
    def Kjlb_browseperspace_piclist_classify(self):
        self.Kjlb_browseperspace_piclist_classifyP = self.p.get_element("id->com.yunlu6.stone:id/btn_new_space","空间列表-浏览私人空间-照片列表-分类到")
        return self.Kjlb_browseperspace_piclist_classifyP

    # 空间列表-浏览私人空间-照片列表-编辑
    def Kjlb_browseperspace_piclist_edit(self):
        self.Kjlb_browseperspace_piclist_editP = self.p.get_element("id->com.yunlu6.stone:id/btn_share_space","空间列表-浏览私人空间-照片列表-编辑")
        return self.Kjlb_browseperspace_piclist_editP

    # 空间列表-浏览私人空间-照片列表-返回
    def Kjlb_browseperspace_piclist_back(self):
        self.Kjlb_browseperspace_piclist_backP = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览私人空间-照片列表-返回")
        return self.Kjlb_browseperspace_piclist_backP

    #空间列表-浏览私人空间-照片列表-照片本身
    def Kjlb_browseperspace_piclist_itself(self):
        self.Kjlb_browseperspace_piclist_itselfP = self.p.get_element("id->com.yunlu6.stone:id/image","空间列表-浏览私人空间-照片列表-照片本身")
        return self.Kjlb_browseperspace_piclist_itselfP

    # 空间列表-浏览私人空间-文件夹名称列表
    def Kjlb_browseperspace_foldername(self):
        self.Kjlb_browseperspace_foldernameP = self.p.get_elements("id->com.yunlu6.stone:id/personzone_item_foldername","空间列表-浏览私人空间-文件夹名称列表")
        return self.Kjlb_browseperspace_foldernameP

    # 空间列表-浏览私人空间-加数据-相册
    def Kjlb_browseperspace_addData_ByAlbum(self):
        self.Kjlb_browseperspace_addData_ByAlbumP = self.p.get_element("id->com.yunlu6.stone:id/iv_cloundlibrary_alumm","空间列表-浏览私人空间--加数据-相册")
        return self.Kjlb_browseperspace_addData_ByAlbumP

#***************************************【PAGE2】菜单栏-名片Kjlb_browseperspace_menu_card***************************************
    # 空间列表-浏览私人空间-菜单栏-名片-返回
    def Kjlb_browseperspace_menu_card_back(self):
        self.Kjlb_browseperspace_menu_card_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_edit_icon","空间列表-浏览私人空间-菜单栏-名片-返回")
        return self.Kjlb_browseperspace_menu_card_backP

    # 空间列表-浏览私人空间-菜单栏-名片-分享
    def Kjlb_browseperspace_menu_card_share(self):
        self.Kjlb_browseperspace_menu_card_shareP = self.p.get_element("id->com.yunlu6.stone:id/title_tv_edit_menu_tv","空间列表-浏览私人空间-菜单栏-名片-分享")
        return self.Kjlb_browseperspace_menu_card_shareP

    # 空间列表-浏览私人空间-菜单栏-名片-分享-微信
    def Kjlb_browseperspace_menu_card_share_wechat(self):
        self.Kjlb_browseperspace_menu_card_share_wechatP = self.p.get_element("id->com.yunlu6.stone:id/iv_cloundlibrary_alumm","空间列表-浏览私人空间-菜单栏-名片-分享-微信")
        return self.Kjlb_browseperspace_menu_card_share_wechatP

    # 空间列表-浏览私人空间-菜单栏-名片-分享-微信朋友圈
    def Kjlb_browseperspace_menu_card_share_circle(self):
        self.Kjlb_browseperspace_menu_card_share_circleP = self.p.get_element("id->com.yunlu6.stone:id/iv_cloundlibrary_cameras","空间列表-浏览私人空间-菜单栏-名片-分享-微信朋友圈")
        return self.Kjlb_browseperspace_menu_card_share_circleP

    # 空间列表-浏览私人空间-菜单栏-名片-分享-QQ空间
    def Kjlb_browseperspace_menu_card_share_qqzone(self):
        self.Kjlb_browseperspace_menu_card_share_qqzoneP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_wifi_sync","空间列表-浏览私人空间-菜单栏-名片-分享-QQ空间")
        return self.Kjlb_browseperspace_menu_card_share_qqzoneP

    # 空间列表-浏览私人空间-菜单栏-名片-分享-QQ
    def Kjlb_browseperspace_menu_card_share_qq(self):
        self.Kjlb_browseperspace_menu_card_share_qqP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_qq","空间列表-浏览私人空间-菜单栏-名片-分享-QQ")
        return self.Kjlb_browseperspace_menu_card_share_qqP

    # 空间列表-浏览私人空间-菜单栏-名片-分享-新浪微博
    def Kjlb_browseperspace_menu_card_share_sina(self):
        self.Kjlb_browseperspace_menu_card_share_sinaP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_weibo","空间列表-浏览私人空间-菜单栏-名片-分享-微博")
        return self.Kjlb_browseperspace_menu_card_share_sinaP

    # 空间列表-浏览私人空间-菜单栏-名片-分享-取消
    def Kjlb_browseperspace_menu_card_share_cancel(self):
        self.Kjlb_browseperspace_menu_card_share_cancelP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_cancel","空间列表-浏览私人空间-菜单栏-名片-分享-取消")
        return self.Kjlb_browseperspace_menu_card_share_cancelP

    # 空间列表-浏览私人空间-菜单栏-名片-手机
    def Kjlb_browseperspace_menu_card_phone(self):
        self.Kjlb_browseperspace_menu_card_phoneP = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_phone_cb","空间列表-浏览私人空间-菜单栏-名片-手机")
        return self.Kjlb_browseperspace_menu_card_phoneP

    # 空间列表-浏览私人空间-菜单栏-名片-邮箱
    def Kjlb_browseperspace_menu_card_email(self):
        self.Kjlb_browseperspace_menu_card_emailP = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_email_cb","空间列表-浏览私人空间-菜单栏-名片-邮箱")
        return self.Kjlb_browseperspace_menu_card_emailP

    # 空间列表-浏览私人空间-菜单栏-名片-地址
    def Kjlb_browseperspace_menu_card_address(self):
        self.Kjlb_browseperspace_menu_card_addressP = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_address_cb","空间列表-浏览私人空间-菜单栏-名片-地址")
        return self.Kjlb_browseperspace_menu_card_addressP

    # 空间列表-浏览私人空间-菜单栏-名片-QQ
    def Kjlb_browseperspace_menu_card_QQ(self):
        self.Kjlb_browseperspace_menu_card_QQP = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_qq_cb","空间列表-浏览私人空间-菜单栏-名片-QQ")
        return self.Kjlb_browseperspace_menu_card_QQP

    # 空间列表-浏览私人空间-菜单栏-名片-有效期
    def Kjlb_browseperspace_menu_card_limit(self):
        self.Kjlb_browseperspace_menu_card_limitP = self.p.get_element("id->com.yunlu6.stone:id/user_card_team_userlife_tv","空间列表-浏览私人空间-菜单栏-名片-有效期")
        return self.Kjlb_browseperspace_menu_card_limitP

    # 空间列表-浏览私人空间-菜单栏-编辑-删除文件夹列表
    def Kjlb_browseperspace_menu_edit_deletefolder(self):
        self.Kjlb_browseperspace_menu_edit_deletefolderP = self.p.get_elements("id->com.yunlu6.stone:id/editlayout_folder_dele","空间列表-浏览私人空间-菜单栏-编辑-删除文件夹名称")
        return self.Kjlb_browseperspace_menu_edit_deletefolderP

     # 空间列表-浏览私人空间-菜单栏-编辑-修改文件夹图标
    def Kjlb_browseperspace_menu_edit_editfolder(self):
        self.Kjlb_browseperspace_menu_edit_editfolderP = self.p.get_elements("id->com.yunlu6.stone:id/editlayout_folder_edite","空间列表-浏览私人空间-菜单栏-编辑-修改文件夹名称")
        return self.Kjlb_browseperspace_menu_edit_editfolderP

    # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称
    def Kjlb_browseperspace_menu_edit_editfolder_fname(self):
        self.Kjlb_browseperspace_menu_edit_editfolder_fnameP = self.p.get_element("id->com.yunlu6.stone:id/edit_folder_name","空间列表-浏览私人空间-菜单栏-编辑-修改文件夹名称-名称列表")
        return self.Kjlb_browseperspace_menu_edit_editfolder_fnameP

     # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-是
    def Kjlb_browseperspace_menu_edit_editfolder_fname_OK(self):
        self.Kjlb_browseperspace_menu_edit_spacename_spaceEditOKP = self.p.get_element("id->com.yunlu6.stone:id/edit_folder_ok","空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-是")
        return self.Kjlb_browseperspace_menu_edit_spacename_spaceEditOKP

    # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-否
    def Kjlb_browseperspace_menu_edit_editfolder_fname_NO(self):
        self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NOP = self.p.get_element("id->com.yunlu6.stone:id/edit_folder_no","空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-否")
        return self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NOP

    # 空间列表-浏览私人空间-菜单栏-编辑-+数据
    def Kjlb_browseperspace_menu_edit_adddata(self):
        self.Kjlb_browseperspace_menu_edit_adddataP = self.p.get_elements("name->＋ 数据","空间列表-浏览私人空间-菜单栏-编辑-+数据")
        return self.Kjlb_browseperspace_menu_edit_adddataP

     # 空间列表-浏览私人空间-菜单栏-编辑-空间类型
    def Kjlb_browseperspace_menu_edit_spacetype(self):
        self.Kjlb_browseperspace_menu_edit_spacetypeP = self.p.get_element("id->com.yunlu6.stone:id/create_img_type","空间列表-浏览私人空间-菜单栏-编辑-空间类型")
        return self.Kjlb_browseperspace_menu_edit_spacetypeP

    # 空间列表-浏览私人空间-菜单栏-编辑-删除空间
    def Kjlb_browseperspace_menu_edit_deletespace(self):
        self.Kjlb_browseperspace_menu_edit_deletespaceP = self.p.get_element("id->com.yunlu6.stone:id/space_dele_icon","空间列表-浏览私人空间-菜单栏-编辑-删除空间")
        return self.Kjlb_browseperspace_menu_edit_deletespaceP

    # 空间列表-浏览私人空间-菜单栏-编辑-删除空间-是
    def Kjlb_browseperspace_menu_edit_deletespace_OK(self):
        self.Kjlb_browseperspace_menu_edit_deletespace_OKP = self.p.get_element("id->com.yunlu6.stone:id/edit_folder_ok","空间列表-浏览私人空间-菜单栏-编辑-删除空间-是")
        return self.Kjlb_browseperspace_menu_edit_deletespace_OKP

     # 空间列表-浏览私人空间-菜单栏-编辑-删除空间-否
    def Kjlb_browseperspace_menu_edit_deletespace_NO(self):
        self.Kjlb_browseperspace_menu_edit_deletespace_NOP = self.p.get_element("id->com.yunlu6.stone:id/edit_folder_no","空间列表-浏览私人空间-菜单栏-编辑-删除空间-否")
        return self.Kjlb_browseperspace_menu_edit_deletespaceP


     # 空间列表-浏览私人空间-菜单栏-编辑-返回
    def Kjlb_browseperspace_menu_edit_back(self):
        self.Kjlb_browseperspace_menu_edit_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览私人空间-菜单栏-编辑-返回")
        return self.Kjlb_browseperspace_menu_edit_backP

     # 空间列表-浏览私人空间-菜单栏-编辑-空间名
    def Kjlb_browseperspace_menu_edit_spacename(self):
        self.Kjlb_browseperspace_menu_edit_spacenameP = self.p.get_element("id->com.yunlu6.stone:id/space_name_edit","空间列表-浏览私人空间-菜单栏-编辑-空间名")
        return self.Kjlb_browseperspace_menu_edit_spacenameP

     # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称列表(0)
    def Kjlb_browseperspace_menu_edit_spacename_spaceEdit(self):
        self.Kjlb_browseperspace_menu_edit_spacename_spaceEditP = self.p.get_elements("id->com.yunlu6.stone:id/edit_folder_name","空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称")
        return self.Kjlb_browseperspace_menu_edit_spacename_spaceEditP

    # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-是
    def Kjlb_browseperspace_menu_edit_spacename_spaceEdit_OK(self):
        self.Kjlb_browseperspace_menu_edit_spacename_spaceEditOKP = self.p.get_element("id->com.yunlu6.stone:id/edit_folder_ok","空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-是")
        return self.Kjlb_browseperspace_menu_edit_spacename_spaceEditOKP

     # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-否
    def Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NO(self):
        self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NOP = self.p.get_element("id->com.yunlu6.stone:id/edit_folder_no","空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-否")
        return self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NOP

#***************************************【PAGE2】菜单栏-客户Kjlb_browseperspace_menu_customer***************************************
    # 空间列表-浏览私人空间-菜单栏-客户-返回
    def Kjlb_browseperspace_menu_customer_back(self):
        self.Kjlb_browseperspace_menu_customer_backP = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览私人空间-菜单栏-客户-返回")
        return self.Kjlb_browseperspace_menu_customer_backP

    # 空间列表-浏览私人空间-菜单栏-客户-搜索栏
    def Kjlb_browseperspace_menu_customer_search(self):
        self.Kjlb_browseperspace_menu_customer_searchP = self.p.get_element("id->com.yunlu6.stone:id/et_search","空间列表-浏览私人空间-菜单栏-客户-搜索栏")
        return self.Kjlb_browseperspace_menu_customer_searchP

    # 空间列表-浏览私人空间-菜单栏-客户-搜索按钮
    def Kjlb_browseperspace_menu_customer_searchbtn(self):
        self.Kjlb_browseperspace_menu_customer_searchbtnP = self.p.get_element("id->com.yunlu6.stone:id/iv_search","空间列表-浏览私人空间-菜单栏-客户-搜索栏")
        return self.Kjlb_browseperspace_menu_customer_searchbtnP

    # 空间列表-浏览私人空间-菜单栏-客户-菜单
    def Kjlb_browseperspace_menu_customer_menu(self):
        self.Kjlb_browseperspace_menu_customer_menuP = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览私人空间-菜单栏-客户-菜单")
        return self.Kjlb_browseperspace_menu_customer_menuP

    # 空间列表-浏览私人空间-菜单栏-客户-菜单-+客户
    def Kjlb_browseperspace_menu_customer_menu_addcus(self):
        self.Kjlb_browseperspace_menu_customer_menu_addcusP = self.p.get_element("id->com.yunlu6.stone:id/btn_new_space","空间列表-浏览私人空间-菜单栏-客户-菜单-+客户")
        return self.Kjlb_browseperspace_menu_customer_menu_addcusP

    # 空间列表-浏览私人空间-菜单栏-客户-客户列表
    def Kjlb_browseperspace_menu_customer_clist(self):
        self.Kjlb_browseperspace_menu_customer_clistP = self.p.get_elements("id->com.yunlu6.stone:id/rl_out","空间列表-浏览私人空间-菜单栏-客户-客户列表")
        return self.Kjlb_browseperspace_menu_customer_clistP

    # 空间列表-浏览私人空间-菜单栏-客户-群聊
    def Kjlb_browseperspace_menu_customer_gchat(self):
        self.Kjlb_browseperspace_menu_customer_gchatP = self.p.get_element("id->com.yunlu6.stone:id/rl_bottom","空间列表-浏览私人空间-菜单栏-客户-群聊")
        return self.Kjlb_browseperspace_menu_customer_gchatP

    # 空间列表-浏览私人空间-菜单栏-+文件夹-文件夹名称-确定
    def Kjlb_browseperspace_menu_addfolder_confirm(self):
        self.Kjlb_browseperspace_menu_addfolder_confirmP = self.p.get_element("id->com.yunlu6.stone:id/zone_add_commit","空间列表-浏览私人空间-菜单栏-+文件夹-确定")
        return self.Kjlb_browseperspace_menu_addfolder_confirmP

     # 空间列表-浏览私人空间-菜单栏-+文件夹-文件夹名称
    def Kjlb_browseperspace_menu_addfolder_foldername(self):
        self.Kjlb_browseperspace_menu_addfolder_foldernameP = self.p.get_element("id->com.yunlu6.stone:id/zone_add_gallery_et","空间列表-浏览私人空间-菜单栏-+文件夹-文件夹名称")
        return self.Kjlb_browseperspace_menu_addfolder_foldernameP

    # 空间列表-浏览私人空间-菜单栏-+文件夹-返回
    def Kjlb_browseperspace_menu_addfolder_back(self):
        self.Kjlb_browseperspace_menu_addfolder_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览私人空间-菜单栏-+文件夹-返回")
        return self.Kjlb_browseperspace_menu_addfolder_backP

#***************************************【PAGE2】+数据Kjlb_browseperspace_adata***************************************
    # 空间列表-浏览私人空间-加数据-相册
    def Kjlb_browseperspace_adata_ByAlbum(self):
        self.Kjlb_browseperspace_adata_ByAlbumP = self.p.get_element("id->com.yunlu6.stone:id/iv_cloundlibrary_alumm","空间列表-浏览私人空间-加数据-相册")
        return self.Kjlb_browseperspace_adata_ByAlbumP

    # 空间列表-浏览私人空间-加数据-拍照
    def Kjlb_browseperspace_adata_ByTakepic(self):
        self.Kjlb_browseperspace_adata_ByTakepicP = self.p.get_element("id->com.yunlu6.stone:id/iv_cloundlibrary_camera","空间列表-浏览私人空间-加数据-拍照")
        return self.Kjlb_browseperspace_adata_ByTakepicP

    # 空间列表-浏览私人空间-加数据-取消
    def Kjlb_browseperspace_adata_cancel(self):
        self.Kjlb_browseperspace_adata_cancelP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_cancel","空间列表-浏览私人空间-加数据-取消")
        return self.Kjlb_browseperspace_adata_cancelP

#***************************************【PAGE2】更多Kjlb_browseperspace_more***************************************
     # 空间列表-浏览私人空间-更多-照片列表
    def Kjlb_browseperspace_more_piclist(self):
        self.Kjlb_browseperspace_more_piclistP = self.p.get_elements("id->com.yunlu6.stone:id/presonzone_gridview_iv","空间列表-浏览私人空间-更多-照片列表")
        return self.Kjlb_browseperspace_more_piclistP

    # 空间列表-浏览私人空间-更多-返回
    def Kjlb_browseperspace_more_back(self):
        self.Kjlb_browseperspace_more_backP = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览私人空间-更多-照片列表-照片本身")
        return self.Kjlb_browseperspace_more_backP

    # 空间列表-浏览私人空间-更多-菜单栏
    def Kjlb_browseperspace_more_menu(self):
        self.Kjlb_browseperspace_more_menuP = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览私人空间-更多-菜单栏")
        return self.Kjlb_browseperspace_more_menuP

    # 空间列表-浏览私人空间-更多-菜单栏-上传
    def Kjlb_browseperspace_more_menu_upload(self):
        self.Kjlb_browseperspace_more_menu_uploadP = self.p.get_element("id->com.yunlu6.stone:id/pop_gallery_photoes_btn_uploade","空间列表-浏览私人空间-更多-菜单栏-上传")
        return self.Kjlb_browseperspace_more_menu_uploadP

    # 空间列表-浏览私人空间-更多-菜单栏-上传-相册
    def Kjlb_browseperspace_more_menu_upload_ByAlbum(self):
        self.Kjlb_browseperspace_more_menu_upload_ByAlbumP = self.p.get_element("id->com.yunlu6.stone:id/iv_cloundlibrary_alumm","空间列表-浏览私人空间-更多-菜单栏-上传-相册")
        return self.Kjlb_browseperspace_more_menu_upload_ByAlbumP

    # 空间列表-浏览私人空间-更多-菜单栏-上传-拍照
    def Kjlb_browseperspace_more_menu_upload_ByTakepic(self):
        self.Kjlb_browseperspace_more_menu_upload_ByTakepicP = self.p.get_element("id->com.yunlu6.stone:id/iv_cloundlibrary_cameras","空间列表-浏览私人空间-更多-菜单栏-上传-拍照")
        return self.Kjlb_browseperspace_more_menu_upload_ByTakepicP

    # 空间列表-浏览私人空间-更多-菜单栏-上传-取消
    def Kjlb_browseperspace_more_menu_upload_cancel(self):
        self.Kjlb_browseperspace_more_menu_upload_cancelP = self.p.get_element("id->com.yunlu6.stone:id/pop_cloundlibrary_tv_cancel","空间列表-浏览私人空间-更多-菜单栏-上传-取消")
        return self.Kjlb_browseperspace_more_menu_upload_cancelP

     # 空间列表-浏览私人空间-更多-菜单栏-编辑
    def Kjlb_browseperspace_more_menu_edit(self):
        self.Kjlb_browseperspace_more_menu_editP = self.p.get_element("id->com.yunlu6.stone:id/pop_gallery_photoes_btn_edit","空间列表-浏览私人空间-更多-菜单栏-编辑")
        return self.Kjlb_browseperspace_more_menu_editP

    # 空间列表-浏览私人空间-更多-菜单栏-排序
    def Kjlb_browseperspace_more_menu_sort(self):
        self.Kjlb_browseperspace_more_menu_sortP = self.p.get_element("id->com.yunlu6.stone:id/pop_gallery_photoes_btn_sort","空间列表-浏览私人空间-更多-菜单栏-排序")
        return self.Kjlb_browseperspace_more_menu_sortP

#***************************************【PAGE2】企业会员Kjlb_browseascspace_ovip***************************************
    # 空间列表-协会空间-企业会员-返回
    def Kjlb_browseascspace_ovip_back(self):
        self.Kjlb_browseascspace_ovip_backA = self.p.get_element("id->com.yunlu6.stone:id/title_main_more_back","空间列表-协会空间-企业会员-返回")
        return self.Kjlb_browseascspace_ovip_backA

    # 空间列表-协会空间-企业会员-搜索栏
    def Kjlb_browseascspace_ovip_search(self):
        self.Kjlb_browseascspace_ovip_searchA = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_keyword","空间列表-协会空间-企业会员-搜索栏")
        return self.Kjlb_browseascspace_ovip_searchA

    # 空间列表-协会空间-企业会员-搜索按钮
    def Kjlb_browseascspace_ovip_searchbtn(self):
        self.Kjlb_browseascspace_ovip_searchbtnA = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_search","空间列表-协会空间-企业会员-搜索按钮")
        return self.Kjlb_browseascspace_ovip_searchbtnA

    # 空间列表-协会空间-企业会员-企业列表
    def Kjlb_browseascspace_ovip_olist(self):
        self.Kjlb_browseascspace_ovip_olistA = self.p.get_elements("id->com.yunlu6.stone:id/ass_company_name","空间列表-协会空间-企业会员-企业列表")
        return self.Kjlb_browseascspace_ovip_olistA

#***************************************【PAGE2】个人会员Kjlb_browseascspace_ovip***************************************
     # 空间列表-协会空间-个人会员-返回
    def Kjlb_browseascspace_pvip_back(self):
        self.Kjlb_browseascspace_pvip_backA = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-协会空间-个人会员-返回")
        return self.Kjlb_browseascspace_pvip_backA

    # 空间列表-协会空间-个人会员-搜索栏
    def Kjlb_browseascspace_pvip_search(self):
        self.Kjlb_browseascspace_pvip_searchA = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_keyword","空间列表-协会空间-个人会员-搜索栏")
        return self.Kjlb_browseascspace_pvip_searchA

    # 空间列表-协会空间-个人会员-搜索按钮
    def Kjlb_browseascspace_pvip_searchbtn(self):
        self.Kjlb_browseascspace_pvip_searchbtnA = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_search","空间列表-协会空间-个人会员-搜索按钮")
        return self.Kjlb_browseascspace_pvip_searchbtnA

    # 空间列表-协会空间-个人会员-人脉列表
    def Kjlb_browseascspace_pvip_plist(self):
        self.Kjlb_browseascspace_pvip_olistA = self.p.get_elements("id->com.yunlu6.stone:id/vip_name","空间列表-协会空间-个人会员-人脉列表")
        return self.Kjlb_browseascspace_pvip_olistA

#***************************************【PAGE2】资讯Kjlb_browseascspace_arch***************************************
    # 空间列表-协会空间-资讯-返回
    def Kjlb_browseascspace_arch_back(self):
        self.Kjlb_browseascspace_arch_backA = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-协会空间-资讯-返回")
        return self.Kjlb_browseascspace_arch_backA

    # 空间列表-协会空间-资讯-资讯文件列表
    def Kjlb_browseascspace_arch_alist(self):
        self.Kjlb_browseascspace_arch_alistA = self.p.get_element("id->com.yunlu6.stone:id/iv_profile","空间列表-协会空间-资讯-资讯文件列表")
        return self.Kjlb_browseascspace_arch_alistA

#***************************************【PAGE2】协会资信信息Kjlb_browseascspace_credit***************************************
    # 空间列表-协会空间-资信-返回
    def Kjlb_browseascspace_credit_back(self):
        self.Kjlb_browseascspace_credit_backA = self.p.get_element("id->com.yunlu6.stone:id/title_back_icone","空间列表-协会空间-资信-返回")
        return self.Kjlb_browseascspace_credit_backA

#***************************************【PAGE2】菜单栏-编辑Kjlb_browseascspace_menu_edit***************************************
     # 空间列表-浏览协会空间-菜单栏-编辑-返回
    def Kjlb_browseascspace_menu_edit_back(self):
        self.Kjlb_browseascspace_menu_edit_backA = self.p.get_elements("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览协会空间-菜单栏-编辑-返回")
        return self.Kjlb_browseascspace_menu_edit_backA

     # 空间列表-浏览协会空间-菜单栏-编辑-Logo
    def Kjlb_browseascspace_menu_edit_logo(self):
        self.Kjlb_browseascspace_menu_edit_logoA = self.p.get_element("id->com.yunlu6.stone:id/iv_open_logo","空间列表-浏览协会空间-菜单栏-编辑-Logo")
        return self.Kjlb_browseascspace_menu_edit_logoA

    # 空间列表-浏览协会空间-菜单栏-编辑-企业全称
    def Kjlb_browseascspace_menu_edit_fullname(self):
        self.Kjlb_browseascspace_menu_edit_fullnameA = self.p.get_element("id->com.yunlu6.stone:id/company_name","空间列表-浏览协会空间-菜单栏-编辑-企业全称")
        return self.Kjlb_browseascspace_menu_edit_fullnameA

     # 空间列表-浏览协会空间-菜单栏-编辑-企业简称
    def Kjlb_browseascspace_menu_edit_simplename(self):
        self.Kjlb_browseascspace_menu_edit_simplenameA = self.p.get_element("id->com.yunlu6.stone:id/company_introduce","空间列表-浏览协会空间-菜单栏-编辑-企业简称")
        return self.Kjlb_browseascspace_menu_edit_simplenameA

    # 空间列表-浏览协会空间-菜单栏-编辑-所在地区
    def Kjlb_browseascspace_menu_edit_address(self):
        self.Kjlb_browseascspace_menu_edit_addressA = self.p.get_element("id->com.yunlu6.stone:id/company_address","空间列表-浏览协会空间-菜单栏-编辑-所在地区")
        return self.Kjlb_browseascspace_menu_edit_addressA

    # 空间列表-浏览协会空间-菜单栏-编辑-所在地区-所在地区列表
    def Kjlb_browseascspace_menu_edit_address_list(self):
        self.Kjlb_browseascspace_menu_edit_address_listA = self.p.get_elements("id->com.yunlu6.stone:id/tv_address" ,"空间列表-浏览协会空间-菜单栏-编辑-所在地区")
        return self.Kjlb_browseascspace_menu_edit_address_listA

    # 空间列表-浏览协会空间-菜单栏-编辑-详细地址
    def Kjlb_browseascspace_menu_edit_detailaddress(self):
        self.Kjlb_browseascspace_menu_edit_detailaddressA = self.p.get_element("id->com.yunlu6.stone:id/company_address_det","空间列表-浏览协会空间-菜单栏-编辑-详细地址")
        return self.Kjlb_browseascspace_menu_edit_detailaddressA

    # 空间列表-浏览协会空间-菜单栏-编辑-联系人
    def Kjlb_browseascspace_menu_edit_contact(self):
        self.Kjlb_browseascspace_menu_edit_contactA = self.p.get_element("id->com.yunlu6.stone:id/people_name","空间列表-浏览协会空间-菜单栏-编辑-联系人")
        return self.Kjlb_browseascspace_menu_edit_contactA

    # 空间列表-浏览协会空间-菜单栏-编辑-手机号
    def Kjlb_browseascspace_menu_edit_phone(self):
        self.Kjlb_browseascspace_menu_edit_phoneA = self.p.get_element("id->com.yunlu6.stone:id/mobile_phone","空间列表-浏览协会空间-菜单栏-编辑-手机号")
        return self.Kjlb_browseascspace_menu_edit_phoneA

    # 空间列表-浏览协会空间-菜单栏-编辑-座机号
    def Kjlb_browseascspace_menu_edit_landline(self):
        self.Kjlb_browseascspace_menu_edit_landlineA = self.p.get_element("id->com.yunlu6.stone:id/phone","空间列表-浏览协会空间-菜单栏-编辑-座机号")
        return self.Kjlb_browseascspace_menu_edit_landlineA

    # 空间列表-浏览协会空间-菜单栏-编辑-邮箱
    def Kjlb_browseascspace_menu_edit_email(self):
        self.Kjlb_browseascspace_menu_edit_emailA = self.p.get_element("id->com.yunlu6.stone:id/email","空间列表-浏览协会空间-菜单栏-编辑-邮箱")
        return self.Kjlb_browseascspace_menu_edit_emailA

    # 空间列表-浏览协会空间-菜单栏-编辑-QQ
    def Kjlb_browseascspace_menu_edit_QQ(self):
        self.Kjlb_browseascspace_menu_edit_QQA = self.p.get_element("id->com.yunlu6.stone:id/qq","空间列表-浏览协会空间-菜单栏-编辑-QQ")
        return self.Kjlb_browseascspace_menu_edit_QQA

    # 空间列表-浏览协会空间-菜单栏-编辑-网站
    def Kjlb_browseascspace_menu_edit_website(self):
        self.Kjlb_browseascspace_menu_edit_websiteA = self.p.get_element("id->com.yunlu6.stone:id/website","空间列表-浏览协会空间-菜单栏-编辑-网站")
        return self.Kjlb_browseascspace_menu_edit_websiteA

    # 空间列表-浏览协会空间-菜单栏-编辑-勾选
    def Kjlb_browseascspace_menu_edit_confirm(self):
        self.Kjlb_browseascspace_menu_edit_confirmA = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览协会空间-菜单栏-编辑-勾选")
        return self.Kjlb_browseascspace_menu_edit_confirmA

#***************************************【PAGE2】菜单栏-团队Kjlb_browseascspace_menu_team***************************************
    # 空间列表-浏览协会空间-菜单栏-团队-返回
    def Kjlb_browseascspace_menu_team_back(self):
        self.Kjlb_browseascspace_menu_team_backA = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-团队-返回")
        return self.Kjlb_browseascspace_menu_team_backA

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏
    def Kjlb_browseascspace_menu_team_menu(self):
        self.Kjlb_browseascspace_menu_team_menuA = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览协会空间-菜单栏-团队-菜单栏")
        return self.Kjlb_browseascspace_menu_team_menuA

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免
    def Kjlb_browseascspace_menu_team_menu_assignjob(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjobA = self.p.get_element("id->com.yunlu6.stone:id/pop_teamedit_personnel","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免")
        return self.Kjlb_browseascspace_menu_team_menu_assignjobA

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门
    def Kjlb_browseascspace_menu_team_menu_mydepartment(self):
        self.Kjlb_browseascspace_menu_team_menu_mydepartmentA = self.p.get_element("id->com.yunlu6.stone:id/pop_teamedit_personnel","空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门")
        return self.Kjlb_browseascspace_menu_team_menu_mydepartmentA

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑
    def Kjlb_browseascspace_menu_team_teamedit(self):
        self.Kjlb_browseascspace_menu_team_teameditA = self.p.get_element("id->com.yunlu6.stone:id/companyteam_btn_edit","空间列表-浏览协会空间-菜单栏-团队-团队编辑")
        return self.Kjlb_browseascspace_menu_team_teameditA

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮
    def Kjlb_browseascspace_menu_team_teamedit_numeidt(self):
        self.Kjlb_browseascspace_menu_team_teamedit_numeidtA = self.p.get_element("id->com.yunlu6.stone:id/companyteam_item_edit","空间列表-浏览协会空间-菜单栏-团队-团队编辑-编辑人数按钮")
        return self.Kjlb_browseascspace_menu_team_teamedit_numeidtA

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-职位人数
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit(self):
        self.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumeditA = self.p.get_element("id->com.yunlu6.stone:id/teamedit_jobs_editnum","空间列表-浏览协会空间-菜单栏-团队-团队编辑-编辑人数按钮-职位人数按钮")
        return self.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumeditA

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-否
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel(self):
        self.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancelA = self.p.get_element("id->com.yunlu6.stone:id/teamedit_cancleedit","空间列表-浏览协会空间-菜单栏-团队-团队编辑-编辑人数按钮-职位人数按钮-否")
        return self.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancelA

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-是
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm(self):
        self.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirmA = self.p.get_element("id->com.yunlu6.stone:id/teamedit_commitedit","空间列表-浏览协会空间-菜单栏-团队-团队编辑-编辑人数-职位人数按钮-是")
        return self.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirmA

# ***************************************【PAGE2】菜单栏-会员Kjlb_browseascspace_menu_vip***************************************
     # 空间列表-浏览协会空间-菜单栏-会员-企业名录
    def Kjlb_browseascspace_menu_vip_companylist(self):
        self.Kjlb_browseascspace_menu_vip_companylistA = self.p.get_element("id->com.yunlu6.stone:id/ass_select_companylist","空间列表-浏览协会空间-菜单栏-会员-企业名录")
        return self.Kjlb_browseascspace_menu_vip_companylistA

    # 空间列表-浏览协会空间-菜单栏-会员-企业名录-企业名列表
    def Kjlb_browseascspace_menu_vip_companylist_companyname(self):
        self.Kjlb_browseascspace_menu_vip_companylist_companynameA = self.p.get_elements("id->com.yunlu6.stone:id/ass_company_name","空间列表-浏览协会空间-菜单栏-会员-企业名录-企业名列表")
        return self.Kjlb_browseascspace_menu_vip_companylist_companynameA

    # 空间列表-浏览协会空间-菜单栏-会员-搜索按钮
    def Kjlb_browseascspace_menu_vip_searchbtn(self):
        self.Kjlb_browseascspace_menu_vip_searchbtnA = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_search","空间列表-浏览协会空间-菜单栏-会员-搜索按钮")
        return self.Kjlb_browseascspace_menu_vip_searchbtnA

     # 空间列表-浏览协会空间-菜单栏-会员-个人名录
    def Kjlb_browseascspace_menu_vip_personlist(self):
        self.Kjlb_browseascspace_menu_vip_personlistA = self.p.get_element("id->com.yunlu6.stone:id/ass_select_personlist","空间列表-浏览协会空间-菜单栏-会员-个人名录")
        return self.Kjlb_browseascspace_menu_vip_personlistA

    # 空间列表-浏览协会空间-菜单栏-会员-个人名录-个人名列表
    def Kjlb_browseascspace_menu_vip_personlist_personname(self):
        self.Kjlb_browseascspace_menu_vip_personlist_personnameA = self.p.get_elements("id->com.yunlu6.stone:id/vip_name","空间列表-浏览协会空间-菜单栏-会员-个人名录-个人名列表")
        return self.Kjlb_browseascspace_menu_vip_personlist_personnameA

     # 空间列表-浏览协会空间-菜单栏-会员-搜索栏
    def Kjlb_browseascspace_menu_vip_search(self):
        self.Kjlb_browseascspace_menu_vip_searchA = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_keyword","空间列表-浏览协会空间-菜单栏-会员-搜索栏")
        return self.Kjlb_browseascspace_menu_vip_searchA

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏
    def Kjlb_browseascspace_menu_vip_menu(self):
        self.Kjlb_browseascspace_menu_vip_menuA = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_menu","空间列表-浏览协会空间-菜单栏-会员-菜单栏")
        return self.Kjlb_browseascspace_menu_vip_menuA

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员
    def Kjlb_browseascspace_menu_vip_menu_addvip(self):
        self.Kjlb_browseascspace_menu_vip_menu_addvipA = self.p.get_element("id->com.yunlu6.stone:id/btn_add_vip","空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员")
        return self.Kjlb_browseascspace_menu_vip_menu_addvipA

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理
    def Kjlb_browseascspace_menu_vip_menu_manage(self):
        self.Kjlb_browseascspace_menu_vip_menu_manageA = self.p.get_element("id->com.yunlu6.stone:id/btn_add_manage","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理")
        return self.Kjlb_browseascspace_menu_vip_menu_manageA

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-返回
    def Kjlb_browseascspace_menu_vip_menu_manage_back(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_backA = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-返回")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_backA

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索栏
    def Kjlb_browseascspace_menu_vip_menu_manage_search(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_searcA = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_keyword","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索栏")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_searcA

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索按钮
    def Kjlb_browseascspace_menu_vip_menu_manage_searchbtn(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_searchbtnA = self.p.get_element("id->com.yunlu6.stone:id/companyclient_search_search","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索按钮")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_searchbtnA

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑
    def Kjlb_browseascspace_menu_vip_menu_manage_edit(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_editA = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_tv","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_editA

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业
    def Kjlb_browseascspace_menu_vip_menu_manage_companyname(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_companynameA = self.p.get_elements("id->com.yunlu6.stone:id/ass_company_name","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_companynameA

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业-返回
    def Kjlb_browseascspace_menu_vip_menu_manage_companyname_back(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_companyname_backA = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业-返回")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_companyname_backA

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人
    def Kjlb_browseascspace_menu_vip_menu_manage_personname(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_personnameA = self.p.get_elements("id->com.yunlu6.stone:id/vip_name","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_personnameA

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人-返回
    def Kjlb_browseascspace_menu_vip_menu_manage_personname_back(self):
        self.Kjlb_browseascspace_menu_vip_menu_manage_personname_backA = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人-返回")
        return self.Kjlb_browseascspace_menu_vip_menu_manage_personname_backA

     # 空间列表-浏览协会空间-菜单栏-会员-返回
    def Kjlb_browseascspace_menu_vip_back(self):
        self.Kjlb_browseascspace_menu_vip_backA = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-返回")
        return self.Kjlb_browseascspace_menu_vip_backA

# ***************************************【PAGE2】菜单栏-+会员-个人会员Kjlb_browseascspace_menu_addvip_addperson***************************************
     #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-添加
    def Kjlb_browseascspace_menu_addvip_addperson_confirm(self):
        self.Kjlb_browseascspace_menu_addvip_addperson_confirmA = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_client_operate","空间列表-浏览协会空间-菜单栏-会员-个人会员-添加失败")
        return self.Kjlb_browseascspace_menu_addvip_addperson_confirmA

    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-圆圈勾选列表
    def Kjlb_browseascspace_menu_addvip_addperson_choose(self):
        self.Kjlb_browseascspace_menu_addvip_addperson_chooseA = self.p.get_elements("id->com.yunlu6.stone:id/item_client_tv_checked","空间列表-浏览协会空间-菜单栏-会员-个人会员-圆圈勾选失败")
        return self.Kjlb_browseascspace_menu_addvip_addperson_chooseA

     #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-全选
    def Kjlb_browseascspace_menu_addvip_addperson_all(self):
        self.Kjlb_browseascspace_menu_addvip_addperson_allA = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_tv","空间列表-浏览协会空间-菜单栏-会员-个人会员-全选失败")
        return self.Kjlb_browseascspace_menu_addvip_addperson_allA

    #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-搜索按钮
    def Kjlb_browseascspace_menu_addvip_addperson_searchbtn(self):
        self.Kjlb_browseascspace_menu_addvip_addperson_searchbtnA = self.p.get_element("id->com.yunlu6.stone:id/iv_search","空间列表-浏览协会空间-菜单栏-会员-个人会员-搜索按钮失败")
        return self.Kjlb_browseascspace_menu_addvip_addperson_searchbtnA

     #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-搜索栏
    def Kjlb_browseascspace_menu_addvip_addperson_search(self):
        self.Kjlb_browseascspace_menu_addvip_addperson_searchA = self.p.get_element("id->com.yunlu6.stone:id/et_search","空间列表-浏览协会空间-菜单栏-会员-个人会员-搜索栏失败")
        return self.Kjlb_browseascspace_menu_addvip_addperson_searchA

     #定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-返回
    def Kjlb_browseascspace_menu_addvip_addperson_back(self):
        self.Kjlb_browseascspace_menu_addvip_addperson_backA = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-个人会员-返回失败")
        return self.Kjlb_browseascspace_menu_addvip_addperson_backA

# ***************************************【PAGE2】菜单栏-+会员-企业会员Kjlb_browseascspace_menu_addvip_addcompany***************************************
     #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-返回
    def Kjlb_browseascspace_menu_addvip_addcompany_back(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_backA = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-会员-企业会员-返回失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_backA

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索栏
    def Kjlb_browseascspace_menu_addvip_addcompany_search(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_searchA = self.p.get_element("id->com.yunlu6.stone:id/buildstone_search_key","空间列表-浏览协会空间-菜单栏-会员-企业会员-搜索栏失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_searchA

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索栏-搜索栏
    def Kjlb_browseascspace_menu_addvip_addcompany_search_search(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_search_searchA = self.p.get_element("id->com.yunlu6.stone:id/et_search_key","空间列表-浏览协会空间-菜单栏-会员-企业会员-搜索栏-搜索栏失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_search_searchA

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索按钮
    def Kjlb_browseascspace_menu_addvip_addcompany_searchbtn(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_searchbtnA = self.p.get_element("id->com.yunlu6.stone:id/iv_search","空间列表-浏览协会空间-菜单栏-会员-企业会员-搜索按钮失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_searchbtnA

     #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-菜单栏
    def Kjlb_browseascspace_menu_addvip_addcompany_menu(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_menuA = self.p.get_element("id->com.yunlu6.stone:id/iv_more","空间列表-浏览协会空间-菜单栏-会员-企业会员-菜单栏失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_menuA

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_nearbyA = self.p.get_element("id->com.yunlu6.stone:id/ll_recover","空间列表-浏览协会空间-菜单栏-会员-企业会员-我的附近失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_nearbyA

    #定位:空间列表-浏览协会空间-菜单栏-浏览记录
    def Kjlb_browseascspace_menu_history(self):
        self.Kjlb_browseascspace_menu_historyA = self.p.get_element("id->com.yunlu6.stone:id/anti","空间列表-浏览协会空间-菜单栏-浏览记录")
        return self.Kjlb_browseascspace_menu_historyA

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-圆圈勾选列表
    def Kjlb_browseascspace_menu_addvip_addcompany_choose(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_chooseA = self.p.get_elements("id->com.yunlu6.stone:id/assadd_select_icon","空间列表-浏览协会空间-菜单栏-会员-企业会员-圆圈勾选失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_chooseA

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-确定
    def Kjlb_browseascspace_menu_addvip_addcompany_confirm(self):
        self.Kjlb_browseascspace_menu_addvip_addcompany_confirmA = self.p.get_element("id->com.yunlu6.stone:id/company_search_assadd","空间列表-浏览协会空间-菜单栏-会员-企业会员-确定失败")
        return self.Kjlb_browseascspace_menu_addvip_addcompany_confirmA

# ***************************************【PAGE2】菜单栏-搜附近Kjlb_browseascspace_menu_nearby***************************************
# 【PAGE3】路线Kjlb_browseascspace_menu_addvip_addcompany_nearby_route
# 【PAGE3】路线-返回Kjlb_browseascspace_menu_addvip_addcompany_nearby_route_back
# 【PAGE3】确定Kjlb_browseascspace_menu_addvip_addcompany_nearby_confirm
# 【PAGE3】搜索栏Kjlb_browseascspace_menu_addvip_addcompany_nearby_search
# 【PAGE3】搜索按钮Kjlb_browseascspace_menu_addvip_addcompany_nearby_searchbtn
# 【PAGE3】返回Kjlb_browseascspace_menu_addvip_addcompany_nearby_back

























































