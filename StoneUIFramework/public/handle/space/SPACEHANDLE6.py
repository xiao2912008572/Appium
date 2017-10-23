__author__ = 'xiaoj'
#空间首页
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import SPACEHANDLE5

class SPACEHANDLE6(SPACEHANDLE5):
#***************************************【PAGE4】添加照片-相册Kjlb_browseorgspace_menu_product_new_addphoto_album***************************************
    #  空间列表-浏览企业空间-菜单栏-产品-新建-添加照片-相册-返回:点击
    def Kjlb_browseorgspace_menu_product_new_addphoto_album_back_click(self):
        return self.p.click(self.Kjlb_browseorgspace_menu_product_new_addphoto_album_back)

