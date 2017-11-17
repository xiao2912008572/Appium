__author__ = 'xiaoj'
# 空间首页
from YunluFramework.public.handle.space.SPACEHANDLE4 import SPACEHANDLE4


class SPACEHANDLE5(SPACEHANDLE4):
    # ***************************************【PAGE4】添加照片-相册Kjlb_browseorgspace_menu_product_new_addphoto_album***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-相册-返回:点击
    def Kjlb_browseorgspace_menu_product_new_addphoto_album_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_addphoto_album_back)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-相册-照片列表:点击
    def Kjlb_browseorgspace_menu_product_new_addphoto_album_list_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_new_addphoto_album_list, n)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-相册-完成:点击
    def Kjlb_browseorgspace_menu_product_new_addphoto_album_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_addphoto_album_confirm)

    # ***************************************【PAGE4】添加照片-产品库Kjlb_browseorgspace_menu_product_new_addphoto_wifisync***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-产品库-返回:点击
    def Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_back)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-产品库-全选:点击
    def Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_all_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_all)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-产品库-照片列表:点击
    def Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_piclist_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_piclist, n)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-产品库-确定:点击
    def Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_confirm)

    # ***************************************【PAGE4】商品名称Kjlb_browseorgspace_menu_product_new_proname***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-返回:点击
    def Kjlb_browseorgspace_menu_product_new_proname_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_proname_back)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-勾选:点击
    def Kjlb_browseorgspace_menu_product_new_proname_choose_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_proname_choose)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-商品名称:发送文本
    def Kjlb_browseorgspace_menu_product_new_proname_name_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_product_new_proname_name, text)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-商品顶部标题:点击
    def Kjlb_browseorgspace_menu_product_new_proname_name_title_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_proname_name_title)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-分类输入框（云庐用）
    def Kjlb_browseorgspace_menu_product_new_proname_yclassify_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_proname_yclassify)

    #  空浏览企业空间-菜单栏-产品-新建-商品名称-推荐标签（云庐用）
    def Kjlb_browseorgspace_menu_product_new_proname_ytag_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_proname_ytag)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-分类（百石堂）:点击
    def Kjlb_browseorgspace_menu_product_new_proname_bclassify_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_proname_bclassify)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-推荐一级标签（百石堂）:点击
    def Kjlb_browseorgspace_menu_product_new_proname_bonetag_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_new_proname_bonetag, n)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-推荐二级标签（百石堂）:点击
    def Kjlb_browseorgspace_menu_product_new_proname_btwotag_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_new_proname_btwotag, n)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-确定（百石堂）:点击
    def Kjlb_browseorgspace_menu_product_new_proname_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_proname_confirm
                            )

    # ***************************************【PAGE4】石种属性Kjlb_browseorgspace_menu_product_new_attribute***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-返回:点击
    def Kjlb_browseorgspace_menu_product_new_attribute_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_attribute_back)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-勾选:点击
    def Kjlb_browseorgspace_menu_product_new_attribute_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_attribute_confirm)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-种类名:发送文本
    def Kjlb_browseorgspace_menu_product_new_attribute_species_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_product_new_attribute_species, text)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-种类名-匹配列表:点击
    def Kjlb_browseorgspace_menu_product_new_attribute_species_match_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_new_attribute_species_match, n)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-颜色:点击
    def Kjlb_browseorgspace_menu_product_new_attribute_color_click(self):
        self.Kjlb_browseorgspace_menu_product_new_attribute_color = self.p.get_element("id->com.yunlu6.stone:id/tv_color_name", "空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-颜色")
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_attribute_color)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-颜色-列表:点击
    def Kjlb_browseorgspace_menu_product_new_attribute_color_list_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_new_attribute_color_list, n)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-深浅:点击
    def Kjlb_browseorgspace_menu_product_new_attribute_attrname_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_attribute_attrname)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-深浅-列表:点击
    def Kjlb_browseorgspace_menu_product_new_attribute_attrname_list_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_new_attribute_attrname_list, n)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-花纹:点击
    def Kjlb_browseorgspace_menu_product_new_attribute_pattern_click(self):
        self.Kjlb_browseorgspace_menu_product_new_attribute_pattern = self.p.get_element("id->com.yunlu6.stone:id/tv_pattern_name", "空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-花纹")
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_attribute_pattern)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-花纹-列表:点击
    def Kjlb_browseorgspace_menu_product_new_attribute_pattern_list_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_attribute_pattern_list)

    # ***************************************【PAGE4】制品/表面Kjlb_browseorgspace_menu_product_new_attrstone***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-返回:点击
    def Kjlb_browseorgspace_menu_product_new_attrstone_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_attrstone_back)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-勾选:点击
    def Kjlb_browseorgspace_menu_product_new_attrstone_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_attrstone_confirm)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-制品:点击
    def Kjlb_browseorgspace_menu_product_new_attrstone_type_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_attrstone_type)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-制品-列表:点击
    def Kjlb_browseorgspace_menu_product_new_attrstone_type_list_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_new_attrstone_type_list, n)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-表面:点击
    def Kjlb_browseorgspace_menu_product_new_attrstone_surface_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_attrstone_surface)

    #  空浏览企业空间-菜单栏-产品-新建-制品/表面-表面-列表:点击
    def Kjlb_browseorgspace_menu_product_new_attrstone_surface_list_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_new_attrstone_surface_list, n)

    # ***************************************【PAGE4】产品参数Kjlb_browseorgspace_menu_product_new_parameter***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-返回:点击
    def Kjlb_browseorgspace_menu_product_new_parameter_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_parameter_back)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-勾选:点击
    def Kjlb_browseorgspace_menu_product_new_parameter_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_parameter_confirm)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-参数名列表:发送文本
    def Kjlb_browseorgspace_menu_product_new_parameter_key_sendkeys(self, n, text):
        return self.p.sends_keys(self.Kjlb_browseorgspace_menu_product_new_parameter_keylist, n, text)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-参数名列表:清空文本
    def Kjlb_browseorgspace_menu_product_new_parameter_key_clear(self, n):
        return self.p.clears(self.Kjlb_browseorgspace_menu_product_new_parameter_keylist, n)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-参数值列表:发送文本
    def Kjlb_browseorgspace_menu_product_new_parameter_value_sendkeys(self, n, text):
        return self.p.sends_keys(self.Kjlb_browseorgspace_menu_product_new_parameter_valuelist, n, text)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-参数值列表:清空文本
    def Kjlb_browseorgspace_menu_product_new_parameter_value_clear(self, n):
        return self.p.clears(self.Kjlb_browseorgspace_menu_product_new_parameter_valuelist, n)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-添加按钮:点击
    def Kjlb_browseorgspace_menu_product_new_parameter_addbtn_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_parameter_addbtn)

    # ***************************************【PAGE4】价格Kjlb_browseorgspace_menu_product_new_price***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-价格-返回:点击
    def Kjlb_browseorgspace_menu_product_new_price_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_price_back)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-价格-单价(元)列表:发送文本
    def Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(self, n, text):
        return self.p.sends_keys(self.Kjlb_browseorgspace_menu_product_new_price_unitpriceyuan, n, text)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-价格-库存列表:发送文本
    def Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(self, n, text):
        return self.p.sends_keys(self.Kjlb_browseorgspace_menu_product_new_price_stockkucun, n, text)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-价格-保存:点击
    def Kjlb_browseorgspace_menu_product_new_price_save_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_price_save)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-价格-新价:点击
    def Kjlb_browseorgspace_menu_product_new_price_add_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_price_add)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-价格-删除:点击
    def Kjlb_browseorgspace_menu_product_new_price_delete_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_price_delete)

    # ***************************************【PAGE4】立即购买Kjlb_browseorgspace_menu_product_lock_list_buynow***************************************
    # 【PAGE5-1】收货地址页面
    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-收货地址页面:元素
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_page_element(self):
        return self.p.get_element(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_page[0],
                                  self.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_page[1])

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-收货地址标题:获取文本
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_gettitle(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_title)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-收货地址-返回：点击
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_back)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-收货地址-收货人：发送文本
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_addressee_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_addressee, text)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-收货地址-联系电话：发送文本
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_cnumber_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_cnumber, text)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-收货地址-所在地区：点击
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_district_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_district)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-收货地址-所在地区-列表：点击
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_districtlist_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_districtlist, n)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-收货地址-详细地址：发送文本
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_detail_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_detail, text)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-收货地址-默认地址：点击
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_default_sendkeys(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_default)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-收货地址-保存：点击
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_save_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_save)

    # 【PAGE5-2】确认订单页面
    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单-返回：点击
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_back)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单页面：元素
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_pagee(self):
        return self.p.get_element(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_page[0],
                                  self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_page[1])

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单标题：获取文本
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_titlee(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_title)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单-收货人：获取文本
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_receive_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_receive)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单-电话：获取文本
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_phone_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_phone)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单-收货地址：获取文本
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_address_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_addressT)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单-地址栏：点击
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_address_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_address)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单-机构列表：点击
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_orglist_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_orglist, n)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单-商品列表：点击
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_prolist_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_prolist, n)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单-商品价格列表：获取文本
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_proprice_text(self, n):
        return self.p.get_texts(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_proprice, n)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单-商品价格'-按钮'列表：点击
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_prreduce_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_preduce, n)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单-商品价格'+按钮'列表：点击
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_padd_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_padd, n)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单-商品价格列表：获取文本
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_pnum_text(self, n):
        return self.p.get_texts(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_pnum, n)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单-合计：获取文本
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_total_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_total)

    #  空间列表-浏览企业空间-菜单栏-产品-立即购买-确认订单-支付：点击
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_pay_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_pay)

    # ***************************************【PAGE4】关联文件Kjlb_browseorgspace_menu_product_new_relation***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-关联文件-返回:点击
    def Kjlb_browseorgspace_menu_product_new_relation_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_relation_back)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-关联文件-选择照片/添加照片:点击
    def Kjlb_browseorgspace_menu_product_new_relation_photo_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_relation_photo)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-关联文件-已关联项:点击
    def Kjlb_browseorgspace_menu_product_new_relation_related_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_relation_related)

    # ***************************************【PAGE4】待任免联系人列表Kjlb_browseorgspace_menu_team_menu_assignjob_contact***************************************
    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-返回:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_contact_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_back)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-确认:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_contact_confrim_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_confirm)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-部门名称-列表:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_contact_department_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_department, n)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-职位名称-列表:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_contact_jobname_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_jobname, n)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-移除:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_contact_delete_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_delete)

    # ***************************************【PAGE4】人事任免新增Kjlb_browseorgspace_menu_team_menu_assignjob_addperson***************************************
    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-返回:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_back)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-搜索栏:发送文本
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_search_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_search, text)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-搜索按钮:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_searchbtn)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-全选:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_all_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_all)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-圆圈勾选:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_choose_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_choose, n)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-联系人列表:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_contact_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_contact, n)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-添加(确认):点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_confirm)

    # ***************************************【PAGE4】添加照片-相册Kjlb_browseorgspace_menu_archivies_new_addphoto_album***************************************
    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-文件库-照片列表:点击
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_list_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_list, n)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-文件库-全选:点击
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_all_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_all)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-文件库-确定:点击
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_confirm
                            )

    # ***************************************【PAGE4】照片统计按钮Kjlb_browseorgspace_menu_archivies_new_count***************************************
    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-文件照片列表:点击
    def Kjlb_browseorgspace_menu_archivies_new_count_list_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_archivies_new_count_list, n)

    # ***************************************【PAGE4】添加照片-相册Kjlb_browseorgspace_menu_archivies_new_addphoto_album***************************************
    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-相册-照片列表:点击
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_album_list_click(self, n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_archivies_new_addphoto_album_list, n)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-相册-完成:点击
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_album_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_addphoto_album_confirm)

    # ***************************************【PAGE4】添加照片-文件库Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync***************************************
    # 照片列表Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_list
    # 全选Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_all
    # 确定Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_confirm

    # ***************************************【PAGE4】分类到Kjlb_browseperspace_more_piclist_classify***************************************
    # 空间列表-浏览私人空间-更多-照片列表-分类到-空间id
    def Kjlb_browseperspace_more_piclist_classify_spaceById_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_classifyspace_ById)

    # 空间列表-浏览私人空间-更多-照片列表-分类到-空间名
    def Kjlb_browseperspace_more_piclist_classify_spaceByName_click(self, name):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_classify_spaceByName(name))

    # 空间列表-浏览私人空间-更多-照片列表-分类到-返回
    def Kjlb_browseperspace_more_piclist_classify_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_classifyspace_back)

    # 空间列表-浏览私人空间-更多-照片列表-分类到-勾选
    def Kjlb_browseperspace_more_piclist_classify_confirm_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_classifyspace_confirm)

    # 空间列表-浏览私人空间-更多-照片列表-分类到-文件夹ById
    def Kjlb_browseperspace_more_piclist_classify_folderByID_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_classifyspace_folderByID)

    # 空间列表-浏览私人空间-更多-照片列表-分类到-文件夹ByName
    def Kjlb_browseperspace_more_piclist_classify_folderByName_click(self, name):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_classify_folderByName(name))

    # ***************************************【PAGE4】编辑Kjlb_browseperspace_more_piclist_edit***************************************
    # 空间列表-浏览私人空间-更多-照片列表-编辑-返回
    def Kjlb_browseperspace_more_piclist_edit_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_edit_back)

    # 空间列表-浏览私人空间-更多-照片列表-编辑-删除
    def Kjlb_browseperspace_more_piclist_edit_delete_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_edit_delete)

    # 空间列表-浏览私人空间-更多-照片列表-编辑-删除-是
    def Kjlb_browseperspace_more_piclist_edit_delete_confirm_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_edit_delete_confirm)

    # 空间列表-浏览私人空间-更多-照片列表-编辑-删除-否
    def Kjlb_browseperspace_more_piclist_edit_delete_cancel_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_edit_delete_cancel)

    # 空间列表-浏览私人空间-更多-照片列表-编辑-名称
    def Kjlb_browseperspace_more_piclist_edit_picname_sendkeys(self, name):
        return self.p.send_keys(self.Kjlb_browseperspace_more_piclist_edit_picname, name)

    # 空间列表-浏览私人空间-更多-照片列表-编辑-备注
    def Kjlb_browseperspace_more_piclist_edit_remark_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_edit_remark)

    # 空间列表-浏览私人空间-更多-照片列表-编辑-保存
    def Kjlb_browseperspace_more_piclist_edit_save_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_edit_save)

    # ***************************************【PAGE4】删除文件夹Kjlb_browseperspace_more_menu_edit_deletefolder***************************************
    # 空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-照片列表
    def Kjlb_browseperspace_more_menu_edit_deletefolder_piclist_click(self, n):
        return self.p.clicks(self.Kjlb_browseperspace_more_menu_edit_deletefolder_piclist, n)

    # 空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-删除按钮
    def Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn)

    # 空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-删除按钮-是
    def Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_y_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_y)

        # 空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-删除按钮-否

    def Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_n_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_n)

    # 空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-全选
    def Kjlb_browseperspace_more_menu_edit_deletefolder_all_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_edit_foldername_all)

    # ***************************************【PAGE4】资讯图片Kjlb_browseascspace_arch_alist_pic***************************************
    # 空间列表-协会空间-资讯-资讯文件列表-资讯图片-资讯详情
    def Kjlb_browseascspace_arch_alist_pic_adetail_click(self):
        return self.p.click(self.Kjlb_browseascspace_arch_alist_pic_adetail)

    # 空间列表-协会空间-资讯-资讯文件列表-资讯图片-返回
    def Kjlb_browseascspace_arch_alist_pic_back(self):
        return self.p.click(self.Kjlb_browseascspace_arch_alist_pic_back)

    # ***************************************【PAGE4】联系人列表Kjlb_browseascspace_menu_team_menu_assignjob_contact***************************************
    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-返回:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_back)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-确认:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_confrim_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_confirm)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-部门名称:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_department_click(self, n):
        return self.p.clicks(self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_department, n)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-职位名称:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_jobname_click(self, n):
        return self.p.clicks(self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_jobname, n)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-移除:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_delete_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_delete)

    # ***************************************【PAGE4】人事任免新增Kjlb_browseascspace_menu_team_menu_assignjob_addperson***************************************
    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-返回:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_back)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-搜索栏:发送文本
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_search_sendkeys(self, text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_search, text)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-搜索按钮:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_searchbtn)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-全选:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_all_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_all)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-圆圈勾选列表:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_choose_click(self, n):
        return self.p.clicks(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_choose, n)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-联系人列表:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_contact_click(self, n):
        return self.p.clicks(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_contact, n)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-添加(确认):点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirm_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirm)
