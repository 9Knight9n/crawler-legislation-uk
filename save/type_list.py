import os.path

import pandas as pd
from save import type_list_dir


def save_type_list(type_dict:dict):
    if os.path.isdir(type_list_dir):
        return
    df = pd.DataFrame({'short_name': type_dict.keys(),'long_name':type_dict.values()})
    df.to_excel(type_list_dir, index=False)




