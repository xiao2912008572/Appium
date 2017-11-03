__author__ = 'xiaoj'
#空间首页
from StoneUIFramework.public.handle.space.SPACEHANDLE3 import SPACEHANDLE3

class SPACEHANDLE4(SPACEHANDLE3):
#***************************************【PAGE3】已发布产品列表Kjlb_browseorgspace_menu_product_lock_list***************************************
   #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-商品名:点击
    def Kjlb_browseorgspace_menu_product_lock_list_proname_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_proname)

     #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-加入购物车:点击
    def Kjlb_browseorgspace_menu_product_lock_list_shoppingcart_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_shoppingcart)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-立即购买:点击
    def Kjlb_browseorgspace_menu_product_lock_list_buynow_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_buynow)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-客服:点击
    def Kjlb_browseorgspace_menu_product_lock_list_contactbusiness_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_contactbusiness)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-收藏:点击
    def Kjlb_browseorgspace_menu_product_lock_list_collection_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_collection)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-分享:点击
    def Kjlb_browseorgspace_menu_product_lock_list_share_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_share)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-公司名:点击
    def Kjlb_browseorgspace_menu_product_lock_list_companyname_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_companyname)

     #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-关联信息:点击
    def Kjlb_browseorgspace_menu_product_lock_list_right_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_right)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-关联信息-标签:点击
    def Kjlb_browseorgspace_menu_product_lock_list_right_tag_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_right_tag)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-产品参数:点击
    def Kjlb_browseorgspace_menu_product_lock_list_middle_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_middle)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-产品参数-石种名:文本
    def Kjlb_browseorgspace_menu_product_lock_list_middle_attribut_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_product_lock_list_middle_attribute)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-产品参数-制品与表面相关属性:文本
    def Kjlb_browseorgspace_menu_product_lock_list_middle_pattern_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_product_lock_list_middle_pattern)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-价格参数:点击
    def Kjlb_browseorgspace_menu_product_lock_list_left_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_left)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-产品参数-参数名/值:文本
    def Kjlb_browseorgspace_menu_product_lock_list_middle_keyvalue_text(self,n):
        return self.p.get_texts(self.Kjlb_browseorgspace_menu_product_lock_list_middle_parameters,n)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-更多价格:点击
    def Kjlb_browseorgspace_menu_product_lock_list_moreprice_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_moreprice)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-更多价格:文本
    def Kjlb_browseorgspace_menu_product_lock_list_moreprice_text(self,n):
        return self.p.get_texts(self.Kjlb_browseorgspace_menu_product_lock_list_moreprice_list,n)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-更多价格-列表:点击
    def Kjlb_browseorgspace_menu_product_lock_list_moreprice_list_click(self,n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_lock_list_moreprice_list,n)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-产品图片:点击
    def Kjlb_browseorgspace_menu_product_lock_list_photo_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_photo)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-下架:点击
    def Kjlb_browseorgspace_menu_product_lock_list_offshelf_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_offshelf)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-下架-是:点击
    def Kjlb_browseorgspace_menu_product_lock_list_offshelf_sure_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_offshelf_sure)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-下架-否:点击
    def Kjlb_browseorgspace_menu_product_lock_list_offshelf_no_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_offshelf_no)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-购物车图标:点击
    def Kjlb_browseorgspace_menu_product_lock_list_shopicon_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_shopicon)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-返回:点击
    def Kjlb_browseorgspace_menu_product_lock_list_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_lock_list_back)

# ***************************************【PAGE3】确认发货：Kjlb_browseorgspace_menu_order_confirm_click***************************************
    #  空间列表-浏览企业空间-菜单栏-订单-确认发货-返回：点击
    def Kjlb_browseorgspace_menu_order_confirm_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_order_confirm_back)

    #  空间列表-浏览企业空间-菜单栏-订单-确认发货-物流公司：点击
    def Kjlb_browseorgspace_menu_order_confirm_logisticsorg_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_order_confirm_logisticsorg)

    #  空间列表-浏览企业空间-菜单栏-订单-确认发货-物流公司-列表：点击
    def Kjlb_browseorgspace_menu_order_confirm_logisticsorg_list_click(self,n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_order_confirm_logisticsorg_list)

    #  空间列表-浏览企业空间-菜单栏-订单-确认发货-物流单号：发送文本
    def Kjlb_browseorgspace_menu_order_confirm_logisticsorgno_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_order_confirm_logisticsorg_list,text)

    #  空间列表-浏览企业空间-菜单栏-订单-确认发货-确定：点击
    def Kjlb_browseorgspace_menu_order_confirm_confirmsend_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_order_confirm_confirmsend)

