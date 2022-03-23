
#   1.0 Use the range() function to make a list of the odd numbers from 1 to 20.

print("\n------------- task 1.0 -------------\n")
print([num for num in range(0, 20 + 1) if num % 2 != 0])                    # This makes a list of 'ONLY ODD' numbers from 0 to 20.

#   2.0 Create a list with the even number values from two to one million. Use min(list) and max(list) to make sure your list actually starts at two and ends at one million. 
#       Also, use the sum(list) function to compute the sum of all values.

print("\n------------- task 2.0 -------------\n")
even_num_list = list((num for num in range(1, 1000001) if not num % 2))     # this makes a list of 'ONLY EVEN' numbers based on our given range().
print(min(even_num_list))                                                   # This line finds and prints the lowest number in our list of even numbers.
print(max(even_num_list))                                                   # This prints the highest number in our list.
print(sum(even_num_list))                                                   # Prints the sum of all even numbers between 1 and 1 million.

#   3.0 Create a list of the multiples of 3 - going from 3 to 300. HINT: USE A LIST COMPREHENSION

print("\n------------- task 3.0 -------------\n")
print([i*3 for i in range(1,101)])                                          # Beacuse 3*100 is = 300 we only need a range of (1, 101) before we reach the desired number 300.

#   4.0 A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Create a list of the first 10 cubes (that is, the cube of each integer from 1 through 10).

print("\n------------- task 4.0 -------------\n")
print([i**3 for i in range(1,11)])                                          # Here we just raise 'i' to the power of 3, based on our range.