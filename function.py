"""定义函数"""
def function_name(a, b):
    '''
    这是一个携带参数和注释的函数
    :param a: 第一个数字
    :param b: 第二个数字
    :return: 两个数字的和
    '''
    print("this is a function demo")
    sum_cum = a +  b
    return sum_cum


print(function_name(2,3))
print(function_name.__doc__) #得到函数内注释的内容
help(function_name)
#位置传参
#关键字传参 function_name(b=3, a=4)
c = function_name(b=3, a=4)
print(c)

#给参数设置默认值, 指定默认值的参数一定要放在最后。 。
def person(name, age, nationality ="China"):
    print(f"名字是{name}")
    if age>18:
        print(f"{name} 是成年人，国籍{nationality}")
    else:
        print(f"{name} 是未成年人, 国籍{nationality}")

person("emma", 28)

person("sydney", 16, "USA")

#默认值要为不可变对象，比如字符串，元组等。不要使用tuple，diction等
def bad_demo(a, b, c=[]):
    c.append(a)
    c.append(b)
    print(a, b, c)

bad_demo(1,2)
bad_demo(100, 200)

"""函数返回值"""
#如果你的函数没有返回值，那么打印结果会得到NONE

"""可变参数"""
#即不定长参数，传入函数中实际的参数可以是任意多个。
#常见的形式 *args **kwargs

"""args 接受任意多个实际参数，并将其放在一个元组中。 使用已经存在的列表或元组作为函数的课变参数，可以在列表名称前加*"""
def print_language(*args):
    print(args)
    for  i in args:
        print(i)

print_language("python","java","php","ruby","go")

lan = ["java","php","ruby"]
print_language(lan)#(['java', 'php', 'ruby'],)   ['java', 'php', 'ruby']
#这种写法是把这个list作为一个元素传进去的。 所以得到的结果不是我们想要的，可以通过添加一个*将其拆分
print_language(*lan)


"""kwarts 接受任意多个类似关键字参数一样显示赋值的实际参数，并将其放到一个字典中。
使用已经存在的字典作为函数的可变参数，在字典前加**"""

def print_info(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k, v)

print_info(Tom=18, Jim=20, Lily=12)

info = {'Tom':18, 'Jim':20, 'Lily':12}
print_info(**info)