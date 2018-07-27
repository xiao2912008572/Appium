__author__ = 'xiaoj'
from YunluFramework.public.pages.yunshi.YUNSHIPAGE3 import YUNSHIPAGE3


class YUNSHIHANDLE1(YUNSHIPAGE3):
    # ******************************************************【HANDLE1】******************************************************
    # 云视：点击
    def YS_click(self):
        return self.p.click(self.YS)

    # 云视-导购赚钱：点击
    def YS_guide_click(self):
        return self.p.click(self.YS_guide)

    # 云视-分享名片
    def YS_share_click(self):
        return self.p.click(self.YS_share)

    # 云视-通知：点击
    def YS_flow_click(self):
        return self.p.click(self.YS_flow)

    # 云视-会话：点击
    def YS_message_click(self):
        return self.p.click(self.YS_message)

    # 云视-购物车：点击
    def YS_shopcart_click(self):
        return self.p.click(self.YS_shopcart)

    # 云视-订单：点击
    def YS_order_click(self):
        return self.p.click(self.YS_order)

    # 云视-定制商品：点击
    def YS_custompro_click(self):
        return self.p.click(self.YS_custompro)

    # 云视-定制企业：点击
    def YS_customecompany_click(self):
        return self.p.click(self.YS_customecompany)