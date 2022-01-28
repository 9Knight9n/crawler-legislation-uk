import os.path
import requests
import pandas as pd
from openpyxl import load_workbook

from extract.act import get_act_details
from save import files_dir,act_list_dir


excel = pd.read_excel(act_list_dir,)
wb = load_workbook(act_list_dir)
ws = wb.worksheets[0]


def dl_file(url,name):
    path = files_dir+"/"+name
    if os.path.isfile(files_dir+"/"+name):
        print(f'file {url} already exist as {path} .skipping...')
        return
    r = requests.get(url)
    open(files_dir+"/"+name, 'wb').write(r.content)




def append_act(p_id:str):
    temp = p_id.split("/")
    type_ = temp[0]
    year = temp[1]
    num = temp[2]
    if already_added(type_, year, num):
        print(f'Act {p_id} already loaded.')
        return
    act_detail = get_act_details(p_id)
    # print(act_detail)
    ws.append([type_,year,num,act_detail['title'],act_detail['extend'],act_detail['note']])
    wb.save(act_list_dir)
    # print(act_detail['files'].keys())
    for key in act_detail['files'].keys():
        dl_file(act_detail['files'][key],type_+"#"+year+"#"+num+key)





def already_added(type_,year,num):
    t_index = -1
    y_index = -1
    n_index = -1
    for index , t in enumerate(excel['type']):
        if t==type_:
            t_index = index
    for index , t in enumerate(excel['year']):
        if str(t)==year:
            y_index = index
    for index , t in enumerate(excel['number']):
        if str(t)==num:
            n_index = index
    if t_index == y_index and t_index==n_index and t_index != -1:
        return True
    else:
        return False





# append_act("eudn/2020/2255")