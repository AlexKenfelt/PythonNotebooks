import random

class Course ():

    def __init__(self, name, class_room, teacher, ects, grade=None):
        self.name = name
        self.class_room = class_room
        self.teacher = teacher
        self.ects = ects
        self.grade = grade

    def set_rand_grade(self):
        grades = [0, 2, 4, 7, 10, 12]
        self.grade = random.choice(grades)