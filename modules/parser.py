import requests
from bs4 import BeautifulSoup


def getip():
    response = requests.get('https://2ip.ru/')

    soup = BeautifulSoup(response.content, 'html.parser')

    my_ip = soup.find('div',class_='ip').find('span')

    return my_ip.text