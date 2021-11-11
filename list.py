"""列表使用：创建"""
#1. 构造方法 list()
li = list()
print(type(li), li)

li1 = list("李斯特")
print(type(li1), li1)

#2. 中括号填充元素【】
li2 = ["3", "4", "李斯特", "#$%^"]
print(type(li2), li2)
#3. 列表推导式
li3 = [i for i in range(1,30) if i%2 == 0]
print(type(li3), li3)

"""列表使用：索引"""
print(li2[2])

"""列表使用：切片 list[start:stop:step]"""
li4 = li3[10:20:3]
print(li4)
print(li3[:4])
print(li3[::4])
print(li3[::-1]) #逆序打印

#[22, 28]
#[2, 4, 6, 8]
#[2, 10, 18, 26]
#[28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

"""列表使用：其他用法"""
#+
print(li2 + li4)
#*
print(li2 * 3)

#in
print( 3 in li3)

#not in
print(4 not in li4)

#append(item) 将一个itemui想添加到列表的末尾
print(li2)
li2.append("100")
print(li2)

#extend(iterable)
li2.extend("hellow")
print(len(li2), li2)
#11 ['3', '4', '李斯特', '#$%^', '100', 'h', 'e', 'l', 'l', 'o', 'w']

#insert(index, item) 将一个对象插入到指定的索引位置
li2.insert(8, "divide")
print(li2)

#pop(index) 弹出并返会指定的数
pop_n = li2.pop(8)
print(pop_n, li2)

#remove(item) 移除列表中第一个等于item的元素
li5 =[1,2,3,4,5,6,6,6,6,2]
li5.remove(2)
print(li5)

#sort(key=None, reverse=False)
li5.sort(reverse=True)
print(li5)

li6 = ["emma","shane","hogwarts","python","java"]
li6.sort(key=len)
print(li6)

#nested list
li7 = [li6, li4]
print("l7", li7)
print(li7[0][1]) #打印li7里第一个元素里的第二个元素

"""列表推导式"""
"""将 1-10 中所有偶数平方之后组成新的列表"""
new_l = [x ** 2 for x in range(1,11) if x % 2 == 0]
print(new_l)