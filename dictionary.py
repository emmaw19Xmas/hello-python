"""字典的创建"""
#1. 使用大括号 {"key:value, key:value..."}
dic1 = {"name":"emma", "age":18}
dic2 = {}
print(type(dic1),dic1)
print(type(dic2),dic2)

#2. dict构造方法 dict([(tuple key, value)])
dic3 = dict([("name", "emma"),("age", 123)])
print(type(dic3),dic3)
#3. 使用字典的推导式 in之后的内容仍为tuple
dic4 = {k: v for k, v in [("name", "emma"),("age", 123)]}
print(type(dic4),dic4)

"""访问元素"""
#使用中括号的key
print(dic4['name'])

"""字典使用"""
dic3['age']=28
print(dic3)

"""嵌套字典"""
dic4={"name":"emma", "age":18,"course": {"magic":90, "python":80}}
print(dic4['course']['magic'])
dic4['course']['python']=10
print(dic4)

"""常用方法"""
#1. keys, values, items 返回字典建组成的新视图对象
print(dic4.keys())
print(dic4.values())
print(dic4.items())

print(list(dic4.keys()))
print(list(dic4.values()))
print(list(dic4.items()))

#2. get() 获取指定key关联的value值。 入参：key，必传。 返回：如果key存在于字典中，返回key关联的value值。如果key不存在，返回none
#好处:不需要担心key是否存在，永远不会引发keyerror错误
course =  dic4.get('course')
print(course) #{'magic': 90, 'python': 10}
course =  dic4.get('magic')
print(course) #None
course =  dic4.get('course').get('magic')
print(course) #90

#update() 使用来自dic的键/值更新字典，覆盖原有的值。入参；dc字典对象，必传
print(dic4)
dic4.update({"hobby":"cooking", "course":{"magic":90, "python":100}})
print(dic4)
print("------------------------------------------------")
#pop() 删除指定key的键值对，并返回对应的value值。 入参：key必传。返回：如果key在字典中，则将其移除并返回value值，如果key不在字典中，则会引发keyerror
#已经存在的key
val = dic4.pop('age')
print(dic4, val)
#不存在的key
#val2 = dic4.pop('few')
#print(dic4, val2)

"""练习：将key和value分别进行对调"""
dict = {'a':1,'b':2,'c':3,'d':4}
new_dict = {v:k for k,v in dict.items()}
print(new_dict)