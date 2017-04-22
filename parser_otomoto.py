import requests
from bs4 import BeautifulSoup

def get_links(url):
    '''
    Function returns list of parsed links within class in variable ads
    :param url: 
    '''
    res = requests.get(url)
#    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')

    ads = soup.select('.offer-item__photo-link')

    links = []
    for ad in ads:
        links.append(ad.get('href'))

    return links
