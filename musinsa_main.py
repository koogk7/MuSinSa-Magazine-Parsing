import re

import requests
from bs4 import BeautifulSoup

from constant import *
from db_connecter import DatabaseConnecter




if __name__ == "__main__":
    html = requests.get(MUSINSA_URL + MAGAZINE_URL).content
    soup = BeautifulSoup(html, "html.parser")
    h_magazine_list = soup.select(".magazine-article-list .listItem")
    magazine_list = list()

    for item in h_magazine_list:
        magazine = dict()
        magazine['title'] = item.select_one(".title").text.replace("\n", "")
        magazine['img_url'] = item.select_one(".lazy-load-image").get("data-original")
        magazine['link'] = MUSINSA_URL + item.select_one('a').get('href')
        magazine['description'] = item.select_one(".description").text
        magazine['description'] = re.sub("\t|\n|\r", "", magazine['description'])
        print(" %s ".center(50,"#") %magazine['title'])
        magazine_list.append(magazine)

    db_connecter = DatabaseConnecter()
    db_connecter.insert(magazine_list)




