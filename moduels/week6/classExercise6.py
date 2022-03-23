from genericpath import getsize
from sys import getsizeof
import requests
import xlrd

"""weather_aarhus = 'http://api.openweathermap.org/data/2.5/weather?lat=56.162939&lon=10.203921&appid=6b6abd89d47312e8119ceca1a16ab9a0'
r = requests.get(weather_aarhus)
aarhus_url = r.json()['weather_url']
print(r.text)"""

#class exercise 1

api_key = "27ad2e6307a3742ba619b71c63384174"

lat = "56.162939"
lon = "10.203921"

data = requests.get(
    "http://api.openweathermap.org/data/2.5/weather?lat=56.162939&lon=10.203921&appid=6b6abd89d47312e8119ceca1a16ab9a0"
)


#print(data.content)
print(data.text)


#class exercisecreate generator

file = xlrd.open_workbook("unisex_navne.xls")

sheet1 = file.sheet_by_index(0)
for row in sheet1.get_rows():
    print (row[0].value)
    print(getsizeof(row))

    x = getsizeof

    print(x)


#løst med egen 

