import csv

filename = 'Jabal_Omar_Marriott_Hotel_Makkah-Mecca_Makkah_Province__en.csv'

with open(filename) as f:
    a = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]