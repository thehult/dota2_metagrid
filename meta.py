import requests
from heroes import heroes
from bs4 import BeautifulSoup

def get_meta():
    '''Entry point to get the meta dict.'''
    return get_dota2protracker_metaplus()


def get_page(url):
    return requests.get(url)

def get_scraper(url):
    page = get_page(url)
    return BeautifulSoup(page.content, "html.parser")

def get_dota2protracker_metaplus():
    scraper = get_scraper("https://dota2protracker.com/metaplus")

    meta = []
    for pos in range(1, 6):
        tab = scraper.find("div", id="tabs-{}".format(pos))
        pick_categories = tab.find_all("div", class_="meta-picks")

        cat = []
        for pcs in pick_categories:
            picks = pcs.find_all("a", class_="meta-pick")
            heroes_ = []
            for pick in picks:
                heroes_.append(heroes[pick['title']]) 
            cat.append(heroes_)
        meta.append(cat)

    return meta