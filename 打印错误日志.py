import logging
import traceback
import sys

try:
    assert 1 == 2
except Exception as e:
    # logging.info(traceback.format_exc())
    print("这是错误回溯信息：", traceback.format_exc() + "结束")
