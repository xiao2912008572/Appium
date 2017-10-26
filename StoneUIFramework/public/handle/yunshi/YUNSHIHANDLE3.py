__author__ = 'xiaoj'
from StoneUIFramework.public.handle.yunshi.YUNSHIHANDLE2 import YUNSHIHANDLE2


class YUNSHIHANDLE3(YUNSHIHANDLE2):
    # ******************************************************【HANDLE2】商品名称列表-点击：YS_order_proname_click******************************************************
    # 云视-订单-商品名称列表-返回：点击
    def YS_order_plist_back_click(self):
        return self.p.click(self.YS_order_plist_back)

    # 云视-订单-商品名称列表-收货人：获取文本
    def YS_order_plist_receive_text(self):
        return self.p.get_text(self.YS_order_plist_receive)

    # 云视-订单-商品名称列表-电话：获取文本
    def YS_order_plist_phone_text(self):
        return self.p.get_text(self.YS_order_plist_phone)

    # 云视-订单-商品名称列表-地址：获取文本
    def YS_order_plist_address_text(self):
        return self.p.get_text(self.YS_order_plist_address)

    # 云视-订单-商品名称列表-商品总价列表：获取文本
    def YS_order_plist_price_text(self,n):
        return self.p.get_texts(self.YS_order_plist_price,n)

    # 云视-订单-商品名称列表-订单总价：获取文本
    def YS_order_plist_amount_text(self):
        return self.p.get_text(self.YS_order_plist_amount)

    # 云视-订单-商品名称列表-订单总价：获取文本
    def YS_order_plist_num_text(self):
        return self.p.get_text(self.YS_order_plist_num)

    # 云视-订单-商品名称列表-联系卖家：点击
    def YS_order_plist_contact_click(self):
        return self.p.click(self.YS_order_plist_contact)

    # 云视-订单-商品名称列表-提醒发货：点击
    def YS_order_plist_remind_click(self):
        return self.p.click(self.YS_order_plist_remind)




