"""lambda表达式-创建匿名函数；"""
"""
用处：需要一个函数，但是又不想费神去命名这个函数；
通常在这个函数只使用一次的场景下，可以指定短小的回调函数。
"""
"""
语法：
result = lambda [arg1 [, arg2, .... , argm]]: expression
"""
import logCurrentTime
result = lambda r:math.pi*r*r

print(result(10))

