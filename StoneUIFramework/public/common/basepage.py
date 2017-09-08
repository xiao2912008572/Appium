#coding=utf-8
__author__ = 'xiaoj'
from StoneUIFramework.public.common.pyappium import PyAppium

class Page(object):
    """
    This is a base page class for Page Object.
    """
    def __init__(self,driver):
        self.driver = driver
        self.p = PyAppium(self.driver)