# ***************************************【PAGE3】查看物流Kjlb_browseorgspace_menu_order_logistics_click***************************************
    #  空间列表-浏览企业空间-菜单栏-订单-查看物流-返回
    def Kjlb_browseorgspace_menu_order_logistics_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_order_logistics_back)

#***************************************【PAGE3】未发布产品列表Kjlb_browseorgspace_menu_product_unlock_list***************************************
     #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-加入购物车:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_shoppingcart_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_shoppingcart)

     #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-立即购买:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_buynow_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_buynow)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-客服:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_contactbusiness_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_contactbusiness)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-收藏:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_collection_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_collection)

     #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-分享:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_share_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_share)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-公司名:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_companyname_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_companyname)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-关联信息:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_right_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_right)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-关联信息-标签
    def Kjlb_browseorgspace_menu_product_unlock_list_right_tag_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_right_tag)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-产品参数:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_middle_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_middle)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-价格参数:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_left_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_left)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-更多价格:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_moreprice_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_moreprice)

    #  空间列表-浏览企业空间-菜单栏-产品-已发布-产品列表-更多价格-列表:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_moreprice_list_click(self,n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_product_unlock_list_moreprice_list,n)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-菜单栏:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_menu_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_menu)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-菜单栏-发布:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_menu_release_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_menu_release)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-菜单栏-发布-确定:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_menu_release_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_menu_release_confirm)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-菜单栏-编辑:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_menu_edit_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_menu_edit)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-菜单栏-删除:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_menu_delete_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_menu_delete)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-购物车图标:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_shopicon_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_shopicon)

    #  空间列表-浏览企业空间-菜单栏-产品-未发布-产品列表-返回:点击
    def Kjlb_browseorgspace_menu_product_unlock_list_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_unlock_list_back)

# ***************************************【PAGE3】新建Kjlb_browseorgspace_menu_product_new***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片:点击
    def Kjlb_browseorgspace_menu_product_new_addphoto_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_addphoto)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-相册:点击
    def Kjlb_browseorgspace_menu_product_new_addphoto_album_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_addphoto_album)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-拍照:点击
    def Kjlb_browseorgspace_menu_product_new_addphoto_takepic_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_addphoto_takepic)

     #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-产品库:点击
    def Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_addphoto_wifisync)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-取消:点击
    def Kjlb_browseorgspace_menu_product_new_addphoto_cancel_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_addphoto_cancel)

     #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称:点击
    def Kjlb_browseorgspace_menu_product_new_proname_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_proname)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性:点击
    def Kjlb_browseorgspace_menu_product_new_attribute_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_attribute)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面:点击
    def Kjlb_browseorgspace_menu_product_new_attrstone_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_attrstone)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-产品参数:点击
    def Kjlb_browseorgspace_menu_product_new_parameter_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_parameter)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-价格:点击
    def Kjlb_browseorgspace_menu_product_new_price_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_price)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-关联文件:点击
    def Kjlb_browseorgspace_menu_product_new_relation_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_relation)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-保存:点击
    def Kjlb_browseorgspace_menu_product_new_save_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_save)

    #  空间列表-浏览企业空间-菜单栏-产品-新建-发布:点击
    def Kjlb_browseorgspace_menu_product_new_release_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_release)

# ***************************************【PAGE3】【PAGE3】人事任免Kjlb_browseorgspace_menu_team_menu_assignjob***************************************
    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-返回:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_assignjob_back)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-搜索栏:发送文本
    def Kjlb_browseorgspace_menu_team_menu_assignjob_search_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_team_menu_assignjob_search,text)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-搜索按钮:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_assignjob_searchbtn)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_contact_click(self,n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact,n)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表:获取文本
    def Kjlb_browseorgspace_menu_team_menu_assignjob_contact_text(self, n):
        return self.p.get_texts(self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact, n)

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增:点击
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson)

