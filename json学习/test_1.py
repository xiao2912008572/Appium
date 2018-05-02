import logging


print("你好！")
import unittest
class A(unittest.TestCase):
    def test_1(self):
        try:
            try:
                assert 1 == 2
            except AssertionError:
                logging.info("1.内部异常")
                raise AssertionError('内部异常')
        except Exception:
            logging.info("2.外部异常")
            raise Exception("外部异常")    