__author__ = 'Administrator'
from StoneUIFramework.public.pages.renmai.RENMAIPAGE6 import _RENMAIPAGE6

class _RENMAIPAGE7(_RENMAIPAGE6):
#*********************************【PAGE6】人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像：RMSY_search_label_groupchat_menu_setting_grouphead_head*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像-拍照
    def RMSY_search_label_groupchat_menu_setting_grouphead_head_takephoto(self):
        self.RMSY_search_label_groupchat_menu_setting_grouphead_head_takephotoC = self.p.get_element("id->com.yunlu6.stone:id/tv_cloundlibrary_camera", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像-拍照")
        return self.RMSY_search_label_groupchat_menu_setting_grouphead_head_takephotoC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像-相册
    def RMSY_search_label_groupchat_menu_setting_grouphead_head_album(self):
        self.RMSY_search_label_groupchat_menu_setting_grouphead_head_albumC = self.p.get_element("id->com.yunlu6.stone:id/tv_cloundlibrary_alumm", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像-相册")
        return self.RMSY_search_label_groupchat_menu_setting_grouphead_head_albumC

    #定位：人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像-取消
    def RMSY_search_label_groupchat_menu_setting_grouphead_head_cancel(self):
        self.RMSY_search_label_groupchat_menu_setting_grouphead_head_cancelC = self.p.get_element("id->com.yunlu6.stone:id/bt_commen_cancel", "人脉首页-搜索-标签列表-点击进入群聊-主菜单-设置-群头像-头像-取消")
        return self.RMSY_search_label_groupchat_menu_setting_grouphead_head_cancelC