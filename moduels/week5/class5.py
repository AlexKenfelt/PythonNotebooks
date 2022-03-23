import numpy as np
import pandas as pd

data = np.array([['','Col1','Col2','col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]])

dd = pd.DataFrame(data=data[1:4,1:4], columns=data[0,1:4], index=data[1:4,0])
print(dd)

""" 01 - Exercise
Make slices of data:
second column using column name
third column using column index (.iloc[])
slice element at third row of second column (use .iloc())"""

col2 = (dd[['Col2']])
#print(col2)

col3 = dd.iloc[:,2]
#print(col3)

element_third = dd.iloc[2,1]
print(element_third)


""" 02 Exercise:
The CO2 Emission data set above is not updated since 2014

Create a Pandas Series with emission data from 2014 for each country or region
Find the 10 Countries/Regions with the highest emissions in 2014 and show emission numbers (reverse sorted)
Remove if you can those rows that are not countries (regions and aggregated groups) (hint: ISO 3166, Alpha-3 country codes, a csv file can be found here: /data/country_codes.csv)
Find the 10 countries with highest emissions in 2014
Plot the emissions of China and USA over time respectively"""


data = pd.read_csv('data/API_EN.ATM.CO2E.KT_DS2_en_csv_v2_1345584.csv', skiprows=4)
emission_country = pd.Series(data=data["2014"].values, index = data ["Country Code"])
print(emission_country)
