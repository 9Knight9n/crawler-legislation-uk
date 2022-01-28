from save.act import append_act
from extract.act_list import get_act_list_single_page



page = 1
count=0

while True:
    acts = get_act_list_single_page(page)
    for index_,act in enumerate(acts):
        count+=1
        append_act(act)
    if page > 10:
        break
    if len(acts)==0:
        break
    page+=1
    print(f'total processed acts :{count} .')
