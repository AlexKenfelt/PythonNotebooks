import pandas as pd
import numpy as np

# This is the data set we will be using for exercise 1.
data = np.array([['','Col1','Col2','col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]])

# Here we create a DataFrame using panda so we can display the data. 
df = pd.DataFrame(data=data[1:4,1:4], columns=data[0,1:4], index=data[1:4,0])

# Exercise 2 A  --- Make slices of data: second column using column name
print(' --- Exercise 2 A ---')
print(df['Col2'])

# Exercise 2 B --- Make slices of data: third column using column index (.iloc[])
print(' --- Exercise 2 B ---')
print(df.iloc[:,2])

# Exercise 3 C --- Make slices of data: slice element at third row of second column (use .iloc())
print(' --- Exercise 2 C ---')
print(df.iloc[2,1])


print(' --- CLASS EXERCISE 02 PANDA --- ')
# Exercise 1 in 02
data = pd.read_csv('./API_EN.ATM.CO2E.KT_DS2_en_csv_v2_1345584.csv', skiprows=4)
print(pd.Series(data=data["2014"].values, index = data ["Country Code"])[:9])