__author__ = 'xiaoj'
#空间首页
from StoneUIFramework.public.pages.space.SPACEPAGE4 import _SPACEPAGE4
class _SPACEPAGE5(_SPACEPAGE4):
#***************************************【PAGE4】添加照片-相册Kjlb_browseorgspace_menu_product_new_addphoto_album***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-相册-返回
    def Kjlb_browseorgspace_menu_product_new_addphoto_album_back(self):
        self.Kjlb_browseorgspace_menu_product_new_addphoto_album_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_edit_icon","空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-相册-返回")
        return self.Kjlb_browseorgspace_menu_product_new_addphoto_album_backP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-相册-照片列表
    def Kjlb_browseorgspace_menu_product_new_addphoto_album_list(self):
        self.Kjlb_browseorgspace_menu_product_new_addphoto_album_listP = self.p.get_elements("id->com.yunlu6.stone:id/item_cloudlibrary_ll_checked","空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-相册-照片列表")
        return self.Kjlb_browseorgspace_menu_product_new_addphoto_album_listP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-相册-完成
    def Kjlb_browseorgspace_menu_product_new_addphoto_album_confirm(self):
        self.Kjlb_browseorgspace_menu_product_new_addphoto_album_confirmP = self.p.get_element("id->com.yunlu6.stone:id/title_tv_edit_menu_tv","空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-相册-完成")
        return self.Kjlb_browseorgspace_menu_product_new_addphoto_album_confirmP

#***************************************【PAGE4】添加照片-产品库Kjlb_browseorgspace_menu_product_new_addphoto_wifisync***************************************
     #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-产品库-返回
    def Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_back(self):
        self.Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_back = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-产品库-返回")
        return self.Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_back

    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-产品库-全选
    def Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_all(self):
        self.Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_allP = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-产品库-全选")
        return self.Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_allP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-产品库-照片列表
    def Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_piclist(self):
        self.Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_piclist = self.p.get_elements("id->com.yunlu6.stone:id/item_cloudlibrary_ll_checked","空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-产品库-照片列表")
        return self.Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_piclist

    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-产品库-确定
    def Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_confirm(self):
        self.Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_confirmP = self.p.get_elements("id->com.yunlu6.stone:id/product_rest_yes","空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-产品库-照片列表")
        return self.Kjlb_browseorgspace_menu_product_new_addphoto_wifisync_confirmP

