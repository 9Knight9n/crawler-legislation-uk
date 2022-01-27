import requests
from bs4 import BeautifulSoup
from extractors import headers,base_url


def get_type_list():
    url = base_url+"search"
    f = requests.get(url, headers=headers)
    soup = BeautifulSoup(f.content, 'lxml')
    # print(soup.prettify())
    type_list_id = ["legChoicesColRight", "legChoicesColLeft"]
    types = soup.find('div', id=type_list_id[0]).find_all('label') + soup.find('div', id=type_list_id[1]).find_all(
        'label')
    print(types)
    return {x['for']: x.get_text() for x in types}
