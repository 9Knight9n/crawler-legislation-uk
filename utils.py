def fix_dir_name(name:str):
    return name.replace("\\","-").replace("/","-").replace(":","-").replace("*","-")\
        .replace('"',"-").replace("<","-").replace(">","-").replace("|","-").replace("?","-")

def trim(string:str):
    return string.strip()


# print(fix_dir_name(r'/\:*?"<>|'))