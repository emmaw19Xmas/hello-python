# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/27/2021 9:21 AM
# @Function:
import csv

def get_csv():
    with open("data.csv",'r') as file:
        row = csv.reader(file)

        for line in row:
            print(line)

if __name__ == '__main__':
    get_csv()