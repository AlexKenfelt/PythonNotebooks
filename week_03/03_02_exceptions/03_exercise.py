"""
    Create a class called: Person with a constructor that takes a string: name.

    Check if name contains only letters and each new word starts with a capital letter. 
    If this is not the case raise an InvalidArgumentException (your own exception here)

    Test your new class by making 2 instances (one with a name, that follows the rules and another that violates them)
"""

class Person(): 

    def __init__(self, name):
        self.name = name

    def is_name_valid (self):
        if (all(char.isalpha() for char in self.name)):
            print('The name is valid.')
        else:
            print('Name is not valid.')
            raise InvalidArgumentException()

class InvalidArgumentException(Exception):
    pass

name = input('Enter your name here : ')
class_instance = Person(name)
print('--- task 1 ---')
class_instance.is_name_valid()