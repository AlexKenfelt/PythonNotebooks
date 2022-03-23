import csv
import platform
import argparse

# Exercise 1

    # Create a python file with 3 functions:
        # def print_file_content(file) that can print content of a csv file to the console
        # def write_list_to_file(output_file, lst) that can take a list or tuple of strings and write each element to a new line in file
            # rewrite the function so that it gets an arbitrary number of strings instead of a list
        # def read_csv(input_file) that take a csv file and read each row into a list. Print the list.
    # Add a functionality so that the file can be called from cli with 2 arguments:
        # path to csv file
        # an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.
    # Add a --help cli argument to describe how the module is used

file = 'C:/Users/23300/IdeaProjects/docker_notebooks/notebooks/my_notebooks/assignments/assignment_02/text.csv'
string1 = "hej med dig janus"
string2 = "hej med dig thor"
string3 = "hej med dig sigurd"

# creating an ArgumentParsert object
parser = argparse.ArgumentParser()



# Prints the content of any given csv file to the console.
def print_file_content(file):
    parser.add_argument('-file', help = "Enter path to file.")              # implemented argparse, so the user can specify the path to file that must be read.
    args = parser.parse_args()
    print(file)
    with open(args.file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)

#   Function that takes an unlimited amount of strings as arguments and then prints them to a given csv file.
def write_strings_to_file(output_file, *strings):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None

    with open(output_file, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(strings)

#   Function that read all the lines in a csv file and converts them to a list. each line corresponds to an index.
def read_csv(file):
    with open(file) as f_obj:
        content = f_obj.readlines()
    return content

#   Function Calls Below Here!
#print_file_content('ERROR')
#write_strings_to_file(file, string1, string2, string3)
print(read_csv(file))
