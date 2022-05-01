import numpy as np
import pandas as pd 
url = 'https://api.statbank.dk/v1/tables'
dst = pd.read_json(url)
dst.to_csv('dk-stat-all-tables.csv', encoding='utf-8', index=False)
dst[:20]

# Exercise 1.5

def divorced():
    url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&K%C3%98N=1%2C2&ALDER=*&CIVILSTAND=U%2CG&Tid=2020K4'
    dst = pd.read_csv(url, sep=';')
    dst.to_csv('divorced2008-2020.csv', encoding='utf-8', index=False)



if __name__ == "__main__":
    divorced()


def never_married() :
    url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&CIVILSTAND=U&Tid=2020K1%2C2020K2%2C2020K3%2C2020K4'
    data = pd.read_csv(url, sep=';', skiprows=range(1,5))
    data = data[data["OMRÅDE"].str.contains("Region") == False]
    return data


