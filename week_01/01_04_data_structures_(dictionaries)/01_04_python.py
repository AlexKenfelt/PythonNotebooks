
#   A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.
#   Create a dict suitable for decoding month names to numbers.
#   use string operations to split the date into 3 items using the '-' character.
#   Translate the month and return a tuple.
#   In the end we have a date 'dd-MMM-yy' format and we get a new string 'd-m-y'

months = {'JAN' : '1', 'FEB' : '2', 'MAR' : '3', 'APR' : '4', 'MAY' : '5', 'JUN' : '6', 'JUL' : '7', 'AUG' : '8', 'SEP' : '9', 'OCT' : '10', 'NOV' : '11', 'DEC' : '12'}

user_input = input("Enter a date in the format 'dd-MMM-yy' ex. '8-MAR-85': ")           # Takes user input and then saves it to our variable.
try:
    print('-'.join([months.get(i, i) for i in user_input.split('-')]))                  # It takes the string and splits it then it checks if there is a match with any of the keys in the dictionary, 
                                                                                        # and if there is, then it sets the value of that key and joins the string back toghether.
except ValueError:
    print("Error: must be in 'dd-MMM-yy' format. ")                                     # Was hoping to do some error handling, but i can't seems to understand how it works right now.
                                                                                        # Problem is it never fails, even if i put in wrong formart, as it is just a string, so if there is nothing to change,
                                                                                        # then it just returns the original input string.