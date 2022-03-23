#A student has a data_sheet and a data_sheet has multiple courses in particular order


from notebooks.MyFolder.moduels.week3.assignment3 import datasheet
import datasheet as ds

class Student(datasheet):

    name = ''
    gender = ''
    datasheet = ds.Datasheet
    image_url = ''

    def __init__(self, name, gender, datasheet, image_url):
        self.name = name
        self.gender = gender
        self.datasheet = datasheet
        self.image_url = image_url