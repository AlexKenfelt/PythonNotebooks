from course import Course
from datasheet import Datasheet
from student import Student
import random

course_list = []
course_list.append(Course("English", "Class-0B", "Christian", 50, 2))
course_list.append(Course("Soccer", "Class-10A", "Dorea", 160, 12))
course_list.append(Course("Religion", "Class-3G", "Nora", 10, 7))

d1 = Datasheet(course_list)

student1 = Student("Theis", "Male", d1, "www.google.com")
student2 = Student("Marie", "Female", d1, "www.facebook.com")

print(student2.show_progression())

print(d1.get_grades_as_list())
print(student2.get_avg_grade())

url_list = []
url_list.append('www.dr.dk/ramasjang')
url_list.append('www.nickelodeon.dk')

names = ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan", "Aazaan", "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul", "Abdul-Aziz", "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "Abdul-Majeed", "Abdulmalik", "Abdul-Rehman", "Abdur", "Abdurraheem", "Abdur-Rahman", "Abdur-Rehmaan", "Abel", "Abhinav", "Abhisumant", "Abid", "Abir", "Abraham", "Abu", "Abubakar", "Ace", "Adain", "Adam", "Adam-James", "Addison", "Addisson", "Adegbola", "Adegbolahan", "Aden", "Adenn", "Adie", "Adil", "Aditya", "Adnan", "Adrian", "Adrien", "Aedan", "Aedin", "Aedyn", "Aeron", "Afonso", "Ahmad", "Ahmed", "Ahmed-Aziz", "Ahoua", "Ahtasham", "Aiadan", "Aidan", "Aiden", "Aiden-Jack", "Aiden-Vee", "Aidian", "Aidy", "Ailin", "Aiman", "Ainsley", "Ainslie", "Airen", "Airidas", "Airlie", "AJ", "Ajay", "A-Jay", "Ajayraj", "Akan", "Akram", "Al", "Ala", "Alan", "Alanas", "Alasdair", "Alastair", "Alber", "Albert", "Albie", "Aldred", "Alec", "Aled", "Aleem", "Aleksandar", "Aleksander", "Aleksandr", "Aleksandrs", "Alekzander", "Alessandro", "Alessio", "Alex", "Alexander", "Alexei", "Alexx", "Alexzander", "Alf", "Alfee", "Alfie", "Alfred", "Alfy", "Alhaji", "Al-Hassan", "Ali", "Aliekber", "Alieu", "Alihaider", "Alisdair", "Alishan", "Alistair", "Alistar", "Alister", "Aliyaan", "Allan", "Allan-Laiton", "Allen", "Allesandro", "Allister", "Ally", "Alphonse", "Altyiab", "Alum", "Alvern", "Alvin"]

def generate_students(amount, name_list, courses, img_url_list):
    genders = ['Male', 'Female']
    index = 0
    students = []
    while index <= amount:
        randCourseArray = []
        randCourse = random.choice(courses)
        randCourse.set_rand_grade()
        randCourseArray.append(randCourse)
        currentStud = Student(
            random.choice(name_list),
            random.choice(genders),
            Datasheet(randCourseArray),
            random.choice(img_url_list)
        )
        students.append(currentStud)  
        index += 1    
    return students[0].name

print(generate_students(5, names, course_list, url_list))