# ***************************************【PAGE3】右上角新增按钮Kjlb_browseorgspace_menu_archivies_new***************************************
    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片:点击
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_addphoto)

     # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-相册:点击
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_album_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_addphoto_album)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-拍照:点击
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_takepic_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_addphoto_takepic)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-文件库:点击
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-取消:点击
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_cancel_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_addphoto_cancel)

     # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-照片统计:点击
    def Kjlb_browseorgspace_menu_archivies_new_count_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_count)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-标题:发送文本
    def Kjlb_browseorgspace_menu_archivies_new_title_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_archivies_new_title,text)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-类型:点击
    def Kjlb_browseorgspace_menu_archivies_new_type_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_type)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-类型-类型列表:点击
    def Kjlb_browseorgspace_menu_archivies_new_type_typelist_click(self,n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_archivies_new_type_typelist,n)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-类型-类型列表-企业身份列表:点击
    def Kjlb_browseorgspace_menu_archivies_new_type_typelist_orglist_click(self,n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_archivies_new_type_typelist_orglist,n)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-返回:点击
    def Kjlb_browseorgspace_menu_archivies_new_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_back)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-勾选按钮:点击
    def Kjlb_browseorgspace_menu_archivies_new_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_confirm)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-勾选按钮-保存:点击
    def Kjlb_browseorgspace_menu_archivies_new_confirm_late_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_confirm_save)

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-勾选按钮-保存并发布:点击
    def Kjlb_browseorgspace_menu_archivies_new_confirm_now_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_new_confirm_saveA)

# ***************************************【PAGE3】图片新增按钮Kjlb_browseorgspace_menu_archivies_picadd***************************************
    '''
        同上函数
    '''
# ***************************************【PAGE3】资讯图片列表Kjlb_browseorgspace_menu_archivies_pic***************************************
     # 空间列表-浏览企业空间-菜单栏-资讯-图片列表-图片-菜单栏:点击
    def Kjlb_browseorgspace_menu_archivies_pic_menu_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_pic_menu)

    # 空间列表-浏览企业空间-菜单栏-资讯-图片列表-图片-菜单栏-发布:点击
    def Kjlb_browseorgspace_menu_archivies_pic_menu_new_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_pic_menu_new)

    # 空间列表-浏览企业空间-菜单栏-资讯-图片列表-图片-菜单栏-发布-资讯类型:获取文本
    def Kjlb_browseorgspace_menu_archivies_pic_menu_new_type_text(self):
        return self.p.get_text(self.Kjlb_browseorgspace_menu_archivies_pic_type)

    # 空间列表-浏览企业空间-菜单栏-资讯-图片列表-图片-菜单栏-编辑:点击
    def Kjlb_browseorgspace_menu_archivies_pic_menu_edit_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_pic_menu_edit)

    # 空间列表-浏览企业空间-菜单栏-资讯-图片列表-图片-菜单栏-删除:点击
    def Kjlb_browseorgspace_menu_archivies_pic_menu_delete_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_pic_menu_delete)

    # 空间列表-浏览企业空间-菜单栏-资讯-图片列表-图片-菜单栏-删除:点击
    def Kjlb_browseorgspace_menu_archivies_pic_menu_offshelf_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_pic_menu_offshelf)

    # 空间列表-浏览企业空间-菜单栏-资讯-图片列表-图片-返回：点击
    def Kjlb_browseorgspace_menu_archivies_pic_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_archivies_pic_back)

# ***************************************【PAGE3】企业资信信息Kjlb_browseorgspace_menu_bcard_credit***************************************
    # 空间列表-浏览企业空间-菜单栏-企业名片-企业资信-社会认证:点击
    def Kjlb_browseorgspace_menu_bcard_credit_social_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_credit_social)

# ***************************************【PAGE3】菜单栏-附近商家Kjlb_browseorgspace_menu_bcard_menu_nearby***************************************
    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-附近商家--返回:点击
    def Kjlb_browseorgspace_menu_bcard_menu_nearby_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_nearby_back)

# ***************************************【PAGE3】菜单栏-编辑Kjlb_browseorgspace_menu_bcard_menu_edit***************************************

# ***************************************【PAGE3】菜单栏-设置Kjlb_browseorgspace_menu_bcard_menu_setting***************************************
     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-设置-返回:点击
    def Kjlb_browseorgspace_menu_bcard_menu_setting_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_setting_back)

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-设置-勾选框列表:点击
    def Kjlb_browseorgspace_menu_bcard_menu_setting_checkbox_click(self,n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_bcard_menu_setting_checkbox,n)

# ***************************************【PAGE3】菜单栏-关闭Kjlb_browseorgspace_menu_bcard_menu_close***************************************
      # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-关闭-是:点击
    def Kjlb_browseorgspace_menu_bcard_menu_close_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_close_confirm)

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-关闭-否:点击
    def Kjlb_browseorgspace_menu_bcard_menu_cancel_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_cancel)

