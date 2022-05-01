"""
1. Create 3 classes: Student, DataSheet and Course
2. A student has a data_sheet and a data_sheet has multiple courses in particular order
3. Each course has name, classroom, teacher, ETCS and optional grade if course is taken.
4. In Student create init() so that a Student can be initiated with name, gender, data_sheet and image_url
5. In DataSheet create a method to get_grades_as_list()
In student create a method: get_avg_grade()
Create a function that can generate n number of students with random: name, gender, courses (from a fixed list of course names), grades, img_url
Let the function write the result to a csv file with format stud_name, course_name, teacher, ,gender, ects, classroom, grade, img_url
Read student data into a list of Students from a csv file (Each student can appear on multiple lines):
loop through the list and print each student with name, img_url and avg_grade.
sort the list by avg_grade
create a bar chart with student_name on x and avg_grade on y-axis
Make a method on Student class that can show progression of the study in % (add up ECTS from all passed courses divided by total of 150 total points (equivalent to 5 semesters))
Show a bar chart of distribution of study progression on x-axis and number of students in each category on y-axis. (e.g. make 10 categories from 0-100%)
Extra: Make the Datasheet class iterable so that next(data_sheet) will return the next course in the list"""