__author__ = 'Administrator'
from YunluIFramework.public.handle.renmai.RENMAIHANDLE6 import RENMAIHANDLE6

class RENMAIHANDLE7(RENMAIHANDLE6):
#*********************************【PAGE6】人脉首页-搜索-标签列表-点击进入群聊-设置-群头像-头像：RMSY_search_label_groupchat_menu_setting_grouphead_head*********************************
    #定位：人脉首页-搜索-标签列表-点击进入群聊-设置-群头像-头像-拍照：点击
    def RMSY_search_label_groupchat_menu_setting_grouphead_head_takephoto_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_grouphead_head_takephoto)

    #定位：人脉首页-搜索-标签列表-点击进入群聊-设置-群头像-头像-相册：点击
    def RMSY_search_label_groupchat_menu_setting_grouphead_head_album_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_grouphead_head_album)


    #定位：人脉首页-搜索-标签列表-点击进入群聊-设置-群头像-头像-取消：点击
    def RMSY_search_label_groupchat_menu_setting_grouphead_head_cancel_click(self):
        return self.p.click(self.RMSY_search_label_groupchat_menu_setting_grouphead_head_cancel)