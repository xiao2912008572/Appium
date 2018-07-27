__author__ = 'xiaoj'
from YunluFramework.public.handle.yunshi.YUNSHIHANDLE1 import YUNSHIHANDLE1


class YUNSHIHANDLE2(YUNSHIHANDLE1):
    # ******************************************************【HANDLE1】******************************************************
    # 云视-订单-返回：点击
    def YS_order_back_click(self):
        return self.p.click(self.YS_order_back)

    # 云视-订单-全部：点击
    def YS_order_all_click(self):
        return self.p.click(self.YS_order_all)

    # 云视-订单-全部：元素获取
    def YS_order_all_element(self):
        return self.p.get_element(self.YS_order_allE[0],
                                  self.YS_order_allE[1])

    # 云视-订单-待付款：点击
    def YS_order_waitforpay_click(self):
        return self.p.click(self.YS_order_waitforpay)

    # 云视-订单-待付款：元素获取
    def YS_order_waitforpay_element(self):
        return self.p.get_element(self.YS_order_waitforpayE[0],
                                  self.YS_order_waitforpayE[1])

    # 云视-订单-待发货：点击
    def YS_order_waitforsend_click(self):
        return self.p.click(self.YS_order_waitforsend)

    # 云视-订单-待发货：元素获取
    def YS_order_waitforsend_element(self):
        return self.p.get_element(self.YS_order_waitforsendE[0],
                                  self.YS_order_waitforsendE[1])

    # 云视-订单-已发货：点击
    def YS_order_alreadysend_click(self):
        return self.p.click(self.YS_order_alreadysend)

    # 云视-订单-已发货：元素获取
    def YS_order_alreadysend_element(self):
        return self.p.get_element(self.YS_order_alreadysendE[0],
                                  self.YS_order_alreadysendE[1])

    # 云视-订单-退款中：点击
    def YS_order_refund_click(self):
        return self.p.click(self.YS_order_refund)

    # 云视-订单-退款中：元素获取
    def YS_order_refund_element(self):
        return self.p.get_element(self.YS_order_refundE[0],
                                  self.YS_order_refundE[1])

    # 云视-订单-待评价：点击
    def YS_order_evaluate_click(self):
        return self.p.click(self.YS_order_evaluate)

    # 云视-订单-待评价：元素获取
    def YS_order_evaluate_element(self):
        return self.p.get_element(self.YS_order_evaluateE[0],
                                  self.YS_order_evaluateE[1])

    # 云视-订单-机构名称列表：文本获取
    def YS_order_orgname_text(self, n):
        return self.p.get_texts(self.YS_order_orgname, n)

    # 云视-订单-机构名称列表：点击
    def YS_order_orgname_click(self, n):
        return self.p.clicks(self.YS_order_orgname, n)

    # 云视-订单-机构名称列表-返回：点击
    def YS_order_orgname_back_click(self):
        return self.p.click(self.YS_order_orgname_back)

    # 云视-订单-商品名称列表：文本获取
    def YS_order_proname_text(self, n):
        return self.p.get_texts(self.YS_order_orgname, n)

    # 云视-订单-商品名称列表：点击
    def YS_order_proname_click(self, n):
        return self.p.clicks(self.YS_order_proname, n)

    # 云视-订单-付款：点击
    def YS_order_pay_click(self):
        return self.p.click(self.YS_order_pay)

    # 云视-订单-取消订单：点击
    def YS_order_cancel_click(self):
        return self.p.click(self.YS_order_cancel)

    # 云视-订单-联系卖家：点击
    def YS_order_contact_click(self):
        return self.p.click(self.YS_order_contact)

    # 云视-订单-提醒发货：点击
    def YS_order_remind_click(self):
        return self.p.click(self.YS_order_remind)

    # 云视-订单-确认收货：点击
    def YS_order_confirm_click(self):
        return self.p.click(self.YS_order_confirm)

    # 云视-订单-确认收货-是：点击
    def YS_order_confirm_y_click(self):
        return self.p.click(self.YS_order_confirm_y)

    # 云视-订单-确认收货-否：点击
    def YS_order_confirm_n_click(self):
        return self.p.click(self.YS_order_confirm_n)

    # 云视-订单-查看物流：点击
    def YS_order_logistics_click(self):
        return self.p.click(self.YS_order_logistics)

    # 云视-订单-查看物流-运单编号：获取文本
    def YS_order_logistics_num_text(self):
        return self.p.get_text(self.YS_order_logistics_num)

    # 云视-订单-查看物流-返回：点击
    def YS_order_logistics_back_click(self):
        return self.p.click(self.YS_order_logistics_back)



















