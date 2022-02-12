# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/25/2021 9:25 PM
# @Function: 传统方法编写测试用例

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest


class Test_Add_Contacts():
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            #"platformVersion":'11.0'
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            #设计进入App之后停留在哪一个页面上
            "appActivity": ".launch.WwMainActivity t42",#.launch.LaunchSplashActivity广告页
            "noReset": True, #以防每次测试时重新登录，清空缓存。
            "skipDeviceInitialization": True, #提升启动速度，跳过初始设置；
            "unicodeKeyBorad": True


        }
        #跟server进行连接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        pass

    def test_build_a_trip(self):
        print("添加一个新联系人")
        """
        1. 切换至通讯录界面
        2. 点击添加成员
        3. 点击手动输入添加
        4. 输入名字与电话，点击保存
        5. 返回通讯录界面
        6. 验证新的成员是否显示在界面上
        """
        contactlist_page = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
        contactlist_page.click()
        """
               有时页面上元素过多，添加成员按钮没有立即显示在可视页面上。
               可以通过滑动查找，如果找不到，就进行滑动。通过try方法来避免异常

               def swipe_find(self):
                   num = 3
                   for i in range(num):
                       try:
                           self.driver.find_element_by_xpath("//*[@text='添加成员']")
                       except:#(找不到就滑动)
                       size = self.driver.get_window_size()
                       width = size.get("width")
                       height = size.get("height")
                       start_x = width/2
                       start_y = height * 0.8
                       end_x = start_x
                       end_y = height*0.3
                       self.driver.swipe()
                       if i == 3:#如果找了3次还没有，就停下报错
                            raise NoSuchElementException(f"找了{num}次，未找到")
                   
        """

        add_button = self.driver.find_element_by_xpath("//*[@text='添加成员']")
        add_button.click()
        print("点击添加成员")



        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.TextView")
        el3.click()
        el4 = self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../*[@text='必填']")
        el4.send_keys("韩梅梅")
        print("添加韩梅梅")
        el5 = self.driver.find_element_by_xpath("//*[contains(@text,'手机')]/..//*[@text='必填']")
        el5.send_keys("18634567890")
        print("添加韩梅梅的电话号码")
        el6 = self.driver.find_element_by_xpath("//*[@text='保存']")
        el6.click()
        el7 = self.driver.find_element_by_id("com.tencent.wework:id/kao")
        el7.click()
        print("保存完毕")
        els1 = self.driver.find_elements_by_accessibility_id("com.tencent.wework:id/c1_")
        print("开始验证")

        while True:
            if "韩梅梅" in self.driver.page_source:
                #print(self.driver.page_source)
                break
        """
        另一个验证方法,通过对添加成功弹窗信息的捕捉，来验证是否添加成功
        result = self.driver.find_element(MobileBy.XPATH, //*[@class='android.widget.Toast']).get_attribute("text")
        assert result == "添加成功"
        """



"""
tips：
1.尽量不要用resource id，因为它是动态的。
2.谨慎使用donStopAppOnReset,在启动app的时候不关闭app
3.找AppActivity时使用：adb logcat ActivityManager:I | findstr "cmp" 通过日志找到启动页
"""