# ***************************************【PAGE3】菜单栏-分享Kjlb_browseorgspace_menu_bcard_menu_share***************************************
     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享-资信:点击
    def Kjlb_browseorgspace_menu_bcard_menu_share_credit_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_share_credit)

      # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享-产品图片列表:点击
    def Kjlb_browseorgspace_menu_bcard_menu_share_product_click(self,n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_bcard_menu_share_product,n)

    # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享-勾选框列表:点击
    def Kjlb_browseorgspace_menu_bcard_menu_share_checkbox_click(self,n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_bcard_menu_share_checkbox,n)

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享-下一步:点击
    def Kjlb_browseorgspace_menu_bcard_menu_share_next_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_share_next)

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享-下一步-发送给微信好友:点击
    def Kjlb_browseorgspace_menu_bcard_menu_share_next_wechat_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_share_next_wechat)

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享-下一步-分享到朋友圈:点击
    def Kjlb_browseorgspace_menu_bcard_menu_share_next_circle_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_share_next_circle)

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享-下一步-QQ空间:点击
    def Kjlb_browseorgspace_menu_bcard_menu_share_next_qqspace_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_share_next_qqspace)

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享-下一步-qq:点击
    def Kjlb_browseorgspace_menu_bcard_menu_share_next_qq_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_share_next_qq)

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享-下一步-微博:点击
    def Kjlb_browseorgspace_menu_bcard_menu_share_next_weibo_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_share_next_weibo)

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享-下一步-取消:点击
    def Kjlb_browseorgspace_menu_bcard_menu_share_next_cancel_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_share_next_cancel)

     # 空间列表-浏览企业空间-菜单栏-企业名片-菜单栏-分享-返回:点击
    def Kjlb_browseorgspace_menu_bcard_menu_share_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_bcard_menu_share_back)

# ***************************************【PAGE3】菜单栏-+客户Kjlb_browseorgspace_menu_customer_menu_add***************************************
     # 空间列表-浏览企业空间-菜单栏-客户-菜单栏+客户-返回:点击
    def Kjlb_browseorgspace_menu_customer_menu_add_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu_add_back)

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏+客户-搜索框:发送文本
    def Kjlb_browseorgspace_menu_customer_menu_add_search_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_customer_menu_add_search,text)

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏+客户-搜索:点击
    def Kjlb_browseorgspace_menu_customer_menu_add_seek_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu_add_seek)

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏+客户-全选:点击
    def Kjlb_browseorgspace_menu_customer_menu_add_all_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu_add_all)

     # 空间列表-浏览企业空间-菜单栏-客户-菜单栏+客户-圆圈勾选列表:点击
    def Kjlb_browseorgspace_menu_customer_menu_add_choose_click(self,n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_customer_menu_add_choose,n)

    # 空间列表-浏览企业空间-菜单栏-客户-菜单栏-+客户-添加:点击
    def Kjlb_browseorgspace_menu_customer_menu_add_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_menu_add_confirm)

# ***************************************【PAGE3】客户列表Kjlb_browseorgspace_menu_customer_list***************************************
      # 空间列表-浏览企业空间-菜单栏-客户-客户列表-返回:点击
    def Kjlb_browseorgspace_menu_customer_clist_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_clist_back)

    # 空间列表-浏览企业空间-菜单栏-客户-客户列表-菜单栏:点击
    def Kjlb_browseorgspace_menu_customer_clist_menu_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_clist_menu)

    # 空间列表-浏览企业空间-菜单栏-客户-客户列表-菜单栏-名片设置:点击
    def Kjlb_browseorgspace_menu_customer_clist_menu_exchange_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_clist_menu_exchange)

     # 空间列表-浏览企业空间-菜单栏-客户-客户列表-机构列表:点击
    def Kjlb_browseorgspace_menu_customer_clist_olist_click(self,n):
        return self.p.clicks(self.Kjlb_browseorgspace_menu_customer_clist_olist,n)

    # 空间列表-浏览企业空间-菜单栏-客户-客户列表-对话框:发送文本
    def Kjlb_browseorgspace_menu_customer_clist_dialog_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseorgspace_menu_customer_clist_dialog,text)

    # 空间列表-浏览企业空间-菜单栏-客户-客户列表-发送:点击
    def Kjlb_browseorgspace_menu_customer_clist_send_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_clist_send)

    # 空间列表-浏览企业空间-菜单栏-客户-客户列表-发送-返回:点击
    def Kjlb_browseorgspace_menu_customer_clist_send_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_customer_clist_send_back)

