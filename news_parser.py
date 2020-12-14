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
        news = soup.find_all('div', {'class': 'boxes_cols'})
        news_data = []
        for one_news in news:      
            news_attributes = one_news.find_all('div', {'class': 'hl__inner'})
            for attribute in news_attributes:
                news_dict = {}
                news_maker = attribute.find('span', {'class': 'src-part'}).contents[0]
                title = attribute.find('a', {'class': 'hll'})
                news_dict['title'] = title.text
                news_dict['url'] = attribute.contents[0].get('href')
                news_dict['news maker'] = news_maker
                if news_dict not in news_data:
                    news_data.append(news_dict)
        return(news_data)



def main():
    parser = NewsParser()
    file = CSVFile('newsnow.csv')
    file.write(parser.parse_html(URL))

if __name__ == '__main__':
    main()
