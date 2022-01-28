from save.act import append_act
from extract.act_list import get_act_list_single_page



page = 1

while True:
    print(f'getting all acts in page {page}...')
    acts = get_act_list_single_page(page)
    print(f'found {len(acts)} acts in page {page}.')
    for index_,act in enumerate(acts):
        print(f'processing act {index_+1} in page {page}.')
        append_act(act)
    if page > 10:
        break
    if len(acts)==0:
        break
    page+=1
    print("---------------------------------------------")
