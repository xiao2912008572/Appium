__author__ = 'Administrator'
# -*- coding: utf-8 -*-

from YunluFramework.testcase.空间.协会空间.test3_1团队人事任免 import *


# 团队人事任免
class TeamAssignJob:
    # 1.初始化
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)

    # 2.协会团队人事任免-公用方法
    def teamAssignJob(self, driver, spacename, AdminstratorLoc, SalespersonLoc, AssistanLoc,
                      AdmNum, SalNum, AssNum, Name, Director, Marketing, Hr):
        # 创建_OrgSpaceTeamHandle公有定位控件对象
        handle = SPACEHANDLE5(driver)
        sleep(1)
        try:
            self.log.info('------START:test3_1团队人事任免.TeamAssignJob.py------')
            # 1.空间首页
            # handle.Kjlb_click()
            # tools.getScreenShot(screen_path,"空间首页")
            # 2.选择空间:测试空间123
            # handle.Kjlb_browseascspaceByName_click(self.spacename)
            # 3.右上角:菜单栏选择团队
            handle.Kjlb_browseascspace_menu_click()  # 右上角菜单
            self.log.info('点击右上角菜单')
            handle.Kjlb_browseascspace_menu_team_click()  # 点击团队
            self.log.info('点击团队')
            # 4.团队编辑，编辑各职位人数
            # 4.1 管理员人数:2人
            handle.Kjlb_browseascspace_menu_team_teamedit_click()  # 点击编辑
            self.log.info('点击编辑')
            # handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self.AdministratorLoc)#编辑管理员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[0].click()
            self.log.info('编辑管理员人数')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_clear()  # 清空
            self.log.info('清空输入框')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(AdmNum)  # 2人
            self.log.info('设置管理员人数：%s' % AdmNum)
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')
            # 4.2 销售员人数:3人
            # handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self.SalespersonLoc)#编辑销售员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[1].click()
            self.log.info('编辑销售员人数')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_clear()  # 清空
            self.log.info('清空输入框')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(SalNum)  # 3人
            self.log.info('设置销售员人数：%s' % SalNum)
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')
            # 4.3 行政助理人数:4人
            # handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self.AssistantLoc)#编辑助理人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[3].click()
            self.log.info('编辑助理人数')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_clear()  # 清空
            self.log.info('清空输入框')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(AssNum)  # 4人
            self.log.info('设置助理人数：%s' % AssNum)
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')
            # 5.检查各职位人数是否保存生效
            # 5.1 检查管理员人数编辑是否生效
            # handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self.AdministratorLoc)#编辑管理员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[0].click()
            self.log.info('点击编辑管理员人数')
            AdmNumm = int(handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前管理员人数：{0}'.format(AdmNumm))
            self.log.info('预期管理员人数：{0}'.format(AdmNum))
            assert AdmNum == AdmNumm, "编辑管理员人数保存后未生效"
            self.log.info('检查管理员人数编辑是否生效')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')
            # 5.2 检查助理人数编辑是否生效
            # handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self.SalespersonLoc)#编辑管理员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[1].click()
            self.log.info('点击编辑助理人数')
            SalNumm = int(handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前助理人数：{0}'.format(SalNumm))
            self.log.info('预期助理人数：{0}'.format(SalNum))
            assert SalNum == SalNumm, "编辑助理人数保存后未生效"
            self.log.info('检查助理人数编辑是否生效')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')
            # 5.3 检查常务理事人数编辑是否生效
            # handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self.AssistantLoc)#编辑管理员人数
            driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_edit")[3].click()
            self.log.info('点击常务理事人数')
            AssNumm = int(handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前常务理事人数：{0}'.format(AssNumm))
            self.log.info('预期常务理事人数：{0}'.format(AssNum))
            assert AssNum == AssNumm, "编辑行政助理人数后未生效"
            self.log.info('检查常务理事人数编辑是否生效')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')
            # 6.关闭编辑
            handle.Kjlb_browseascspace_menu_team_teamedit_click()  # 点击编辑按钮
            self.log.info('点击编辑按钮')
            # 7.菜单栏-人事任免
            handle.Kjlb_browseascspace_menu_team_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_click()  # 点击人事任免
            self.log.info('点击人事任免')
            if driver.find_elements_by_id("com.yunlu6.stone:id/removaljobs_name") != []:  # 列表是否为空
                listT = handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact()
                for i in range(len(listT)):  # 遍历列表
                    if handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact()[i].text == Name:  # 再判断是否该人已被任免
                        handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_click(0)  # 待任免联系人
                        self.log.info('判断该人是否已被任免')
                        self.log.info('点击待任免联系人')
                        handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_delete_click()  # 点击移除
                        self.log.info('点击移除')
                    else:
                        pass
            else:
                pass
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_click()  # 点击人事任免新增按钮
            self.log.info('点击人事任免新增按钮')
            # 8.搜索姓名:肖静远
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_search_sendkeys(Name)  # 搜索关键字
            self.log.info('搜索人脉关键字：%s' % Name)
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_searchbtn_click()  # 点击搜索
            self.log.info('点击搜索')
            # 9.点击搜索的结果,添加
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_choose_click(0)  # 勾选
            self.log.info('勾选')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirm_click()  # 添加
            self.log.info('添加')
            # 10.待任免列表点击联系人-任免职位-勾选-返回
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_click(0)  # 待任免联系人
            self.log.info('点击待任免联系人')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_department_click(Director)  # 秘书处
            self.log.info('点击秘书处')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_jobname_click(1)  # 秘书长
            self.log.info('勾选秘书长')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_confrim_click()  # 勾选
            self.log.info('勾选')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_back_click()  # 返回
            self.log.info('返回')
            namee = driver.find_elements_by_id("com.yunlu6.stone:id/companyteam_item_name")[1].text  # 获取秘书长姓名
            assert Name == namee, "秘书长任免失败"
            self.log.info('判断该人脉秘书长职位是否任免成功')
            # 11.移除任免,还原
            handle.Kjlb_browseascspace_menu_team_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_click()  # 点击人事任免
            self.log.info('点击人事任免')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_click(0)  # 待任免联系人
            self.log.info('待任免联系人')
            handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_delete_click()  # 点击移除
            self.log.info('点击移除')
            self.log.info('------END:test3_1团队人事任免.TeamAssignJob.py------')
        except Exception as err:
            self.log.error("Error Information TeamAssignJob Inside : %s" % err)
            raise err
