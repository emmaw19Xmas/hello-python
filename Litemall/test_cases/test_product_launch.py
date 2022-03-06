# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 3/5/2022 2:24 PM
# @Function:
from Litemall.page_objects.login_page import LoginPage


class TestProductLaunch:
    def test_product_launch(self):
        name = LoginPage().\
            login().\
            go_to_product_launch().\
            product_launch().\
            get_product_name()
        assert name == "1234"