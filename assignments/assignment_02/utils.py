import os
if __name__ == '__main__':
    print('This is utils.py')

def get_file_names(folderpath, out = 'output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    with open(out, 'w') as f_obj:
        for i in os.listdir(folderpath):
            f_obj.write(i + '\n')

def get_all_file_names(folderpath, out = 'output.txt'):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    with open(out, 'w') as f_obj:
        for (root, dirs, files) in os.walk(folderpath):
            for i in files:
                f_obj.write(i + '\n')

def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    for file in os.listdir(file_names):
        with open(file) as f_obj:
            print(f_obj.readlines())

def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    for file in os.listdir(file_names):
        with open(file) as f_obj:
            for line in f_obj.readlines():
                if '@' in line:
                    print(line)

def write_headlines(md_files, out = 'output.txt'):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    with open(out, 'w') as f_obj:
        for file in os.listdir(md_files):
            if file.endswith('.md'):
                with open(file) as f_obj:
                    for line in f_obj.readlines():
                        if line.startswith('#'):
                            f_obj.write(line + '\n')
