__author__ = 'xiaoj'
from StoneUIFramework.public.pages.setting.SETTINGPAGE3 import _SETTINGPAGE3

class _SETTINGPAGE4(_SETTINGPAGE3):
# ******************************************************【PAGE3】意向地区 Setting_userinfo_menu_shopping_address******************************************************
    #设置:设置-基本资料-主菜单-导购机会-意向地区-返回
    def Setting_userinfo_menu_shopping_address_back(self):
        self.Setting_userinfo_menu_shopping_address_backS = self.p.get_element("id->com.yunlu6.stone:id/title_back_icon","设置-基本资料-主菜单-导购机会-意向地区-返回")
        return self.Setting_userinfo_menu_shopping_address_backS

    #设置:设置-基本资料-主菜单-导购机会-意向地区-确认
    def Setting_userinfo_menu_shopping_address_confirm(self):
        self.Setting_userinfo_menu_shopping_address_confirmS = self.p.get_element("id->com.yunlu6.stone:id/title_tv_menu","设置-基本资料-主菜单-导购机会-意向地区-确认")
        return self.Setting_userinfo_menu_shopping_address_confirmS

     #设置:设置-基本资料-主菜单-导购机会-意向地区-地区列表
    def Setting_userinfo_menu_shopping_address_alist(self):
        self.Setting_userinfo_menu_shopping_address_alistS = self.p.get_elements("id->com.yunlu6.stone:id/lv_address_no","设置-基本资料-主菜单-导购机会-意向地区-地区列表")
        return self.Setting_userinfo_menu_shopping_address_alistS

    #设置:设置-基本资料-主菜单-导购机会-意向地区-已选择地区列表
    def Setting_userinfo_menu_shopping_address_hlist(self):
        self.Setting_userinfo_menu_shopping_address_hlistS = self.p.get_elements("id->com.yunlu6.stone:id/lv_address","设置-基本资料-主菜单-导购机会-意向地区-已选地区列表")
        return self.Setting_userinfo_menu_shopping_address_hlistS

# ******************************************************【PAGE3】周期 Setting_userinfo_menu_hot_cycle******************************************************
    #设置:设置-基本资料-主菜单-热度设置-周期-返回
    def Setting_userinfo_menu_hot_cycle_back(self):
        self.Setting_userinfo_menu_hot_cycle_backS = self.p.get_element("id->com.yunlu6.stone:id/title_main_back_more_icon","设置-基本资料-主菜单-热度设置-周期-返回")
        return self.Setting_userinfo_menu_hot_cycle_backS

    #设置:设置-基本资料-主菜单-热度设置-周期-每天
    def Setting_userinfo_menu_hot_cycle_back_allday(self):
        self.Setting_userinfo_menu_hot_cycle_back_alldayS = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_allday","设置-基本资料-主菜单-热度设置-周期-每天")
        return self.Setting_userinfo_menu_hot_cycle_back_alldayS

    #设置:设置-基本资料-主菜单-热度设置-周期-工作日
    def Setting_userinfo_menu_hot_cycle_back_workday(self):
        self.Setting_userinfo_menu_hot_cycle_back_workdayS = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_workday","设置-基本资料-主菜单-热度设置-周期-工作日")
        return self.Setting_userinfo_menu_hot_cycle_back_workdayS

    #设置:设置-基本资料-主菜单-热度设置-周期-节假日
    def Setting_userinfo_menu_hot_cycle_back_holiday(self):
        self.Setting_userinfo_menu_hot_cycle_back_holidayS = self.p.get_element("id->com.yunlu6.stone:id/msgsetting_btn_holiday","设置-基本资料-主菜单-热度设置-周期-节假日")
        return self.Setting_userinfo_menu_hot_cycle_back_holidayS

    #设置:设置-基本资料-主菜单-热度设置-周期-择日
    def Setting_userinfo_menu_hot_cycle_back_messday(self):
        self.Setting_userinfo_menu_hot_cycle_back_messdayS = self.p.get_element("id->com.yunlu6.stone:id/tag_mess_day","设置-基本资料-主菜单-热度设置-周期-择日")
        return self.Setting_userinfo_menu_hot_cycle_back_messdayS

    #设置:设置-基本资料-主菜单-热度设置-周期-择日+
    def Setting_userinfo_menu_hot_cycle_back_adddays(self):
        self.Setting_userinfo_menu_hot_cycle_back_adddaysS = self.p.get_element("id->com.yunlu6.stone:id/im_add_days","设置-基本资料-主菜单-热度设置-周期-择日+")
        return self.Setting_userinfo_menu_hot_cycle_back_adddaysS

    #设置:设置-基本资料-主菜单-热度设置-周期-保存
    def Setting_userinfo_menu_hot_cycle_back_save(self):
        self.Setting_userinfo_menu_hot_cycle_back_saveS = self.p.get_element("id->com.yunlu6.stone:id/btn_messagetime_save","设置-基本资料-主菜单-热度设置-周期-保存")
        return self.Setting_userinfo_menu_hot_cycle_back_saveS

