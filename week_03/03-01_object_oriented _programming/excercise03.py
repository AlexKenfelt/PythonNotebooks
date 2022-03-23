"""Create a Python module, which consists of a class TextContainer. 
The class must have a constructor which allow objects to be initialized with a text ala: 
tc = TextContainer(my_text). The class must implement the following methods for computing statistics on texts.

    Counting the amount of words used in a text.
    Counting the amount of chars used in a text.
    Counting the amount of letters, where letters are all ASCII letter characters, see

    import string
    string.ascii_letters  # returns 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    Remove all punctuation characters, see

    import string
    string.punctuation  # returns '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

"""
import string

class TextContainer () :

    def __init__(self, my_text):
        self.my_text = my_text

    def counting_words_in_text(self):
        print('This is the string we are counting words on : ' + self.my_text)
        res = len(self.my_text.split())
        print('This is the number of words in our string : ' + str(res))

    def counting_chars_in_text(self):
        count = 0
        for i in range(0, len(self.my_text)):  
            if(self.my_text[i] != ' '):  
                count = count + 1;
        print("Total number of characters in a string: " + str(count));  

    def counting_amount_of_letters(self):
        user_text = input("Enter a text to analyze: ")
        total_count = len(user_text)
        ascii_count = sum(c in string.ascii_letters for c in user_text)
        print("Total number of characters:", total_count)
        print("Total number of ASCII characters:", ascii_count)
        print("Total number of all punctuation characters:", total_count-ascii_count)
        

string.ascii_letters  # returns 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.punctuation  # returns '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

my_text = 'This is just a string of some words.'
class_instance = TextContainer(my_text)
print('--- task 1 ---')
class_instance.counting_words_in_text()
print('--- task 2 ---')
class_instance.counting_chars_in_text()
print('--- task 3 ---')
class_instance.counting_amount_of_letters()
