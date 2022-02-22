import os

import pandas as pd

base_dir = "extracted_data"
# type_list_dir = base_dir+"/types.xlsx"
files_list_dir = base_dir+"/files.xlsx"
skipped_files_list_dir = base_dir+"/skipped_files.xlsx"
# ref_list_dir = base_dir+"/refs.xlsx"
files_dir = base_dir+"/files"
fetched_urls_dir = base_dir+"/fetched_pages"
txt_files_dir = files_dir+"/txt"
txt_files_dir_converted = files_dir+"/txt_converted"
xht_files_dir = files_dir+"/xht"
pdf_files_dir = files_dir+"/pdf"

if not os.path.isdir(base_dir):
    os.mkdir(base_dir)

if not os.path.isdir(files_dir):
    os.mkdir(files_dir)

if not os.path.isdir(fetched_urls_dir):
    os.mkdir(fetched_urls_dir)

if not os.path.isdir(txt_files_dir):
    os.mkdir(txt_files_dir)

if not os.path.isdir(txt_files_dir_converted):
    os.mkdir(txt_files_dir_converted)

if not os.path.isdir(xht_files_dir):
    os.mkdir(xht_files_dir)

if not os.path.isdir(pdf_files_dir):
    os.mkdir(pdf_files_dir)

if not os.path.isfile(files_list_dir):
    df = pd.DataFrame({'type': [],'year':[],'number':[],'title':[],'extend':[],'note':[]})
    df.to_excel(files_list_dir, index=False)

if not os.path.isfile(skipped_files_list_dir):
    df = pd.DataFrame({'url': []})
    df.to_excel(skipped_files_list_dir, index=False)

# if not os.path.isfile(ref_list_dir):
#     df = pd.DataFrame({'act1': [],'act2':[]})
#     df.to_excel(ref_list_dir, index=False)