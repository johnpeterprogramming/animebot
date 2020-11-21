from bs4 import BeautifulSoup
from qbittorrent import Client
import requests
import os
import lxml

def get_option(num):
    option = options[num].find_all('td')
    return option


def get_title(num):
    option = get_option(num)[1]
    title = option.find('a', class_='')
    return title.text

anime = input('Search ( ͡☉ ͜ʖ ͡☉) ').replace(' ', '+')
input('Open Qbittorrent then press ENTER')


qb = Client("http://127.0.0.1:8080/")
qb.login("admin", "adminadmin")

url = 'https://nyaa.si/?f=0&c=0_0&q=' + anime

site = requests.get(url)
soup = BeautifulSoup(site.text, 'lxml')

options = soup.find_all('tr', class_='default') + soup.find_all('tr', class_='success')

if options:
    for i in range(1, len(options)):
        print(i, ': ', get_title(i))

    selection = int(input('Which one? '))
    chosen = get_option(selection)[2]
    magnet_link = chosen.find_all('a')[1]['href']
    qb.download_from_link(magnet_link)

    print('Downloading!!')
else:
    print('nothing')
