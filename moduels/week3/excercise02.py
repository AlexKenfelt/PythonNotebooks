"""Exercise 1
1. Create a python file with 3 functions:
    a. def print_file_content(file) that can print content of a csv file to the console
    b. def write_list_to_file(output_file, lst) that can take a list or tuple of strings and write each element to a new line in file
        - rewrite the function so that it gets an arbitrary number of strings instead of a list
    C. def read_csv(input_file) that take a csv file and read each row into a list. Print the list.
2. Add a functionality so that the file can be called from cli with 2 arguments:
    A. path to csv file
    B. an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.
3. Add a --help cli argument to describe how the module is used"""

from fileinput import filename
import csv
import platform

file = 'C:/Users/alexk/OneDrive/Skrivebord/4Sem/Python/docker_notebooks/notebooks/MyFolder/moduels/week3/text.csv'
list_new = ['blue', 'purple', 'yellow']
# 1.a
def print_file_content(file):
    with open(file) as f_obj:
        content = f_obj.readlines()

    for line in content[:20]:
        print(line.strip().split(','))

#print(print_file_content(file))

# 1.b
def write_list_to_file(output_file, lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None

    with open(output_file, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(lst)

#write_list_to_file(file, list_new)

# 1.c 
def read_csv(file):
    with open(file) as f_obj:
        content = f_obj.readlines()
    return content

print(read_csv(file))






