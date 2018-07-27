__author__ = 'Administrator'
import sys
sys.path.append("/Users/xiaojingyuan/PycharmProjects/Appium")
from YunluFramework.testcase.空间.机构空间.test2_1上下架产品 import *
import time


# 上下架产品
@ddt.ddt
class space_ProductO(unittest.TestCase):
    # 1.创建数据库操作对象
    d = DataMysql()
    sql01 = "select * from test2_1_orgcreateproduct_01"
    sql03 = "select * from test2_1_orgcreateproduct_03"
    data01 = d.select(sql01, 0)
    data03 = d.select(sql03, 0)

    # 2.初始化
    @classmethod
    def setUpClass(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()

        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具

        # 3.创建_SPACEHANDLE5公有定位控件对象
        self.handle = SPACEHANDLE5(self.driver)

        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')

        # 5.获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "org_path_002_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名

        # 6.创建日志记录模块
        self.log = Log(self.logfile)

        # 7.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------START:test2_1上下架产品.CreateProduct002_1.py------------")

        # 8.创建空间公有对象
        self.common = CommonSpace(self.handle, self.log, self.tools)

    # 3.释放资源
    @classmethod
    def tearDownClass(self):
        # 1.打印日志
        self.log.info("------------END:test2_1上下架产品.CreateProduct002_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        # 2.关闭driver
        # self.driver.quit()

    # 4.测试用例
    # 4.1 进入空间
    @ddt.data(data01)
    @ddt.unpack
    def test_createProduct01(self, spacename):
        '''进入空间
        :param spacename: 空间名
        '''
        try:
            # 1.进入空间
            self.common.enter_space(spacename)

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_createProduct01 : %s" % err)
            raise err

    # 4.2 点击产品
    def test_createProduct02(self):
        '''点击产品
        :return:
        '''
        try:
            # 1.进入产品
            self.common.click_org_menu('product')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_createProduct02 : %s" % err)
            raise err

    # 4.3 新建产品
    @ddt.data(data03)
    @ddt.unpack
    def test_createProduct03(self, photo, proname, key, value, price1, stock1, price2, stock2, price3,
                             stock3, price4, stock4):
        '''新建产品
        :param photo: 图片列表第N张
        :param proname:产品名
        :param key:参数名
        :param value:参数值
        :param price1:价格1
        :param stock1:库存1
        :param price2:价格2
        :param stock2:库存2
        :param price3:价格3
        :param stock3:库存3
        :param price4:价格4
        :param stock4:库存4
        :return:
        '''
        try:
            # -----------------新建产品-----------------
            self.handle.Kjlb_browseorgspace_menu_product_new_click()  # 点击新建按钮
            self.log.info('点击新建按钮')
            # 1.添加照片
            self.handle.Kjlb_browseorgspace_menu_product_new_addphoto_click()  # 点击添加照片按钮
            self.log.info('点击添加照片按钮')
            self.handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_click()  # 选择相册添加
            self.log.info('选择相册添加')
            self.handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_list_click(photo)  # 选择第一张照片
            self.log.info('选择第%s张照片' % photo)
            self.handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_confirm_click()  # 点击完成
            self.log.info('点击完成')
            sleep(4)

            # 2.商品名称
            # 2.1商品名称
            self.handle.Kjlb_browseorgspace_menu_product_new_proname_click()  # 点击商品名称
            self.log.info('点击商品名称')
            self.handle.Kjlb_browseorgspace_menu_product_new_proname_name_sendkeys(proname)  # 输入商品名称
            self.log.info('输入商品名称：%s' % proname)
            self.handle.Kjlb_browseorgspace_menu_product_new_proname_name_title_click()  # 点击顶部标题
            self.log.info('点击顶部标题')

            # 2.2商品分类
            self.handle.Kjlb_browseorgspace_menu_product_new_proname_yclassify_click()
            self.log.info('点击商品分类')
            self.handle.Kjlb_browseorgspace_menu_product_new_proname_ytag_click('石制品')
            self.log.info('选择"石制品"标签')

            '''
                20180320弧板标签暂无,下面更新，start
            '''
            # self.handle.Kjlb_browseorgspace_menu_product_new_proname_ytag_click('弧板')
            # self.log.info('选择"弧板"标签')
            self.handle.Kjlb_browseorgspace_menu_product_new_proname_ytag_click('宝玉石')  # 选择宝玉石标签
            self.log.info('点击宝玉石标签')
            self.handle.Kjlb_browseorgspace_menu_product_new_proname_ytag_click('蓝宝石')
            self.log.info('点击蓝宝石标签')
            '''
                20180320,end
            '''

            self.handle.Kjlb_browseorgspace_menu_product_new_proname_choose_click()  # 点击勾选按钮
            self.log.info('点击勾选按钮')

            # 2.3石种属性
            self.handle.Kjlb_browseorgspace_menu_product_new_attribute_click()
            self.log.info('点击石种属性')
            self.handle.Kjlb_browseorgspace_menu_product_new_attribute_species_sendkeys('蓝玉')
            self.log.info('输入石种类名：蓝玉')
            self.handle.Kjlb_browseorgspace_menu_product_new_attribute_species_match_click(1)
            self.log.info('选择种类名-匹配类名列表：蓝玉石')
            self.handle.Kjlb_browseorgspace_menu_product_new_attribute_color_click()
            self.log.info('点击颜色')
            self.handle.Kjlb_browseorgspace_menu_product_new_attribute_color_list_click(0)
            self.log.info('点击颜色列表：黑')
            self.handle.Kjlb_browseorgspace_menu_product_new_attribute_attrname_click()
            self.log.info('点击深浅')
            self.handle.Kjlb_browseorgspace_menu_product_new_attribute_attrname_list_click(0)
            self.log.info('选择：深')
            self.handle.Kjlb_browseorgspace_menu_product_new_attribute_pattern_click()
            self.log.info('点击花纹')
            self.handle.Kjlb_browseorgspace_menu_product_new_attribute_pattern_list_click(0)
            self.log.info('选择：云')
            self.handle.Kjlb_browseorgspace_menu_product_new_attribute_confirm_click()
            self.log.info('点击勾选')

            # 2.4制品和表面
            self.handle.Kjlb_browseorgspace_menu_product_new_attrstone_click()
            self.log.info('点击制品和表面')
            self.handle.Kjlb_browseorgspace_menu_product_new_attrstone_type_click()
            self.log.info('点击制品')
            self.handle.Kjlb_browseorgspace_menu_product_new_attrstone_type_list_click(0)
            self.log.info('选择：平板')
            self.handle.Kjlb_browseorgspace_menu_product_new_attrstone_surface_click()
            self.log.info('点击表面')
            self.handle.Kjlb_browseorgspace_menu_product_new_attrstone_surface_list_click(0)
            self.log.info('选择：光面')
            self.handle.Kjlb_browseorgspace_menu_product_new_attrstone_confirm_click()
            self.log.info('点击勾选')

            # 3.产品参数
            self.handle.Kjlb_browseorgspace_menu_product_new_parameter_click()  # 点击产品参数
            self.log.info('点击产品参数')


            '''
                20180320已过期，故注释，并更新，start
            '''
            # self.handle.Kjlb_browseorgspace_menu_product_new_parameter_key_clear(0)  # 先清空参数名
            # self.log.info('清空参数名')
            self.handle.Kjlb_browseorgspace_menu_product_new_parameter_input() #点击请输入
            self.log.info('点击请输入')
            '''
                20180320，end
            '''


            self.handle.Kjlb_browseorgspace_menu_product_new_parameter_key_sendkeys(0, key)  # 输入参数名
            self.log.info('输入参数名：%s' % key)
            self.handle.Kjlb_browseorgspace_menu_product_new_parameter_value_sendkeys(0, value)  # 输入参数值
            self.log.info('输入参数值：%s' % value)
            self.handle.Kjlb_browseorgspace_menu_product_new_parameter_confirm_click()  # 点击勾选
            self.log.info('点击勾选')

            # 4.价格
            self.handle.Kjlb_browseorgspace_menu_product_new_price_click()  # 点击价格
            self.log.info('点击价格')

            # 4.1 价格:0 库存:0
            time.sleep(1)
            self.tools.swipeUp(500)
            self.log.info('向上滑动屏幕0.5秒')
            self.handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2, price1)  # 单价0元
            self.log.info('单价：%s' % price1)
            self.handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1, stock1)  # 库存0
            self.log.info('库存：%s' % stock1)
            self.handle.Kjlb_browseorgspace_menu_product_new_price_save_click()  # 点击保存
            self.log.info('点击保存')

            # 4.2 价格:123 库存:空
            self.handle.Kjlb_browseorgspace_menu_product_new_price_add_click()  # +新价
            self.log.info('点击+新价')
            self.tools.swipeUp(500)
            self.log.info('向上滑动屏幕0.5秒')
            self.handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2, price2)  # 单价123元
            self.log.info('单价：%s' % price2)
            self.handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1, stock2)  # 库存空
            self.log.info('库存：%s' % stock2)
            self.handle.Kjlb_browseorgspace_menu_product_new_price_save_click()  # 点击保存
            self.log.info('点击保存')

            # 4.3 价格:空 库存:123
            self.handle.Kjlb_browseorgspace_menu_product_new_price_add_click()  # +新价
            self.log.info('点击+新价')
            self.tools.swipeUp(500)
            self.log.info('向上滑动屏幕0.5秒')
            self.handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1, stock3)  # 库存123
            self.log.info('库存：%s' % stock3)
            self.handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2, price3)  # 单价空
            self.log.info('单价：%s' % price1)
            self.handle.Kjlb_browseorgspace_menu_product_new_price_save_click()  # 点击保存
            self.log.info('点击保存')

            # 4.4 价格:999 库存:999
            self.handle.Kjlb_browseorgspace_menu_product_new_price_add_click()  # +新价
            self.log.info('点击+新价')
            self.tools.swipeUp(500)
            self.log.info('向上滑动屏幕0.5秒')
            self.handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2, price4)  # 单价999元
            self.log.info('单价：%s' % price4)
            self.handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1, stock4)  # 库存999
            self.log.info('库存：%s' % stock4)
            self.handle.Kjlb_browseorgspace_menu_product_new_price_save_click()  # 点击保存
            self.log.info('点击保存')
            self.handle.Kjlb_browseorgspace_menu_product_new_price_back_click()  # 点击返回
            self.log.info('点击返回')

            # 5.保存->发布
            self.handle.Kjlb_browseorgspace_menu_product_new_save_click()  # 点击保存
            self.log.info('点击保存')
            self.log.info('------END:test2_1上下架产品.CreateProduct.py------')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_createProduct03 : %s" % err)
            raise err

    # 4.4 发布产品
    def test_createProduct04(self):
        '''未发布列表-发布产品
        :return:
        '''
        try:
            # 1.未发布列表点击
            self.handle.Kjlb_browseorgspace_menu_product_unlock_click()  # 未发布列表点击
            self.log.info('点击未发布列表')

            # 2.访问最后一个（刚上架的产品）
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_click(-1)  # 访问最后一个（刚上架的）
            self.log.info('点击最后一个产品-刚上架')

            # 3.点击菜单栏
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_menu_click()  # 菜单栏
            self.log.info('点击菜单栏')

            # 4.点击发布
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_menu_release_click()  # 点击发布
            self.log.info('点击发布')

            # 5.确认发布
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_menu_release_confirm_click()  # 确认
            self.log.info('点击确认')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_createProduct04 : %s" % err)
            raise err

    # 4.5 已发布产品参数检查
    def test_createProduct05(self):
        '''已发布产品参数检查
        :return:
        '''
        try:
            # 0.已发布列表-产品检查
            self.handle.Kjlb_browseorgspace_menu_product_lock_click()  # 已发布列表
            self.log.info('点击已发布列表')
            sleep(2)
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_click(-1)  # 访问最后一个
            self.log.info('点击最后一个产品-刚发布')

            # 1.商品名检查
            proname = self.handle.Kjlb_browseorgspace_menu_product_lock_list_proname_text()
            assert proname == proname, "Proname Show Error!"
            self.log.info('商品名检查')

            # 2.更多价格检查
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_moreprice_click()
            self.log.info('点击更多价格')
            price = self.driver.find_element_by_id('com.yunlu6.yunlu:id/select_money')
            prices = price.find_elements_by_class_name('android.widget.RadioButton')
            p = ['赠品', '￥123.00', '￥999.00', '定制']
            for i in range(0, 4):
                assert prices[i].get_attribute('text') in p,'第{0}价格不在price中！'.format(i)

            """
            price1 = self.handle.Kjlb_browseorgspace_menu_product_lock_list_moreprice_text(0)
            price2 = self.handle.Kjlb_browseorgspace_menu_product_lock_list_moreprice_text(1)
            price3 = self.handle.Kjlb_browseorgspace_menu_product_lock_list_moreprice_text(2)
            price4 = self.handle.Kjlb_browseorgspace_menu_product_lock_list_moreprice_text(3)
            assert price1 == '赠品', "Price1 Show Error!"
            assert price2 == '123.00', 'Price2 Show Error!'
            assert price3 == '999.00', "Price3 Show Error!"
            assert price4 == '定制', "Price4 Show Error!
            """

            self.log.info('价格检查完毕，无误')

            # 3.点击第一个价格
            prices[1].click() # 点击第二个价格
            self.log.info('点击第二个价格')
            self.driver.find_element_by_id('com.yunlu6.yunlu:id/iv_close').click()
            self.log.info('关闭更多价格')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_createProduct05 : %s" % err)
            raise err

    # 4.6 下架产品
    def test_createProduct06(self):
        '''下架产品
        :return:
        '''
        try:
            # 1.下架产品
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_offshelf_click()  # 点击下架
            self.log.info('点击下架')

            # 2.确定下架
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_offshelf_sure_click()  # 确定下架
            self.log.info('确定下架')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_createProduct06 : %s" % err)
            raise err

    # 4.7 删除产品
    def test_createProduct07(self):
        '''删除产品，还原测试场景
        :return:
        '''
        try:
            # 1.删除产品,还原测试场景
            self.handle.Kjlb_browseorgspace_menu_product_unlock_click()  # 点击未发布列表
            self.log.info('点击未发布列表')
            sleep(1)
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_click(-1)  # 访问最后一个（刚下架）
            self.log.info('点击最后一个产品-刚下架')

            # 2.点击菜单栏
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')

            # 3.点击删除
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_menu_delete_click()  # 删除产品
            self.log.info('点击删除')
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_menu_delete_y_click()  # 确认删除该产品
            self.log.info('确认删除')

        except Exception as err:

            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_createProduct07 : %s" % err)
            raise err

if __name__ == '__main__':
    unittest.main()