# ***************************************【PAGE3】开启列表Kjlb_browseorgspace_menu_upgrade_open***************************************
      # 空间列表-浏览企业空间-菜单栏-业务升级-开启-返回:点击
    def Kjlb_browseorgspace_menu_upgrade_open_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_upgrade_open_back)

    # 空间列表-浏览企业空间-菜单栏-业务升级-开启-客户类型:点击
    def Kjlb_browseorgspace_menu_upgrade_open_customertype_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_upgrade_open_customertype)

    # 空间列表-浏览企业空间-菜单栏-业务升级-开启-确认定制:点击
    def Kjlb_browseorgspace_menu_upgrade_open_confirm_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_upgrade_open_confirm)

# ***************************************【PAGE3】菜单栏-分类到Kjlb_browseperspace_piclist_classify***************************************
    # 空间列表-浏览私人空间-照片列表-分类到-空间id
    def Kjlb_browseperspace_piclist_classify_spaceById_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_classifyspace_ByIdP)

    # 空间列表-浏览私人空间-照片列表-分类到-空间名
    def Kjlb_browseperspace_piclist_classify_spaceByName(self,name):
        return self.p.click(self.Kjlb_browseperspace_piclist_classify_spaceByName(name))

    # 空间列表-浏览私人空间-照片列表-分类到-返回
    def Kjlb_browseperspace_piclist_classify_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_classifyspace_back)

    # 空间列表-浏览私人空间-照片列表-分类到-勾选
    def Kjlb_browseperspace_piclist_classify_confirm_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_classifyspace_confirm)

    # 空间列表-浏览私人空间-照片列表-分类到-文件夹ById
    def Kjlb_browseperspace_piclist_classify_folderByID_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_classifyspace_folderByID)

    # 空间列表-浏览私人空间-照片列表-分类到-文件夹ByName
    def Kjlb_browseperspace_piclist_classify_folderByName(self,name):
        return self.p.click(self.Kjlb_browseperspace_piclist_classify_folderByNameP(name))

# ***************************************【PAGE3】菜单栏-编辑Kjlb_browseperspace_piclist_edit***************************************
      # 空间列表-浏览私人空间-照片列表-编辑-返回
    def Kjlb_browseperspace_piclist_edit_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_edit_back)

    # 空间列表-浏览私人空间-照片列表-编辑-删除
    def Kjlb_browseperspace_piclist_edit_delete_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_edit_delete)

    # 空间列表-浏览私人空间-照片列表-编辑-删除-是
    def Kjlb_browseperspace_piclist_edit_delete_confirm_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_edit_delete_confirm)

    # 空间列表-浏览私人空间-照片列表-编辑-删除-否
    def Kjlb_browseperspace_piclist_edit_delete_cancel_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_edit_delete_cancel)

    # 空间列表-浏览私人空间-照片列表-编辑-名称
    def Kjlb_browseperspace_piclist_edit_picname_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_edit_picname)

    # 空间列表-浏览私人空间-照片列表-编辑-备注
    def Kjlb_browseperspace_piclist_edit_remark_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_edit_remark)

    # 空间列表-浏览私人空间-照片列表-编辑-保存
    def Kjlb_browseperspace_piclist_edit_save_click(self):
        return self.p.click(self.Kjlb_browseperspace_piclist_edit_save)

# ***************************************【PAGE3】加数据-相册Kjlb_browseperspace_addData_ByAlbum***************************************
     # 空间列表-浏览私人空间-加数据-相册-完成
    def Kjlb_browseperspace_addData_ByAlbum_confirm_click(self):
        return self.p.click(self.Kjlb_browseperspace_addData_ByAlbum_confirm)

     # 空间列表-浏览私人空间-加数据-相册-完成-返回
    def Kjlb_browseperspace_addData_ByAlbum_confirm_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_addData_ByAlbum_confirm_back)

    # 空间列表-浏览私人空间-加数据-相册-返回
    def Kjlb_browseperspace_addData_ByAlbum_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_adata_ByAlbum_back)

    # 空间列表-浏览私人空间-加数据-相册-照片列表
    def Kjlb_browseperspace_addData_ByAlbum_piclist_click(self,n):
        return self.p.clicks(self.Kjlb_browseperspace_addData_ByAlbum_piclist,n)

# ***************************************【PAGE3】删除文件夹列表Kjlb_browseperspace_menu_edit_deletefolder***************************************
#     【PAGE4】照片列表
#     【PAGE4】删除
#     【PAGE4】删除-是
#     【PAGE4】删除-否

