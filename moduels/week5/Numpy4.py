
import numpy as np
from collections import Counter

filename = './data/befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
dd = bef_stats_df
print(type(bef_stats_df),' of size: ',bef_stats_df.size)
print('The skip_header=1 means that we have only the data\n\nfirst line:\n',bef_stats_df[0],'\nlast line\n',bef_stats_df[len(bef_stats_df)-1])


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
    mask1 = (dd[:, 0] == 2015) & (dd[:, 2] > 65)
    return int(sum(dd[mask1][:, 4]))


if __name__ == "__main__":
    print('Hello world')
