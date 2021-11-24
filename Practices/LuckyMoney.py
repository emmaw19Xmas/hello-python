# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/20/2021 8:57 PM
# @Function: Regular Lucky Money

"""
1. 群主负责发红包，成员人数平均分，红包金额为整数；
2. 成员负责抢红包，抢到的红包存在余额中。
3. 一轮抢红包之后需要报数，打印格式为"我是XX， 现在有XX钱"
"""
import random


class Owner:

    def __init__(self, balance: int):
        self.balance = balance

    def send_money(self, amount):
        self.balance = self.balance - amount
        print(f"发出了{amount}的红包，群主的余额为{self.balance}")


class Member:
    def __init__(self, balance: int):
        self.balance = balance

    def receive_money(self, amount):
        self.balance = self.balance + amount
        print(f"收到了{amount}的红包，当前成员的余额为{self.balance}")


def host_group(b):
    num_member = random.randint(1, b)
    print(num_member)
    for i in range(1,num_member):
        locals()[f'member{i}'] = Member(random.randint(1,200))
        print(i)




owner1 = Owner(1000)
host_group(4)

