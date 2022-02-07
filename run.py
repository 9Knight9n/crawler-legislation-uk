import sys

from save import base_dir
from save.act import append_act
from extract.act_list import get_act_list_single_page
import os

page_file_dir = base_dir+'/pages_loaded.txt'
if not os.path.isfile(page_file_dir):
    f = open(page_file_dir, "w")
    f.write(str(1)+"\n")
    f.close()
file = open(page_file_dir,"r")
page = file.readline()
file.close()
page = int(page)

count=0
stored_exception=None

while True:
    acts=[]
    try:
        acts = get_act_list_single_page(page)
    except KeyboardInterrupt or SystemExit:
        stored_exception=sys.exc_info()
    except :
        print(f'error fetching page {page}')
        continue
    for index_,act in enumerate(acts):
        try:
            count+=1
            append_act(act)
        except KeyboardInterrupt or SystemExit:
            stored_exception = sys.exc_info()
        except:
            print(f'error fetching act {act}')
            continue
    if stored_exception:
        break
        # break
    # break
    # if page > 10:
    #     break
    if len(acts)==0:
        break
    page+=1
    f = open(page_file_dir, "w")
    f.write(str(page) + "\n")
    f.close()
    print(f'total processed acts :{count}')


if stored_exception:
    raise stored_exception[0](stored_exception[1]).with_traceback(stored_exception[2])
