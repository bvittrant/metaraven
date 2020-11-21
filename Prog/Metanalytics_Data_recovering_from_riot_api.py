###############################################################################
###############################################################################

# Retrieve information we want from champions

###############################################################################

# Import libraries

import requests
import os
import json
import pandas as pd
import itertools
import importlib.util
import time
from datetime import datetime
from datetime import date

###############################################################################
# Main features
current_date = date.today()
current_date = current_date.strftime("%d-%m-%Y")
current_time = datetime.now()
current_time = current_time.strftime("%H-%M-%S")
DateTime = current_date+"_"+current_time

###############################################################################
# Import setting (API key)

exec(open('Scripts/Settings.py').read())

###############################################################################

# WARNING : Don't touch the list order in any way during the process
# because eveything is linked by the order of the lists

###############################################################################
###############################################################################
# For each available region & Leagues retrieve players names 
Regions = ["br1","eun1","euw1", "jp1", "kr","la1","la2","na1","oc1","ru","tr1"]
Regions_list = []
Leagues = ["challengerleagues", "grandmasterleagues"]
Leagues_list = []
summoner_list = []
ReqLim = 1 # Need to limit request in test because of riot
for Leagues_IT in Leagues:
    for Regions_IT in Regions:
        # Define URL request by regions and league
        UrlFile5x5JSON = "https://"+Regions_IT+".api.riotgames.com/lol/league/v4/"+Leagues_IT+"/by-queue/RANKED_SOLO_5x5"+API_URL
        # Request url json data
        File5x5JSON = requests.get(UrlFile5x5JSON)
        # Write data into json file
        open('.\\Data\\File5x5JSON.json', 'wb').write(File5x5JSON.content)
        # read the json file
        # Opening JSON file 
        tmp = open('.\\Data\\File5x5JSON.json', "r", encoding='utf-8')
        # returns JSON object as a dictionary 
        Data5x5JSON = json.load(tmp)
        # closing the file 
        tmp.close()
        if "status" in Data5x5JSON:
            print(Data5x5JSON["status"]["message"])
            break
        # Iterating through the json
        for i in range(0,len(Data5x5JSON['entries'])):
            # Create a row per stats per champ
            summoner_list.append(Data5x5JSON["entries"][i]["summonerId"])
            # Add the region in the list
            Regions_list.append(Regions_IT)
            # Add the leagues in the list
            Leagues_list.append(Leagues_IT)
            ReqLim = ReqLim + 1
            #if ReqLim == 3:
            #    ReqLim = 1
            #    break

# Clean JSON       
if os.path.exists(".\\Data\\File5x5JSON.json"):
  os.remove(".\\Data\\File5x5JSON.json")
else:
  print("The file does not exist")

# Create dataframe
df_players_names = pd.DataFrame(columns=['Region','League','Summoner'])
df_players_names['Region'],df_players_names['League'], df_players_names['Summoner'] = Regions_list, Leagues_list, summoner_list
# Export the file as tsv
df_players_names.to_csv(".\\Data\\Results\\Summoner\\results_"+current_date+"_df_summoner001.tsv", sep='\t', index=False)
# read the file
df_summoners = pd.read_csv(".\\Data\\Results\\Summoner\\results_"+current_date+"_df_summoner001.tsv", sep='\t')

###############################################################################
###############################################################################
# Add puuid
puuid_list = []
for i in range(0,df_summoners.shape[0]):
    UrlsummonerIdJSON = "https://"+df_summoners.loc[i,"Region"]+".api.riotgames.com/lol/summoner/v4/summoners/"+df_summoners.loc[i,"Summoner"]+API_URL
    # Request url json data
    UrlsummonerIdJSON = requests.get(UrlsummonerIdJSON)
    # Write data into json file
    open('.\\Data\\tmp.json', 'wb').write(UrlsummonerIdJSON.content)
    # Open the temporary summonerId file
    tmp = open('.\\Data\\tmp.json', "r", encoding='utf-8')
    # returns JSON object as a dictionary 
    DatasummonerIdJSON = json.load(tmp)
    # closing the file 
    tmp.close()
    if "status" in DatasummonerIdJSON:
        print(DatasummonerIdJSON["status"]["message"])
        break
    puuid_list.append(DatasummonerIdJSON["puuid"])

# Clean JSON       
if os.path.exists(".\\Data\\tmp.json"):
  os.remove(".\\Data\\tmp.json")
