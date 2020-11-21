###############################################################################

# Main Video analysis program
# Benjamin Vittrant & Pierre Boileau for metaraven
# 10/2020

###############################################################################

# Import libraries
exec(open('Scripts/Modules.py').read())

###############################################################################
# Functions
###############################################################################

# Import a bunch of useful function
exec(open('Scripts/Functions.py').read())

###############################################################################
# Main features
###############################################################################

current_date = date.today()
current_date = current_date.strftime("%d-%m-%Y")
current_time = datetime.now()
current_time = current_time.strftime("%H-%M-%S")
DateTime = current_date+"_"+current_time

###############################################################################
# Recovering current summoner

UrlsummonerUs = "http://ddragon.leagueoflegends.com/cdn/10.21.1/data/en_US/summoner.json"
# Write data into tmp json file
open('.\\Data\\tmp.json', 'wb').write(requests.get(UrlsummonerUs).content)
# Open the tmp json file downloaded
Datasummoner = json.load(open('.\\Data\\tmp.json', "r", encoding='utf-8'))

################################################################################

# Use the keys from the data downloaded to get icons
for sum in Datasummoner["data"].keys():
    # Get URL for iterated cham
    UrlRequestSum = "http://ddragon.leagueoflegends.com/cdn/10.21.1/img/spell/"+sum+".png"
    # Create save path
    SavePath = "Data\\Images\\Summoner\\10.21.1\\"+sum+".png"
    # Request the png file
    urllib.request.urlretrieve(UrlRequestSum, SavePath)


