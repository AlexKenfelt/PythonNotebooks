import datasheet as ds

class Student () :

    def __init__ (self, name, gender, datasheet, image_url) :
        self.name = name
        self.gender = gender
        self.datasheet = datasheet
        self.image_url = image_url

    def get_avg_grade (self) :
        grade = self.datasheet.get_grades_as_list()
        return sum(grade) / len(grade)

    def show_progression (self) :
        max_value = len(self.datasheet.courses) * 150
        ects_sum = self.datasheet.get_ects_sum()
        return ects_sum / max_value * 100