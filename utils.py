def fix_dir_name(name:str):
    return name.replace("\\","-").replace("/","-").replace(":","-").replace("*","-")\
        .replace('"',"-").replace("<","-").replace(">","-").replace("|","-").replace("?","-")


# print(fix_dir_name(r'/\:*?"<>|'))