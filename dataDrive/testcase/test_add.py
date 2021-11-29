# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/27/2021 8:55 AM
# @Function:
# test_add.py 文件内容
import pytest
import openpyxl

def get_excel():
    book = openpyxl.load_workbook("../data/param.xlsx")
    sheet = book.active
    cells = sheet["A1":"C3"]
    print(cells)
    values = []
    for row in cells:
        data = []
        for cell in row:
            data.append(cell.value)
        values.append(data)
    print(values)
    return values

class TestWithEXCEL:
     @pytest.mark.parametrize('x,y,expected', [[1,2,4]])
     def test_add(self, x, y, expected):
         assert my_add(int(x), int(y)) == int(expected)