import math

#    1.0 Create 5 list comprehensions to solve the following 5 problems:

names = ['Hans', 'Grete', 'Jørgen', 'henrik', 'Helle', 'Ida', 'Alex', 'Janus']      #Array of names used for tasks (1.1 - 1.3 -)
sentence = "5fladeflødebollerpå1fladtflødebollefad"                                 #String used for task (1.4)
dice1 = ['1','2','3','4','5','6']                                                   #Array of eyes that a dice contains used for (1.5)
dice2 = ['1','2','3','4','5','6']                                                   #Array of eyes that a dice contains used for (1.5)

#       1.1 Iterate a list of names to return a list of the names starting with H

print("\n------------- task 1.1 -------------\n")
print([element for element in names if element.upper().startswith("H")])

#       1.2 In one line create a list of the numbers 1-100 to the power of 3

print("\n------------- task 1.2 -------------\n")
print([i**3 for i in range(1,101)])

#       1.3 Iterate a list of names to create a list of tuples where the tuples first value is the length of the name and the second is the name

print("\n------------- task 1.3 -------------\n")
print([(len(name), name) for name in names])

#       1.4 Iterate over each character in a string and get only those that are nummeric

print("\n------------- task 1.4 -------------\n")
print([number for number in sentence if number in "0123456789"])

#       1.5 Using only a list comprehension wrapped in set() get all possible combination from throwing 2 dice (hint use 2 for loops in a single list comprehension)

print("\n------------- task 1.5 -------------\n")
print(set([d1+' '+d2 for d2 in dice2 for d1 in dice1]))

#   2.0 Create 2 dictionary comprehensions to solve the following:

print("\n------------- task 2.1 -------------\n")
numbers = [500,10,50]                                                               #Array of random number used for task (2.2)

#       2.1 Iterate a list of names and create a dictionary where key is the name and value is the length of the name

print({name: len(name) for name in names})

#       2.2 Iterate a list of numbers and create a dictionary with {key:value} being {number:squareroot_of_number}

print("\n------------- task 2.2 -------------\n")
print({number: math.sqrt(number) for number in numbers})


#   3.0 Extra assignment (This one goes beyond what is covered in the course notebooks. So only do it if you want an extra challenge).

dice_comb = [8,6,7,8,5,10,6,8,3,7,9,4,9,11,11,6,7,9,10,4,6,10,5,8,12,4,7,7,2,5,3,7,8,6,5,9]     #An array list that contains all 36 possible outcomes when throwing 2 dices.
dice_dict = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}                                             #A dictionary that contains possible outcomes of a throw of two dices.

#       3.1 Progammatically using loops create a small program to produce a dictionary with all the 2 dice throw combinations as keys (eg: 2,3,4...etc) and their likelyhood in percent as values

print("\n------------- task 3.1 -------------\n")
print({element: str(round((dice_comb.count(element) / 36)*100, 1)) + ' %' for element in dice_dict})


print("\nAll assignments complete!")