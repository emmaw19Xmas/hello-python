from Py_OOP_Assignment.Cat import Cat
from Py_OOP_Assignment.Dog import Dog

if __name__ == '__main__':
    tom = Cat(name="Tom", color="灰色",age="10",gender="男")
    tom.catch_mouse()

    goofy = Dog(name="Goofy",color="橘色",age=6, gender="男")
    goofy.guard_house()