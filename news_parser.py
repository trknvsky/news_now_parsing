import urllib.request
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from news_csv_writer import *

URL = 'https://www.newsnow.co.uk/h/'


class NewsParser:

    def parse_html(self, url):
        response = requests.get(url)
        contents = response.text
        soup = BeautifulSoup(contents, 'lxml')
        news = soup.find_all('main', {'class': 'rs-grid__main js-maincontent'})
        news_data = []
        for one_news in news:
            news_attributes = one_news.select('div[class=hl]')
            for attribute in news_attributes:
                news_dict = {}               
                title = attribute.find('a', {'class': 'hll'})
                news_maker = attribute.find('span', {'class': 'src-part'})
                news_url = attribute.select('a[href]')[0]
                news_dict['title'] = title.text
                news_dict['url'] = news_url.get('href')
                news_dict['news maker'] = news_maker.text
                if news_dict not in news_data:
                    news_data.append(news_dict)
        return news_data


def main():
    parser = NewsParser()
    file = CSVFile('newsnow.csv')
    file.write(parser.parse_html(URL))

if __name__ == '__main__':
    main()
