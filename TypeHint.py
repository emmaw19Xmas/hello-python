"""类型提示的作用"""
from typing import List

"""用法一：为参数与返回数据指定类型"""


# 第一个name后面的str代表name的类型
# 第二个->后面的str代表返回的内容的类型
def greeting(name: str) -> str:
    return "Hello" + name.split(',')[1]


print(greeting("Python, Java"))

"""用法二：为类型起别名"""
Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


print(scale(1.1, [1.2, 4, 43.3]))
#print(scale("A",[1.2, 4, 43.3]))

"""用法三；自定义类型"""
class Student:
    name: str
    age: int

def get_stu(name: str) -> Student:
    return Student()

get_stu("Harry").age

"""用法四：静态代码检查"""
#需要安装mypy
import mypy
a: List[int] =[]
a = [1,2,3]

#PS D:\Python_H> mypy TypeHint.py
#Success: no issues found in 1 source file

