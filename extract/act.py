import requests
from bs4 import BeautifulSoup
from extract import headers,base_url

def is_note_available(soup):
    extend = soup.find_all(id="legEnLink")
    return len(extend)>0


def get_act_details(p_id):
    url = base_url + p_id + "?view=extent"
    # print(url)
    f = requests.get(url, headers=headers)
    # print(f.content)
    soup = BeautifulSoup(f.content, 'lxml')
    extend = get_extent(soup)
    title = get_title(soup)
    # pdf=get_dl_act_url(p_id,"pdf")
    xht=get_dl_act_url(p_id,"xht?view=snippet&wrap=true")
    # note_pdf=get_dl_act_note_url(p_id,"pdf")
    # note_xht=get_dl_act_note_url(p_id,"xht?view=snippet&wrap=true")
    # files = {'.pdf':pdf,'.xht':xht}
    files = {'.xht':xht}
    note_available = is_note_available(soup)
    # if note_available:
    #     files['#note.pdf']=note_pdf
    #     files['#note.xht']=note_xht
    return {"extend":extend,'title':title,'note':"yes" if note_available else "no",'files':files}


def get_txt(url):
    f = requests.get(url, headers=headers)
    soup = BeautifulSoup(f.content, 'lxml')
    # kill all script and style elements
    for script in soup(["script", "style", "head"]):
        script.extract()  # rip it out
    return soup



def get_links(url):
    f = requests.get(url, headers=headers)
    soup = BeautifulSoup(f.content, 'lxml')
    links = []
    tags =  soup.find_all("a")
    for tag in tags:
        if "href" in str(tag) and str(tag['href']).startswith(base_url):
            links.append(tag['href'])
    return links

def get_extent(soup):
    extend = soup.find_all(class_ = "LegExtentRestriction")
    if len(extend)>0:
        extend = extend[0]
    else:
        return ""
    return extend.get_text()

def get_title(soup):
    # print(soup.prettify())
    title = soup.select("#pageTitle")[0]
    return title.get_text()

def get_dl_act_url(p_id,file_type):
    url = base_url+p_id+"/data."+file_type
    return url


def get_dl_act_note_url(p_id,file_type):
    url = base_url + p_id + "/note/data." + file_type
    return url



