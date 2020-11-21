###############################################################################

# Treat champions infos from dragon file from LoL api

###############################################################################

# Open python interactive windows in VCS

# Python: Show Python Interactive window

###############################################################################

# Import libraries

# python -m pip install simplejson
# import simplejson as json

import json
import os
import pandas as pd

###############################################################################

# Checking current working directory

os.getcwd()
#os.chdir('C:\\Users\\Dafdesade\\Work\\Projets\\Meta')

###############################################################################

# Creating an empty rows list
rows = []
champ_list = []
key_list = []
lang_list = []
# Load the champ json file
for File in os.listdir("Data\Dragon\Champions"):
    if File.endswith("FR.json"):
        L = "FR"
    if File.endswith("EN.json"):
        L = "EN"
    # Opening JSON file
    JSON = ".\\Data\\Dragon\\Champions\\" + str(File)
    f = open(JSON , "r", encoding='utf-8')
    data = json.load(f)
    # Iterating through the json 
    for champ in data['data']:
        # Create a row per stats per champ
        rows.append(data['data'][champ]['stats'])
        champ_list.append(champ)
        key_list.append(data['data'][champ]['key'])
        lang_list.append(L)
    # Closing file 
    f.close()

 # Transforming all the rows in a dataframe
df_champ_stats = pd.DataFrame.from_dict(rows, orient='columns')
# Adding champions names to the df with stats
df_champ_stats['Champions'] = champ_list
df_champ_stats['key'] = key_list
df_champ_stats["Version"] = data['version']
df_champ_stats["Lang"] = lang_list
# Export the file as tsv
File_tsv = ".\\Data\\Results\\Dragon\\Champions\\results_champ_stats"+".tsv"
df_champ_stats.to_csv(File_tsv, sep='\t', index=False, quotechar='"')
###############################################################################

