import requests
from bs4 import BeautifulSoup
from extract import headers,base_url


def get_type_list():
    url = base_url+"search"
    f = requests.get(url, headers=headers)
    soup = BeautifulSoup(f.content, 'lxml')
    type_list_id = ["legChoicesColRight", "legChoicesColLeft"]
    types = soup.find('div', id=type_list_id[0]).find_all('label') + soup.find('div', id=type_list_id[1]).find_all(
        'label')
    return {x['for'][4:]: x.get_text() for x in types}



print(get_type_list())