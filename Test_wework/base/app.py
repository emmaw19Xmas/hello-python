# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/27/2021 11:43 AM
# @Function: this is the base for WEWORK APP

"""
管理APP相关的操作；
1. 启动app
2. 关闭app
3. 重启app

"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest

from Test_wework.page.MainPage import MainPage


class App:
    def start(self):
        desired_caps = {
            "platformName": "Android",
            # "platformVersion":'11.0'
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            # 设计进入App之后停留在哪一个页面上
            "appActivity": ".launch.WwMainActivity t42",  # .launch.LaunchSplashActivity广告页
            "noReset": True,  # 以防每次测试时重新登录，清空缓存。
            "skipDeviceInitialization": True,  # 提升启动速度，跳过初始设置；
            "unicodeKeyBorad": True

        }
        # 跟server进行连接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)

        return self

    def restart(self):
        self.driver.quit()

    def stop(self):
        pass
    '''
    '''
    """
    """

    def goto_main(self):
        return MainPage(self.driver)  # MainPage应该被创建在po level, 即page level

    def page_source(self):
        return self.driver.page_source
