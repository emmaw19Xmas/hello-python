from Py_OOP_Assignment.Animal import Animal


class Dog(Animal):
    hair = "长"
    def __init__(self,name, color, age, gender):
        super().__init__(name,color,age,gender)

    def guard_house(self):
        print(f"doggy {self.name} is watching you.它{self.age}岁,{self.hair}毛狗")

    def mk_sound(cls):
        print("汪汪汪")