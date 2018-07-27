import unittest
from StoneUIFramework.runcase.suitefactory import SuiteFactory

#测试用例：控制器
class SuiteController(SuiteFactory):
    def chooseSuite(self, index_F=None, index_S=None, all=None):
        # 1.跑全部测试用例
        if all == "ALL" and index_F == None and index_S == None:
            return unittest.TestSuite(self.suiteLoader())
        # 2.跑指定的某个测试用例
        else:
            return unittest.TestSuite(self.suiteLoader()[index_F - 1:index_S])

# if __name__ == "__main__":
#     SC = SuiteController()
#     suiteA = SC.chooseSuite(1, 2, 'ALL')  # 所有用例
#     unittest.TextTestRunner(verbosity=2).run(suiteA)
