__author__ = 'Administrator'
#coding=utf-8
import unittest
from time import sleep

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.testcase.空间.机构空间.test2_1上下架产品.CreateProduct import CreateProduct
from StoneUIFramework.testcase.空间.机构空间.test2_1上下架产品.DeleteProduct import DeleteProduct
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log

#上下架产品
class space_Product(unittest.TestCase):
    @classmethod#装饰器，类方法
    def setUpClass(self):#最开始执行
        #建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        #创建工具类
        self.tools = Tools(self.driver)#tools工具
        #创建_SPACEHANDLE5公有定位控件对象
        self.handle = _SPACEHANDLE5(self.driver)
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space',"org_path_002_1")#通过配置文件获取截图的路径
        self.logfile = cf.getParam('log',"logfile")#日志文件名
        #创建CreateProduct和DeleteProduct对象
        self.cr = CreateProduct()
        self.dl = DeleteProduct()
        #测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        self.spacename = d.cell("test002-上架产品",2,1)#空间名
        self.proname = d.cell("test002-上架产品",2,3)
        #创建日志记录模块
        self.log = Log(self.logfile)
    def test_spaceproduct(self):
        """
        产品上下架
        """
        try:
            self.log.info("------------START:test2_1上下架产品.CreateProduct002_1.py------------")
            # self.tools.coverUpdate(self.log_path,self.screen_path)#覆盖更新日志,覆盖更新截图
        #1.点击进入空间界面
            sleep(1)
            self.handle.Kjlb_click()#点击进入空间列表
            self.log.info('点击进入空间列表')
            self.handle.Kjlb_browseorgspaceByName_click(self.spacename)#点击进入测试空间123
            self.log.info('点击进入%s'%self.spacename)
            self.handle.Kjlb_browseorgspace_menu_click()#点击菜单栏
            self.log.info('点击菜单栏')
            # self.driver.tap([(self.menu_x,self.menu_y)], 500)#菜单栏
            self.handle.Kjlb_browseorgspace_menu_product_click()#点击产品
            self.log.info('点击产品')
        #2.新建产品
            self.cr.createProduct(self.driver)
        #3.未发布列表:发布
            self.handle.Kjlb_browseorgspace_menu_product_unlock_click()#未发布列表点击
            self.log.info('点击未发布列表')
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_click(-1)#访问最后一个（刚上架的）
            self.log.info('点击最后一个产品-刚上架')
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_menu_click()#菜单栏
            self.log.info('点击菜单栏')
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_menu_release_click()#点击发布
            self.log.info('点击发布')
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_menu_release_confirm_click()#确认
            self.log.info('点击确认')
        #4.已发布列表-产品检查
            self.handle.Kjlb_browseorgspace_menu_product_lock_click()#已发布列表
            self.log.info('点击已发布列表')
            sleep(2)
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_click(-1)#访问最后一个
            self.log.info('点击最后一个产品-刚发布')
            #4.1商品名检查
            proname = self.handle.Kjlb_browseorgspace_menu_product_lock_list_proname_text()
            assert proname == self.proname,"Proname Show Error!"
            self.log.info('商品名检查')
            #4.2更多价格检查
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_moreprice_click()#点击更多价格
            price1 = self.handle.Kjlb_browseorgspace_menu_product_lock_list_moreprice_text(0)
            price2 = self.handle.Kjlb_browseorgspace_menu_product_lock_list_moreprice_text(1)
            price3 = self.handle.Kjlb_browseorgspace_menu_product_lock_list_moreprice_text(2)
            price4 = self.handle.Kjlb_browseorgspace_menu_product_lock_list_moreprice_text(3)
            assert price1 == '赠品',"Price1 Show Error!"
            assert price2 == '123.00','Price2 Show Error!'
            assert price3 == '999.00',"Price3 Show Error!"
            assert price4 == '定制',"Price4 Show Error!"
            self.log.info('价格检查')
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_moreprice_list_click(0)#点击第一个价格
            self.log.info('点击第一个价格')
            #4.3石种属性检查
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_middle_click()#点击产品参数
            self.log.info('点击产品参数')
            attribute = self.handle.Kjlb_browseorgspace_menu_product_lock_list_middle_attribut_text()#获取石种相关属性
            assert attribute == "西班牙米黄 /浅 /黄 /云","Attribute Show Error!"
            self.log.info('石种属性检查')
            #4.4制品与表面检查
            pattern = self.handle.Kjlb_browseorgspace_menu_product_lock_list_middle_pattern_text()#获取制品与表面相关属性

            assert pattern == "平板 /光  面","Pattern Show Error!"
            self.log.info('制品与表面检查')
            #4.5参数名,参数值检查
            self.tools.swipeUp(500)#上滑,展示出key/value
            parameter = self.handle.Kjlb_browseorgspace_menu_product_lock_list_middle_keyvalue_text(1)
            assert parameter == "key:value","Parameter Shwo Error!"
            self.log.info('参数名/参数值检查')
        #5.下架产品
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_offshelf_click()#点击下架
            self.log.info('点击下架')
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_offshelf_sure_click()#确定下架
            self.log.info('确定下架')
        #6.删除产品,还原测试场景
            self.handle.Kjlb_browseorgspace_menu_product_unlock_click()#点击未发布列表
            self.log.info('点击未发布列表')
            sleep(1)
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_click(-1)#访问最后一个（刚下架）
            self.log.info('点击最后一个产品-刚下架')
            self.dl.deleteProduct(self.driver)#删除产品，回归
            self.log.info("------------END:test2_1上下架产品.CreateProduct002_1.py------------")
        except Exception as err:
            self.tools.getScreenShot(self.screen_path,"ExceptionShot")
            self.log.error("CreateProduct Outside : %s"%err)
            raise err
        finally:
            self.driver.quit()