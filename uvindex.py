#!/usr/bin/python3.4

#This program determines the UV index of a certain place and temp when given a ZIP code
#The program pulls the data from weather.com

import requests
import urllib.request
import time
import os
from bs4 import BeautifulSoup

os.system('clear')

print('*****')
print('Temperature and UV checker')
print('*****')
print('\n')
print('Enter zip code')

zipcode = input()

weather_link = 'https://weather.com/weather/today/l/' + zipcode + ':4:US'

try:
    response = requests.get(weather_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    spans = soup.find('div', {'class' : 'today_nowcard-hilo'})
    location = soup.find('h1', {'class' : 'h4 today_nowcard-location'})

    print('\n')
    print('*****')
    print('Location: ' + location.text)

    for div in spans:
        div.findAll('div')
        print(div.text)
    print('*****')
except:
    print('I can only check zip codes in the United States!')


