from human import Human

class Student(Human):
    def __init__(self, name, age, sex, mark, alive):
        self.mark = mark


    def study(self):
        pass

    def __str__(self):
        return f"{self.name}: age = {self.age};"\
                f"sex = {self.sex};"\
                f"mark = {self.mark};"\
                f"alive = {self.alive}"