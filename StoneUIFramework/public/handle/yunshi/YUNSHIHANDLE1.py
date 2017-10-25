__author__ = 'xiaoj'
from StoneUIFramework.public.pages.yunshi.YUNSHIPAGE2 import YUNSHIPAGE2


class YUNSHIHANDLE1(YUNSHIPAGE2):
    # ******************************************************【HANDLE1】******************************************************
    # 云视：点击
    def YS_click(self):
        return self.p.click(self.YS)

    # 云视-流程：点击
    def YS_flow_click(self):
        return self.p.click(self.YS_flow)

    # 云视-会话：点击
    def YS_message_click(self):
        return self.p.click(self.YS_message)

    # 云视-会话：点击
    def YS_collection_click(self):
        return self.p.click(self.YS_collection)

    # 云视-订单：点击
    def YS_order_click(self):
        return self.p.click(self.YS_order)
