import numpy as np

#Class Exercise 01
"""
    On the above image find the 5 different slicings using only the array slicing notation
"""

a = np.arange(10, 30).reshape(4, 5)

red = a[0, 1:4]
blue = a[0:3:2,4]
green = a[0:3:,2]
yellow = a[0,0]
turquise = a[:,1:4:2].T

#print(a)
#print('red:\n',red,'\nblue:\n',blue,'\ngreen:\n',green,'\nyellow:\n',yellow, '\nturquise:\n',turquise)

#Class Exercise 02
"""
    Slice out [12 13 14] from the above cube using only one slice. e.g: a[:,:,:]
    Slice out [3 12 21].
    Slice out all y-values where x is 2 and z is 0.
"""

b = np.arange(0, 27).reshape((3, 3, 3))

neon_red = b[1,1,0:]
neon_blue = b[:,1,0]
neon_green = b[:,2,0]

#print(b)
#print('neon_red:\n',neon_red,'\nneon_blue:\n',neon_blue,'\nneon_green:\n',neon_green)

#Class Exercise 03

"""
For the dataset: data = np.arange(1,101).reshape(10,10)
    apply a mask that will return only the even numbers
    using np.where() return only numbers that ends with 6 (use %)
"""


#Class Exercise 04

"""
    load the csv file: befkbhalderstatkode.csv into a numpy ndarray
    How many german children of 0 years were there in Copenhagen in 2015?
    create a function that can take any combination of the 4 parameters:AAR,BYDEL,ALDER,STATKODE and return population data
    create a new function like previous so that it can sum values for all ages if age is not provided to the function
    further add functionality to sum values if citizenship or area was not provided to function.
    create a new function that can also give average values for each year if year whas not provided.
    create a function, that given year and nationality can return which area had the most of these nationals by that year. Test it by finding out which area had the most Moroccan people in both 1992 and 2015
    Find the Area(s) where fewest foreingers lived in Copenhagen in 1992 and 2015 respectively
    Find out what age most French people have in 2015
"""
filename = 'C:/Users/23300/IdeaProjects/docker_notebooks/notebooks/data/befkbhalderstatkode.csv'
bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
dd = bef_stats_df


#mask1 = (dd[:,0] == 2015) & (dd[:,2] == 0) & (dd[:,3] == 5180)
#print(dd[mask1])
AAR = int(input("enter number: "))
BYDEL = int(input("skriv bydel nummer:"))
ALDER = int(input("skriv alder:"))
STATKODE = int(input("skriv statkode:"))

    #   AAR,BYDEL,ALDER,STATKODE,PERSONER
def data(AAR, BYDEL, ALDER, STATKODE):
    mask_input = (dd[:,0] == AAR) & (dd[:,1] == BYDEL) & (dd[:,2] == ALDER) & (dd[:,3] == STATKODE)
    print(dd[mask_input])

print(data(AAR, BYDEL, ALDER, STATKODE))
#print(type(bef_stats_df),' of size: ',bef_stats_df.size)
#print('The skip_header=1 means that we have only the data\n\nfirst line:\n',bef_stats_df[0],'\nlast line\n',bef_stats_df[len(bef_stats_df)-1])



