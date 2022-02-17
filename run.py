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
    "ukpga",
    "ukla",
    "ukcm",
    "ukci",
    "uksro",
    "uksi",
]

excel = pd.read_excel(skipped_files_list_dir,)
wb = load_workbook(skipped_files_list_dir)
ws = wb.worksheets[0]

for index,url in enumerate(urls):
    print(f"started fetching '{base_url}{url}' ...")
    page_file_dir = fetched_urls_dir + f"/url_{url}.txt"
    if not os.path.isfile(page_file_dir):
        f = open(page_file_dir, "w")
        f.write(str(1) + "\n")
        f.close()
    file = open(page_file_dir, "r")
    page = file.readline()
    file.close()
    page = int(page)

    count = 0
    stored_exception = None

    while True:
        acts = []
        try:
            acts = get_act_list_single_page(url,page)
        except KeyboardInterrupt or SystemExit:
            stored_exception = sys.exc_info()
        except:
            print(f'error fetching page "{base_url}{url}?page={page}"')
            continue
        for index_, act in enumerate(acts):
            try:
                # if count > 100:
                #     break
                count += 1
                status = append_act(act)
                if status is None:
                    ws.append([trim(base_url+act)])
                    wb.save(skipped_files_list_dir)
            except KeyboardInterrupt or SystemExit:
                stored_exception = sys.exc_info()
            except:
                print(f'error fetching act {act}')
                ws.append([trim(base_url + act)])
                wb.save(skipped_files_list_dir)
                continue
        if stored_exception:
            break
            # break
        # break
        # if page > 10:
        #     break
        # if count > 100:
        #     break
        if len(acts) == 0:
            break
        page += 1
        try:
            f = open(page_file_dir, "w")
            f.write(str(page) + "\n")
            f.close()
        except KeyboardInterrupt or SystemExit:
            stored_exception = sys.exc_info()

        print(f'total processed acts :{count}')

    if stored_exception:
        raise stored_exception[0](stored_exception[1]).with_traceback(stored_exception[2])

    print(f"finished fetching '{base_url}{url}' ...")




