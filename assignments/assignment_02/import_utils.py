import utils as util

if __name__ == '__main__':
    str('This is import_utils.py')


out = 'output.txt'

folderpath = 'C:/Users/23300/IdeaProjects/docker_notebooks/notebooks/my_notebooks/assignments/assignment_02'

util.get_all_file_names(folderpath, out)