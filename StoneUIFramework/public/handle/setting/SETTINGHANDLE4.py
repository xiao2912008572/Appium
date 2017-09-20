__author__ = 'xiaoj'
from StoneUIFramework.public.handle.setting.SETTINGHANDLE3 import _SETTINGHANDLE3

class _SETTINGHANDLE4(_SETTINGHANDLE3):
# ******************************************************【PAGE3】意向地区 Setting_userinfo_menu_shopping_address******************************************************
    #设置:设置-基本资料-主菜单-导购机会-意向地区-返回
    def Setting_userinfo_menu_shopping_address_back_click(self):
        return self.p.click(self.Setting_userinfo_menu_shopping_address_back)

    #设置:设置-基本资料-主菜单-导购机会-意向地区-确认
    def Setting_userinfo_menu_shopping_address_confirm_click(self):
        return self.p.click(self.Setting_userinfo_menu_shopping_address_confirm)

     #设置:设置-基本资料-主菜单-导购机会-意向地区-地区列表
    def Setting_userinfo_menu_shopping_address_alist_click(self,n):
        return self.p.clicks(self.Setting_userinfo_menu_shopping_address_alist,n)

    #设置:设置-基本资料-主菜单-导购机会-意向地区-已选择地区列表
    def Setting_userinfo_menu_shopping_address_hlist_click(self,n):
        return self.p.clicks(self.Setting_userinfo_menu_shopping_address_hlist,n)

# ******************************************************【PAGE3】周期 Setting_userinfo_menu_hot_cycle******************************************************
    #设置:设置-基本资料-主菜单-热度设置-周期-返回
    def Setting_userinfo_menu_hot_cycle_back_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_cycle_back)

    #设置:设置-基本资料-主菜单-热度设置-周期-每天
    def Setting_userinfo_menu_hot_cycle_back_allday_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_cycle_back_allday)

    #设置:设置-基本资料-主菜单-热度设置-周期-工作日
    def Setting_userinfo_menu_hot_cycle_back_workday_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_cycle_back_workday)

    #设置:设置-基本资料-主菜单-热度设置-周期-节假日
    def Setting_userinfo_menu_hot_cycle_back_holiday_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_cycle_back_holiday)

    #设置:设置-基本资料-主菜单-热度设置-周期-择日
    def Setting_userinfo_menu_hot_cycle_back_messday_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_cycle_back_messday)

    #设置:设置-基本资料-主菜单-热度设置-周期-择日+
    def Setting_userinfo_menu_hot_cycle_back_adddays_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_cycle_back_adddays)

    #设置:设置-基本资料-主菜单-热度设置-周期-保存
    def Setting_userinfo_menu_hot_cycle_back_save_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_cycle_back_save)

# ******************************************************【PAGE3】+时段 Setting_userinfo_menu_hot_addtime******************************************************
    #设置:设置-基本资料-主菜单-热度设置-+时段-确定
    def Setting_userinfo_menu_hot_addtime_confirm_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_addtime_confirm)

    #设置:设置-基本资料-主菜单-热度设置-+时段-取消
    def Setting_userinfo_menu_hot_addtime_cancel_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_addtime_cancel)

    #设置:设置-基本资料-主菜单-热度设置-+时段-早上
    def Setting_userinfo_menu_hot_addtime_zaoshang_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_addtime_zaoshang)

    #设置:设置-基本资料-主菜单-热度设置-+时段-凌晨
    def Setting_userinfo_menu_hot_addtime_lingchen_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_addtime_lingchen)

    #设置:设置-基本资料-主菜单-热度设置-+时段-傍晚
    def Setting_userinfo_menu_hot_addtime_bangwan_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_addtime_bangwan)

    #设置:设置-基本资料-主菜单-热度设置-+时段-晚上
    def Setting_userinfo_menu_hot_addtime_wanshang_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_addtime_wanshang)

    #设置:设置-基本资料-主菜单-热度设置-+时段-下午
    def Setting_userinfo_menu_hot_addtime_xiawu_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_addtime_xiawu)

    #设置:设置-基本资料-主菜单-热度设置-+时段-中午
    def Setting_userinfo_menu_hot_addtime_zhongwu_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_addtime_zhongwu)

    #设置:设置-基本资料-主菜单-热度设置-+时段-上午
    def Setting_userinfo_menu_hot_addtime_shangwu_click(self):
        return self.p.click(self.Setting_userinfo_menu_hot_addtime_shangwu)