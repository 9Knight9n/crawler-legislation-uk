import sys
import pandas as pd
from extract import base_url
from save import fetched_urls_dir, skipped_files_list_dir
from save.act import append_act
from extract.act_list import get_act_list_single_page
import os
from openpyxl import load_workbook

from utils import trim

urls=[
    "?list_itself=&bpas=cd00000&a3=102000484&a3type=1&a3value=&a6=&a6type=1&a6value=&a15=&a15type=1&a15value=&a7type=1&a7from=&a7to=&a7date=&a8=&a8type=1&a1=&a0=&a16=&a16type=1&a16value=&a17=&a17type=1&a17value=&a4=&a4type=1&a4value=&a23=&a23type=1&a23value=&textpres=&sort=7&x=51&y=11",
    # "?searchlist=&bpas=cd00000&a3=102000484&a3type=1&a3value=&a6=&a6type=1&a6value=&a15=&a15type=1&a15value=&a7type=1&a7from=&a7to=&a7date=&a8=&a8type=1&a1=&a0=&a16=&a16type=1&a16value=&a17=&a17type=1&a17value=&a4=&a4type=1&a4value=&a23=&a23type=1&a23value=&textpres=&sort=7&x=51&y=11",
    # "ukla",
    # "ukcm",
    # "ukci",
    # "uksro",
    # "uksi",
]
urls_max=[
    5,
    # 4000,
    # 4000,
    # 4000,
    # 4000,
    # 4000,
]

excel = pd.read_excel(skipped_files_list_dir,)
wb = load_workbook(skipped_files_list_dir)
ws = wb.worksheets[0]

for index,url in enumerate(urls):
    print(f"started fetching '{base_url}{url}' ...")
    # page_file_dir = fetched_urls_dir + f"/url_{url}.txt"
    # if not os.path.isfile(page_file_dir):
    #     f = open(page_file_dir, "w")
    #     f.write(str(1) + "\n")
    #     f.close()
    # file = open(page_file_dir, "r")
    # page = file.readline()
    # file.close()
    # page = int(page)
    start=0
    count = 0
    stored_exception = None

    while True:
        # acts = []
        # try:
        acts = get_act_list_single_page(url,start)
        print(acts)
        start +=20
        # except KeyboardInterrupt or SystemExit:
        #     stored_exception = sys.exc_info()
        # except:
        #     print(f'error fetching page "{base_url}{url}?page={start}"')
        #     continue
        for index_, act in enumerate(acts):
            # try:
                # count += 1
                # print(f'fetching {act}')
            status = append_act(act)
            # if status is None:
            #     ws.append([trim(base_url+act)])
            #     wb.save(skipped_files_list_dir)
            #     continue
            count += 1

            if count == urls_max[index]:
                stored_exception = "None"
                break
            # except KeyboardInterrupt or SystemExit:
            #     stored_exception = sys.exc_info()
            # except:
            #     print(f'error fetching act {act["pid"]}')
            #     ws.append([trim(base_url + act['pid'])])
            #     wb.save(skipped_files_list_dir)
            #     continue
        # if stored_exception:
        #     break
        # if len(acts) == 0:
        #     break
        # page += 1
        # try:
        #     f = open(page_file_dir, "w")
        #     f.write(str(page) + "\n")
        #     f.close()
        # except KeyboardInterrupt or SystemExit:
        #     stored_exception = sys.exc_info()

        print(f'total processed acts :{count}')

    if stored_exception:
        print("Either max act count limit reached or user stopped the process!")

    print(f"finished fetching '{base_url}{url}' ...")




