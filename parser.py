import requests
from PyInstaller.utils.cliutils.archive_viewer import get_content
from bs4 import BeautifulSoup
import re

NEWS_URL = 'https://www.cochrane.org'
LIB_URL = 'https://www.cochranelibrary.com'


def get_html(url, params=''):
    resp = requests.get(url)
    return resp


def get_content(html_, url, filename='post_key'):
    soup = BeautifulSoup(html_, 'html.parser')
    items = soup.find_all('div', class_='views-row')
    l = []
    for item in items:
        lvl1 = item.find('div', class_='views-row-inner')
        if lvl1 is not None:
            l.append({
                'short_description': lvl1.find('div', class_='views-field views-field-title').get_text(),
                'article_link': url + lvl1.find('div', class_='views-field views-field-title').find('a').get('href'),
                'img_link': lvl1.find('div', class_='views-field views-field-field-news-image').find('img').get('src'),
                'publish_date': lvl1.find('div', class_='views-field views-field-field-version-published').get_text()
            })
    return l


class NewsParser:
    def __init__(self):
        self.last_post_key = 0

    def get_last_post_key(self, filename='post_key'):
        return self.last_post_key

    def update_last_post_key(self, new_post_key):
        self.last_post_key = new_post_key

    def get_new_post_key(self):
        html = get_html(NEWS_URL)
        content = get_content(html.text, NEWS_URL)
        new_post = get_html(content[0]['article_link'])
        new_post_key = int(re.findall(r'\d{4,6}', re.findall(r'page-node-\d{4,6}', new_post.text)[0])[0])
        return new_post_key


class LibParser:
    pass
