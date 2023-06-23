import csv
import json

import requests
from bs4 import BeautifulSoup


websites = [
    {
        'name': 'Remanga',
        'url': 'https://remanga.org/',
        'data_selector': 'div.jsx-1931804356',
    },
    {
        'name': 'Serial Time',
        'url': 'https://serial-time.com/network/netflix/',
        'data_selector': 'div.main_title_sid ',
    },
    {
        'name': 'ANIMEGO',
        'url': 'https://animego.org/',
        'data_selector': 'div.list-group-item a.card-title',
    },
]


def scrape_website(website):
    response = requests.get(website['url'])
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.select(website['data_selector'])
    data = [element.text for element in elements]
    return data


def save_to_csv(data):
    with open('scraped_data.csv', 'a', newline='', encoding='UTF-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)


def save_to_json(data):
    with open('scraped_data.json', 'a', encoding='UTF-8') as jsonfile:
        jsonfile.write(json.dumps(data, sort_keys=True, indent=2))


def main():
    for website in websites:
        data = scrape_website(website)
        save_to_csv([website['name'], data])
        save_to_json([website['name'], data])


if __name__ == '__main__':
    main()