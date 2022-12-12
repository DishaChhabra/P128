from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time
import csv


url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(url, verify=False)
soup = bs(page.text, 'html.parser')
star_table = soup.find('table')
temp = []
table_rows = star_table.find_all('tr')


for i in table_rows:
    td = i.find_all('td')
    r = [i.text.rstrip() for i in td]
    temp.append(r)

star_name = []
radius = []
mass = []
distance = []

for i in range(1,len(temp)):
    star_name.append(temp[i][1])
    radius.append(temp[i][6])
    distance.append(temp[i][3])
    mass.append(temp[i][5])

df = pd.DataFrame(list(zip(star_name,distance,radius,mass)), columns = ["Star_name" , "distance" , "radius" , "mass" ])

df.to_csv("Projects/P128/star.csv")