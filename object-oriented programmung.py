class Person:
    name = "default"
    age = 0
    weight = 0


    # def set_param(self, name):
    #     self.name = name
#如果每个参数都这么设置会很麻烦,所以引出了python的构造方法
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight




    def eat(self):
        print("eating")

    def play(self):
        print("paying")


#实例化
# zs.set_param() = "张三"
person1 = Person("emma",19, 100)
print(f"person1的姓名是{person1.name},年龄是{person1.age}，体重是{person1.weight}")