else:
  print("The file does not exist")

# add PUIID to dataframe
df_summoners = df_summoners.loc[0:(len(puuid_list)-1),]
df_summoners['puuid'] = puuid_list
# Export the file as tsv
df_summoners.to_csv(".\\Data\\Results\\Summoner\\results_"+current_date+"_df_summoner002.tsv", sep='\t', index=False)
# read the file
df_summoners = pd.read_csv(".\\Data\\Results\\Summoner\\results_"+current_date+"_df_summoner002.tsv", sep='\t')

###############################################################################
###############################################################################
# Add account ID
accountId_list = []
for i in range(0,df_summoners.shape[0]):
    UrlsummonerIdJSON = "https://"+df_summoners.loc[i,"Region"]+".api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+df_summoners.loc[i,"puuid"]+API_URL
    # Request url json data
    UrlaccountIdJSON = requests.get(UrlsummonerIdJSON)
    # Write data into json file
    open('.\\Data\\tmp.json', 'wb').write(UrlaccountIdJSON.content)
    # Open the temporary summonerId file
    tmp = open('.\\Data\\tmp.json', "r", encoding='utf-8')
    # returns JSON object as a dictionary 
    DataaccountIdJSON = json.load(tmp)
    # closing the file 
    tmp.close()
    if "status" in DataaccountIdJSON:
        print(DataaccountIdJSON["status"]["message"])
        break
    accountId_list.append(DataaccountIdJSON["accountId"])

# Clean JSON       
if os.path.exists(".\\Data\\tmp.json"):
  os.remove(".\\Data\\tmp.json")
else:
  print("The file does not exist")

# add account ID to dataframe
df_summoners = df_summoners.loc[0:(len(accountId_list)-1),]
df_summoners['accountId'] = accountId_list
# Export the file as tsv
df_summoners.to_csv(".\\Data\\Results\\Summoner\\results_"+current_date+"_df_summoner003.tsv", sep='\t', index=False)
# read the file
df_summoners = pd.read_csv(".\\Data\\Results\\Summoner\\results_"+current_date+"_df_summoner003.tsv", sep='\t')

###############################################################################
###############################################################################
# Now we have a list of accountID associated to interesting players we can
# check all the matchs associated to these accounts
matches_list = []
for i in range(0, df_summoners.shape[0]):
    UrlaccountIdJSON = "https://"+df_summoners.loc[i,"Region"]+".api.riotgames.com/lol/match/v4/matchlists/by-account/"+df_summoners.loc[i,"accountId"]+API_URL
    UrlaccountIdJSON = requests.get(UrlaccountIdJSON)
    # Write data into json file
    open('.\\Data\\tmp.json', 'wb').write(UrlaccountIdJSON.content)
    # Open the temporary summonerId file
    tmp = open('.\\Data\\tmp.json', "r", encoding='utf-8')
    # returns JSON object as a dictionary 
    DatamatchesJSON = json.load(tmp)
    # closing the file 
    tmp.close()
    if "status" in DatamatchesJSON:
        print(DatamatchesJSON["status"]["message"])
        break
    for j in range(0,len(DatamatchesJSON['matches'])):
        tmp_dic = DatamatchesJSON['matches'][j]
        tmp_dic['accountId'] = accountId_list[i]
        matches_list.append(tmp_dic)
    # closing the file 
    tmp.close()

# Clean JSON       
if os.path.exists(".\\Data\\tmp.json"):
  os.remove(".\\Data\\tmp.json")
else:
  print("The file does not exist")

# Transforming all the rows in a dataframe
df_matches_infos = pd.DataFrame.from_dict(matches_list, orient='columns')
# Export the file as tsv
df_matches_infos.to_csv(".\\Data\\Results\\Matches\\results_"+current_date+"_matches_infos.tsv", sep='\t', index=False)
# read the file
df_matches_infos = pd.read_csv(".\\Data\\Results\\Matches\\results_"+current_date+"_matches_infos.tsv", sep='\t')

###############################################################################
###############################################################################

# Now we have a list of games associated to all interesting queue (Grandmaster&challenger)
# linked to accountId, puuId. We can work on the interesting data within all those games.

# Define a list of gameId & Region list
GameId_Dic = []
rowsMatch = []
T1 = 0
T2 = 1

