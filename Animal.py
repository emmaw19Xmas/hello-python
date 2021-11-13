class Animal:

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    @classmethod
    def mk_sound(cls):
        print("animal make sound")

    @classmethod
    def run(cls):
        print("the animal run")

