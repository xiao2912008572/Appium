__author__ = 'xiaoj'
import os
from StoneUIFramework.public.common.readconfig import Config

class GlobalParam():
    def __init__(self,folder,file):
        self.BASE_DIR = os.path.dirname(os.path.dirname(__file__)) #获取当前文件夹的父目录绝对路径
        self.file_path = os.path.join(self.BASE_DIR,folder,file) #获取config文件夹中的的path_file.conf文件————截图和日志配置文件路径

    def getParam(self,path_Section,path_NO):
        #创建读取配置文件的对象
        cf1 = Config(self.file_path)
        path = cf1.get_PATH(path_Section,path_NO)
        path = self.BASE_DIR + path #将父目录和配置文件读取的相对路径拼接
        return path



