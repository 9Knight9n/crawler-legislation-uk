import requests
from bs4 import BeautifulSoup
from extract import headers,base_url



def get_act_list_single_page(url,num):
    f = requests.get(base_url+url+"?page="+str(num), headers=headers)
    soup = BeautifulSoup(f.content, 'lxml')
    current_page = soup.select("li.currentPage strong")[0].get_text().replace("This is results page ","")
    if num != int(current_page):
        return []
    acts_query = soup.select("#content tbody tr")
    acts=[]
    last = ["",""]
    for tr in acts_query:
        act = {}
        a = tr.select("td a")
        act['pid'] = a[0]['href'].replace("/contents","")[1:]
        if len(a)>1:
            temp = a[1].get_text().split(" ")
            last=temp
        else:
            temp = last
        act['year'] = temp[0]
        act['number'] = temp[1]
        acts.append(act)
    # acts = [x['href'].replace("/contents","")[1:] for x in acts_query]
    #     print(act['number'])
    # years =
    return acts


# get_act_list_single_page("ukpga",1)