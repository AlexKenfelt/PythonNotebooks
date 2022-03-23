import numpy as np
import pandas as pd 
url = 'https://api.statbank.dk/v1/tables'
dst = pd.read_json(url)
dst.to_csv('dk-stat-all-tables.csv', encoding='utf-8', index=False)
dst[:20]

# 5.a

import pandas as pd 

url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&K%C3%98N=1%2C2&ALDER=*&CIVILSTAND=U%2CG&Tid=2020K4'
df = pd.read_csv(url, sep=';')

url1 = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&K%C3%98N=1%2C2&ALDER=*&CIVILSTAND=U%2CG&Tid=2008K4'
df1 = pd.read_csv(url1, sep=';')

# 2020 data
test = df[(df['CIVILSTAND']=='Gift/separeret') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Hele landet')  & (df['KØN']=='Mænd')]
stats = test[['INDHOLD']].apply(pd.to_numeric)
print(test)
print(stats)

# 2008 data
test1 = df1[(df1['CIVILSTAND']=='Gift/separeret') & (df1['ALDER']=='I alt') & (df1['OMRÅDE']=='Hele landet')  & (df1['KØN']=='Mænd')]
stats1 = test1[['INDHOLD']].apply(pd.to_numeric)
print(test1)
print(stats1)

diff = stats-stats1
print('The difference between divorced danes in 2008 to 2020 in percent ->')
#diff = stats-stats1
#print(str(round((diff/stats1) * 100, 2)) + '%')

#1072984 - 1096210 = -23226
#( -23226 / 1096210 ) · 100 = -2.12%

#Copenhagen (Sjaelland)
unmarried_cophenhagen_men = df[(df['CIVILSTAND']=='Gift/separeret') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Hele landet')  & (df['KØN']=='Mænd')]
unmarried_cophenhagen_women = df[(df['CIVILSTAND']=='Gift/separeret') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Hele landet')  & (df['KØN']=='Mænd')]
#Aarhus (Jylland)
unmarried_aarhus_men = df[(df['CIVILSTAND']=='Gift/separeret') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Hele landet')  & (df['KØN']=='Mænd')]
unmarried_aarhus_women = df[(df['CIVILSTAND']=='Gift/separeret') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Hele landet')  & (df['KØN']=='Mænd')]
#Odense (Fyn)
unmarried_odense_men = df[(df['CIVILSTAND']=='Gift/separeret') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Hele landet')  & (df['KØN']=='Mænd')]
unmarried_odense_women = df[(df['CIVILSTAND']=='Gift/separeret') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Hele landet')  & (df['KØN']=='Mænd')]
#Aalborg (Jylland)
unmarried_aalborg_men = df[(df['CIVILSTAND']=='Gift/separeret') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Hele landet')  & (df['KØN']=='Mænd')]
unmarried_aalborg_women = df[(df['CIVILSTAND']=='Gift/separeret') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Hele landet')  & (df['KØN']=='Mænd')]
#Esbjerg (Jylland)
unmarried_esbjerg_men = df[(df['CIVILSTAND']=='Gift/separeret') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Hele landet')  & (df['KØN']=='Mænd')]
unmarried_esbjerg_women = df[(df['CIVILSTAND']=='Gift/separeret') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Hele landet')  & (df['KØN']=='Mænd')]

def divorced():
    url = "https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND(Head)=F&Tid(Head)=2008K1%2C2020K4&OMR%C3%85DE(Head)=000"
    data = pd.read_csv(url, sep=";")

    first = data.iloc[0, 3]
    second = data.iloc[1, 3]

    difference = second - first

    percent_raise = difference / first * 100

    return percent_raise


def never_married():
    # URLs
    never_married_url = "https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&CIVILSTAND=U&Tid=2020K1%2C2020K2%2C2020K3%2C2020K4"

    all_url = "https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&Tid=2020K1%2C2020K2%2C2020K3%2C2020K4&CIVILSTAND=TOT"

    # All
    all_data = pd.read_csv(all_url, sep=";", skiprows=range(1, 5))
    all_data = all_data[all_data["OMRÅDE"].str.contains("Region") == False]
    all_data_summed = all_data.groupby("OMRÅDE")["INDHOLD"].sum()
    five_biggest_cities = all_data_summed.nlargest(5)

    # Unmarried
    unmarried_data = pd.read_csv(never_married_url, sep=";", skiprows=range(1, 5))
    unmarried_data = unmarried_data[
        unmarried_data["OMRÅDE"].str.contains("Region") == False
    ]
    unmarried_data_summed = unmarried_data.groupby("OMRÅDE")["INDHOLD"].sum()
    unmarried_series = unmarried_data_summed[
        ["København", "Aarhus", "Aalborg", "Odense", "Vejle"]
    ]

    # Percentage
    percentage_series = unmarried_series / five_biggest_cities * 100

    return percentage_series


def marrital_status():
    url = "https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=U%2CG%2CE%2CF&Tid=*&OMR%C3%85DE=101"
    data = pd.read_csv(url, sep=";")

    data = data[data["TID"].str.contains("2022") == False]

    data["TID"] = data["TID"].map(lambda x: str(x)[:-2])

    # Dataframes
    unmarried_data = data[data["CIVILSTAND"].str.contains("Ugift") == True]

    married_data = data[data["CIVILSTAND"].str.contains("Gift") == True]

    divorced_data = data[data["CIVILSTAND"].str.contains("Fraskilt") == True]

    widow_data = data[data["CIVILSTAND"].str.contains("Enke") == True]

    # Sum by year
    unmarried_data_summed = unmarried_data.groupby("TID")["INDHOLD"].sum()
    married_data_summed = married_data.groupby("TID")["INDHOLD"].sum()
    divorced_data_summed = divorced_data.groupby("TID")["INDHOLD"].sum()
    widow_data_summed = widow_data.groupby("TID")["INDHOLD"].sum()

    return (
        unmarried_data_summed,
        married_data_summed,
        divorced_data_summed,
        widow_data_summed,
    )


def marriage_status_2020():
    url = "https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&ALDER=*&CIVILSTAND=U%2CG&Tid=2020K1%2C2020K2%2C2020K3%2C2020K4"
    data = pd.read_csv(url, sep=";")

    data = data[data["ALDER"].str.contains("I alt") == False]
    data["TID"] = data["TID"].map(lambda x: str(x)[:-2])
    data["ALDER"] = data["ALDER"].map(lambda x: str(x)[:-2]).apply(pd.to_numeric)

    unmarried_data = data[data["CIVILSTAND"].str.contains("Ugift") == True]

    married_data = data[data["CIVILSTAND"].str.contains("Gift") == True]

    unmarried_data_summed = unmarried_data.groupby("ALDER")["INDHOLD"].sum()
    married_data_summed = married_data.groupby("ALDER")["INDHOLD"].sum()

    return unmarried_data_summed, married_data_summed