# ***************************************【PAGE3】菜单栏-+客户com.yunlu6.stone:id/btn_new_space***************************************
    # 空间列表-浏览私人空间-菜单栏-客户-菜单-+客户-添加
    def Kjlb_browseperspace_menu_customer_menu_addcus_add_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_menu_addcus_add)

    # 空间列表-浏览私人空间-菜单栏-客户-菜单-+客户-勾选框列表
    def Kjlb_browseperspace_menu_customer_menu_addcus_choose_click(self,n):
        return self.p.clicks(self.Kjlb_browseperspace_menu_customer_menu_addcus_choose,n)

     # 空间列表-浏览私人空间-菜单栏-客户-菜单-+客户-全选
    def Kjlb_browseperspace_menu_customer_menu_addcus_all_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_menu_addcus_all)

    # 空间列表-浏览私人空间-菜单栏-客户-菜单-+客户-搜索栏
    def Kjlb_browseperspace_menu_customer_menu_addcus_search_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_menu_addcus_search)

    # 空间列表-浏览私人空间-菜单栏-客户-菜单-+客户-搜索按钮
    def Kjlb_browseperspace_menu_customer_menu_addcus_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_menu_addcus_searchbtn)

    # 空间列表-浏览私人空间-菜单栏-客户-菜单-+客户-返回
    def Kjlb_browseperspace_menu_customer_menu_addcus_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_menu_addcus_back)

# ***************************************【PAGE3】客户列表Kjlb_browseperspace_menu_customer_clist***************************************
      # 空间列表-浏览私人空间-菜单栏-客户-客户列表-会话
    def Kjlb_browseperspace_menu_customer_clist_conversation_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_clist_conversation)

    # 空间列表-浏览私人空间-菜单栏-客户-客户列表-返回
    def Kjlb_browseperspace_menu_customer_clist_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_clist_back)

    # 空间列表-浏览私人空间-菜单栏-客户-客户列表-发送
    def Kjlb_browseperspace_menu_customer_clist_send_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_clist_send)

    # 空间列表-浏览私人空间-菜单栏-客户-客户列表-发送-返回
    def Kjlb_browseperspace_menu_customer_clist_send_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_clist_send_back)

    # 空间列表-浏览私人空间-菜单栏-客户-客户列表-空间列表
    def Kjlb_browseperspace_menu_customer_clist_slist_click(self,n):
        return self.p.clicks(self.Kjlb_browseperspace_menu_customer_clist_slist,n)

    # 空间列表-浏览私人空间-菜单栏-客户-客户列表-空间列表-返回
    def Kjlb_browseperspace_menu_customer_clist_slist_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_clist_slist_back)

# ***************************************【PAGE3】群聊Kjlb_browseperspace_menu_customer_gchat***************************************
      # 空间列表-浏览私人空间-菜单栏-客户-群聊-会话框
    def Kjlb_browseperspace_menu_customer_gchat_conversation_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_gchat_conversation)

    # 空间列表-浏览私人空间-菜单栏-客户-群聊-发送
    def Kjlb_browseperspace_menu_customer_gchat_sned_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_gchat_sned)

    # 空间列表-浏览私人空间-菜单栏-客户-群聊-返回
    def Kjlb_browseperspace_menu_customer_gchat_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_menu_customer_gchat_back)

# ***************************************【PAGE3】相册Kjlb_browseperspace_adata_ByAlbum***************************************
     # 空间列表-浏览私人空间-加数据-相册-照片列表
    def Kjlb_browseperspace_adata_ByAlbum_piclist_click(self,n):
        return self.p.clicks(self.Kjlb_browseperspace_adata_ByAlbum_piclist,n)

    # 空间列表-浏览私人空间-加数据-相册-返回
    def Kjlb_browseperspace_adata_ByAlbum_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_adata_ByAlbum_back)

    # 空间列表-浏览私人空间-加数据-相册-完成
    def Kjlb_browseperspace_adata_ByAlbum_confirm_click(self):
        return self.p.click(self.Kjlb_browseperspace_adata_ByAlbum_confirm)

# ***************************************【PAGE3】照片列表Kjlb_browseperspace_more_piclist***************************************
   # 空间列表-浏览私人空间-更多-照片列表-分类到
    def Kjlb_browseperspace_more_piclist_classify_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_classify)

    # 空间列表-浏览私人空间-更多-照片列表-编辑
    def Kjlb_browseperspace_more_piclist_edit_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_edit)

     # 空间列表-浏览私人空间-更多-照片列表-返回
    def Kjlb_browseperspace_more_piclist_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_back)

    # 空间列表-浏览私人空间-更多-照片列表-照片本身
    def Kjlb_browseperspace_more_piclist_itself_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_piclist_itself)

