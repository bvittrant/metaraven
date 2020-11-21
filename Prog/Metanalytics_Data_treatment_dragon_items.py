###############################################################################

# Treat item infos from dragon file from LoL api

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

Stats_items = data['basic']['stats'].keys()
Items = []
# Load the champ json file
for File in os.listdir("Data\Dragon\Items"):
    if File.endswith("FR.json"):
        L = "FR"
    if File.endswith("EN.json"):
        L = "EN"
    # Opening JSON file
    JSON = ".\\Data\\Dragon\\Items\\" + str(File)
    f = open(JSON , "r", encoding='utf-8')
    # returns JSON object as a dictionary 
    data = json.load(f)
    for item in data['data']:
        tmp_row = []
        # Create values per item
        version = data['version']
        ImageFull = data['data'][item]['image']['full']
        ImageSprite = data['data'][item]['image']['sprite']
        Map11 = data['data'][item]['maps']['11']
        name = data['data'][item]['name']
        plaintext = data['data'][item]['plaintext']
        goldbase = data['data'][item]['gold']['base']
        goldtotal = data['data'][item]['gold']['total']
        goldsell = data['data'][item]['gold']['sell']
        if "into" in data['data'][item]:
            Into = '-'.join(data['data'][item]['into'])
        else:
            Into = "Nothing"
        if "from" in data['data'][item]:
            From = '-'.join(data['data'][item]['from'])
        else:
            From = "Nothing"
        Id = item
        tmp_row = [version,L,ImageFull,ImageSprite,Map11,Id,name,plaintext,goldbase,goldtotal,goldsell,Into,From]

        tmp_stats = data['data'][item]['stats']
        # Now we iterate on all the stats and see if we have it in tmp_stat
        for stat in Stats_items:
            if stat in tmp_stats:
                tmp_row.append(data['data'][item]['stats'][stat])
            else:
                tmp_row.append(0)
        Items.append(tmp_row)

    # Closing file 
f.close()
DfItemsStats = pd.DataFrame.from_dict(Items, orient='columns')
Colnames = ["Version","Lang","Image Full","Image sprite","Map11","Id","Name","Description","Cost", "Total cost", "Sell value","Into","From"]
Colnames = Colnames + list(Stats_items)
DfItemsStats.columns = Colnames

# Export the file as tsv
File_tsv = ".\\Data\\Results\\Dragon\\items\\results_items_stats"+".tsv"
DfItemsStats.to_csv(File_tsv, sep='\t', index=False, quotechar='"')
DfItemsStats
