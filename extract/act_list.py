import requests
from bs4 import BeautifulSoup
from extract import headers,base_url



def get_act_list_single_page(url,num):
    f = requests.get(base_url+url+"?page="+str(num), headers=headers)
    soup = BeautifulSoup(f.content, 'lxml')
    current_page = soup.select("li.currentPage strong")[0].get_text().replace("This is results page ","")
    if num != int(current_page):
        return []
    acts_query = soup.select("td a")
    acts = [x['href'].replace("/contents","")[1:] for x in acts_query]
    return list(dict.fromkeys(acts))