#***************************************【PAGE4】商品名称Kjlb_browseorgspace_menu_product_new_proname***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-返回
    def Kjlb_browseorgspace_menu_product_new_proname_back(self):
        self.Kjlb_browseorgspace_menu_product_new_proname_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-返回")
        return self.Kjlb_browseorgspace_menu_product_new_proname_backP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-勾选
    def Kjlb_browseorgspace_menu_product_new_proname_choose(self):
        self.Kjlb_browseorgspace_menu_product_new_proname_chooseP = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-勾选")
        return self.Kjlb_browseorgspace_menu_product_new_proname_chooseP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-商品名称
    def Kjlb_browseorgspace_menu_product_new_proname_name(self):
        self.Kjlb_browseorgspace_menu_product_new_proname_nameP = self.p.get_element("id->com.yunlu6.stone:id/et_name","空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-商品名称")
        return self.Kjlb_browseorgspace_menu_product_new_proname_nameP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-商品顶部标题
    def Kjlb_browseorgspace_menu_product_new_proname_name_title(self):
        self.Kjlb_browseorgspace_menu_product_new_proname_name_titleP = self.p.get_element("id->com.yunlu6.stone:id/title_tv_title","空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-商品顶部标题")
        return self.Kjlb_browseorgspace_menu_product_new_proname_name_titleP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-分类输入框（云庐用）
    def Kjlb_browseorgspace_menu_product_new_proname_yclassify(self):
        self.Kjlb_browseorgspace_menu_product_new_proname_yclassifyP = self.p.get_element("id->com.yunlu6.stone:id/et_classify","空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-分类输入框")
        return self.Kjlb_browseorgspace_menu_product_new_proname_yclassifyP

    #  空浏览企业空间-菜单栏-产品-新建-商品名称-推荐标签（云庐用）
    def Kjlb_browseorgspace_menu_product_new_proname_ytag(self):
        self.Kjlb_browseorgspace_menu_product_new_proname_ytagP = self.p.get_elements("id->com.yunlu6.stone:id/tag_id","空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-推荐标签")
        return self.Kjlb_browseorgspace_menu_product_new_proname_ytagP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-分类（百石堂）
    def Kjlb_browseorgspace_menu_product_new_proname_bclassify(self):
        self.Kjlb_browseorgspace_menu_product_new_proname_bclassifyP = self.p.get_element("id->com.yunlu6.stone:id/et_classify","空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-分类")
        return self.Kjlb_browseorgspace_menu_product_new_proname_bclassifyP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-推荐一级标签（百石堂）
    def Kjlb_browseorgspace_menu_product_new_proname_bonetag(self):
        self.Kjlb_browseorgspace_menu_product_new_proname_bonetag = self.p.get_elements("id->com.yunlu6.stone:id/item_cate_tv","空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-推荐标签")
        return self.Kjlb_browseorgspace_menu_product_new_proname_bonetag

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-推荐二级标签（百石堂）
    def Kjlb_browseorgspace_menu_product_new_proname_btwotag(self):
        self.Kjlb_browseorgspace_menu_product_new_proname_btwotagP = self.p.get_elements("id->com.yunlu6.stone:id/tv_name","空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-推荐标签")
        return self.Kjlb_browseorgspace_menu_product_new_proname_btwotagP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-确定（百石堂）
    def Kjlb_browseorgspace_menu_product_new_proname_confirm(self):
        self.Kjlb_browseorgspace_menu_product_new_proname_confirmP = self.p.get_element("id->com.yunlu6.stone:id/title_tv_edit","空间列表-浏览企业空间-菜单栏-产品-新建-商品名称-确定")
        return self.Kjlb_browseorgspace_menu_product_new_proname_confirmP

#***************************************【PAGE4】石种属性Kjlb_browseorgspace_menu_product_new_attribute***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-返回
    def Kjlb_browseorgspace_menu_product_new_attribute_back(self):
        self.Kjlb_browseorgspace_menu_product_new_attribute_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-返回")
        return self.Kjlb_browseorgspace_menu_product_new_attribute_backP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-勾选
    def Kjlb_browseorgspace_menu_product_new_attribute_confirm(self):
        self.Kjlb_browseorgspace_menu_product_new_attribute_confirmP = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-勾选")
        return self.Kjlb_browseorgspace_menu_product_new_attribute_confirmP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-种类名
    def Kjlb_browseorgspace_menu_product_new_attribute_species(self):
        self.Kjlb_browseorgspace_menu_product_new_attribute_speciesP = self.p.get_element("id->com.yunlu6.stone:id/species_name","空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-种类名")
        return self.Kjlb_browseorgspace_menu_product_new_attribute_speciesP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-种类名-匹配
    def Kjlb_browseorgspace_menu_product_new_attribute_species_match(self):
        self.Kjlb_browseorgspace_menu_product_new_attribute_species_matchP = self.p.get_elements("id->com.yunlu6.stone:id/tv","空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-种类名-匹配")
        return self.Kjlb_browseorgspace_menu_product_new_attribute_species_matchP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-颜色
    def Kjlb_browseorgspace_menu_product_new_attribute_color(self):
        self.Kjlb_browseorgspace_menu_product_new_attribute_colorP = self.p.get_element("id->com.yunlu6.stone:id/tv_color_name","空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-颜色")
        return self.Kjlb_browseorgspace_menu_product_new_attribute_colorP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-颜色-列表
    def Kjlb_browseorgspace_menu_product_new_attribute_color_list(self):
        self.Kjlb_browseorgspace_menu_product_new_attribute_color_listP = self.p.get_elements("id->android:id/text1","空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-颜色-列表")
        return self.Kjlb_browseorgspace_menu_product_new_attribute_color_listP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-深浅
    def Kjlb_browseorgspace_menu_product_new_attribute_attrname(self):
        self.Kjlb_browseorgspace_menu_product_new_attribute_attrnameP = self.p.get_element("id->com.yunlu6.stone:id/tv_attr_name","空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-深浅")
        return self.Kjlb_browseorgspace_menu_product_new_attribute_attrnameP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-深浅-列表
    def Kjlb_browseorgspace_menu_product_new_attribute_attrname_list(self):
        self.Kjlb_browseorgspace_menu_product_new_attribute_attrname_listP = self.p.get_elements("id->android:id/text1","空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-深浅-列表")
        return self.Kjlb_browseorgspace_menu_product_new_attribute_attrname_listP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-花纹
    def Kjlb_browseorgspace_menu_product_new_attribute_pattern(self):
        self.Kjlb_browseorgspace_menu_product_new_attribute_patternP = self.p.get_element("id->com.yunlu6.stone:id/tv_pattern_name","空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-花纹")
        return self.Kjlb_browseorgspace_menu_product_new_attribute_patternP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-花纹-列表
    def Kjlb_browseorgspace_menu_product_new_attribute_pattern_list(self):
        self.Kjlb_browseorgspace_menu_product_new_attribute_pattern_listP = self.p.get_elements("id->android:id/text1","空间列表-浏览企业空间-菜单栏-产品-新建-石种属性-花纹-列表")
        return self.Kjlb_browseorgspace_menu_product_new_attribute_pattern_listP

