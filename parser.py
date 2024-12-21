from bs4 import BeautifulSoup
import requests

def hills():

    url = "https://ski-gv.ru/hills/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    elements = soup.find_all('div', class_='track-option__info')
    for element in elements:
        dates = element.text.replace("\n", '').strip()
        print(dates)
        
    data_name = soup.find_all('div', class_='track-option__name')

    for i in range(len(data_name)):
        name = data_name[i-1].text.strip()
        print(name)



hills()