# ***************************************【PAGE3】菜单栏-上传-相册Kjlb_browseperspace_more_menu_upload_ByAlbum***************************************
    # 空间列表-浏览私人空间-更多-菜单栏-上传-相册-返回
    def Kjlb_browseperspace_more_menu_upload_ByAlbum_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_upload_ByAlbum_back)

    # 空间列表-浏览私人空间-更多-菜单栏-上传-相册-照片列表
    def Kjlb_browseperspace_more_menu_upload_ByAlbum_piclist_click(self,n):
        return self.p.clicks(self.Kjlb_browseperspace_more_menu_upload_ByAlbum_piclist,n)

   # 空间列表-浏览私人空间-更多-菜单栏-上传-相册-完成
    def Kjlb_browseperspace_more_menu_upload_ByAlbum_confirm_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_upload_ByAlbum_confirm)

# ***************************************【PAGE3】菜单栏-编辑Kjlb_browseperspace_more_menu_edit***************************************
     # 空间列表-浏览私人空间-更多-菜单栏-编辑-返回
    def Kjlb_browseperspace_more_menu_edit_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_edit_back)

     # 空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹列表
    def Kjlb_browseperspace_more_menu_edit_deletefolder_click(self,n):
        return self.p.clicks(self.Kjlb_browseperspace_more_menu_edit_deletefolder,n)

    # 空间列表-浏览私人空间-更多-菜单栏-编辑-修改文件夹名称
    def Kjlb_browseperspace_more_menu_edit_foldername_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_edit_foldername)

    # 空间列表-浏览私人空间-更多-菜单栏-编辑-空间类型
    def Kjlb_browseperspace_more_menu_edit_spacetype_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_spacetypeP)

     # 空间列表-浏览私人空间-更多-菜单栏-编辑-空间类型-选择空间类型
    def Kjlb_browseperspace_more_menu_edit_spacetype_choosetype_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_spacetype_choosetype)

    # 空间列表-浏览私人空间-更多-菜单栏-编辑-修改空间名按钮
    def Kjlb_browseperspace_more_menu_edit_editsbtn_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_editsbtn)

    # 空间列表-浏览私人空间-更多-菜单栏-编辑-修改空间名按钮-空间名称
    def Kjlb_browseperspace_more_menu_edit_editsbtn_sname_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_editsbtn_sname)

# ***************************************【PAGE3】菜单栏-排序Kjlb_browseperspace_more_menu_sort***************************************
     # 空间列表-浏览私人空间-更多-菜单栏-排序-返回
    def Kjlb_browseperspace_more_menu_sort_back_click(self):
        return self.p.click(self.Kjlb_browseperspace_more_menu_sort_back)

    # 空间列表-浏览私人空间-更多-菜单栏-排序-照片列表
    def Kjlb_browseperspace_more_menu_sort_piclist_click(self,n):
        return self.p.clicks(self.Kjlb_browseperspace_more_menu_sort_piclist,n)

# ***************************************【PAGE3】企业列表Kjlb_browseascspace_ovip_olist***************************************
    # 空间列表-浏览协会空间-菜单栏-会员-企业名录-企业名列表-返回:点击
    def Kjlb_browseascspace_menu_vip_companylist_companyname_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_companylist_companyname_back)

# ***************************************【PAGE3】人脉列表Kjlb_browseascspace_pvip_plist***************************************
    # 空间列表-协会空间-个人会员-人脉列表-人脉页面返回
    def Kjlb_browseascspace_pvip_plist_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_pvip_plist_back)