#***************************************【PAGE4】制品/表面Kjlb_browseorgspace_menu_product_new_attrstone***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-返回
    def Kjlb_browseorgspace_menu_product_new_attrstone_back(self):
        self.Kjlb_browseorgspace_menu_product_new_attrstone_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-返回")
        return self.Kjlb_browseorgspace_menu_product_new_attrstone_backP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-勾选
    def Kjlb_browseorgspace_menu_product_new_attrstone_confirm(self):
        self.Kjlb_browseorgspace_menu_product_new_attrstone_confirmP = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-勾选")
        return self.Kjlb_browseorgspace_menu_product_new_attrstone_confirmP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-制品
    def Kjlb_browseorgspace_menu_product_new_attrstone_type(self):
        self.Kjlb_browseorgspace_menu_product_new_attrstone_typeP = self.p.get_element("id->com.yunlu6.stone:id/tv_type","空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-制品")
        return self.Kjlb_browseorgspace_menu_product_new_attrstone_typeP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-制品-列表
    def Kjlb_browseorgspace_menu_product_new_attrstone_type_list(self):
        self.Kjlb_browseorgspace_menu_product_new_attrstone_type_listP = self.p.get_elements("id->android:id/text1","空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-制品-列表")
        return self.Kjlb_browseorgspace_menu_product_new_attrstone_type_listP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-表面
    def Kjlb_browseorgspace_menu_product_new_attrstone_surface(self):
        self.Kjlb_browseorgspace_menu_product_new_attrstone_surfaceP = self.p.get_element("id->com.yunlu6.stone:id/tv_surface","空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-表面")
        return self.Kjlb_browseorgspace_menu_product_new_attrstone_surfaceP

    #  空浏览企业空间-菜单栏-产品-新建-制品/表面-表面-列表
    def Kjlb_browseorgspace_menu_product_new_attrstone_surface_list(self):
        self.Kjlb_browseorgspace_menu_product_new_attrstone_surface_listP = self.p.get_elements("id->android:id/text1","空间列表-浏览企业空间-菜单栏-产品-新建-制品/表面-表面")
        return self.Kjlb_browseorgspace_menu_product_new_attrstone_surface_listP

