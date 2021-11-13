from Py_OOP_Assignment.Animal import Animal


class Cat(Animal):
    hair = "短"
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)

    def catch_mouse(self):
        print(f"{self.color}的猫猫{self.name}捉到了老鼠,它{self.age}岁了，是{self.hair}毛猫")

    @classmethod
    def mk_sound(cls):
        print("喵喵喵")
        """要点2 - 类方法内，不可以直接调用实例方法以及实例变量"""
        #cls.catch_mouse() #TypeError: catch_mouse() missing 1 required positional argument: 'self'

    @staticmethod
    def static_demo(param1):
        print("this is a static method", param1)

"""要点1 - 类，可以直接调用类方法和类变量： 类。方法名"""
#Cat.catch_mouse() #TypeError: catch_mouse() missing 1 required positional argument: 'self'
Cat.mk_sound()
print(Cat.hair)

Cat.static_demo("test")
tom = Cat(name="Tom", color="灰色",age="10",gender="男")
tom.static_demo("thisistom")