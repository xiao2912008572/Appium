__author__ = 'xiaoj'
import configparser

class Config:
    def __init__(self,configPath):
        self.configPath = configPath

    def get_PATH(self,path_Section,path_NO):
        cf = configparser.ConfigParser()
        cf.read(self.configPath)

        # path_section填写"PATH_YUNKU"
        # 此处path_config = "path_001"以此类推
        path = cf.get(path_Section,path_NO)
        return path