#***************************************【PAGE4】产品参数Kjlb_browseorgspace_menu_product_new_parameter***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-返回
    def Kjlb_browseorgspace_menu_product_new_parameter_back(self):
        self.Kjlb_browseorgspace_menu_product_new_parameter_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-返回")
        return self.Kjlb_browseorgspace_menu_product_new_parameter_backP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-勾选
    def Kjlb_browseorgspace_menu_product_new_parameter_confirm(self):
        self.Kjlb_browseorgspace_menu_product_new_parameter_confirmP = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-返回")
        return self.Kjlb_browseorgspace_menu_product_new_parameter_confirmP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-参数名列表
    def Kjlb_browseorgspace_menu_product_new_parameter_key(self):
        self.Kjlb_browseorgspace_menu_product_new_parameter_keylistP = self.p.get_elements("id->com.yunlu6.stone:id/et_key","空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-参数名")
        return self.Kjlb_browseorgspace_menu_product_new_parameter_keylistP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-参数值
    def Kjlb_browseorgspace_menu_product_new_parameter_value(self):
        self.Kjlb_browseorgspace_menu_product_new_parameter_valuelistP = self.p.get_elements("id->com.yunlu6.stone:id/et_value","空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-参数值")
        return self.Kjlb_browseorgspace_menu_product_new_parameter_valuelistP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-添加按钮
    def Kjlb_browseorgspace_menu_product_new_parameter_addbtn(self):
        self.Kjlb_browseorgspace_menu_product_new_parameter_addbtnP = self.p.get_elements("id->com.yunlu6.stone:id/iv_add_attr","空间列表-浏览企业空间-菜单栏-产品-新建-产品参数-添加按钮")
        return self.Kjlb_browseorgspace_menu_product_new_parameter_addbtnP

#***************************************【PAGE4】价格Kjlb_browseorgspace_menu_product_new_price***************************************
   #  空间列表-浏览企业空间-菜单栏-产品-新建-价格-返回
    def Kjlb_browseorgspace_menu_product_new_price_back(self):
        self.Kjlb_browseorgspace_menu_product_new_price_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览企业空间-菜单栏-产品-新建-返回")
        return self.Kjlb_browseorgspace_menu_product_new_price_backP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-价格-单价(元)
    def Kjlb_browseorgspace_menu_product_new_price_unitprice(self):
        self.Kjlb_browseorgspace_menu_product_new_price_unitpriceyuanP = self.p.get_elements("id->com.yunlu6.stone:id/et_conten" ,"空间列表-浏览企业空间-菜单栏-产品-新建-价格-单价(元)")
        return self.Kjlb_browseorgspace_menu_product_new_price_unitpriceyuanP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-价格-库存
    def Kjlb_browseorgspace_menu_product_new_price_stock(self):
        self.Kjlb_browseorgspace_menu_product_new_price_stockkucunP = self.p.get_elements("id->com.yunlu6.stone:id/et_conten","空间列表-浏览企业空间-菜单栏-产品-新建-价格-库存")
        return self.Kjlb_browseorgspace_menu_product_new_price_stockkucunP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-价格-保存
    def Kjlb_browseorgspace_menu_product_new_price_save(self):
        self.Kjlb_browseorgspace_menu_product_new_price_saveP = self.p.get_element("id->com.yunlu6.stone:id/bt_sure_offer","空间列表-浏览企业空间-菜单栏-产品-新建-价格-保存")
        return self.Kjlb_browseorgspace_menu_product_new_price_saveP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-价格-新价
    def Kjlb_browseorgspace_menu_product_new_price_add(self):
        self.Kjlb_browseorgspace_menu_product_new_price_addP = self.p.get_element("id->com.yunlu6.stone:id/bt_add_offer","空间列表-浏览企业空间-菜单栏-产品-新建-价格")
        return self.Kjlb_browseorgspace_menu_product_new_price_addP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-价格-删除
    def Kjlb_browseorgspace_menu_product_new_price_delete(self):
        self.Kjlb_browseorgspace_menu_product_new_price_deleteP = self.p.get_element("id->com.yunlu6.stone:id/bt_delete_offer","空间列表-浏览企业空间-菜单栏-产品-新建-价格-删除")
        return self.Kjlb_browseorgspace_menu_product_new_price_deleteP

