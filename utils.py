from bs4 import BeautifulSoup
import html2text


def fix_dir_name(name:str):
    return name.replace("\\","-").replace("/","-").replace(":","-").replace("*","-")\
        .replace('"',"-").replace("<","-").replace(">","-").replace("|","-").replace("?","-")

def trim(string:str):
    return string.strip()


def convert_xht_to_txt(html):
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style","head"]):
        script.extract()  # rip it out


    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    print(text)

    return text


def convert_xht_to_txt_2(html):
    h = html2text.HTML2Text()
    h.ignore_links = True
    # print(h.handle(html))
    return trim(h.handle(html))
