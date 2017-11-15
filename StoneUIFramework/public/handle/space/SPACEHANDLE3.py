__author__ = 'xiaoj'
# 空间首页
from StoneUIFramework.public.handle.space.SPACEHANDLE2 import SPACEHANDLE2


class SPACEHANDLE3(SPACEHANDLE2):
    # ***************************************【PAGE2】产品Kjlb_browseorgspace_menu_product***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-返回:点击
    def Kjlb_browseorgspace_menu_product_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_back)

    #  空间列表-浏览企业空间-菜单栏-产品-新建:点击
    def Kjlb_browseorgspace_menu_product_new_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_unlock_list, n)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-产品名查找
    def Kjlb_browseorgspace_menu_product_unlock_list_byname(self, name):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_byname(name))

    #  空间列表-浏览企业空间-菜单栏-产品-未发布
    def Kjlb_browseorgspace_menu_product_unlock_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-产品名查找:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_byname_click(self, name):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_byname(name)[0])

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-产品名查找:点击
    def Kjlb_browseorgspace_menu_product_lock_list_byname_click(self, name):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_byname(name)[0])

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表:点击
    def Kjlb_browseorgspace_menu_product_lock_list_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_lock_list, n)

    #   空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-商品名检查
    def Kjlb_browseorgspace_menu_product_lock_list_proname_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_product_lock_list_proname)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布:点击
    def Kjlb_browseorgspace_menu_product_lock_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock)

    # 空间列表-浏览企业空间-菜单栏-产品-收款账号:点击
    def Kjlb_browseorgspace_menu_product_account_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_account)

    # 空间列表-浏览企业空间-菜单栏-产品-搜索:点击
    def Kjlb_browseorgspace_menu_product_seek_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_seek)

    # ***************************************【PAGE2】团队Kjlb_browseorgspace_menu_team***************************************
    # 空间列表-浏览企业空间-菜单栏-团队-返回:点击
    def Kjlb_browseorgspace_menu_team_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_back)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏:点击
    def Kjlb_browseorgspace_menu_team_menu_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_assignjob)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门:点击
    def Kjlb_browseorgspace_menu_team_menu_mydepartment_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_mydepartment)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-返回:点击
    def Kjlb_browseorgspace_menu_team_menu_mydepartment_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_mydepartment_back)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-我的部门-搜索:点击
    def Kjlb_browseorgspace_menu_team_menu_mydepartment_seek_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_mydepartment_seek)

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑:点击
    def Kjlb_browseorgspace_menu_team_teamedit_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_teamedit)

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮列表:点击
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_team_teamedit_numeidt, n)

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-职位人数:发送文本
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit, text)

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-职位人数:清空文本
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_claer(self):
        return self.p.clear(self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit)

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-职位人数:获取文本
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit)

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-否:点击
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancel_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancel)

    # 空间列表-浏览企业空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-是:点击
    def Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirm)

    # ***************************************【PAGE2】资讯Kjlb_browseorgspace_menu_archivies***************************************
    # 空间列表-浏览企业空间-菜单栏-资讯-返回:点击
    def Kjlb_browseorgspace_menu_archivies_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_back)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮:点击
    def Kjlb_browseorgspace_menu_archivies_new_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-资讯:点击
    def Kjlb_browseorgspace_menu_archivies_new_archivies_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_archivies)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-章程:点击
    def Kjlb_browseorgspace_menu_archivies_new_constitution_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_constitution)

    # 空间列表-浏览企业空间-菜单栏-资讯-图片新增:点击
    def Kjlb_browseorgspace_menu_archivies_picadd_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_picadd)

    # 空间列表-浏览企业空间-菜单栏-资讯-图片列表:点击
    def Kjlb_browseorgspace_menu_archivies_pic_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_archivies_pic, n)

    # 空间列表-浏览企业空间-菜单栏-资讯-图片列表-标题:文本获取
    def Kjlb_browseorgspace_menu_archivies_pic_title_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_archivies_pic_title)

    # ***************************************【PAGE2】企业名片Kjlb_browseorgspace_menu_bcard***************************************
    # 空间列表-浏览企业空间-菜单栏-编辑-返回:点击
    def Kjlb_browseorgspace_menu_edit_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_edit_back)

    # 空间列表-浏览企业空间-菜单栏-编辑-Logo:点击
    def Kjlb_browseorgspace_menu_edit_logo_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_edit_logo)

    # 空间列表-浏览企业空间-菜单栏-编辑-Logo-相册:点击
    def Kjlb_browseorgspace_menu_edit_logo_album_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_edit_logo_album)

    # 空间列表-浏览企业空间-菜单栏-编辑-Logo-拍照:点击
    def Kjlb_browseorgspace_menu_edit_logo_takepic_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_edit_logo_takepic)

    # 空间列表-浏览企业空间-菜单栏-编辑-Logo-取消:点击
    def Kjlb_browseorgspace_menu_edit_logo_cancel_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_edit_logo_cancel)

    # 空间列表-浏览企业空间-菜单栏-编辑-企业全称:发送文本
    def Kjlb_browseorgspace_menu_edit_fullname_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_edit_fullname, text)

        # 空间列表-浏览企业空间-菜单栏-编辑-企业简称:发送文本

    def Kjlb_browseorgspace_menu_edit_simplename_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_edit_simplename, text)

    # 空间列表-浏览企业空间-菜单栏-编辑-所在地区:点击
    def Kjlb_browseorgspace_menu_edit_address_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_edit_address)

    # 空间列表-浏览企业空间-菜单栏-编辑-所在地区-所在地区列表:点击
    def Kjlb_browseorgspace_menu_edit_address_list_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_edit_address_list, n)

    # 空间列表-浏览企业空间-菜单栏-编辑-详细地址:发送文本
    def Kjlb_browseorgspace_menu_edit_detailaddress_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_edit_detailaddress, text)

    # 空间列表-浏览企业空间-菜单栏-编辑-联系人:发送文本
    def Kjlb_browseorgspace_menu_edit_contact_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_edit_contact, text)

    # 空间列表-浏览企业空间-菜单栏-编辑-联系人:获取文本
    def Kjlb_browseorgspace_menu_edit_contact_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_edit_contact)

    # 空间列表-浏览企业空间-菜单栏-编辑-联系人:清空文本
    def Kjlb_browseorgspace_menu_edit_contact_clear(self):
        return self.p.clear(self.Kjlb_browseorgspace_menu_edit_contact)

    # 空间列表-浏览企业空间-菜单栏-编辑-手机号:发送文本
    def Kjlb_browseorgspace_menu_edit_phone_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_edit_phone, text)

    # 空间列表-浏览企业空间-菜单栏-编辑-手机号:获取文本
    def Kjlb_browseorgspace_menu_edit_phone_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_edit_phone)

    # 空间列表-浏览企业空间-菜单栏-编辑-手机号:清空文本
    def Kjlb_browseorgspace_menu_edit_phone_clear(self):
        return self.p.clear(self.Kjlb_browseorgspace_menu_edit_phone)

    # 空间列表-浏览企业空间-菜单栏-编辑-座机号:发送文本
    def Kjlb_browseorgspace_menu_edit_landline_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_edit_landline, text)

    # 空间列表-浏览企业空间-菜单栏-编辑-座机号:获取文本
    def Kjlb_browseorgspace_menu_edit_landline_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_edit_landline)

    # 空间列表-浏览企业空间-菜单栏-编辑-座机号:清空文本
    def Kjlb_browseorgspace_menu_edit_landline_clear(self):
        return self.p.clear(self.Kjlb_browseorgspace_menu_edit_landline)

    # 空间列表-浏览企业空间-菜单栏-编辑-邮箱:发送文本
    def Kjlb_browseorgspace_menu_edit_email_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_edit_email, text)

    # 空间列表-浏览企业空间-菜单栏-编辑-邮箱:获取文本
    def Kjlb_browseorgspace_menu_edit_email_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_edit_email)

    # 空间列表-浏览企业空间-菜单栏-编辑-邮箱:清空文本
    def Kjlb_browseorgspace_menu_edit_email_clear(self):
        return self.p.clear(self.Kjlb_browseorgspace_menu_edit_email)

    # 空间列表-浏览企业空间-菜单栏-编辑-QQ:发送文本
    def Kjlb_browseorgspace_menu_edit_QQ_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_edit_QQ, text)

    # 空间列表-浏览企业空间-菜单栏-编辑-QQ:获取文本
    def Kjlb_browseorgspace_menu_edit_QQ_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_edit_QQ)

    # 空间列表-浏览企业空间-菜单栏-编辑-QQ:清空文本
    def Kjlb_browseorgspace_menu_edit_QQ_clear(self):
        return self.p.clear(self.Kjlb_browseorgspace_menu_edit_QQ)

    # 空间列表-浏览企业空间-菜单栏-编辑-网站:发送文本
    def Kjlb_browseorgspace_menu_edit_website_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_edit_website, text)

    # 空间列表-浏览企业空间-菜单栏-编辑-网站:获取文本
    def Kjlb_browseorgspace_menu_edit_website_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_edit_website)

    # 空间列表-浏览企业空间-菜单栏-编辑-网站:清空文本
    def Kjlb_browseorgspace_menu_edit_website_clear(self):
        return self.p.clear(self.Kjlb_browseorgspace_menu_edit_website)

    # 空间列表-浏览企业空间-菜单栏-编辑-勾选:点击
    def Kjlb_browseorgspace_menu_edit_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_edit_confirm)

    # ***************************************【PAGE2】订单Kjlb_browseorgspace_menu_order***************************************
    # 空间列表-浏览企业空间-菜单栏-订单-返回：点击
    def Kjlb_browseorgspace_menu_order_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_order_back)

    # 空间列表-浏览企业空间-菜单栏-订单-搜索栏：发送文本
    def Kjlb_browseorgspace_menu_order_search_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_order_search, text)

    # 空间列表-浏览企业空间-菜单栏-订单-搜索按钮：点击
    def Kjlb_browseorgspace_menu_order_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_order_searchbtn)

    # 空间列表-浏览企业空间-菜单栏-订单-空白页：元素
    def Kjlb_browseorgspace_menu_order_nonepage_element(self):
        return self.p.get_element(self.Kjlb_browseorgspace_menu_order_nonepage)

    # 空间列表-浏览企业空间-菜单栏-订单-全部：点击
    def Kjlb_browseorgspace_menu_order_all_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_order_all)

    # 空间列表-浏览企业空间-菜单栏-订单-全部：元素获取
    def Kjlb_browseorgspace_menu_order_all_element(self):
        return self.p.get_element(self.Kjlb_browseorgspace_menu_order_allE[0],
                                  self.Kjlb_browseorgspace_menu_order_allE[1])

    # 空间列表-浏览企业空间-菜单栏-订单-待付款：点击
    def Kjlb_browseorgspace_menu_order_waitforpay_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_order_waitforpay)

    # 空间列表-浏览企业空间-菜单栏-订单-待付款：元素获取
    def Kjlb_browseorgspace_menu_order_waitforpay_element(self):
        return self.p.get_element(self.Kjlb_browseorgspace_menu_order_waitforpayE[0],
                                  self.Kjlb_browseorgspace_menu_order_waitforpayE[1])

    # 空间列表-浏览企业空间-菜单栏-订单-待发货：点击
    def Kjlb_browseorgspace_menu_order_waitforsend_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_order_waitforsend)

    # 空间列表-浏览企业空间-菜单栏-订单-待发货：元素获取
    def Kjlb_browseorgspace_menu_order_waitforsend_element(self):
        return self.p.get_element(self.Kjlb_browseorgspace_menu_order_waitforsendE[0],
                                  self.Kjlb_browseorgspace_menu_order_waitforsendE[1])

    # 空间列表-浏览企业空间-菜单栏-订单-已发货：点击
    def Kjlb_browseorgspace_menu_order_alreadysend_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_order_alreadysend)

    # 空间列表-浏览企业空间-菜单栏-订单-已发货：元素获取
    def Kjlb_browseorgspace_menu_order_alreadysend_element(self):
        return self.p.get_element(self.Kjlb_browseorgspace_menu_order_alreadysendE[0],
                                  self.Kjlb_browseorgspace_menu_order_alreadysendE[1])

    # 空间列表-浏览企业空间-菜单栏-订单-退款中：点击
    def Kjlb_browseorgspace_menu_order_refund_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_order_refund)

    # 空间列表-浏览企业空间-菜单栏-订单-退款中：元素获取
    def Kjlb_browseorgspace_menu_order_refund_element(self):
        return self.p.get_element(self.Kjlb_browseorgspace_menu_order_refundE[0],
                                  self.Kjlb_browseorgspace_menu_order_refundE[1])

    # 空间列表-浏览企业空间-菜单栏-订单-待评价：点击
    def Kjlb_browseorgspace_menu_order_evaluate_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_order_evaluate)

    # 空间列表-浏览企业空间-菜单栏-订单-待评价：元素获取
    def Kjlb_browseorgspace_menu_order_evaluate_element(self):
        return self.p.get_element(self.Kjlb_browseorgspace_menu_order_evaluateE[0],
                                  self.Kjlb_browseorgspace_menu_order_evaluateE[1])

    # 空间列表-浏览企业空间-菜单栏-订单-商品名列表卖家：点击
    def Kjlb_browseorgspace_menu_order_prolist_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_order_prolistS, n)

    # 空间列表-浏览企业空间-菜单栏-订单-商品名列表-商品名：获取文本
    def Kjlb_browseorgspace_menu_order_prolist_pronameT(self, n):
        return self.p.get_texts(self.Kjlb_browseorgspace_menu_order_prolist_proname, n)

    # 空间列表-浏览企业空间-菜单栏-订单-订单编号：文本
    def Kjlb_browseorgspace_menu_order_no_text(self, n):
        return self.p.get_texts(self.Kjlb_browseorgspace_menu_order_no, n)

    # 空间列表-浏览企业空间-菜单栏-订单-确认发货：点击
    def Kjlb_browseorgspace_menu_order_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_order_confirm)

    # 空间列表-浏览企业空间-菜单栏-订单-查看物流：点击
    def Kjlb_browseorgspace_menu_order_logistics_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_order_logistics)

    # ***************************************【PAGE2】访客Kjlb_browseorgspace_menu_visitor***************************************
    # 空间列表-浏览企业空间-菜单栏-访客-访客列表:点击
    def Kjlb_browseorgspace_menu_visitor_list_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_visitor_list, n)

    # 空间列表-浏览企业空间-菜单栏-访客-访客列表-返回:点击
    def Kjlb_browseorgspace_menu_visitor_list_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_visitor_list_back)

    # ***************************************【PAGE2】客户Kjlb_browseorgspace_menu_customer***************************************
    # 空间列表-浏览企业空间-菜单栏-客户-返回:点击
    def Kjlb_browseorgspace_menu_customer_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_back)

        # 空间列表-浏览企业空间-菜单栏-客户-搜索框:发送文本

    def Kjlb_browseorgspace_menu_customer_search_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_customer_search, text)

    # 空间列表-浏览企业空间-菜单栏-客户-搜索:点击
    def Kjlb_browseorgspace_menu_customer_seek_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_seek)

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏:点击
    def Kjlb_browseorgspace_menu_customer_menu_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu)

    # 空间列表-浏览企业空间-菜单栏-客户-客户列表
    def Kjlb_browseorgspace_menu_customer_clist_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_customer_clist, n)

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏+客户:点击
    def Kjlb_browseorgspace_menu_customer_menu_add_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu_add)

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作:点击
    def Kjlb_browseorgspace_menu_customer_menu_batch_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu_batch)

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-返回:点击
    def Kjlb_browseorgspace_menu_customer_menu_batch_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu_batch_back)

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-全选:点击
    def Kjlb_browseorgspace_menu_customer_menu_batch_all_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu_batch_all)

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-批量操作-圆圈勾选列表:点击
    def Kjlb_browseorgspace_menu_customer_menu_batch_choose_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_customer_menu_batch_choose, n)

    # ***************************************【PAGE2】业务升级Kjlb_browseorgspace_menu_upgrade***************************************
    # 空间列表-浏览企业空间-菜单栏-业务升级-开启:点击
    def Kjlb_browseorgspace_menu_upgrade_open_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_upgrade_open)

    # 空间列表-浏览企业空间-菜单栏-业务升级-返回:点击
    def Kjlb_browseorgspace_menu_upgrade_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_upgrade_back)

    # ***************************************【PAGE2】照片列表(包括点击照片加数据)Kjlb_browseperspace_piclist***************************************
    # 空间列表-浏览私人空间-照片列表-菜单栏
    def Kjlb_browseperspace_piclist_menu_click(self, n):
        return self.p.clicks(self.Kjlb_browseperspace_piclist_menu, n)

    # 空间列表-浏览私人空间-照片列表-分类到
    def Kjlb_browseperspace_piclist_classify_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_classify)

        # 空间列表-浏览私人空间-照片列表-编辑

    def Kjlb_browseperspace_piclist_edit_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_edit)

    # 空间列表-浏览私人空间-照片列表-返回
    def Kjlb_browseperspace_piclist_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_back)

        # 空间列表-浏览私人空间-照片列表-照片本身

    def Kjlb_browseperspace_piclist_itself_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_itself)

    # 空间列表-浏览私人空间-文件夹名称列表
    def Kjlb_browseperspace_foldername_click(self, n):
        return self.p.clicks(self.Kjlb_browseperspace_foldername, n)

    # 空间列表-浏览私人空间-文件夹名称列表-获取元素
    def Kjlb_browseperspace_foldername_get(self):
        return self.p.get_elements(self.Kjlb_browseperspace_foldername[0], self.Kjlb_browseperspace_foldername[1])

    # 空间列表-浏览私人空间-加数据-相册
    def Kjlb_browseperspace_addData_ByAlbum_click(self):
        return self.p.click(self.Kjlb_browseperspace_addData_ByAlbum)

    # ***************************************【PAGE2】菜单栏-名片Kjlb_browseperspace_menu_card***************************************
    # 空间列表-浏览私人空间-菜单栏-名片-返回
    def Kjlb_browseperspace_menu_card_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_back)

    # 空间列表-浏览私人空间-菜单栏-名片-分享
    def Kjlb_browseperspace_menu_card_share_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_share)

    # 空间列表-浏览私人空间-菜单栏-名片-分享-微信
    def Kjlb_browseperspace_menu_card_share_wechat_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_share_wechat)

    # 空间列表-浏览私人空间-菜单栏-名片-分享-微信朋友圈
    def Kjlb_browseperspace_menu_card_share_circle_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_share_circle)

    # 空间列表-浏览私人空间-菜单栏-名片-分享-QQ空间
    def Kjlb_browseperspace_menu_card_share_qqzone_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_share_qqzone)

    # 空间列表-浏览私人空间-菜单栏-名片-分享-QQ
    def Kjlb_browseperspace_menu_card_share_qq_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_share_qq)

    # 空间列表-浏览私人空间-菜单栏-名片-分享-新浪微博
    def Kjlb_browseperspace_menu_card_share_sina_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_share_sina)

    # 空间列表-浏览私人空间-菜单栏-名片-分享-取消
    def Kjlb_browseperspace_menu_card_share_cancel_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_share_cancel)

    # 空间列表-浏览私人空间-菜单栏-名片-手机
    def Kjlb_browseperspace_menu_card_phone_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_phone)

    # 空间列表-浏览私人空间-菜单栏-名片-邮箱
    def Kjlb_browseperspace_menu_card_email_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_email)

    # 空间列表-浏览私人空间-菜单栏-名片-地址
    def Kjlb_browseperspace_menu_card_address_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_address)

    # 空间列表-浏览私人空间-菜单栏-名片-QQ
    def Kjlb_browseperspace_menu_card_QQ_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_QQ)

    # 空间列表-浏览私人空间-菜单栏-名片-有效期
    def Kjlb_browseperspace_menu_card_limit_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_card_limit)

    # 空间列表-浏览私人空间-菜单栏-编辑-删除文件夹列表
    def Kjlb_browseperspace_menu_edit_deletefolder_click(self, n):
        return self.p.clicks(self.Kjlb_browseperspace_menu_edit_deletefolder, n)

    # 空间列表-浏览私人空间-菜单栏-编辑-修改文件夹图标列表
    def Kjlb_browseperspace_menu_edit_editfolder_click(self, n):
        return self.p.clicks(self.Kjlb_browseperspace_menu_edit_editfolder, n)

        # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表

    def Kjlb_browseperspace_menu_edit_editfolder_fname_sendkeys(self, name):
        return self.p.send_keys(self.Kjlb_browseperspace_menu_edit_editfolder_fname, name)

        # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-是

    def Kjlb_browseperspace_menu_edit_editfolder_fname_OK_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_editfolder_spaceEdit_OK)

    # 空间列表-浏览私人空间-菜单栏-编辑-文件夹名称-名称列表-否
    def Kjlb_browseperspace_menu_edit_editfolder_fname_NO_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_editfolder_spaceEdit_NO)

    # 空间列表-浏览私人空间-菜单栏-编辑-+数据
    def Kjlb_browseperspace_menu_edit_adddata_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_adddata)

    # 空间列表-浏览私人空间-菜单栏-编辑-空间类型
    def Kjlb_browseperspace_menu_edit_spacetype_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_spacetype)

    # 空间列表-浏览私人空间-菜单栏-编辑-删除空间
    def Kjlb_browseperspace_menu_edit_deletespace_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_deletespace)

    # 空间列表-浏览私人空间-菜单栏-编辑-删除空间-是
    def Kjlb_browseperspace_menu_edit_deletespace_OK_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_deletespace_OK)

    # 空间列表-浏览私人空间-菜单栏-编辑-删除空间-否
    def Kjlb_browseperspace_menu_edit_deletespace_NO_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_deletespace_NO)

    # 空间列表-浏览私人空间-菜单栏-编辑-返回
    def Kjlb_browseperspace_menu_edit_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_back)

        # 空间列表-浏览私人空间-菜单栏-编辑-空间名

    def Kjlb_browseperspace_menu_edit_spacename_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_spacename)

    # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称列表(0)
    def Kjlb_browseperspace_menu_edit_spacename_spaceEdit_sendkeys(self, n, name):
        return self.p.sends_keys(self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit, n, name)

    # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-是
    def Kjlb_browseperspace_menu_edit_spacename_spaceEdit_OK_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit_OK)

    # 空间列表-浏览私人空间-菜单栏-编辑-空间名-空间名称-否
    def Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NO_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_edit_spacename_spaceEdit_NO)

    # ***************************************【PAGE2】菜单栏-客户Kjlb_browseperspace_menu_customer***************************************
    # 空间列表-浏览私人空间-菜单栏-客户-返回
    def Kjlb_browseperspace_menu_customer_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_back)

    # 空间列表-浏览私人空间-菜单栏-客户-搜索栏
    def Kjlb_browseperspace_menu_customer_search_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_search)

        # 空间列表-浏览私人空间-菜单栏-客户-搜索按钮

    def Kjlb_browseperspace_menu_customer_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_searchbtn)

    # 空间列表-浏览私人空间-菜单栏-客户-菜单
    def Kjlb_browseperspace_menu_customer_menu_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_menu)

    # 空间列表-浏览私人空间-菜单栏-客户-菜单-+客户
    def Kjlb_browseperspace_menu_customer_menu_addcus_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_menu_addcus)

        # 空间列表-浏览私人空间-菜单栏-客户-客户列表

    def Kjlb_browseperspace_menu_customer_clist_click(self, n):
        return self.p.clicks(self.Kjlb_browseperspace_menu_customer_clist, n)

    # 空间列表-浏览私人空间-菜单栏-客户-群聊
    def Kjlb_browseperspace_menu_customer_gchat_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_gchat)

    # 空间列表-浏览私人空间-菜单栏-+文件夹-文件夹名称
    def Kjlb_browseperspace_menu_addfolder_confirm_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_addfolder_confirm)

        # 空间列表-浏览私人空间-菜单栏-+文件夹-文件夹名称

    def Kjlb_browseperspace_menu_addfolder_foldername_sendkeys(self, name):
        return self.p.send_keys(self.Kjlb_browseperspace_menu_addfolder_foldername, name)

    # 空间列表-浏览私人空间-菜单栏-+文件夹-返回
    def Kjlb_browseperspace_menu_addfolder_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_addfolder_back)

    # ***************************************【PAGE2】+数据Kjlb_browseperspace_adata***************************************
    # 空间列表-浏览私人空间-加数据-相册
    def Kjlb_browseperspace_adata_ByAlbum_click(self):
        return self.p.click(self.Kjlb_browseperspace_adata_ByAlbum)

    # 空间列表-浏览私人空间-加数据-拍照
    def Kjlb_browseperspace_adata_ByTakepic_click(self):
        return self.p.click(self.Kjlb_browseperspace_adata_ByTakepic)

    # 空间列表-浏览私人空间-加数据-取消
    def Kjlb_browseperspace_adata_cancel_click(self):
        return self.p.click(self.Kjlb_browseperspace_adata_cancel)

    # ***************************************【PAGE2】更多Kjlb_browseperspace_more***************************************
    # 空间列表-浏览私人空间-更多-照片列表
    def Kjlb_browseperspace_more_piclist_click(self, n):
        return self.p.clicks(self.Kjlb_browseperspace_more_piclist, n)

    # 空间列表-浏览私人空间-更多-返回
    def Kjlb_browseperspace_more_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_back)

    # 空间列表-浏览私人空间-更多-菜单栏
    def Kjlb_browseperspace_more_menu_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu)

    # 空间列表-浏览私人空间-更多-菜单栏-上传
    def Kjlb_browseperspace_more_menu_upload_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_upload)

    # 空间列表-浏览私人空间-更多-菜单栏-上传-相册
    def Kjlb_browseperspace_more_menu_upload_ByAlbum_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_upload_ByAlbum)

    # 空间列表-浏览私人空间-更多-菜单栏-上传-拍照
    def Kjlb_browseperspace_more_menu_upload_ByTakepic_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_upload_ByTakepic)

    # 空间列表-浏览私人空间-更多-菜单栏-上传-取消
    def Kjlb_browseperspace_more_menu_upload_cancel_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_upload_cancel)

    # 空间列表-浏览私人空间-更多-菜单栏-编辑
    def Kjlb_browseperspace_more_menu_edit_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_edit)

    # 空间列表-浏览私人空间-更多-菜单栏-排序
    def Kjlb_browseperspace_more_menu_sort_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_sort)

    # ***************************************【PAGE2】企业会员Kjlb_browseascspace_ovip***************************************
    # 空间列表-协会空间-企业会员-返回
    def Kjlb_browseascspace_ovip_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_ovip_back)

    # 空间列表-协会空间-企业会员-搜索栏
    def Kjlb_browseascspace_ovip_search_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_ovip_search, text)

    # 空间列表-协会空间-企业会员-搜索按钮
    def Kjlb_browseascspace_ovip_searchbtn(self):
        return self.p.click(self.Kjlb_browseascspace_ovip_search)

    # 空间列表-协会空间-企业会员-企业列表
    def Kjlb_browseascspace_ovip_olist_click(self, n):
        return self.p.clicks(self.Kjlb_browseascspace_ovip_olist, n)

    # ***************************************【PAGE2】个人会员Kjlb_browseascspace_ovip***************************************
    # 空间列表-协会空间-个人会员-返回
    def Kjlb_browseascspace_pvip_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_pvip_back)

    # 空间列表-协会空间-个人会员-搜索栏
    def Kjlb_browseascspace_pvip_search_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_pvip_search, text)

    # 空间列表-协会空间-个人会员-搜索按钮
    def Kjlb_browseascspace_pvip_searchbtn(self):
        return self.p.click(self.Kjlb_browseascspace_pvip_searchbtn)

    # 空间列表-协会空间-个人会员-人脉列表
    def Kjlb_browseascspace_pvip_plist_click(self, n):
        return self.p.clicks(self.Kjlb_browseascspace_pvip_olist, n)

    # ***************************************【PAGE2】资讯Kjlb_browseascspace_arch***************************************
    # 空间列表-协会空间-资讯-返回
    def Kjlb_browseascspace_arch_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_arch_back)

    # 空间列表-协会空间-资讯-资讯文件列表
    def Kjlb_browseascspace_arch_alist_click(self, n):
        return self.p.clicks(self.Kjlb_browseascspace_arch_alist, n)

    # ***************************************【PAGE2】协会资信信息Kjlb_browseascspace_credit***************************************
    # 空间列表-协会空间-资信-返回
    def Kjlb_browseascspace_credit_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_credit_back)

    # ***************************************【PAGE2】菜单栏-编辑Kjlb_browseascspace_menu_edit***************************************
    # 空间列表-浏览协会空间-菜单栏-编辑-返回:点击
    def Kjlb_browseascspace_menu_edit_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_back)

        # 空间列表-浏览协会空间-菜单栏-编辑-Logo:点击

    def Kjlb_browseascspace_menu_edit_logo_sendkeys(self, text):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_logo)

    # 空间列表-浏览协会空间-菜单栏-编辑-企业全称:发送文本
    def Kjlb_browseascspace_menu_edit_fullname_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_fullname, text)

    # 空间列表-浏览协会空间-菜单栏-编辑-企业简称:发送文本
    def Kjlb_browseascspace_menu_edit_simplename_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_simplename, text)

    # 空间列表-浏览协会空间-菜单栏-编辑-所在地区:点击
    def Kjlb_browseascspace_menu_edit_address_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_address)

    # 空间列表-浏览协会空间-菜单栏-编辑-所在地区-所在地区列表
    def Kjlb_browseascspace_menu_edit_address_list_click(self, n):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_address_list)

    # 空间列表-浏览协会空间-菜单栏-编辑-详细地址:发送文本
    def Kjlb_browseascspace_menu_edit_detailaddress_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_detailaddress, text)

    # 空间列表-浏览协会空间-菜单栏-编辑-联系人:发送文本
    def Kjlb_browseascspace_menu_edit_contact_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_contact, text)

    # 空间列表-浏览协会空间-菜单栏-编辑-联系人:获取文本
    def Kjlb_browseascspace_menu_edit_contact_text(self):
        return self.p.get_text(self.Kjlb_browseascspace_menu_edit_contact)

    # 空间列表-浏览协会空间-菜单栏-编辑-联系人:清空文本
    def Kjlb_browseascspace_menu_edit_contact_clear(self):
        return self.p.clear(self.Kjlb_browseascspace_menu_edit_contact)

    # 空间列表-浏览协会空间-菜单栏-编辑-手机号:发送文本
    def Kjlb_browseascspace_menu_edit_phone_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_phone, text)

    # 空间列表-浏览协会空间-菜单栏-编辑-手机号:获取文本
    def Kjlb_browseascspace_menu_edit_phone_text(self):
        return self.p.get_text(self.Kjlb_browseascspace_menu_edit_phone)

    # 空间列表-浏览协会空间-菜单栏-编辑-手机号:清空文本
    def Kjlb_browseascspace_menu_edit_phone_clear(self):
        return self.p.clear(self.Kjlb_browseascspace_menu_edit_phone)

    # 空间列表-浏览协会空间-菜单栏-编辑-座机号:发送文本
    def Kjlb_browseascspace_menu_edit_landline_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_landline, text)

    # 空间列表-浏览协会空间-菜单栏-编辑-座机号:获取文本
    def Kjlb_browseascspace_menu_edit_landline_text(self):
        return self.p.get_text(self.Kjlb_browseascspace_menu_edit_landline)

    # 空间列表-浏览协会空间-菜单栏-编辑-座机号:清空文本
    def Kjlb_browseascspace_menu_edit_landline_clear(self):
        return self.p.clear(self.Kjlb_browseascspace_menu_edit_landline)

    # 空间列表-浏览协会空间-菜单栏-编辑-邮箱:发送文本
    def Kjlb_browseascspace_menu_edit_email_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_email, text) \
 \
    # 空间列表-浏览协会空间-菜单栏-编辑-邮箱:获取文本
    def Kjlb_browseascspace_menu_edit_email_text(self):
        return self.p.get_text(self.Kjlb_browseascspace_menu_edit_email)

    # 空间列表-浏览协会空间-菜单栏-编辑-邮箱:清空文本
    def Kjlb_browseascspace_menu_edit_email_clear(self):
        return self.p.clear(self.Kjlb_browseascspace_menu_edit_email)

    # 空间列表-浏览协会空间-菜单栏-编辑-QQ:发送文本
    def Kjlb_browseascspace_menu_edit_QQ_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_QQ, text)

    # 空间列表-浏览协会空间-菜单栏-编辑-QQ:获取文本
    def Kjlb_browseascspace_menu_edit_QQ_text(self):
        return self.p.get_text(self.Kjlb_browseascspace_menu_edit_QQ)

    # 空间列表-浏览协会空间-菜单栏-编辑-QQ:清空文本
    def Kjlb_browseascspace_menu_edit_QQ_clear(self):
        return self.p.clear(self.Kjlb_browseascspace_menu_edit_QQ)

    # 空间列表-浏览协会空间-菜单栏-编辑-网站:发送文本
    def Kjlb_browseascspace_menu_edit_website_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_edit_website, text)

    # 空间列表-浏览协会空间-菜单栏-编辑-网站:获取文本
    def Kjlb_browseascspace_menu_edit_website_text(self):
        return self.p.get_text(self.Kjlb_browseascspace_menu_edit_website)

    # 空间列表-浏览协会空间-菜单栏-编辑-网站:清空文本
    def Kjlb_browseascspace_menu_edit_website_clear(self):
        return self.p.clear(self.Kjlb_browseascspace_menu_edit_website)

    # 空间列表-浏览协会空间-菜单栏-编辑-勾选:点击
    def Kjlb_browseascspace_menu_edit_confirm_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_confirm)

    # ***************************************【PAGE2】菜单栏-团队Kjlb_browseascspace_menu_team***************************************
    # 空间列表-浏览协会空间-菜单栏-团队-返回:点击
    def Kjlb_browseascspace_menu_team_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_back)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏:点击
    def Kjlb_browseascspace_menu_team_menu_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门:点击
    def Kjlb_browseascspace_menu_team_menu_mydepartment_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_mydepartment)

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑:点击
    def Kjlb_browseascspace_menu_team_teamedit_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_teamedit)

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮:点击
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_teamedit_numeidt)

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-职位人数:发送文本
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit, text)

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-职位人数:清空文本
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_clear(self):
        return self.p.clear(self.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit)

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-职位人数:获取文本
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_text(self):
        return self.p.get_text(self.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit)

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-否:点击
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel)

    # 空间列表-浏览协会空间-菜单栏-团队-团队编辑按钮-编辑人数按钮-是:点击
    def Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm)

        # 空间列表-浏览协会空间-菜单栏-会员-企业名录:点击

    def Kjlb_browseascspace_menu_vip_companylist_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_companylist)

    # 空间列表-浏览协会空间-菜单栏-会员-企业名录-企业名列表:点击
    def Kjlb_browseascspace_menu_vip_companylist_companyname_click(self, n):
        return self.p.clicks(self.Kjlb_browseascspace_menu_vip_companylist_companyname, n)

    # 空间列表-浏览协会空间-菜单栏-会员-搜索按钮:点击
    def Kjlb_browseascspace_menu_vip_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_searchbtn)

    # 空间列表-浏览协会空间-菜单栏-会员-个人名录:点击
    def Kjlb_browseascspace_menu_vip_personlist_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_personlist)

    # 空间列表-浏览协会空间-菜单栏-会员-个人名录-个人名列表:点击
    def Kjlb_browseascspace_menu_vip_personlist_personname_click(self, n):
        return self.p.clicks(self.Kjlb_browseascspace_menu_vip_personlist_personname, n)

    # 空间列表-浏览协会空间-菜单栏-会员-搜索栏:发送文本
    def Kjlb_browseascspace_menu_vip_search_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_vip_search, text)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏:点击
    def Kjlb_browseascspace_menu_vip_menu_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu)

        # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员:点击

    def Kjlb_browseascspace_menu_vip_menu_addvip_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_addvip)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-返回:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_back)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索栏:发送文本
    def Kjlb_browseascspace_menu_vip_menu_manage_search_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_vip_menu_manage_search, text)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-搜索按钮:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_searchbtn)

        # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑:点击

    def Kjlb_browseascspace_menu_vip_menu_manage_edit_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_edit)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_companyname_click(self, n):
        return self.p.clicks(self.Kjlb_browseascspace_menu_vip_menu_manage_companyname, n)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&企业-返回:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_companyname_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_companyname_back)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_personname_click(self, n):
        return self.p.clicks(self.Kjlb_browseascspace_menu_vip_menu_manage_personname, n)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-名录列表&个人-返回:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_personname_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_personname_back)

        # 空间列表-浏览协会空间-菜单栏-会员-返回:点击

    def Kjlb_browseascspace_menu_vip_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_back)

    # ***************************************【PAGE2】菜单栏-+会员-个人会员Kjlb_browseascspace_menu_addvip_addperson***************************************
    # 定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-添加:点击
    def Kjlb_browseascspace_menu_addvip_addperson_confirm_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addperson_confirm)

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-圆圈勾选列表:点击
    def Kjlb_browseascspace_menu_addvip_addperson_choose_click(self, n):
        return self.p.clicks(self.Kjlb_browseascspace_menu_addvip_addperson_choose, n)

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-全选:点击
    def Kjlb_browseascspace_menu_addvip_addperson_all_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addperson_all)

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-搜索按钮:点击
    def Kjlb_browseascspace_menu_addvip_addperson_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addperson_searchbtn)

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-搜索栏:发送文本
    def Kjlb_browseascspace_menu_addvip_addperson_search_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_addvip_addperson_search, text)

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-个人会员-返回:点击
    def Kjlb_browseascspace_menu_addvip_addperson_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addperson_back)

    # ***************************************【PAGE2】菜单栏-+会员-企业会员Kjlb_browseascspace_menu_addvip_addcompany***************************************
    # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-返回:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_back)

        # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索栏-:点击

    def Kjlb_browseascspace_menu_addvip_addcompany_search_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_search)

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索栏-搜索栏:发送文本
    def Kjlb_browseascspace_menu_addvip_addcompany_search_search_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_addvip_addcompany_search_search, text)

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-搜索按钮:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_searchbtn)

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-菜单栏:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_menu_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_menu)

        # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近:点击

    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_nearby)

    # 定位:空间列表-浏览协会空间-菜单栏-浏览记录
    def Kjlb_browseascspace_menu_history_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_history)

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-圆圈勾选列表:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_choose_click(self, n):
        return self.p.clicks(self.Kjlb_browseascspace_menu_addvip_addcompany_choose, n)

    # 定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-确定:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_confirm_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_confirm)

# ***************************************【PAGE2】菜单栏-搜附近Kjlb_browseascspace_menu_nearby***************************************
# 【PAGE3】路线Kjlb_browseascspace_menu_addvip_addcompany_nearby_route
# 【PAGE3】路线-返回Kjlb_browseascspace_menu_addvip_addcompany_nearby_route_back
# 【PAGE3】确定Kjlb_browseascspace_menu_addvip_addcompany_nearby_confirm
# 【PAGE3】搜索栏Kjlb_browseascspace_menu_addvip_addcompany_nearby_search
# 【PAGE3】搜索按钮Kjlb_browseascspace_menu_addvip_addcompany_nearby_searchbtn
# 【PAGE3】返回Kjlb_browseascspace_menu_addvip_addcompany_nearby_back