# Create vec name for timelapse
TimelapseNamesGold = []
TimelapseNamesXp = []


for i in range(0,df_matches_infos.shape[0]):
    #print(f"We're at i:{i}")
    UrlgameIdJSON = "https://"+df_matches_infos.loc[i,"platformId"].lower()+".api.riotgames.com/lol/match/v4/matches/"+str(df_matches_infos.loc[i,"gameId"])+API_URL
    gameIdJSON = requests.get(UrlgameIdJSON)
    # Write data into json file
    open('.\\Data\\tmp.json', 'wb').write(gameIdJSON.content)
    # Open the temporary summonerId file
    tmp = open('.\\Data\\tmp.json', "r", encoding='utf-8')
    # returns JSON object as a dictionary 
    DataGameJSON = json.load(tmp)
    # Closing file 
    tmp.close()
    # If status exist as a key that means we just have a json with error
    # Mostly limit request excceed then we break ton continue the script. Need to renew key api.
    if "status" in DataGameJSON:
        print(DataGameJSON["status"]["message"])
        break
    # Now we can buil a list with what we want exactly
    # defining features for better readability
    Team1_Ban = []
    Team1_Champ = []
    Team1_roleChamp = []
    Team1_DeltaXp = []
    Team1_DeltaGold = []
    Team2_Ban = []
    Team2_Champ = []
    Team2_roleChamp = []
    Team2_DeltaXp = []
    Team2_DeltaGold = []

    # participants range from 0 to 9 (for team 1 and then team 2)
    # Id follow the same logic but range from 1 to 10
    for j in range(0,5):
        # Handle case when there is no ban (a player didn't ban)
        if not DataGameJSON["teams"][T1]["bans"]:
            Team1_Ban.append("NA")
        else:
            Team1_Ban.append(str(DataGameJSON["teams"][T1]["bans"][j]["championId"]))
        if not DataGameJSON["teams"][T2]["bans"]:
            Team2_Ban.append("NA")
        else:
            Team2_Ban.append(str(DataGameJSON["teams"][T2]["bans"][j]["championId"]))

        Team1_Champ.append(str(DataGameJSON["participants"][j]["championId"]))
        Team2_Champ.append(str(DataGameJSON["participants"][j+5]["championId"]))

        Team1_roleChamp.append(DataGameJSON["participants"][j]["timeline"]["lane"]+"-"+DataGameJSON["participants"][j]["timeline"]["role"]+"-"+str(DataGameJSON["participants"][j]["championId"]))
        Team2_roleChamp.append(DataGameJSON["participants"][j+5]["timeline"]["lane"]+"-"+DataGameJSON["participants"][j+5]["timeline"]["role"]+"-"+str(DataGameJSON["participants"][j+5]["championId"]))
        
        # The hard part comes here. We need to fill xp and gold delta per player.
        # To deal with the json notation which like x-END for the last timelaspe available we need
        # to set up a tmp_delta. Just notice that the first timelapse is alway 0-10 and not 0-END
        
        # Check if match last long enough or there will be no timeline data
        if "goldPerMinDeltas" in DataGameJSON["participants"][j]["timeline"].keys():
            # Check final delta value - Set the len of the timeline
            tmpLen = len(DataGameJSON["participants"][j]["timeline"]["goldPerMinDeltas"].keys())
            # Gold
            Team1_DeltaGold.append(list(DataGameJSON["participants"][j]["timeline"]["goldPerMinDeltas"].values())[tmpLen-1])
            Team2_DeltaGold.append(list(DataGameJSON["participants"][j+5]["timeline"]["goldPerMinDeltas"].values())[tmpLen-1])
            # XP
            Team1_DeltaXp.append(list(DataGameJSON["participants"][j]["timeline"]["xpPerMinDeltas"].values())[tmpLen-1])
            Team2_DeltaXp.append(list(DataGameJSON["participants"][j+5]["timeline"]["xpPerMinDeltas"].values())[tmpLen-1])
        # If match too short just put NA values
        else:
            Team1_DeltaGold.append("NA")
            Team2_DeltaGold.append("NA")
            Team1_DeltaXp.append("NA")
            Team2_DeltaXp.append("NA")


    # Now we fill a row with all the info we want for a game
    # Team 1
    Team1_List = [str(DataGameJSON["gameId"])] + [str(DataGameJSON["gameVersion"])] + [str(DataGameJSON["gameDuration"])] + [str(DataGameJSON["gameMode"])]+ \
    [df_matches_infos.loc[i,"platformId"]] + [str(DataGameJSON["teams"][T1]["teamId"])] +\
    [DataGameJSON["teams"][T1]["win"]] +[DataGameJSON["teams"][T1]["firstBlood"]] +[DataGameJSON["teams"][T1]["firstTower"]] +[DataGameJSON["teams"][T1]["firstInhibitor"]] +\
    [DataGameJSON["teams"][T1]["firstBaron"]] +[DataGameJSON["teams"][T1]["firstDragon"]] +[DataGameJSON["teams"][T1]["firstRiftHerald"]] +[DataGameJSON["teams"][T1]["towerKills"]] +\
    [DataGameJSON["teams"][T1]["inhibitorKills"]] +[DataGameJSON["teams"][T1]["baronKills"]] +[DataGameJSON["teams"][T1]["dragonKills"]] +[DataGameJSON["teams"][T1]["riftHeraldKills"]] +\
    Team1_Ban + Team1_Champ + Team1_roleChamp + Team1_DeltaGold + Team1_DeltaXp
    # Team 2
    Team2_List = [str(DataGameJSON["gameId"])] + [str(DataGameJSON["gameVersion"])] + [str(DataGameJSON["gameDuration"])] + [str(DataGameJSON["gameMode"])]+ \
    [df_matches_infos.loc[i,"platformId"]] + [str(DataGameJSON["teams"][T2]["teamId"])] +\
    [DataGameJSON["teams"][T2]["win"]] +[DataGameJSON["teams"][T2]["firstBlood"]] +[DataGameJSON["teams"][T2]["firstTower"]] +[DataGameJSON["teams"][T2]["firstInhibitor"]] +\
    [DataGameJSON["teams"][T2]["firstBaron"]] +[DataGameJSON["teams"][T2]["firstDragon"]] +[DataGameJSON["teams"][T2]["firstRiftHerald"]] +[DataGameJSON["teams"][T2]["towerKills"]] +\
    [DataGameJSON["teams"][T2]["inhibitorKills"]] +[DataGameJSON["teams"][T2]["baronKills"]] +[DataGameJSON["teams"][T2]["dragonKills"]] +[DataGameJSON["teams"][T2]["riftHeraldKills"]] +\
    Team2_Ban + Team2_Champ + Team2_roleChamp + Team2_DeltaGold + Team2_DeltaXp

    rowsMatch.append(Team1_List)
    rowsMatch.append(Team2_List)

# Clean JSON       
if os.path.exists(".\\Data\\tmp.json"):
  os.remove(".\\Data\\tmp.json")
else:
  print("The file does not exist")

TimelapseNamesGold = ["Id1_gold","Id2_gold","Id3_gold","Id4_gold","Id5_gold"]
TimelapseNamesXp = ["Id1_xp","Id2_xp","Id3_xp","Id4_xp","Id5_xp"]

df_matches_infos = pd.DataFrame.from_dict(rowsMatch, orient='columns')
NamesMatches = ["gameId","gameVersion","gameDuration","gameMode", "platformId", "teamsId", "win","firstBlood","firstTower","firstInhibitor","firstBaron","firstDragon",\
"firstRiftHerald","towerKills","inhibitorKills","baronKills","dragonKills","riftHeraldKills",\
"Ban1", "Ban2", "Ban3", "Ban4", "Ban5", "Pick1", "Pick2", "Pick3", "Pick4", "Pick5", "RolePick1", "RolePick2", "RolePick3", "RolePick4", "RolePick5",\
] + TimelapseNamesGold + TimelapseNamesXp
df_matches_infos.columns = NamesMatches

# Export the file as tsv
df_matches_infos.to_csv(".\\Data\\Results\\Matches\\results_"+current_date+"_allData_001.tsv", sep='\t', index=False)
# Read the new file
df_matches_infos = pd.read_csv(".\\Data\\Results\\Matches\\results_"+current_date+"_allData_001.tsv", sep='\t')

###############################################################################
###############################################################################

# Data treatment from previous Dataframe. We're going to create new data to help
# work on the draft
df_matches_infos["TOP"] = "NA"
df_matches_infos["ADC"] = "NA"
df_matches_infos["SUP"] = "NA"
df_matches_infos["JUNGLER"] = "NA"
df_matches_infos["MID"] = "NA"
df_matches_infos["FullTeam"] = "NA"

