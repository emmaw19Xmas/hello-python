# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/27/2021 10:31 AM
# @Function:

import allure


TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'

@allure.feature("搜索模块")
class TestSearch():
    @allure.link('https://www.youtube.com/watch?v=4YYzUTYZRMU')
    @allure.story("搜索成功")
    def test_case1(self):
        print('200 success')

    @allure.story("搜索失败")
    @allure.link('https://www.youtube.com/watch?v=Su5p2TqZxKU', name='Click me')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_case2(self):
        print('not found anything')

@allure.feature("登录模块")
class TestLogin():
    #allure.attach.file("C:\Users\18635\OneDrive\Pictures\Saved Pictures\冰箱贴.jpg", name="冰箱贴",
                       #attachemnt_type=allure.attachment_type.JPG, extension='.jpg')
    @allure.story("登录成功")
    @allure.issue('140', 'Pytest-flaky test retries shows like test steps')
    def test_login_success(self):
        with allure.step("step1:打开应用"):
            print("打开应用")
        with allure.step("step2:进入登录页面"):
            print("登录页面")
        with allure.step("step3:输入用户名和密码"):
            assert 1==2
            print("输入用户名和密码")
        with allure.step("step4:打开应用"):
            print("这是登录：测试用例， 登陆成功")

    @allure.story("登录失败")
    @allure.testcase(TEST_CASE_LINK, 'Test case title')
    def test_log_fail(self):
        print("打开应用")
        print("登录页面")
        print("输入用户名和密码")
        print("这是登录：测试用例， 登陆失败")