import requests
from bs4 import BeautifulSoup
from extract import headers,base_url

url = base_url+"all?page="

# def get_act_list():
#     f = requests.get(url, headers=headers)
#     soup = BeautifulSoup(f.content, 'lxml')
#     print(soup.prettify())
#     # type_list_id = ["legChoicesColRight", "legChoicesColLeft"]
#     # types = soup.find('div', id=type_list_id[0]).find_all('label') + soup.find('div', id=type_list_id[1]).find_all(
#     #     'label')
#     # print(types)
#     # return {x['for']: x.get_text() for x in types}


def get_act_list_single_page(num):
    f = requests.get(url+str(num), headers=headers)
    soup = BeautifulSoup(f.content, 'lxml')
    current_page = soup.select("li.currentPage strong")[0].get_text().replace("This is results page ","")
    if num != int(current_page):
        return []
    acts_query = soup.select("td a")
    acts = [x['href'].replace("/contents","")[1:] for x in acts_query]
    return list(dict.fromkeys(acts))