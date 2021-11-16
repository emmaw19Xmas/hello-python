# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/15/2021 7:26 PM
# @Function:

import re
'''
prog: 正则对象，可以直接调用匹配、替换、分割的方法，不需要再传入正则表达式；
pattern：正则表达式
flags：可选，控制匹配的方式：
    -A: 只进行ASCII匹配；
    -I: 不区分大小写
    -M: 将^和$用于包括这弓字符串的开始和结尾的每一行
    -S: 使用（.)字符匹配所有的字符，包括换行符；
    -X: 忽略模式字符串中未转义的空格和注释

re.match(pattern, string, [flags]) 从字符串的开始处进行匹配
re.search(pattern, string, [flags]) 在整个字符串中搜索第一个匹配的值
re.findall(pattern, string, [flags]) 在整个字符串中搜索所有符合的字符串，并返回列表
'''
#compile() 将字符串转换为正则表达式对象。
#匹配包含harry的字符串
pattern = r"Har\w+"
#转换为正则对象
prog = re.compile(pattern)
print(type(prog)) #<class 're.Pattern'>

s1 = "Harry potter is from Hogwarts, and another person called Harrison is watching the movie"

match1 = re.match(pattern, s1, re.I)

print(match1)
print(f"第一句的匹配值的起始与结束位置为{match1.start()}和{match1.end()}")
print(f"第一句的匹配值的元组为{match1.span()}")
print(f"第一句的匹配值的字符串为{match1.string}")
print(f"第一句的匹配值的数据为{match1.group()}")




match1_2 = re.search(pattern, s1, re.I)
match1_3 = re.findall(pattern, s1, re.I)
print(match1_2)
print(match1_3)
print("==============================")
s2 = "Emma is Harry's friend"
match2 = re.match(pattern, s2, re.I)
print(match2)
match2_2 = re.search(pattern, s1, re.I)
match2_3 = re.findall(pattern, s1, re.I)
print(match2_2)
print(match2_3)

print("==============================")
"""
sub() 实现字符串替换,返回一个字符串
re.sub(pattern, repl(要替换的字符串)，
        string(要被替换的原始字符串)，
        count(可选，表示要替换的最大次数，默认值为0，替换所有匹配)
        flags(可选，控制匹配方式))
"""
pattern2=r"垃圾"
message = "你玩得很垃圾,你垃圾分类了吗"
result = re.sub(pattern2, repl ="**", string = message, count=1)
print(result)

print("==============================")
"""
split(): 根据正则表达式分割字符串，返回列表

re.split(pattern:re表达式；
         string: 要匹配的字符串；
         maxsplit: 可选，表示最大拆分次数；
         flags)
"""
url = "https://developers.google.com/edu/python/regular-expressions"
pattern3 = r"[/|:]"
result = re.split(pattern3, url)
print(result)