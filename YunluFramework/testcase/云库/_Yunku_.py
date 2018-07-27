__author__ = 'xiaoj'
# -*- coding: utf-8 -*-
import logging
class Yunku(object):
    def __init__(self,driver):
        self.driver = driver

    #定位:云库，进入云库页
    def Jryk(self):
        try:
            __Jryk = self.driver.find_element_by_id("com.yunlu6.stone:id/navi_item_work_cloundlibrary")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
                "定位云库页失败"
        return __Jryk

    #定位:云库右上角三个点
    def Yunku_Sgd(self):
        try:
            __Yunku_Sgd = self.driver.find_element_by_id("com.yunlu6.stone:id/iv_right_search_cloundlibrary")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位右上角三个点失败"
        return __Yunku_Sgd

    #定位:三个点下面的"+文件"
    def Jwj(self):
        try:
            __Jwj = self.driver.find_element_by_id("com.yunlu6.stone:id/btn_pop_cloundlibrary_fragement_upload")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位右上角三个点下面的'+文件'失败"
        return __Jwj

    #定位:+文件下面的相册方式上传
    def Xc(self):
        try:
            __Xc = self.driver.find_element_by_id("com.yunlu6.stone:id/pop_cloundlibrary_tv_album")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位相册失败"
        return __Xc

    #定位:相册照片
    def Xc_Zp(self):
        try:
            __Xc_Zp = self.driver.find_elements_by_id("com.yunlu6.stone:id/item_cloudlibrary_ll_checked")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位相册第一张照片失败"
        return __Xc_Zp

    #定位:右上角完成按钮
    def Complete(self):
        try:
            __Complete = self.driver.find_element_by_id("com.yunlu6.stone:id/title_tv_edit_menu_tv")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位完成按钮失败"
        return __Complete

    #定位：云库照片
    def Yk_Zp(self):
        try:
            __Yk_ZP = self.driver.find_elements_by_id("com.yunlu6.stone:id/cloudlibrary_image_item")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位云库第一张照片失败"
        return __Yk_ZP

    #定位：云库照片右上角主菜单
    def Main_menu(self):
        try:
            __Main_menu = self.driver.find_element_by_id("com.yunlu6.stone:id/title_main_tv_more_menu")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位云库照片右上角主菜单失败"
        return __Main_menu

    #定位:菜单栏中编辑按钮
    def Main_menu_edit(self):
        try:
            __Main_menu_edit = self.driver.find_element_by_id("com.yunlu6.stone:id/btn_share_space")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位菜单栏中编辑按钮失败"
        return __Main_menu_edit

    #定位:菜单栏中分类按钮
    def Main_menu_classify(self):
        try:
            __Main_menu_classify = self.driver.find_element_by_id("com.yunlu6.stone:id/btn_new_space")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位菜单栏中分类按钮失败"
        return __Main_menu_classify

    #定位：选择分类到中的"xjy机构"
    def Main_menu_classify_xjy_Org(self):
        try:
            __Main_menu_classify_xjy_Org = self.driver.find_element_by_name("xjy机构")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位菜单栏分类到:xjy机构按钮失败"
        return __Main_menu_classify_xjy_Org

    #定位：选择分类到中的产品
    def Main_menu_classify_product(self):
        try:
            __Main_menu_classify_product = self.driver.find_element_by_name("产品")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位菜单栏分类到:产品按钮失败"
        return __Main_menu_classify_product

    #定位:选择分类到中的资讯
    def Main_menu_classify_xjy_Org_archieves(self):
        try:
            __Main_menu_classify_xjy_Org_archieves = self.driver.find_element_by_name("资讯")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位菜单栏分类到:资讯按钮失败"
        return __Main_menu_classify_xjy_Org_archieves

    #定位:勾选按钮"√"
    def Title_tv_menu(self):
        try:
            __Title_tv_menu = self.driver.find_element_by_id("com.yunlu6.stone:id/title_tv_menu")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位菜单栏分类到:勾选按钮'√'失败"
        return __Title_tv_menu

    #定位:主菜单-编辑-垃圾回收图标按钮
    def Main_menu_edit_delete(self):
        try:
            __Main_menu_edit_delete = self.driver.find_element_by_id("com.yunlu6.stone:id/title_tv_edit_menu_delete")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位主菜单-编辑-垃圾回收图标按钮失败"
        return __Main_menu_edit_delete

    #定位:删除后确认对话框中的确认按钮
    def Confirm(self):
        try:
            __Confirm = self.driver.find_element_by_id("com.yunlu6.stone:id/bt_affirm")
        except Exception as err:
            logging.info("error@@!!!!!!!")
            assert False,\
            "定位删除后确认对话框中的确认按钮失败"
        return __Confirm




