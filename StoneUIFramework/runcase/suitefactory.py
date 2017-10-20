from StoneUIFramework.runcase import *

#测试用例：工厂
class SuiteFactory():
    def suiteLoader(self):
        # ----------------------------------【云库-测试用例】----------------------------------
        yunku_uploadPic_01 = unittest.TestLoader().loadTestsFromTestCase(yunku_UploadPic)                   # test1_1 云库上传图片
        yunku_EditPic_01 = unittest.TestLoader().loadTestsFromTestCase(yunku_EditPic)                       # test2_1 云库编辑图片
        # suite.addTest(yunku_FenLei("test_fenlei"))#云库分类到产品库
        # suite.addTest(yunku_GongSi("test_gongsi"))#云库分类到公司档
        # suite.addTest(yunku_Edit("test_edit"))#云库编辑图片信息

        # ----------------------------------【人脉-测试用例】----------------------------------
        # suite.addTest(contact_Add("test_addContact"))                                                     #人脉添加
        # suite.addTest(contact_Browse("test_borwseContact"))                                               #人脉浏览
        # suite.addTest(contact_Del("test_delContact"))                                                     #人脉删除——— 需要手动从黑名单中删除
        # suite.addTest(contact_Exc("test_excContact"))                                                     #人脉换名片
        # suite.addTest(contact_Label("test_labelContact"))                                                 #打标签

        # ----------------------------------【空间-测试用例】----------------------------------
        # @机构空间
        sapce_CreateO_01 = unittest.TestLoader().loadTestsFromTestCase(space_CreateO)                       # test1_1 创建机构空间
        space_ProductO_01 = unittest.TestLoader().loadTestsFromTestCase(space_ProductO)                     # test2_1 上下架产品
        space_AssignO_01 = unittest.TestLoader().loadTestsFromTestCase(team_AssignO)                        # test3_1 团队认识任免
        space_ArchiviesO_01 = unittest.TestLoader().loadTestsFromTestCase(space_ArchiviesO)                 # test4_1 资讯发布
        space_BusinessCardO_01 = unittest.TestLoader().loadTestsFromTestCase(space_BusinessCardO)           # test5_1 编辑企业名片
        # @私人空间
        perspace_CreateP_01 = unittest.TestLoader().loadTestsFromTestCase(perspace_CreateP)                 # test1_1 创建私人空间
        perspace_NewFloderP_01 = unittest.TestLoader().loadTestsFromTestCase(perspace_NewFloderP)           # test1_2 创建私人空间文件夹
        # @协会空间
        ascspace_CreateA_01 = unittest.TestLoader().loadTestsFromTestCase(ascspace_CreateA)                 # test1_1 创建协会空间
        space_EditA_01 = unittest.TestLoader().loadTestsFromTestCase(space_EditA)                           # test2_1 编辑
        team_AssignA_01 = unittest.TestLoader().loadTestsFromTestCase(team_AssignA)                         # test3_1 团队人事任免
        AddAtoPRefuseA_01 = unittest.TestLoader().loadTestsFromTestCase(AddAtoPRefuseA)                     # test5_1 加会员_管理员_个人_拒绝
        AddPtoPRefuseA_01 = unittest.TestLoader().loadTestsFromTestCase(AddPtoPRefuseA)                     # test5_2 加会员_个人_个人_拒绝
        AddAtoPAgreeA_01 = unittest.TestLoader().loadTestsFromTestCase(AddAtoPAgreeA)                       # test5_3 加会员_管理员_个人_同意
        AddPtoPAgreeA_01 = unittest.TestLoader().loadTestsFromTestCase(AddPtoPAgreeA)                       # test5_4 加会员_个人_个人_同意
        AddAtoORefuseA_01 = unittest.TestLoader().loadTestsFromTestCase(AddAtoORefuseA)                     # test5_5 加会员_管理员_企业_拒绝
        AddPtoORefuseA_01 = unittest.TestLoader().loadTestsFromTestCase(AddPtoORefuseA)                     # test5_6 加会员_个人_企业_拒绝
        AddAtoOAgreeA_01 = unittest.TestLoader().loadTestsFromTestCase(AddAtoOAgreeA)                       # test5_6 加会员_管理员_企业_同意
        AddPtoOAgreeA_01 = unittest.TestLoader().loadTestsFromTestCase(AddPtoOAgreeA)                       # test5_6 加会员_管理员_企业_同意
        space_ArchiviesA_01 = unittest.TestLoader().loadTestsFromTestCase(space_ArchiviesA)                 # test6_1 资讯发布

        self.suite = [
            # ----------------------------------【云库-测试用例：2】----------------------------------
            yunku_uploadPic_01,                                                                             # test1_1 云库上传图片
            yunku_EditPic_01,                                                                               # test2_1 云库编辑图片
            # ----------------------------------【空间-测试用例:19】----------------------------------
            # --------------------@机构空间:5--------------------
            sapce_CreateO_01,                                                                               # test1_1 创建机构空间
            space_ProductO_01,                                                                              # test2_1 上下架产品
            space_AssignO_01,                                                                               # test3_1 团队认识任免
            space_ArchiviesO_01,                                                                            # test4_1 资讯发布
            space_BusinessCardO_01,                                                                         # test5_1 编辑企业名片
            # --------------------@私人空间：2--------------------
            perspace_CreateP_01,                                                                            # test1_1 创建私人空间
            perspace_NewFloderP_01,                                                                         # test1_2 创建私人空间文件夹
            # --------------------@协会空间:12--------------------
            ascspace_CreateA_01,                                                                            # test1_1 创建协会空间
            space_EditA_01,                                                                                 # test2_1 编辑
            team_AssignA_01,                                                                                # test3_1 团队人事任免
            AddAtoPRefuseA_01,                                                                              # test5_1 加会员_管理员_个人_拒绝
            AddPtoPRefuseA_01,                                                                              # test5_2 加会员_个人_个人_拒绝
            AddAtoPAgreeA_01,                                                                               # test5_3 加会员_管理员_个人_同意
            AddPtoPAgreeA_01,                                                                               # test5_4 加会员_个人_个人_同意
            AddAtoORefuseA_01,                                                                              # test5_5 加会员_管理员_企业_拒绝
            AddPtoORefuseA_01,                                                                              # test5_6 加会员_个人_企业_拒绝
            AddAtoOAgreeA_01,                                                                               # test5_6 加会员_管理员_企业_同意
            AddPtoOAgreeA_01,                                                                               # test5_6 加会员_管理员_企业_同意
            space_ArchiviesA_01,                                                                            # test6_1 资讯发布
        ]
        return self.suite