#***************************************【PAGE4】关联文件Kjlb_browseorgspace_menu_product_new_relation***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-关联文件-返回
    def Kjlb_browseorgspace_menu_product_new_relation_back(self):
        self.Kjlb_browseorgspace_menu_product_new_relation_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览企业空间-菜单栏-产品-新建-关联文件-返回")
        return self.Kjlb_browseorgspace_menu_product_new_relation_backP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-关联文件-选择照片/添加照片
    def Kjlb_browseorgspace_menu_product_new_relation_photo(self):
        self.Kjlb_browseorgspace_menu_product_new_relation_photoP = self.p.get_elements("id->com.yunlu6.stone:id/iv_relate_photo","空间列表-浏览企业空间-菜单栏-产品-新建-关联文件-选择照片/添加照片")
        return self.Kjlb_browseorgspace_menu_product_new_relation_photoP

    #  空间列表-浏览企业空间-菜单栏-产品-新建-关联文件-已关联项
    def Kjlb_browseorgspace_menu_product_new_relation_related(self):
        self.Kjlb_browseorgspace_menu_product_new_relation_relatedP = self.p.get_elements("id->com.yunlu6.stone:id/tv_related_name","空间列表-浏览企业空间-菜单栏-产品-新建-关联文件-已关联项")
        return self.Kjlb_browseorgspace_menu_product_new_relation_relatedP

#***************************************【PAGE4】待任免联系人列表Kjlb_browseorgspace_menu_team_menu_assignjob_contact***************************************
    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-返回
    def Kjlb_browseorgspace_menu_team_menu_assignjob_contact_back(self):
        self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_backT = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-返回")
        return self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_backT

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-确认
    def Kjlb_browseorgspace_menu_team_menu_assignjob_contact_confirm(self):
        self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_confirmT = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-确认")
        return self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_confirmT

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-部门名称
    def Kjlb_browseorgspace_menu_team_menu_assignjob_contact_department(self):
        self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_departmentT = self.p.get_elements("id->com.yunlu6.stone:id/setjobs_unassi_jobname","空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-部门名称")
        return self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_departmentT

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-职位名称
    def Kjlb_browseorgspace_menu_team_menu_assignjob_contact_jobname(self):
        self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_jobname = self.p.get_elements("id->com.yunlu6.stone:id/tag_id","空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-职位名称")
        return self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_jobname

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-移除
    def Kjlb_browseorgspace_menu_team_menu_assignjob_contact_delete(self):
        self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_deleteT = self.p.get_element("id->com.yunlu6.stone:id/setjobs_dele","空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-联系人列表-移除")
        return self.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_deleteT

#***************************************【PAGE4】人事任免新增Kjlb_browseorgspace_menu_team_menu_assignjob_addperson***************************************
    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-返回
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_back(self):
        self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_back = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-返回")
        return self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_back

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-搜索栏
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_search(self):
        self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_search = self.p.get_element("id->com.yunlu6.stone:id/img_btn_search","空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-搜索栏")
        return self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_search

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-搜索按钮(实际是人脉列表确定)
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_searchbtn(self):
        self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_searchbtn = self.p.get_element("id->com.yunlu6.stone:id/iv_search","空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-搜索按钮")
        return self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_searchbtn

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-全选
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_all(self):
        self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_all = self.p.get_element("id->com.yunlu6.stone:id/title_main_tv_more_tv","空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-全选")
        return self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_all

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-圆圈勾选
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_choose(self):
        self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_chooseT = self.p.get_elements("id->com.yunlu6.stone:id/item_client_tv_checked","空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-圆圈勾选")
        return self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_chooseT

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-联系人列表
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_contact(self):
        self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_contact = self.p.get_elements("id->com.yunlu6.stone:id/item_client_username_tv","空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-联系人列表")
        return self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_contact

    # 空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-添加(确认)
    def Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_confirm(self):
        self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_confirm = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_client_operate","空间列表-浏览企业空间-菜单栏-团队-菜单栏-人事任免-新增-添加")
        return self.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_confirm

#***************************************【PAGE4】添加照片-相册Kjlb_browseorgspace_menu_archivies_new_addphoto_album***************************************
     # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-文件库-照片列表
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_list(self):
        self.Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_list = self.p.get_elements("id->com.yunlu6.stone:id/item_cloudlibrary_ll_checked","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-文件库-照片列表")
        return self.Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_list

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-文件库-全选
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_all(self):
        self.Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_all = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-文件库-全选")
        return self.Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_all

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-文件库-确定
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_confirm(self):
        self.Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_confirm = self.p.get_element("id->com.yunlu6.stone:id/product_rest_yes","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-文件库-确定")
        return self.Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_confirm

