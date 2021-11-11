"""集合创建"""
#1. 通过{}创建
set1 = {1,2,3,4,"programmer", "#$%@", True}
print(set1, type(set1))
#2. 通过set()
set2 = set('programmer')
print(set2, type(set2))
set3 = set([1, 3, 5, 7, 9])
print(set3, type(set3))
set4 = set()
print(set4, type(set4))

#3. 通过集合推导式
set5 = {i for i in range(1,10)}
print(set5, type(set5))

"""集合使用：成员检测"""
print(1 in set5)
print(100 in set5)
print("p" not in set1)


"""集合方法"""
#add(item) to the set
set5.add("harry potter")
print(set5)

#update(iterable) 批量添加课迭代对象中的所有元素
set5.update("emma")
print(set5)

#remove(item) 从集合中移除指定的元素
set5.remove("e")
print(set5)
#set5.remove(100) #报错


#discard(item) 从集合中移除指定的元素，如果元素不在，也不会报错
print(set5.discard(100))

#pop() 随机从集合中移除并返回一个元素, 返回被删除的元素，如果集合为空会引发KeyError
print(set5.pop())
print(set5)

#clear() 清空集合，移除所有元素

#set6 = set5.clear()
#print(set6) #None 函数的返回值
#print(set5) #set() 本身

"""集合运算"""
# 交集 intersection() &
print(set3.intersection(set5))
print(set3 & set5)
# 并集 unioni() |
print(set3.union(set5))
print(set3 | set5)
# 查缉 difference() -
print(set3.difference(set5))
print(set3-set5)


"""集合推导式"""
#harrypotter里和hellowworld里有那些相同字母
set6 = {x for x in "harry potter" if x in "hellow world"}
print(set6)