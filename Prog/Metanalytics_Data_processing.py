###############################################################################
# Data processing
###############################################################################
# Save the list of list of rows in a dataframe
DataVideoDF = pd.DataFrame(DataVideo)

# Create names for the columns
NamesPlayerLife = []
NamesPlayerSubBar = []
NamesPlayerGold = []
NamesPlayerKDA = []
NamesPlayerMinions = []
NamesPlayerWards = []
NamesChamps = []

for i in range(1,11):
    i = str(i)
    NamesPlayerLife.append("Player_"+i+"_Life")
    NamesPlayerSubBar.append("Player_"+i+"_SubBar")
    NamesPlayerGold.append("Player_"+i+"_GoldCurrent")
    NamesPlayerGold.append("Player_"+i+"_GoldTotal")
    NamesPlayerKDA.append("Player_"+i+"_K")
    NamesPlayerKDA.append("Player_"+i+"_D")
    NamesPlayerKDA.append("Player_"+i+"_A")
    NamesPlayerMinions.append("Player_"+i+"_Minions")
    NamesPlayerWards.append("Player_"+i+"_Wards")
    NamesChamps.append("Player_"+i+"_Champion")

NamesColumns = ['UserId',"Frame",'MIN','SEC', "TotalRedGold", "TotalBlueGold","RedKillsTotal", "BlueKillsTotal","RedTowerKill", "BlueTowerKill"]+\
    NamesPlayerLife + NamesPlayerSubBar +\
        NamesPlayerGold + NamesPlayerKDA + NamesPlayerMinions + NamesPlayerWards+\
            NamesChamps

# Visual checking
DataVideoDF.columns = NamesColumns

###############################################################################
# Data treatment
###############################################################################
# Lot of laundry treatment

for i in range(0,DataVideoDF.shape[0]):
    # take only integer character then add a dot just before the last 
    # Red gold change 
    tmp = re.sub("[^0-9]", "", DataVideoDF.loc[i, "TotalRedGold"])
    DataVideoDF.loc[i, "TotalRedGold"] = tmp[:-1] + "." + tmp[:1]
    # Blue gold change
    tmp = re.sub("[^0-9]", "", DataVideoDF.loc[i, "TotalBlueGold"])
    DataVideoDF.loc[i, "TotalBlueGold"] = tmp[:-1] + "." + tmp[:1]
    # Sometime 0 is interpreted as O/o (letter) or a (letter) when alone by OCR. Difficult to change that.
    # We start loop at 1 because we avoid user column that character
    for j in range(0,DataVideoDF.shape[1]):
        if DataVideoDF.iloc[i, j] in ("O", "o", "a", "oo", "Oo", "oO", "Q", "Oa", "aO","Oy","Oo,","0 1"):
            DataVideoDF.iloc[i, j] = 0
        if DataVideoDF.iloc[i, j] == "S7":
            DataVideoDF.iloc[i, j] = 57

# remove all non numeric character (except dot) from col that expect numeric only
for col in ['MIN','SEC'] + NamesPlayerGold + NamesPlayerLife + NamesPlayerSubBar + NamesPlayerKDA + NamesPlayerMinions +NamesPlayerWards  :
    #print(col)
    for i in range(0,DataVideoDF.shape[0]):
        #print(DataVideoDF.loc[i,col])
        # remove alpha caracter and convert to float
        tmp = re.sub('[^0-9.]','', str(DataVideoDF.loc[i,col]))
        if len(tmp) == 0 or tmp == "." :
            DataVideoDF.loc[i,col] = 'NaN'
        else:
            DataVideoDF.loc[i,col] = float(tmp)

# Now we need to remove extrem value that are just a pytesseract fail
# iterate on desired columns
F = 1.5
T = 30
for col in ['MIN','SEC'] + NamesPlayerGold  :
    #print(col)
    # Iterate on all row cell
    for i in range(0,DataVideoDF.shape[0]):
        #print(DataVideoDF.loc[i,col])
        # skip if value is already NA
        if DataVideoDF.loc[i,col] == 'NaN':
            #print("Skipped")
            continue
        # Compute mean
        if i < T :
            tmp_mean = DataVideoDF.loc[i:(i+T),col].median()
        else : 
            tmp_mean = DataVideoDF.loc[(i-T):(i),col].median()
        
        # Put NA if aberrant value, add 1 to avoid problem with first value at 0
        if abs(tmp_mean-DataVideoDF.loc[i,col]) > F*tmp_mean + 1 :
            DataVideoDF.loc[i,col] = 'NaN'

###############################################################################
# Save the file
###############################################################################

End_time = datetime.now()
End_time = End_time.strftime("%H-%M-%S")
tmp_path = "..\\Data\\Users\\"+User+"\\Output\\TSV\\Game_"+IdVideo+"_"+DateTime+"_"+End_time+"_"+str(totalFramecount)+".tsv"
DataVideoDF.to_csv(tmp_path, sep="\t", index = False)

# Check the DF
DataVideoDF
###############################################################################