#***************************************【PAGE4】照片统计按钮Kjlb_browseorgspace_menu_archivies_new_count***************************************
    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-文件照片列表
    def Kjlb_browseorgspace_menu_archivies_new_count_list(self):
        self.Kjlb_browseorgspace_menu_archivies_new_count_list = self.p.get_element("id->com.yunlu6.stone:id/drag_list_item_image","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-照片统计-文件照片列表")
        return self.Kjlb_browseorgspace_menu_archivies_new_count_list

#***************************************【PAGE4】添加照片-相册Kjlb_browseorgspace_menu_archivies_new_addphoto_album***************************************
     # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-相册-照片列表
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_album_list(self):
        self.Kjlb_browseorgspace_menu_archivies_new_addphoto_album_list = self.p.get_elements("id->com.yunlu6.stone:id/item_cloudlibrary_ll_checked","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-相册-照片列表")
        return self.Kjlb_browseorgspace_menu_archivies_new_addphoto_album_list

    # 空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-相册-完成
    def Kjlb_browseorgspace_menu_archivies_new_addphoto_album_confirm(self):
        self.Kjlb_browseorgspace_menu_archivies_new_addphoto_album_confirm = self.p.get_element("id->com.yunlu6.stone:id/title_tv_edit_menu_tv","空间列表-浏览企业空间-菜单栏-资讯-新增按钮-添加照片-相册-完成")
        return self.Kjlb_browseorgspace_menu_archivies_new_addphoto_album_confirm

#***************************************【PAGE4】添加照片-文件库Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync***************************************
    # 照片列表Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_list
    # 全选Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_all
    # 确定Kjlb_browseorgspace_menu_archivies_new_addphoto_wifisync_confirm

#***************************************【PAGE4】分类到Kjlb_browseperspace_more_piclist_classify***************************************
    # 空间列表-浏览私人空间-更多-照片列表-分类到-空间id
    def Kjlb_browseperspace_more_piclist_classify_spaceById(self):
        self.Kjlb_browseperspace_more_piclist_classifyspace_ByIdP = self.p.get_elements("id->com.yunlu6.stone:id/image","空间列表-浏览私人空间-更多-照片列表-分类到-空间ById")
        return self.Kjlb_browseperspace_more_piclist_classifyspace_ByIdP

     # 空间列表-浏览私人空间-更多-照片列表-分类到-空间名
    def Kjlb_browseperspace_more_piclist_classify_spaceByName(self,name):
        self.Kjlb_browseperspace_more_piclist_classify_spaceByNameP = self.p.get_element("name->%s"%name,"空间列表-浏览私人空间-更多-照片列表-分类到-空间ByName")
        return self.Kjlb_browseperspace_more_piclist_classify_spaceByNameP

    # 空间列表-浏览私人空间-更多-照片列表-分类到-返回
    def Kjlb_browseperspace_more_piclist_classify_back(self):
        self.Kjlb_browseperspace_more_piclist_classifyspace_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览私人空间-更多-照片列表-分类到-返回")
        return self.Kjlb_browseperspace_more_piclist_classifyspace_backP

    # 空间列表-浏览私人空间-更多-照片列表-分类到-勾选
    def Kjlb_browseperspace_more_piclist_classify_confirm(self):
        self.Kjlb_browseperspace_more_piclist_classifyspace_confirmP = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览私人空间-更多-照片列表-分类到-勾选")
        return self.Kjlb_browseperspace_more_piclist_classifyspace_confirmP

    # 空间列表-浏览私人空间-更多-照片列表-分类到-文件夹ById
    def Kjlb_browseperspace_more_piclist_classify_folderByID(self):
        self.Kjlb_browseperspace_more_piclist_classifyspace_folderByIDP = self.p.get_element("id->com.yunlu6.stone:id/tv_name","空间列表-浏览私人空间-更多-照片列表-分类到-文件夹ByID")
        return self.Kjlb_browseperspace_more_piclist_classifyspace_folderByIDP

    # 空间列表-浏览私人空间-更多-照片列表-分类到-文件夹ByName
    def Kjlb_browseperspace_more_piclist_classify_folderByName(self,name):
        self.Kjlb_browseperspace_more_piclist_classify_folderByNameP = self.p.get_element("name->%s"%name,"空间列表-浏览私人空间-更多-照片列表-分类到-文件夹ByName")
        return self.Kjlb_browseperspace_more_piclist_classify_folderByNameP

