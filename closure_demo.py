# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/20/2021 4:44 PM
# @Function:

# 1. 闭包的内部函数中，对外部作用域的变量进行引用 ----innner里可以引用外部的grade函数
# 2. 闭包无法修改外部函数的局部变量 ----
# 3. 闭包可以保存当前的运行环境。



#年级是一个会变化的属性，那么我们可以把grade的值拿出来，放在外部，然后在引用时做修改。
def output_student(grade):
    #grade = 3
    def inner(name, gender):
        print(f"hogwarts new year starts! student name is {name}, gender is {gender}, grade is {grade}")
    return inner

student = output_student(1)
student("rone", 'male')
student("harry", "male")
student("hermione","female")