PickList = ["RolePick1","RolePick2","RolePick3","RolePick4","RolePick5"] 
for i in range(0,df_matches_infos.shape[0]):
    WholeTeamList = []
    for pick in PickList:
        PoseRolCham = df_matches_infos.loc[i, pick].split("-")
        # Define jungler
        if PoseRolCham[0] == "JUNGLE" and PoseRolCham[1] == "NONE":
            df_matches_infos.loc[i,"JUNGLER"] = PoseRolCham[2]
        # Define TOP
        if PoseRolCham[0] == "TOP" and PoseRolCham[1] == "SOLO":
            df_matches_infos.loc[i,"TOP"] = PoseRolCham[2]
        # Define Middle
        if PoseRolCham[0] == "MIDDLE" and PoseRolCham[1] == "SOLO":
            df_matches_infos.loc[i,"MID"] = PoseRolCham[2]
        # Define ADC
        if PoseRolCham[0] == "BOTTOM" and PoseRolCham[1] == "DUO_CARRY":
            df_matches_infos.loc[i,"ADC"] = PoseRolCham[2]
         # Define SUP
        if PoseRolCham[0] == "BOTTOM" and PoseRolCham[1] == "DUO_SUPPORT":
            df_matches_infos.loc[i,"SUP"] = PoseRolCham[2]
        WholeTeamList.append(PoseRolCham[2])
        
    # Define whole team
    df_matches_infos.loc[i,"FullTeam"] = "-".join(WholeTeamList)

# Export the file as tsv
df_matches_infos.to_csv(".\\Data\\Results\\Matches\\results_"+current_date+"_allData_002.tsv", sep='\t', index=False)
# Read the new file
df_matches_infos = pd.read_csv(".\\Data\\Results\\Matches\\results_"+current_date+"_allData_002.tsv", sep='\t')
# Ajouter gold diff à la fin et level/xp diff on pourra créer un taux de win rate personnalisé.
# Add all info founder here https://developer.riotgames.com/apis#match-v4/GET_getMatchl

###############################################################################
# Retrieve timeline data info per player and match

matchTimelineInfo = []
PreviousMatch = "0"
tmp_row = []

for i in range(0,df_matches_infos.shape[0]):
    #print(f"We're at i:{i}")
    if(str(df_matches_infos.loc[i,"gameId"]) == PreviousMatch ):
        continue
    PreviousMatch = str(df_matches_infos.loc[i,"gameId"])
    UrlgameIdJSON = "https://"+df_matches_infos.loc[i,"platformId"].lower()+".api.riotgames.com/lol/match/v4/timelines/by-match/"+str(df_matches_infos.loc[i,"gameId"])+API_URL
    gameIdJSON = requests.get(UrlgameIdJSON)
    # Write data into json file
    open('.\\Data\\tmp.json', 'wb').write(gameIdJSON.content)
    # Open the temporary summonerId file
    tmp = open('.\\Data\\tmp.json', "r", encoding='utf-8')
    # returns JSON object as a dictionary 
    DataGameJSON = json.load(tmp)
    # Closing file 
    tmp.close()
    # If status exist as a key that means we just have a json with error
    # Mostly limit request excceed then we break ton continue the script. Need to renew key api.
    if "status" in DataGameJSON:
        print(DataGameJSON["status"]["message"])
        break
    # Now we can buil a list with what we want exactly
    # defining features for better readability
    for j in range(1,11):
        tmp_row = [df_matches_infos.loc[i,"platformId"]] + [str(df_matches_infos.loc[i,"gameId"])] + list(DataGameJSON['frames'][len(DataGameJSON['frames'])-1]['participantFrames'][str(j)].values())
        matchTimelineInfo.append(tmp_row)
    
    # Find number of frame

namesTimeline = ['platformId','gameId','participantId', 'currentGold', 'totalGold', 'level', 'xp', 'minionsKilled', 'jungleMinionsKilled']
df_timeline_infos = pd.DataFrame.from_dict(matchTimelineInfo , orient='columns')
df_timeline_infos .columns = namesTimeline

# Export the file as tsv
df_matches_infos.to_csv(".\\Data\\Results\\Matches\\results_"+current_date+"_LastTimeline_001.tsv", sep='\t', index=False)

###############################################################################

# End