#***************************************【PAGE4】编辑Kjlb_browseperspace_more_piclist_edit***************************************
    # 空间列表-浏览私人空间-更多-照片列表-编辑-返回
    def Kjlb_browseperspace_more_piclist_edit_back(self):
        self.Kjlb_browseperspace_more_piclist_edit_backP = self.p.get_element("id->com.yunlu6.stone:id/title_back_edit_icon","空间列表-浏览私人空间-更多-照片列表-编辑-返回")
        return self.Kjlb_browseperspace_more_piclist_edit_backP

    # 空间列表-浏览私人空间-更多-照片列表-编辑-删除
    def Kjlb_browseperspace_more_piclist_edit_delete(self):
        self.Kjlb_browseperspace_more_piclist_edit_deleteP = self.p.get_element("id->com.yunlu6.stone:id/title_ll_edit_menu","空间列表-浏览私人空间-更多-照片列表-编辑-删除")
        return self.Kjlb_browseperspace_more_piclist_edit_deleteP

    # 空间列表-浏览私人空间-更多-照片列表-编辑-删除-是
    def Kjlb_browseperspace_more_piclist_edit_delete_confirm(self):
        self.Kjlb_browseperspace_more_piclist_edit_delete_confirmP = self.p.get_element("id->com.yunlu6.stone:id/bt_affirm","空间列表-浏览私人空间-更多-照片列表-编辑-删除-是")
        return self.Kjlb_browseperspace_more_piclist_edit_delete_confirmP

    # 空间列表-浏览私人空间-更多-照片列表-编辑-删除-否
    def Kjlb_browseperspace_more_piclist_edit_delete_cancel(self):
        self.Kjlb_browseperspace_more_piclist_edit_delete_cancelP = self.p.get_element("id->com.yunlu6.stone:id/bt_cancel","空间列表-浏览私人空间-更多-照片列表-编辑-删除-否")
        return self.Kjlb_browseperspace_more_piclist_edit_delete_cancelP

    # 空间列表-浏览私人空间-更多-照片列表-编辑-名称
    def Kjlb_browseperspace_more_piclist_edit_picname(self):
        self.Kjlb_browseperspace_more_piclist_edit_picnameP = self.p.get_element("id->com.yunlu6.stone:id/image_edit_et_name","空间列表-浏览私人空间-更多-照片列表-编辑-名称")
        return self.Kjlb_browseperspace_more_piclist_edit_picnameP

    # 空间列表-浏览私人空间-更多-照片列表-编辑-备注
    def Kjlb_browseperspace_more_piclist_edit_remark(self):
        self.Kjlb_browseperspace_more_piclist_edit_remarkP = self.p.get_element("id->com.yunlu6.stone:id/image_edit_et_remark","空间列表-浏览私人空间-更多-照片列表-编辑-备注")
        return self.Kjlb_browseperspace_more_piclist_edit_remarkP

    # 空间列表-浏览私人空间-更多-照片列表-编辑-保存
    def Kjlb_browseperspace_more_piclist_edit_save(self):
        self.Kjlb_browseperspace_more_piclist_edit_saveP = self.p.get_element("id->com.yunlu6.stone:id/btn_image_edit_save","空间列表-浏览私人空间-更多-照片列表-编辑-保存")
        return self.Kjlb_browseperspace_more_piclist_edit_saveP

