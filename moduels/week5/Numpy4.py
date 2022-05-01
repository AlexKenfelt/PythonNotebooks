"""Open the file './data/befkbhalderstatkode.csv'
Turn the csv file into a numpy ndarray with np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
Using this data:
neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}
Find out how many people lived in each of the 11 areas in 2015
Make a bar plot to show the size of each city area from the smallest to the largest in 2015
Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015
How many of those were from the other nordic countries (not dk). Hint: see notebook: "04 Numpy"
Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015"""


import numpy as np

filename = './data/befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
dd = bef_stats_df
print(type(bef_stats_df),' of size: ',bef_stats_df.size)
print('The skip_header=1 means that we have only the data\n\nfirst line:\n',bef_stats_df[0],'\nlast line\n',bef_stats_df[len(bef_stats_df)-1])

mask1 = (dd[:,0] ==  2015) & (dd[:,2] == 0) & (dd[:,3] == 5180)
print (dd[mask1])