# ***************************************【PAGE3】资讯文件列表Kjlb_browseascspace_arch_alist***************************************
     # 空间列表-协会空间-资讯-资讯文件列表-资讯图片
    def Kjlb_browseascspace_arch_alist_pic_click(self):
        return self.p.click(self.Kjlb_browseascspace_arch_alist_pic)

    # 空间列表-协会空间-资讯-资讯文件列表-返回
    def Kjlb_browseascspace_arch_alist_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_arch_alist_back)

 # ***************************************【PAGE3】Logo：Kjlb_browseascspace_menu_edit_logo***************************************
    # 空间列表-浏览协会空间-菜单栏-编辑-Logo-相册:点击
    def Kjlb_browseascspace_menu_edit_logo_album_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_logo_album)

    # 空间列表-浏览协会空间-菜单栏-编辑-Logo-拍照:点击
    def Kjlb_browseascspace_menu_edit_logo_takepic_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_logo_takepic)

    # 空间列表-浏览协会空间-菜单栏-编辑-Logo-取消:点击
    def Kjlb_browseascspace_menu_edit_logo_cancel_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_edit_logo_cancel)

 # ***************************************【PAGE3】菜单栏-人事任免Kjlb_browseascspace_menu_team_menu_assignjob***************************************
    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-返回:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_back)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-搜索栏:发送文本
    def Kjlb_browseascspace_menu_team_menu_assignjob_search_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_team_menu_assignjob_search,text)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-搜索按钮:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_searchbtn)

     # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_click(self,n):
        return self.p.clicks(self.Kjlb_browseascspace_menu_team_menu_assignjob_contact,n)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增:点击
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson)

 # ***************************************【PAGE3】菜单栏-我的部门Kjlb_browseascspace_menu_team_menu_mydepartment***************************************
    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门-返回:点击
    def Kjlb_browseascspace_menu_team_menu_mydepartment_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_mydepartment_back)

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-我的部门-搜索:点击
    def Kjlb_browseascspace_menu_team_menu_mydepartment_seek_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_team_menu_mydepartment_seek)

 # ***************************************【PAGE3】企业名录-企业名录列表Kjlb_browseascspace_menu_vip_companylist_companyname***************************************
    # 空间列表-浏览协会空间-菜单栏-会员-企业名录-企业名列表-返回:点击
    def Kjlb_browseascspace_menu_vip_companylist_companyname_backO_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_companylist_companyname_backA)

 # ***************************************【PAGE3】个人名录-个人名录列表Kjlb_browseascspace_menu_vip_personlist_personname***************************************
     # 空间列表-浏览协会空间-菜单栏-会员-个人名录-个人名列表-返回
    def Kjlb_browseascspace_menu_vip_personlist_personname_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_personlist_personname_back)

# ***************************************【PAGE3】菜单栏-+会员Kjlb_browseascspace_menu_vip_menu_addvip***************************************
    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-返回:点击
    def Kjlb_browseascspace_menu_vip_menu_addvip_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_addvip_back)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-搜索栏:发送文本
    def Kjlb_browseascspace_menu_vip_menu_addvip_search_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_vip_menu_addvip_search,text)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-搜索按钮:点击
    def Kjlb_browseascspace_menu_vip_menu_addvip_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_addvip_searchbtn)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-圆圈勾选&个人:点击
    def Kjlb_browseascspace_menu_vip_menu_addvip_chooseperson_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_addvip_chooseperson)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-圆圈勾选&企业:点击
    def Kjlb_browseascspace_menu_vip_menu_addvip_choosecompany_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_addvip_choosecompany)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-全选:点击
    def Kjlb_browseascspace_menu_vip_menu_addvip_all_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_addvip_all)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-加会员-添加:点击
    def Kjlb_browseascspace_menu_vip_menu_addvip_confirm_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_addvip_confirm)

# ***************************************【PAGE3】菜单栏-管理-编辑Kjlb_browseascspace_menu_vip_menu_manage_edit***************************************
    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-同意:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_agree_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_edit_agree)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-拒绝:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_refuse_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_edit_refuse)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-移除:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_delete_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_edit_delete)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-取消:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_cancel_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_vip_menu_manage_edit_cancel)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-圆圈勾选&个人:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_chooseperson_click(self,n):
        return self.p.clicks(self.Kjlb_browseascspace_menu_vip_menu_manage_edit_chooseperson,n)

    # 空间列表-浏览协会空间-菜单栏-会员-菜单栏-管理-编辑-圆圈勾选&企业:点击
    def Kjlb_browseascspace_menu_vip_menu_manage_edit_choosecompany_click(self,n):
        return self.p.clicks(self.Kjlb_browseascspace_menu_vip_menu_manage_edit_choosecompany,n)

# ***************************************【PAGE3】菜单栏-我的附近Kjlb_browseascspace_menu_addvip_addcompany_nearby***************************************
    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-路线:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_route_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_route)

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-路线-返回:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_route_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_route_back)

     #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-返回:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_back_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_back)

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-搜索栏:发送文本
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_search_sendkeys(self,text):
        return self.p.send_keys(self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_search,text)

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-搜索按钮:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_searchbtn_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_searchbtn)

    #定位:空间列表-浏览协会空间-菜单栏-加会员-企业会员-我的附近-确定:点击
    def Kjlb_browseascspace_menu_addvip_addcompany_nearby_confirm_click(self):
        return self.p.click(self.Kjlb_browseascspace_menu_addvip_addcompany_nearby_confirm)

# ***************************************【PAGE3】菜单栏-浏览记录Kjlb_browseascspace_menu_history ***************************************
    #定位:空间列表-浏览协会空间-菜单栏-浏览记录-返回
    def Kjlb_browseascspace_menu_history_back_click(self):
        return  self.p.click(self.Kjlb_browseascspace_menu_history_back)