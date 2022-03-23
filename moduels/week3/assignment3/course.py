# Each course has name, classroom, teacher, ETCS and optional grade if course is taken.

class Course():
    name = ''
    classroom = ''
    teacher = ''
    ETCS = 0
    grade = 0

    def __init__(self, name, classroom, teacher, ETC, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETC = ETC
        self.grade = grade

        

