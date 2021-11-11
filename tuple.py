"""元组的构造"""
#1. 直接用逗号分割
t1 = 1, 2, 3,
print(type(t1))

#2. 通过小括号填充元素
t2 = (1, 2, "ts", "java", ['a', 'b', 'c'])
print(type(t2), t2)

#3. 通过构造函数tuple
t3 = tuple("python")
print(type(t3), t3)

t4 = tuple([1, 2, 3, 4, "python"])
print(type(t4), t4)

#4. 注意：单元素元组，逗号不可或缺
t5 = 3,
print(type(t5), t5)

#5. 注意：如果没有加逗号，打出来的是int类型
t6 = (3)
print(type(t6), t6)

"""元组的索引"""
t7 = tuple('Harry Potter')
print(t7[3])
print(t7[-2])
print(t7[5])

"""元组的切片 [start: stop: step]"""
print(t7[3:7])
print(t7[3:10:2])
print(t7[-1:-7:-1]) #逆序打印potter

"""元组的常用方法"""
#index(item) 返回与目标元素匹配的第一个元素的索引值
print(t7.index('t'))
#print(t7.index('z')) #ValueError: tuple.index(x): x not in tuple

#count(item) 计算某个元素在元组中出现的次数
print(t7.count('r'))

"""元组的解包"""
#把一个可迭代对象里的元素，一并赋值到对应变量组成的元组中。
tup1 = 1, 2, 3
#1. 传统赋值方式
a = tup1[0]
b = tup1[1]
c = tup1[2]
print(a, b, c)
#2. 解包
a2,  b2, c2 = tup1
print(a2, b2, c2)