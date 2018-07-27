from YunluFramework.testcase.空间.common import *


class CommonSpace:
    '''
    空间公有方法抽离
    '''

    def __init__(self, handle, log, tools):
        '''
        初始化函数
        :param handle: 操作对象
        :param log: 日志对象
        :param tools: 工具对象
        '''
        self.handle = handle
        self.log = log
        self.tools = tools

    # 进入空间
    def enter_space(self, spacename):
        '''进入企业空间
        :param spacename: 空间名
        :return:
        '''
        sleep(1)
        # 1.点击进入空间列表
        self.handle.Kjlb_click()
        self.log.info('点击进入空间列表')

        # 2.搜索空间名找到空间
        self.tools.find_space_by_name(spacename)
        self.log.info('搜索栏搜索结果:{0}'.format(spacename))

        # 3. 点击搜索结果第一条
        try:
            self.handle.Kjlb_browseorgspaceByID_click()
            self.log.info('点击进入%s' % spacename)
        except Exception as err:
            self.log.error("空间不存在 : %s" % err)
            raise err

    # 进入机构空间菜单项
    def click_org_menu(self, menu):
        '''进入机构空间菜单栏各级菜单
        :param menu: 菜单选项，例如进入产品，传入product等
        :order : 订单
        :money : 资金
        :team : 团队
        :customer : 客户
        :archivies : 资讯
        :upgrade : 业务升级
        :edit : 编辑
        :setup : 设置
        :near : 搜附近
        :close : 关闭
        :quitteam : 退出团队
        :visitor : 访客
        :return:
        '''
       
        # 产品
        if menu == 'product':
            self.handle.Kjlb_browseorgspace_menu_product_click()  # 点击产品
            self.log.info('点击产品')

        # 订单
        elif menu == 'order':
            self.handle.Kjlb_browseorgspace_menu_order_click()  # 点击订单
            self.log.info('点击订单')

        # 资金
        elif menu == 'money':
            self.handle.Kjlb_browseorgspace_menu_money_click()  # 点击资金
            self.log.info('点击资金')

        # 团队
        elif menu == 'team':
            self.handle.Kjlb_browseorgspace_menu_team_click()  # 点击团队
            self.log.info('点击团队')

        # 客户
        elif menu == 'customer':
            self.handle.Kjlb_browseorgspace_menu_customer_click()  # 点击客户
            self.log.info('点击客户')

        # 资讯
        elif menu == 'archivies':
            self.handle.Kjlb_browseorgspace_menu_archivies_click()  # 点击资讯
            self.log.info('点击资讯')

        # 流程
        elif menu == 'process':
            self.handle.Kjlb_browseorgspace_menu_flow_click()    #点击流程
            self.log.info('点击流程')

        # 业务升级
        elif menu == 'upgrade':
            self.handle.Kjlb_browseorgspace_menu_upgrade_click()  # 点击业务升级
            self.log.info('点击业务升级')

        # 编辑
        elif menu == 'edit':
            self.handle.Kjlb_browseorgspace_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')
            self.handle.Kjlb_browseorgspace_menu_edit_click()  # 点击编辑
            self.log.info('点击编辑')

        # 设置
        elif menu == 'setup':
            self.handle.Kjlb_browseorgspace_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')
            self.handle.Kjlb_browseorgspace_menu_setup_click()  # 点击设置
            self.log.info('点击设置')

        # 搜附近
        elif menu == 'near':
            self.handle.Kjlb_browseorgspace_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')
            self.handle.Kjlb_browseorgspace_menu_near_click()  # 搜附近
            self.log.info('点击搜附近')

        # 关闭
        elif menu == 'close':
            self.handle.Kjlb_browseorgspace_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')
            self.handle.Kjlb_browseorgspace_menu_close_click()  # 点击关闭
            self.log.info('点击关闭')

        # 退出团队
        elif menu == 'quitteam':
            self.handle.Kjlb_browseorgspace_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')
            self.handle.Kjlb_browseorgspace_menu_quitteam_click()  # 点击退出团队
            self.log.info('点击退出团队')

        # 访客
        elif menu == 'visitor':
            self.handle.Kjlb_browseorgspace_menu_visitor_click()  # 点击访客
            self.log.info('点击访客')
        else:
            self.log.error('Error : menu值不正确！')

    # 进入协会空间菜单项
    def click_asc_menu(self, menu):
        '''进入机构空间菜单栏各级菜单
        :param menu: 菜单选项，例如进入产品，传入product等
        :order : 订单
        :money : 资金
        :team : 团队
        :customer : 客户
        :archivies : 资讯
        :upgrade : 业务升级
        :edit : 编辑
        :setup : 设置
        :near : 搜附近
        :close : 关闭
        :quitteam : 退出团队
        :visitor : 访客
        :return:
        '''
        self.handle.Kjlb_browseascspace_menu_click()  # 点击菜单栏
        self.log.info('点击菜单栏')
        # 团队
        if menu == 'team':
            self.handle.Kjlb_browseascspace_menu_team_click()  # 点击团队
            self.log.info('点击团队')

        # 客户
        elif menu == 'customer':
            self.handle.Kjlb_browseascspace_menu_customer_click()  # 点击客户
            self.log.info('点击客户')

        # 资讯
        elif menu == 'archivies':
            self.handle.Kjlb_browseascspace_menu_arc_click()  # 点击资讯
            self.log.info('点击资讯')

        # 编辑
        elif menu == 'edit':
            self.handle.Kjlb_browseascspace_menu_edit_click()  # 点击编辑
            self.log.info('点击编辑')

        # 设置
        elif menu == 'setup':
            self.handle.Kjlb_browseascspace_menu_setting_click()  # 点击设置
            self.log.info('点击设置')

        # 搜附近
        elif menu == 'near':
            self.handle.Kjlb_browseascspace_menu_nearby_click()  # 搜附近
            self.log.info('点击搜附近')

        # 关闭
        elif menu == 'close':
            self.handle.Kjlb_browseascspace_menu_close_click()  # 点击关闭
            self.log.info('点击关闭')

        # 退出团队
        elif menu == 'quitteam':
            self.handle.Kjlb_browseorgspace_menu_quitteam_click()  # 点击退出团队
            self.log.info('点击退出团队')
        else:
            self.log.error('Error : menu值不正确！')

    # 进入私人空间菜单项
    def click_ps_menu(self, menu):
        '''进入机构空间菜单栏各级菜单
                :param menu: 菜单选项，例如进入产品，传入product等
                :card : 名片
                :edit : 编辑
                :customer : 客户
                :add : 文件夹
                :return:
                '''
        self.handle.Kjlb_browseascspace_menu_click()  # 点击菜单栏
        self.log.info('点击菜单栏')
        # 名片
        if menu == 'card':
            self.handle.Kjlb_browseperspace_menu_card_click()  # 点击名片
            self.log.info('点击名片')
        # 编辑
        elif menu == 'edit':
            self.handle.Kjlb_browseperspace_menu_edit_click()  # 编辑
            self.log.info('点击编辑')
        # 客户
        elif menu == 'customer':
            self.handle.Kjlb_browseperspace_menu_customer_click()  #客户
            self.log.info('点击客户')
        # 文件夹
        elif menu == 'add':
            self.handle.Kjlb_browseperspace_menu_addfolder_click()  #文件夹
            self.log.info('点击文件夹')
        else:
            self.log.error('Error : menu值不正确！')


    # 从各页面退出当前账号
    def logout_from_page(self, N):
        '''从各页面退退出当前账号
        :return:
        '''
        # 1.点击设置按钮
        self.handle.Setting_click1(N)
        self.log.info('点击设置按钮')

        # 2.点击关于我们
        self.handle.Setting_aboutus_click()
        self.log.info('点击关于我们')

        # 3.点击退出
        self.handle.Setting_about_loginout_click()
        self.log.info('点击退出')

        # 4.点击确定
        self.handle.Setting_aboutus_loginout_confirm_click()
        self.log.info('点击确定')