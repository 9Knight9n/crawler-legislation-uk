import os

import pandas as pd

from save import files_list_dir,txt_files_dir


def remove_files_with_type(type_:str):
    excel = pd.read_excel(files_list_dir, )
    docs = excel.loc[excel['type'] == type_]
    count = 0
    # print(docs["title"])
    for doc in docs['title']:
        # print(doc)
        # print(doc['title'])
        if os.path.exists(txt_files_dir+"/"+doc+".txt"):
            os.remove(txt_files_dir+"/"+doc+".txt")
            count += 1

    print(f'{count} files deleted.')




if __name__ == '__main__':
    remove_files_with_type("Church of England Measures")
    remove_files_with_type("Church Instruments")