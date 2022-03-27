"""
"Download datasettet fra dette link.
https://www.kaggle.com/sanjeetsinghnaik/top-1000-highest-grossing-movies 

1. Find the top 10 highest grossing Disney movies measured by world sales

2. Create a pie chart that shows the distribution of Licenses (PG, R, M and so on)

3. Get the percentage of PG rated movies between 2001 and 2015

4. Calculate the average of world sales for each Genre and visualize the data with a bar chart. (Hint: use groupBy)
"
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# I first collect the data from the CSV
data = pd.read_csv('./Highest Holywood Grossing Movies.csv', skiprows=0)
print(data)

# (1.)
# I will first collect and save the Disney Movies from the Distributor. 

df = data[(data['Distributor'] == 'Walt Disney Studios Motion Pictures')]
#print(df)

# Now I have the Disney movies measured by world sales, but I need to convert the sales so it is readable. 
df.loc[:,('World Sales (in $)')].astype('int')  

#From the converted Disney Movies data in int, I can now sort the the top 10 highest grossing Disney movies measured by world sales.
print(df.sort_values('World Sales (in $)', ascending=False).head(10)[['World Sales (in $)']])
    # Todo: type out number 1-10 


#----------------------------------------------------------------------------------------------------------------------------------------------------------

# (2.)
# Create a pie chart that shows the distribution of Licenses (PG, R, M and so on)
# I will have to use the data from the csv file, but only collected the relevant data (Licenses).
#license = pd.Series(data['License'])   

# I will use the License data in a pandaseries, so I can use it to count the value of the data, save it, sum it up and then be used in the pie chart.
#license_count = license.value_counts() 
#license_count.plot(kind='pie', autopct='%1.0f%%')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# (3.)
df1 = data[['License','Release Date']]
# I add a column 'Year'
# normalize = true --> data_norm = (data - data.min())/ (data.max() - data.min())
df1[['Release Date', 'Year']] = df1['Release Date'].str.split(',', 1, expand=True) 
df1_filter = df1[(df1['Year'] >= " 2001") & (df1['Year'] < " 2015")]
df1 = df1_filter['License'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'            
print('PG = ' + df1.iloc[1]) 

#-----------------------------------------------------------------------------------------------------------------------------------------------------------


# (4.)
def cal_avg():
    df1 = df_movies [['License','Release Date', 'Genre', 'World Sales (in $)']]
    df2 = pd.DataFrame(data, colums = ['World Sales (in $)', 'Genre'])
    df3 = df2['Genre'].str.get_dummies(sep="")

    print(df2)