#***************************************【PAGE4】删除文件夹Kjlb_browseperspace_more_menu_edit_deletefolder***************************************
     # 空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-照片列表
    def Kjlb_browseperspace_more_menu_edit_deletefolder_piclist(self):
        self.Kjlb_browseperspace_more_menu_edit_deletefolder_piclistP = self.p.get_elements("id->com.yunlu6.stone:id/item_cloudlibrary_ll_checked","空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-照片列表")
        return self.Kjlb_browseperspace_more_menu_edit_deletefolder_piclistP

    # 空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-删除按钮
    def Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn(self):
        self.Kjlb_browseperspace_more_menu_edit_deletefolder_dbtnP = self.p.get_element("id->com.yunlu6.stone:id/btn_gallery_photos_cancle","空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-删除按钮")
        return self.Kjlb_browseperspace_more_menu_edit_deletefolder_dbtnP

    # 空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-删除按钮-是
    def Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_y(self):
        self.Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_yP = self.p.get_element("id->com.yunlu6.stone:id/bt_affirm","空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-删除按钮-是")
        return self.Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_yP

     # 空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-删除按钮-否
    def Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_n(self):
        self.Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_nP = self.p.get_element("id->com.yunlu6.stone:id/bt_cancel","空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-删除按钮-否")
        return self.Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_nP

    # 空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-全选
    def Kjlb_browseperspace_more_menu_edit_deletefolder_all(self):
        self.Kjlb_browseperspace_more_menu_edit_foldername_allP = self.p.get_element("id->com.yunlu6.stone:id/title_tv_more_tv_selected","空间列表-浏览私人空间-更多-菜单栏-编辑-删除文件夹-全选")
        return self.Kjlb_browseperspace_more_menu_edit_foldername_allP

#***************************************【PAGE4】资讯图片Kjlb_browseascspace_arch_alist_pic***************************************
    # 空间列表-协会空间-资讯-资讯文件列表-资讯图片-资讯详情
    def Kjlb_browseascspace_arch_alist_pic_adetail(self):
        self.Kjlb_browseascspace_arch_alist_pic_adetailA = self.p.get_element("id->com.yunlu6.stone:id/image","空间列表-协会空间-资讯-资讯文件列表-资讯图片-资讯详情")
        return self.Kjlb_browseascspace_arch_alist_pic_adetailA

    # 空间列表-协会空间-资讯-资讯文件列表-资讯图片-返回
    def Kjlb_browseascspace_arch_alist_pic_back(self):
        self.Kjlb_browseascspace_arch_alist_pic_backA = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-协会空间-资讯-资讯文件列表-资讯图片-返回")
        return self.Kjlb_browseascspace_arch_alist_pic_backA

#***************************************【PAGE4】联系人列表Kjlb_browseascspace_menu_team_menu_assignjob_contact***************************************
     # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-返回
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_back(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_backA = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-返回")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_backA

     # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-确认
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_confirm(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_confirmA = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-确认")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_confirmA

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-部门名称
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_department(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_departmentA = self.p.get_elements("id->com.yunlu6.stone:id/setjobs_unassi_jobname","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-部门名称")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_departmentA

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-职位名称
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_jobname(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_jobnameA = self.p.get_elements("id->com.yunlu6.stone:id/tag_id","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-职位名称")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_jobnameA

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-移除
    def Kjlb_browseascspace_menu_team_menu_assignjob_contact_delete(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_deleteA = self.p.get_element("id->com.yunlu6.stone:id/setjobs_dele","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-联系人列表-移除")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_contact_deleteA

#***************************************【PAGE4】人事任免新增Kjlb_browseascspace_menu_team_menu_assignjob_addperson***************************************
     # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-返回
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_back(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_backA = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-返回")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_backA

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-搜索栏
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_search(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_searchA = self.p.get_element("id->com.yunlu6.stone:id/img_btn_search","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-搜索栏")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_searchA

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-搜索按钮(人脉搜索按钮)
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_searchbtn(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_searchbtnA = self.p.get_element("id->com.yunlu6.stone:id/iv_search","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-搜索按钮")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_searchbtnA

     # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-全选
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_all(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_allA = self.p.get_elements("id->com.yunlu6.stone:id/title_main_tv_more_tv","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-全选")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_allA

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-圆圈勾选列表
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_choose(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_allA = self.p.get_elements("id->com.yunlu6.stone:id/item_client_tv_checked","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-圆圈勾选")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_allA

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-联系人列表
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_contact(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_contactA = self.p.get_elements("id->com.yunlu6.stone:id/item_client_username_tv","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-圆圈勾选")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_contactA

    # 空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-添加(确认)
    def Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirm(self):
        self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirmA = self.p.get_element("id->com.yunlu6.stone:id/btn_pop_client_operate","空间列表-浏览协会空间-菜单栏-团队-菜单栏-人事任免-新增-添加")
        return self.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirmA







