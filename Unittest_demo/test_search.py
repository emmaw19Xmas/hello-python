# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/23/2021 9:17 PM
# @Function:
import unittest


class Search():
    def search(self):
        print("search method")
        return 0

class TestSearch(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.s= Search()

    def setUp(self) -> None:
        self.s= Search()

    def test_if0(self):
        #s = Search()
        self.assertEqual(self.s.search(), 0,"verify if the result is 0")

    def test_iflargert2(self):
        #s = Search()
        self.assertGreater(s.search, -2, "verfiy if the result is larger than -2")

        #https://cloud.tencent.com/developer/article/1630094