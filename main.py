from urllib import response
from bs4 import BeautifulSoup as BS
import requests
import csv



def get_soup(html):
    soup = BS(html, 'lxml')
    return soup


def get_data(soup):
    catalog = soup.find('div', class_ = 'list-view')
    phones = catalog.find_all('div', class_ = 'item product_listbox oh')

    for phone in phones:
        title = phone.find('div', class_ = 'product_text pull-left').text.strip()
        img = phone.find('img').get('src')
        img = f'https://www.kivano.kg{img}'
        price = phone.find('div', class_ = 'listbox_price text-center').text.strip()
        

        write_csv({
            'title': title,
            'price': price,
            'img': img
        })        
    

def write_csv(data):
    with open('phones.csv', 'a') as file:
        names = ['title', 'price', 'img']
        write = csv.DictWriter(file, delimiter = ',', fieldnames = names)
        write.writerow(data)


def get_html(url):
    response = requests.get(url)
    return response.text
    


def main():
    for i in range(1, 10):
        BASE_URL = 'https://www.kivano.kg/mobilnye-telefony'
        html = get_html(BASE_URL)
        soup = get_soup(html)
        get_data(soup)

if __name__ == '__main__':
    main()