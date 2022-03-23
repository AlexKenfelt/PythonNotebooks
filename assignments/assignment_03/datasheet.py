from course import Course

class Datasheet () :                            #   Our Datasheet Class.

    #   Our init function for our datasheet class. it takes two arguments, self and a course object.
    def __init__ (self, courses) :
        self.courses = []                       #   Declaring that courses is an array of course objects.
        for course in courses :                 #   Looping through for every new course and setting the values. ->
            new_course = Course (               #   <-
                course.name,                    #   <-
                course.class_room,              #   <-
                course.teacher,                 #   <-
                course.ects,                    #   <-
                course.grade,                   #   <-
            )
            self.courses.append(new_course)     #   Then we're adding every new course to our course array.


    def get_grades_as_list (self) : 
        grades = [courses.grade for courses in self.courses if courses.grade != None]           #   Using list comprehension to get our list of grades from our courses.
        #print('DEBUG: Getting our grades as a list : \n' + grades)                              #   Uncomment me to see what is going on.
        return grades                                                                           #   And then returning said list.


    def get_ects_sum (self) :
        total = sum([course.ects for course in self.courses])
        #print('DEBUG: Getting our ECTS total : \n' + total)  
        return total