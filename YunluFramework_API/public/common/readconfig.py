import configparser

class Config:
    def __init__(self,configPath):
        self.configPath = configPath

    def get_PATH(self,path_Section,path_NO):
        cf = configparser.ConfigParser()
        '''
        与master不一样的地方，加入了encoding=utf-8
        '''
        cf.read(self.configPath,encoding='utf-8')

        # path_section填写"PATH_YUNKU"
        # 此处path_config = "path_001"以此类推
        path = cf.get(path_Section,path_NO)
        return path

# a = Config(configPath='/Users/xiaojingyuan/PycharmProjects/Appium/YunluFramework_API/config/path_file.conf')
# path_1 = a.get_PATH('workspace','path')

