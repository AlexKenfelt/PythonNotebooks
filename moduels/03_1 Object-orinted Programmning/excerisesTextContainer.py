""""
Exercises
1. Create a Python module, which consists of a class TextContainer. The class must have a constructor which allow objects to be initialized with a text ala: tc = TextContainer(my_text). The class must implement the following methods for computing statistics on texts.
Counting the amount of words used in a text.
Counting the amount of chars used in a text.
Counting the amount of letters, where letters are all ASCII letter characters, see
import string
string.ascii_letters  # returns 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
Remove all punctuation characters, see
import string
string.punctuation  # returns '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'"""



class TextContainer ():
   
    def __init__(self, my_text):
        my_text = "magasine"
        self.tc = TextContainer(my_text)

    
    def count_words_in_text (self):
        print ('This needs printing:' + self.tc)



 