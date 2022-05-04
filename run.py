import sys
import os
import time

sys.dont_write_bytecode = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django

django.setup()

# Import your models for use in your script
from db.models import *
from extract import base_url
from extract.act import get_act_details, get_act_txt
from extract.act_list import get_act_list_single_page

urls = [
    "ukpga",
    "ukla",
    "uksi",
]
urls_max = [
    90000,
    90000,
    90000,
]

start = time.time()

for index, url in enumerate(urls):
    print(f"started fetching '{base_url}{url}' ...")
    page = 0

    count = 0
    stored_exception = None
    second_chance = False

    while True:
        page += 1
        page_loaded = Page.objects.filter(url=url, num=page).count() > 0
        if page_loaded:
            continue

        acts = []
        try:
            print(f'fetching page "{base_url}{url}?page={page}"')
            acts = get_act_list_single_page(url, page)
        except KeyboardInterrupt or SystemExit:
            stored_exception = sys.exc_info()
            break
        except Exception as e:
            print(f'error fetching page "{base_url}{url}?page={page} (error:{e})"')
            continue
        if len(acts) == 0 and second_chance:
            break
        second_chance = len(acts) == 0
        for index_, act in enumerate(acts):
            try:
                act = get_act_details(act)
                text = get_act_txt(act['files']['.xht'])
            except KeyboardInterrupt or SystemExit:
                stored_exception = sys.exc_info()
                break
            except Exception as e:
                print(f'error fetching act {act["url"]} (error:{e})')
                continue
            if 'skipped' in act.keys():
                continue
            count += 1
            if count == urls_max[index]:
                stored_exception = "None"
                end = time.time()
                print(end - start)
                break
            Act.objects.create(url=act['url'], title=act['title'], text=text, type=act['type'], year=act['year'],
                               number=act['number'])

        Page.objects.create(url=url, num=page)

        print(f'total processed acts :{count}')
        if stored_exception:
            print("Either user stopped the process or max act count limit reached!")
            break


    if stored_exception:
        print("Either user stopped the process or max act count limit reached!")
        break

    print(f"finished fetching '{base_url}{url}' ...")
