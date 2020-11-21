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

# User = "Pierre"
User = "Benjamin"

###############################################################################
# Load champions database to get all names

DataChamp = pd.read_csv("Data\\Results\\Dragon\\Champions\\results_champ_stats.tsv",sep='\t')

###############################################################################

for champ in DataChamp["Champions"]:
    # Get URL for iterated cham
    UrlRequestChamp = "http://ddragon.leagueoflegends.com/cdn/10.21.1/img/champion/"+champ+".png"
    # Create save path
    SavePath = "Data\\Images\\Champions\\ChampionSquareAssets\\"+champ+".png"
    # Request the png file
    urllib.request.urlretrieve(UrlRequestChamp, SavePath)
