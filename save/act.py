import os.path
import requests
from save import files_dir, txt_files_dir
from utils import fix_dir_name


def dl_file(url, name, _dir):
    path = files_dir + "/" + _dir + "/" + name
    if os.path.isfile(files_dir + "/" + name):
        print(f'file {url} already exist as {path} .skipping...')
        return
    try:
        r = requests.get(url)
        open(path, 'wb').write(r.content)
    except:
        return None
    return True


def save_txt(name, text):
    try:
        f = open(txt_files_dir + "/" + fix_dir_name(name).strip() + ".txt", "w", encoding="utf-8")
        for line in text:
            f.write(line)
        f.close()
    except Exception as e:
        print(f'failed to save file {name}.')
        return False
    return True
