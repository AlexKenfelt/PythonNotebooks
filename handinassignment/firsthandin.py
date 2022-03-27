"""
"Download datasettet fra dette link.
https://www.kaggle.com/sanjeetsinghnaik/top-1000-highest-grossing-movies 

1. Find the top 10 highest grossing Disney movies measured by world sales

2. Create a pie chart that shows the distribution of Licenses (PG, R, M and so on)

3. Get the percentage of PG rated movies between 2001 and 2015

4. Calculate the average of world sales for each genre and visualize the data with a bar chart. (Hint: use groupBy)
"
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# I first collect the data from the CSV
data = pd.read_csv('./Highest Holywood Grossing Movies.csv', skiprows=0)
print(data)

# 1. 
# I will first collect and save the Disney Movies from the Distributor. 

df = data[(data['Distributor'] == 'Walt Disney Studios Motion Pictures')]
#print(df)

# Now I have the Disney movies measured by world sales, but I need to convert the sales so it is readable. 
df.loc[:,('World Sales (in $)')].astype('int')  

#From the converted Disney Movies data in int, I can now sort the the top 10 highest grossing Disney movies measured by world sales.
print(df.sort_values('World Sales (in $)', ascending=False).head(10)[['World Sales (in $)']])
