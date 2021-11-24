# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/23/2021 9:05 PM
# @Function:
import unittest

class TestStringMethods(unittest.TestCase):
    """The setUp() and tearDown() methods allow you to define instructions
    that will be executed before and after each test method.
    They are covered in more detail in the section Organizing test code."""
    def setUp(self) -> None:
        print("set up")

    def tearDown(self) -> None:
        print("tear down")


    """
    A class method called before tests in an individual class are run. 
    setUpClass is called with the class as the only argument and must 
    be decorated as a classmethod():
    """
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")
    """
    A class method called after tests in an individual class have run. 
    tearDownClass is called with the class as the only argument and must
    be decorated as a classmethod():
    """
    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class")

    def test_abc(self):
        print('testabc')
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()