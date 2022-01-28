import os

import pandas as pd

base_dir = "extracted_data"
type_list_dir = base_dir+"/types.xlsx"
act_list_dir = base_dir+"/acts.xlsx"
files_dir = base_dir+"/files"

if not os.path.isdir(base_dir):
    os.mkdir(base_dir)

if not os.path.isdir(files_dir):
    os.mkdir(files_dir)

if not os.path.isfile(act_list_dir):
    df = pd.DataFrame({'type': [],'year':[],'number':[],'title':[],'extend':[],'note':[]})
    df.to_excel(act_list_dir, index=False)