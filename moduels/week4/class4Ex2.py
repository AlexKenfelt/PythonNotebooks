# read data from csv file into 2d numpy array
"""load the csv file: befkbhalderstatkode.csv into a numpy ndarray
How many german children of 0 years were there in Copenhagen in 2015?
create a function that can take any combination of the 4 parameters:AAR,BYDEL,ALDER,STATKODE and return population data
create a new function like previous so that it can sum values for all ages if age is not provided to the function
further add functionality to sum values if citizenship or area was not provided to function.
create a new function that can also give average values for each year if year whas not provided.
create a function, that given year and nationality can return which area had the most of these nationals by that year. Test it by finding out which area had the most Moroccan people in both 1992 and 2015
Find the Area(s) where fewest foreingers lived in Copenhagen in 1992 and 2015 respectively
Find out what age most French people have in 2015"""



import numpy as np
from collections import Counter

bef_stats_df = np.genfromtxt(
    "befkbhalderstatkode.csv", delimiter=",", dtype=np.uint, skip_header=1
)
dd = bef_stats_df

neighb = {
    1: "Indre By",
    2: "Østerbro",
    3: "Nørrebro",
    4: "Vesterbro/Kgs. Enghave",
    5: "Valby",
    6: "Vanløse",
    7: "Brønshøj-Husum",
    8: "Bispebjerg",
    9: "Amager Øst",
    10: "Amager Vest",
    99: "Udenfor",
}

def people_by_area():
    year_mask = dd[:, 0] == 2015
    set_of_areas = np.unique(dd[:, 1])
    freq_areas = np.array(
        [np.sum(dd[year_mask & (dd[:, 1] == area)][:, 4]) for area in set_of_areas]
    )
    dict_from_list = dict(zip(set_of_areas, freq_areas))
    return dict_from_list

def people_over_65():
    mask = (dd[:, 0] == 2015) & (dd[:, 2] > 65)
    return int(sum(dd[mask][:, 4]))