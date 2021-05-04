import re

import requests
from bs4 import BeautifulSoup

NEWS_URL = 'https://www.cochrane.org'
LIB_URL = 'https://www.cochranelibrary.com'


def get_html(url, params_=''):
    resp = requests.get(url, params=params_)
    return resp


class NewsParser:
    def __init__(self):
        self.last_post_key = 0
        self.url = NEWS_URL
        self.html_ = get_html(self.url)

    def get_evidence(self):
        soup = BeautifulSoup(self.html_.text, 'html.parser')
        items = soup.find('div', id='top10', class_='latest-top').find_all('div', class_='views-row')
        evidence_content = []
        for item in items:
            evidence_content.append({
                'short_description': item.get_text(),
                'article_link': self.url + item.find('a').get('href')
            })
        return evidence_content

    def get_content(self):
        soup = BeautifulSoup(self.html_.text, 'html.parser')
        items = soup.find_all('div', class_='views-row')
        news_content = []
        for item in items:
            lvl1_find = item.find('div', class_='views-row-inner')
            if lvl1_find is not None:
                news_content.append({
                    'short_description': lvl1_find.find('div', class_='views-field views-field-title').get_text(),
                    'article_link': self.url + lvl1_find.find('div', class_='views-field views-field-title').find(
                        'a').get(
                        'href'),
                    'img_link': lvl1_find.find('div', class_='views-field views-field-field-news-image').find(
                        'img').get(
                        'src'),
                    'publish_date': lvl1_find.find('div',
                                                   class_='views-field views-field-field-version-published').get_text()
                })
        return l

    def get_last_post_key(self):
        return self.last_post_key

    def update_last_post_key(self, new_post_key):
        self.last_post_key = new_post_key

    def get_new_post_key(self):
        content = self.get_content()
        new_post = get_html(content[0]['article_link'])
        new_post_key = int(re.findall(r'\d{4,6}', re.findall(r'page-node-\d{4,6}', new_post.text)[0])[0])
        return new_post_key