# ******************************************************【PAGE3】+时段 Setting_userinfo_menu_hot_addtime******************************************************
    #设置:设置-基本资料-主菜单-热度设置-+时段-确定
    def Setting_userinfo_menu_hot_addtime_confirm(self):
        self.Setting_userinfo_menu_hot_addtime_confirmS = self.p.get_element("id->com.yunlu6.stone:id/tv_dialog_ok","设置-基本资料-主菜单-热度设置-+时段-确定")
        return self.Setting_userinfo_menu_hot_addtime_confirmS

    #设置:设置-基本资料-主菜单-热度设置-+时段-取消
    def Setting_userinfo_menu_hot_addtime_cancel(self):
        self.Setting_userinfo_menu_hot_addtime_cancelS = self.p.get_element("id->com.yunlu6.stone:id/tv_dialog_cancel","设置-基本资料-主菜单-热度设置-+时段-取消")
        return self.Setting_userinfo_menu_hot_addtime_cancelS

    #设置:设置-基本资料-主菜单-热度设置-+时段-早上
    def Setting_userinfo_menu_hot_addtime_zaoshang(self):
        self.Setting_userinfo_menu_hot_addtime_zaoshangS = self.p.get_element("id->com.yunlu6.stone:id/ll_dialog_zaoshang","设置-基本资料-主菜单-热度设置-+时段-早上")
        return self.Setting_userinfo_menu_hot_addtime_zaoshangS

    #设置:设置-基本资料-主菜单-热度设置-+时段-凌晨
    def Setting_userinfo_menu_hot_addtime_lingchen(self):
        self.Setting_userinfo_menu_hot_addtime_lingchenS = self.p.get_element("id->com.yunlu6.stone:id/ll_dialog_lingchen","设置-基本资料-主菜单-热度设置-+时段-凌晨")
        return self.Setting_userinfo_menu_hot_addtime_lingchenS

    #设置:设置-基本资料-主菜单-热度设置-+时段-傍晚
    def Setting_userinfo_menu_hot_addtime_bangwan(self):
        self.Setting_userinfo_menu_hot_addtime_bangwanS = self.p.get_element("id->com.yunlu6.stone:id/ll_dialog_bangwan","设置-基本资料-主菜单-热度设置-+时段-傍晚")
        return self.Setting_userinfo_menu_hot_addtime_bangwanS

    #设置:设置-基本资料-主菜单-热度设置-+时段-晚上
    def Setting_userinfo_menu_hot_addtime_wanshang(self):
        self.Setting_userinfo_menu_hot_addtime_wanshangS = self.p.get_element("id->com.yunlu6.stone:id/ll_dialog_wanshang","设置-基本资料-主菜单-热度设置-+时段-晚上")
        return self.Setting_userinfo_menu_hot_addtime_wanshangS

    #设置:设置-基本资料-主菜单-热度设置-+时段-下午
    def Setting_userinfo_menu_hot_addtime_xiawu(self):
        self.Setting_userinfo_menu_hot_addtime_xiawuS = self.p.get_element("id->com.yunlu6.stone:id/ll_dialog_xiawu","设置-基本资料-主菜单-热度设置-+时段-下午")
        return self.Setting_userinfo_menu_hot_addtime_xiawuS

    #设置:设置-基本资料-主菜单-热度设置-+时段-中午
    def Setting_userinfo_menu_hot_addtime_zhongwu(self):
        self.Setting_userinfo_menu_hot_addtime_zhongwuS = self.p.get_element("id->com.yunlu6.stone:id/ll_dialog_zhongwu","设置-基本资料-主菜单-热度设置-+时段-中午")
        return self.Setting_userinfo_menu_hot_addtime_zhongwuS

    #设置:设置-基本资料-主菜单-热度设置-+时段-上午
    def Setting_userinfo_menu_hot_addtime_shangwu(self):
        self.Setting_userinfo_menu_hot_addtime_shangwuS = self.p.get_element("id->com.yunlu6.stone:id/ll_dialog_shangwu","设置-基本资料-主菜单-热度设置-+时段-上午")
        return self.Setting_userinfo_menu_hot_addtime_shangwuS