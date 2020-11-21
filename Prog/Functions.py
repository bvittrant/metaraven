###############################################################################
###############################################################################
# Functions : Benjamin Vittrant & Pierre Boileau
###############################################################################
print("Importing your functions")
print("###")
###############################################################################
# OpenCV function
# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def get_RGB_images(image):
    b = image.copy()
    # set green and red channels to 0
    b[:, :, 1] = 0
    b[:, :, 2] = 0
    g = image.copy()
    # set blue and red channels to 0
    g[:, :, 0] = 0
    g[:, :, 2] = 0
    r = image.copy()
    # set blue and green channels to 0
    r[:, :, 0] = 0
    r[:, :, 1] = 0
    return(r,g,b)

###############################################################################
# Converting video fromat function
def convert(inputted_file):
    video_name = inputted_file+".avi"
    #ff = ffmpy.FFmpeg(inputs={inputted_file :None }, outputs={video_name: '-c:v libx264 -crf 19 -c:a aac -b:a 192k -ac 2'})
    ff = ffmpy.FFmpeg(inputs={inputted_file :None }, outputs={video_name: '-q:v 0 -preset ultrafast'})
    ff.cmd
    ff.run()
    return video_name

###############################################################################
# TOP CENTER PART OF THE REPLAY
###############################################################################

# Get time info on frame
def GetInfoReplayTimeUxScale1(img,Thres):
    y1 = int(75)
    y2 = int(100)
    x1 = int(930)
    x2 = int(1000)
    TmpImg = img[y1:y2,x1:x2]
    TmpImg = get_grayscale(TmpImg)
    TmpImg = 1 - TmpImg
    ret,TmpImg = cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY)
    #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
    #plt.show()
    Tmp = pytesseract.image_to_string(TmpImg)
    if ":" not in Tmp:
        return "NaN", "NaN"
    Tmp = str(Tmp.encode("unicode_escape")).split(":")
    user_min = Tmp[0].split("'")[1]
    user_sec = Tmp[1][0] + Tmp[1][1]

    return user_min,user_sec
def GetInfoReplayTime(img,Thres):
    y1 = int(105)
    y2 = int(140)
    x1 = int(920)
    x2 = int(1015)
    TmpImg = img[y1:y2,x1:x2]
    TmpImg = get_grayscale(TmpImg)
    TmpImg = 1 - TmpImg
    ret,TmpImg = cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY)
    #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
    #plt.show()
    Tmp = pytesseract.image_to_string(TmpImg)
    if ":" not in Tmp:
        return "NaN", "NaN"
    Tmp = str(Tmp.encode("unicode_escape")).split(":")
    user_min = Tmp[0].split("'")[1]
    user_sec = Tmp[1][0] + Tmp[1][1]

    return user_min,user_sec

# get total red kills on fram
def GetRedKillUxScale1(img,Thres):
    y1 = int(20)
    y2 = int(50)
    x1 = int(980)
    x2 = int(1035)
    TmpImg = img[y1:y2,x1:x2]
    TmpImg = get_grayscale(TmpImg)
    ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
    Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
    Tmp = str(Tmp.encode("unicode_escape")).split("\\")
    Tmp = Tmp[0].split("'")[1]
    return Tmp
def GetRedKill(img,Thres):
    y1 = int(25)
    y2 = int(80)
    x1 = int(985)
    x2 = int(1050)
    TmpImg = img[y1:y2,x1:x2]
    #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
    #plt.show()
    TmpImg = get_grayscale(TmpImg)
    ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
    Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
    Tmp = str(Tmp.encode("unicode_escape")).split("\\")
    Tmp = Tmp[0].split("'")[1]
    return Tmp

# get total red kills on fram
def GetBlueKillUxScale1(img,Thres):
    y1 = int(20)
    y2 = int(50)
    x1 = int(895)
    x2 = int(950)
    TmpImg = img[y1:y2,x1:x2]
    TmpImg = get_grayscale(TmpImg)
    ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
    Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
    Tmp = str(Tmp.encode("unicode_escape")).split("\\")
    Tmp = Tmp[0].split("'")[1]
    return Tmp
def GetBlueKill(img,Thres):
    y1 = int(20)
    y2 = int(80)
    x1 = int(894)
    x2 = int(952)
    TmpImg = img[y1:y2,x1:x2]
    TmpImg = get_grayscale(TmpImg)
    ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
    Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
    Tmp = str(Tmp.encode("unicode_escape")).split("\\")
    Tmp = Tmp[0].split("'")[1]
    return Tmp

# Get total red gold
def GetRedGoldTotalUxScale1(img,Thres):
    y1 = int(15)
    y2 = int(45)
    x1 = int(1140)
    x2 = int(1190)
    TmpImg = img[y1:y2,x1:x2]
    TmpImg = get_grayscale(TmpImg)
    ret,TmpImg = cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
    Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
    Tmp = Tmp.split('k')[0]
    return Tmp
def GetRedGoldTotal(img,Thres):
    y1 = int(15)
    y2 = int(60)
    x1 = int(1215)
    x2 = int(1300)
    TmpImg = img[y1:y2,x1:x2]
    TmpImg = get_grayscale(TmpImg)
    ret,TmpImg = cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
    Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
    Tmp = Tmp.split('k')[0]
    return Tmp

# Get total blue gold
def GetBlueGoldTotalUxScale1(img,Thres):
    y1 = int(15)
    y2 = int(45)
    x1 = int(757)
    x2 = int(810)
    TmpImg = img[y1:y2,x1:x2]
    TmpImg = get_grayscale(TmpImg)
    ret,TmpImg = cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
    Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
    Tmp = Tmp.split('k')[0]
    return Tmp
def GetBlueGoldTotal(img,Thres):
    y1 = int(15)
    y2 = int(60)
    x1 = int(673)
    x2 = int(755)
    TmpImg = img[y1:y2,x1:x2]
    TmpImg = get_grayscale(TmpImg)
    ret,TmpImg = cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
    Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
    Tmp = Tmp.split('k')[0]
    return Tmp

# Get Red Tower Kill
def GetRedTowerKillUxScale1(img,Thres):
    y1 = int(15)
    y2 = int(45)
    x1 = int(1260)
    x2 = int(1290)
    TmpImg = img[y1:y2,x1:x2]
    TmpImg = get_grayscale(TmpImg)
    ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
    Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
    Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
    return Tmp
def GetRedTowerKill(img,Thres):
    y1 = int(15)
    y2 = int(60)
    x1 = int(1385)
    x2 = int(1450)
    TmpImg = img[y1:y2,x1:x2]
    TmpImg = get_grayscale(TmpImg)
    ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
    Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
    Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
    return Tmp

# Get Blue Tower Kill
def GetBlueTowerKillUxScale1(img,Thres):
    y1 = int(15)
    y2 = int(45)
    x1 = int(670)
    x2 = int(700)
    TmpImg = img[y1:y2,x1:x2]
    TmpImg = get_grayscale(TmpImg)
    ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
    Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
    Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
    return Tmp
def GetBlueTowerKill(img,Thres):
    y1 = int(15)
    y2 = int(60)
    x1 = int(548)
    x2 = int(625)
    TmpImg = img[y1:y2,x1:x2]
    TmpImg = get_grayscale(TmpImg)
    ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
    Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
    Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
    return Tmp

###############################################################################
# LEFT AND RIGHT PART OF THE REPLAY
###############################################################################

### Life for all players
def GetPlayerLifeUxScale1(img, Thres):

    # 
    ## Team 1
    x1T1 = int(32)
    x2T1 = int(72)
    ## Team 2
    x1T2 = int(1848)
    x2T2 = int(1888)

    # Starting y
    y1 = 208
    # There is 103 pixel between player's Life bar
    # And we take only 1 pixel bar.

    PlayerLifeListT1 = []
    PlayerLifeListT2 = []
   
    for i in range(1,6):
        y2 = y1 + 1
        # Team 1
        TmpImg = img[y1:y2,x1T1:x2T1]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg = cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY)
        if cv2.countNonZero(TmpImg) == 0:
            PlayerLifeListT1.append(0)
        else:
            PlayerLifeListT1.append(round(cv2.countNonZero(TmpImg)/TmpImg.shape[1],3))
        # Team 2
        TmpImg = img[y1:y2,x1T2:x2T2]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY)
        if cv2.countNonZero(TmpImg) == 0:
            PlayerLifeListT2.append(0)
        else:
            PlayerLifeListT2.append(round(cv2.countNonZero(TmpImg)/TmpImg.shape[1],3))
        y1 = y1 + 103
    # End function
    return PlayerLifeListT1 + PlayerLifeListT2
def GetPlayerLife(img, Thres):

    ## Team 1
    x1T1 = int(44)
    x2T1 = int(101)
    ## Team 2
    x1T2 = int(1818)
    x2T2 = int(1875)

    # Starting y
    y1 = 292

    PlayerLifeListT1 = []
    PlayerLifeListT2 = []
   
    for i in range(1,6):
        y2 = y1 + 4
        # Team 1
        TmpImg = img[y1:y2,x1T1:x2T1]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY)
        if cv2.countNonZero(TmpImg) == 0:
            PlayerLifeListT1.append(0)
        else:
            PlayerLifeListT1.append(round(cv2.countNonZero(TmpImg)/(TmpImg.shape[1]*TmpImg.shape[0]),3))
        # Team 2
        TmpImg = img[y1:y2,x1T2:x2T2]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY)
        if cv2.countNonZero(TmpImg) == 0:
            PlayerLifeListT2.append(0)
        else:
            PlayerLifeListT2.append(round(cv2.countNonZero(TmpImg)/(TmpImg.shape[1]*TmpImg.shape[0]),3))
        y1 = y1 + 145
    # End function
    return PlayerLifeListT1 + PlayerLifeListT2

### Sub bar life (mana, energy etc)
def GetPlayerSubLifeBarUxScale1(img, Thres):

    ## Team 1
    x1T1 = int(32)
    x2T1 = int(72)
    ## Team 2
    x1T2 = int(1848)
    x2T2 = int(1888)

    # Starting y
    y1 = 217
    # There is 103 pixel between player's Life bar
    # And we take only 1 pixel bar.

    PlayerListT1 = []
    PlayerListT2 = []
   
    for i in range(1,6):
        y2 = y1 + 1
        # Team 1
        TmpImg = img[y1:y2,x1T1:x2T1]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY)
        #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
        #plt.show()
        if cv2.countNonZero(TmpImg) == 0:
            PlayerListT1.append(0)
        else:
            PlayerListT1.append(round(cv2.countNonZero(TmpImg)/TmpImg.shape[1],3))
        # Team 2
        TmpImg = img[y1:y2,x1T2:x2T2]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY)
        if cv2.countNonZero(TmpImg) == 0:
            PlayerListT2.append(0)
        else:
            PlayerListT2.append(round(cv2.countNonZero(TmpImg)/TmpImg.shape[1],3))
        y1 = y1 + 103
    # End function
    return PlayerListT1 + PlayerListT2
def GetPlayerSubLifeBar(img, Thres):

    ## Team 1
    x1T1 = int(44)
    x2T1 = int(101)
    ## Team 2
    x1T2 = int(1818)
    x2T2 = int(1875)

    # Starting y
    y1 = 304
    # There is 103 pixel between player's Life bar
    # And we take only 1 pixel bar.

    PlayerListT1 = []
    PlayerListT2 = []
   
    for i in range(1,6):
        y2 = y1 + 1
        # Team 1
        TmpImg = img[y1:y2,x1T1:x2T1]
        #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
        #plt.show()
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY)
        if cv2.countNonZero(TmpImg) == 0:
            PlayerListT1.append(0)
        else:
            PlayerListT1.append(round(cv2.countNonZero(TmpImg)/TmpImg.shape[1],3))
        # Team 2
        TmpImg = img[y1:y2,x1T2:x2T2]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY)
        if cv2.countNonZero(TmpImg) == 0:
            PlayerListT2.append(0)
        else:
            PlayerListT2.append(round(cv2.countNonZero(TmpImg)/TmpImg.shape[1],3))
        y1 = y1 + 145
    # End function
    return PlayerListT1 + PlayerListT2

###############################################################################
# SCOREBOARD
###############################################################################

### ScoreBoard gold
def GetScoreBoardGoldUxScale1(img, Thres):

    ## Team 1
    x1T1 = int(640)
    x2T1 = int(790)
    ## Team 2
    x1T2 = int(1140)
    x2T2 = int(1300)

    # Starting y
    y1 = 860
    # There is 103 pixel between player's Life bar
    # And we take only 1 pixel bar.

    PlayerListT1 = []
    PlayerListT2 = []
   
    for i in range(1,6):
        y2 = y1 + 30
        # Team 1
        TmpImg = img[y1:y2,x1T1:x2T1]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        Tmp = Tmp.split(")")[0].split("(")
        if len(Tmp) == 2:
            PlayerListT1.append(Tmp[0])
            PlayerListT1.append(Tmp[1])
        else:
            PlayerListT1.append("NA")
            PlayerListT1.append("NA")
        # Team 2
        TmpImg = img[y1:y2,x1T2:x2T2]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
        #plt.show()
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        Tmp = Tmp.split(")")[0].split("(")
        if len(Tmp) == 2:
            PlayerListT2.append(Tmp[0])
            PlayerListT2.append(Tmp[1])
        else:
            PlayerListT2.append("NA")
            PlayerListT2.append("NA")

        y1 = y1 + 45
    # End function
    return PlayerListT1 + PlayerListT2
def GetScoreBoardGold(img, Thres):

    Thres = Thres # 50
    ## Team 1
    x1T1 = int(500)
    x2T1 = int(750)
    ## Team 2
    x1T2 = int(1250)
    x2T2 = int(1400)

    # Starting y
    y1 = 765
    # There is 103 pixel between player's Life bar
    # And we take only 1 pixel bar.

    PlayerGoldListT1 = []
    PlayerGoldListT2 = []
   
    for i in range(1,6):
        y2 = y1 + 55
        # Team 1
        TmpImg = img[y1:y2,x1T1:x2T1]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg = cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        Tmp = Tmp.split(")")[0].split("(")
        if len(Tmp) == 2:
            PlayerGoldListT1.append(Tmp[0])
            PlayerGoldListT1.append(Tmp[1])
        else:
            PlayerGoldListT1.append("NaN")
            PlayerGoldListT1.append("NaN")
        # Team 2
        TmpImg = img[y1:y2,x1T2:x2T2]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
        #plt.show()
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        Tmp = Tmp.split(")")[0].split("(")
        if len(Tmp) == 2:
            PlayerGoldListT2.append(Tmp[0])
            PlayerGoldListT2.append(Tmp[1])
        else:
            PlayerGoldListT2.append("NA")
            PlayerGoldListT2.append("NA")

        y1 = y1 + 60
    # End function
    return PlayerGoldListT1 + PlayerGoldListT2

### ScoreBoard KDA
def GetScoreBoardKDAUxScale1(img, Thres):
    ## Team 1
    x1T1 = int(790)
    x2T1 = int(870)
    ## Team 2
    x1T2 = int(1060)
    x2T2 = int(1140)

    # Starting y
    y1 = 867
    # There is 103 pixel between player's Life bar
    # And we take only 1 pixel bar.

    PlayerListT1 = []
    PlayerListT2 = []
   
    for i in range(1,6):
        y2 = y1 + 17
        # Team 1
        TmpImg = img[y1:y2,x1T1:x2T1]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg = cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
        #plt.show()
        Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
        Tmp = Tmp.split('/')
        if len(Tmp) == 3:
            PlayerListT1.append(Tmp[0])
            PlayerListT1.append(Tmp[1])
            PlayerListT1.append(Tmp[2])
        else:
            PlayerListT1.append("NaN")
            PlayerListT1.append("NaN")
            PlayerListT1.append("NaN")
        # Team 2
        TmpImg = img[y1:y2,x1T2:x2T2]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
        #plt.show()
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
        Tmp = Tmp.split('/')
        if len(Tmp) == 3:
            PlayerListT2.append(Tmp[0])
            PlayerListT2.append(Tmp[1])
            PlayerListT2.append(Tmp[2])
        else:
            PlayerListT2.append("NA")
            PlayerListT2.append("NA")
            PlayerListT1.append("NA")

        y1 = y1 + 44
    # End function
    return PlayerListT1 + PlayerListT2
def GetScoreBoardKDA(img, Thres):

    ## Team 1
    x1T1 = int(700)
    x2T1 = int(850)
    ## Team 2
    x1T2 = int(1085)
    x2T2 = int(1250)

    # Starting y
    y1 = 783
    # There is 103 pixel between player's Life bar
    # And we take only 1 pixel bar.

    PlayerListT1 = []
    PlayerListT2 = []
   
    for i in range(1,6):
        y2 = y1 + 25
        # Team 1
        TmpImg = img[y1:y2,x1T1:x2T1]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg = cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
        #plt.show()
        #print(Tmp)
        Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
        Tmp = Tmp.split('/')
        #print(Tmp)
        if len(Tmp) == 3:
            PlayerListT1.append(Tmp[0])
            PlayerListT1.append(Tmp[1])
            PlayerListT1.append(Tmp[2])
        else:
            PlayerListT1.append("NaN")
            PlayerListT1.append("NaN")
            PlayerListT1.append("NaN")
        # Team 2
        TmpImg = img[y1:y2,x1T2:x2T2]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
        #plt.show()
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
        Tmp = Tmp.split('/')
        if len(Tmp) == 3:
            PlayerListT2.append(Tmp[0])
            PlayerListT2.append(Tmp[1])
            PlayerListT2.append(Tmp[2])
        else:
            PlayerListT2.append("NA")
            PlayerListT2.append("NA")
            PlayerListT1.append("NA")

        y1 = y1 + 61
    # End function
    return PlayerListT1 + PlayerListT2

### Scoreboard Minions
def GetScoreBoardMinionsUxScale1(img, Thres):
    ## Team 1
    x1T1 = int(870)
    x2T1 = int(916)
    ## Team 2
    x1T2 = int(1014)
    x2T2 = int(1060)

    # Starting y
    y1 = 860
    # There is 103 pixel between player's Life bar
    # And we take only 1 pixel bar.

    PlayerListT1 = []
    PlayerListT2 = []
   
    for i in range(1,6):
        y2 = y1 + 30
        # Team 1
        TmpImg = img[y1:y2,x1T1:x2T1]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg = cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
        #plt.show()
        Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
        PlayerListT1.append(Tmp)
        # Team 2
        TmpImg = img[y1:y2,x1T2:x2T2]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
        #plt.show()
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
        PlayerListT2.append(Tmp)

        y1 = y1 + 45
    # End function
    return PlayerListT1 + PlayerListT2
def GetScoreBoardMinions(img, Thres):

    Thres = Thres # 50
    ## Team 1
    x1T1 = int(830)
    x2T1 = int(900)
    ## Team 2
    x1T2 = int(1040)
    x2T2 = int(1110)

    # Starting y
    y1 = 765
    # There is 103 pixel between player's Life bar
    # And we take only 1 pixel bar.

    PlayerListT1 = []
    PlayerListT2 = []
   
    for i in range(1,6):
        y2 = y1 + 55
        # Team 1
        TmpImg = img[y1:y2,x1T1:x2T1]
        #TmpImg = get_grayscale(TmpImg)
        ret,TmpImg = cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
        #plt.show()
        Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
        PlayerListT1.append(Tmp)
        # Team 2
        TmpImg = img[y1:y2,x1T2:x2T2]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
        #plt.show()
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
        PlayerListT2.append(Tmp)

        y1 = y1 + 60
    # End function
    return PlayerListT1 + PlayerListT2

### ScoreBoard Wards
def GetScoreBoardWardsUxScale1(img, Thres):

    ## Team 1
    x1T1 = int(610)
    x2T1 = int(640)
    ## Team 2
    x1T2 = int(1290)
    x2T2 = int(1324)

    # Starting y
    y1 = 873
    # There is 103 pixel between player's Life bar
    # And we take only 1 pixel bar.

    PlayerListT1 = []
    PlayerListT2 = []
   
    for i in range(1,6):
        y2 = y1 + 20
        # Team 1
        TmpImg = img[y1:y2,x1T1:x2T1]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
        PlayerListT1.append(Tmp)
        # Team 2
        TmpImg = img[y1:y2,x1T2:x2T2]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
        #plt.show()
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
        PlayerListT2.append(Tmp)

        y1 = y1 + 45
    # End function
    return PlayerListT1 + PlayerListT2
def GetScoreBoardWards(img, Thres):

    ## Team 1
    x1T1 = int(474)
    x2T1 = int(509)
    ## Team 2
    x1T2 = int(1400)
    x2T2 = int(1470)

    # Starting y
    y1 = 783
    # There is 103 pixel between player's Life bar
    # And we take only 1 pixel bar.

    PlayerListT1 = []
    PlayerListT2 = []
   
    for i in range(1,6):
        y2 = y1 + 55
        # Team 1
        TmpImg = img[y1:y2,x1T1:x2T1]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
        PlayerListT1.append(Tmp)
        # Team 2
        TmpImg = img[y1:y2,x1T2:x2T2]
        TmpImg = get_grayscale(TmpImg)
        ret,TmpImg= cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY_INV)
        #plt.imshow(cv2.cvtColor(TmpImg, cv2.COLOR_RGB2BGR))
        #plt.show()
        Tmp = pytesseract.image_to_string(TmpImg, lang='eng', config='--psm 7')
        Tmp = str(Tmp.encode("unicode_escape")).split("\\")[0].split('\'')[1]
        PlayerListT2.append(Tmp)

        y1 = y1 + 58
    # End function
    return PlayerListT1 + PlayerListT2

### Scoreboard champ icons
# On 1080 by 1920:
# IconsScoreboardSize = 36
# RowInterval = 44
def GetScoreBoardChampionsUxScale1(img, PathToRiotIcons, IconsScoreboardSize, RowInterval):

    Data = []
    Names = []
    x1T1 = 923
    x2T1 = 959
    x1T2 = 975
    x2T2 = 1011
    DIR = PathToRiotIcons
    # Collect champ name
    for FILE in os.listdir(DIR):
            if FILE.endswith(".ini"):
                continue
            Names.append(FILE.split(".")[0])

    # Defining the position of the starting row
    y1 = 860
    for j in range(1,6):
        y2 = y1 + IconsScoreboardSize
        img1 = img[y1:y2,x1T1:x2T1]
        img2 = img[y1:y2,x1T2:x2T2]
        #plt.imshow(cv2.cvtColor(img1, cv2.COLOR_RGB2BGR))
        #plt.show()
        #plt.imshow(cv2.cvtColor(img2, cv2.COLOR_RGB2BGR))
        #plt.show()
        row1 = []
        row2 = []
        for FILE in os.listdir(DIR):
            if FILE.endswith(".ini"):
                continue
            img3 = cv2.imread(DIR+FILE)
            # Comparaison on the team1 champ
            # Initiate SIFT detector
            sift = cv2.SIFT_create()
            FLANN_INDEX_KDTREE = 1
            index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 10)
            search_params = dict(checks = 50)
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            # find the keypoints and descriptors with SIFT
            kp1, des1 = sift.detectAndCompute(img3,None)
            kp2, des2 = sift.detectAndCompute(img1,None)
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(des1, des2, k=2)
            Dist = 0.6
            # Store all the good matches as per Lowe's ratio test.
            good = []
            for m,n in matches:
                if m.distance < Dist*n.distance:
                    good.append(m)
            row1.append(len(good))
            # Comparaison on the team1 champ
            # Initiate SIFT detector
            sift = cv2.SIFT_create()
            kp1, des1 = sift.detectAndCompute(img3,None)
            kp2, des2 = sift.detectAndCompute(img2,None)
            matches = flann.knnMatch(des1, des2, k=2)
            # store all the good matches as per Lowe's ratio test.
            good = []
            for m,n in matches:
                if m.distance < Dist*n.distance:
                    good.append(m)
            row2.append(len(good))

            #print(len(good))
        Data.append(row1)
        Data.append(row2)
        # Go on the next row of the scoreboard
        y1 = y1 + RowInterval

    Data = pd.DataFrame(Data)
    Data.columns = Names
    return(Data.idxmax(axis=1))
def GetScoreBoardChampions(img, PathToRiotIcons, IconsScoreboardSize, RowInterval):

    Data = []
    Names = []
    x1T1 = 910
    x2T1 = 956
    x1T2 = 982
    x2T2 = 1030
    DIR = PathToRiotIcons
    # Collect champ name
    for FILE in os.listdir(DIR):
            if FILE.endswith(".ini"):
                continue
            Names.append(FILE.split(".")[0])

    # Defining the position of the starting row
    y1 = 772
    for j in range(1,6):
        y2 = y1 + IconsScoreboardSize
        img1 = img[y1:y2,x1T1:x2T1]
        img2 = img[y1:y2,x1T2:x2T2]
        #plt.imshow(cv2.cvtColor(img1, cv2.COLOR_RGB2BGR))
        #plt.show()
        #plt.imshow(cv2.cvtColor(img2, cv2.COLOR_RGB2BGR))
        #plt.show()
        row1 = []
        row2 = []
        for FILE in os.listdir(DIR):
            if FILE.endswith(".ini"):
                continue
            img3 = cv2.imread(DIR+FILE)
            # Comparaison on the team1 champ
            # Initiate SIFT detector
            sift = cv2.SIFT_create()
            FLANN_INDEX_KDTREE = 1
            index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 10)
            search_params = dict(checks = 50)
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            # find the keypoints and descriptors with SIFT
            kp1, des1 = sift.detectAndCompute(img3,None)
            kp2, des2 = sift.detectAndCompute(img1,None)
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(des1, des2, k=2)
            Dist = 0.6
            # Store all the good matches as per Lowe's ratio test.
            good = []
            for m,n in matches:
                if m.distance < Dist*n.distance:
                    good.append(m)
            row1.append(len(good))
            # Comparaison on the team1 champ
            # Initiate SIFT detector
            sift = cv2.SIFT_create()
            kp1, des1 = sift.detectAndCompute(img3,None)
            kp2, des2 = sift.detectAndCompute(img2,None)
            matches = flann.knnMatch(des1, des2, k=2)
            # store all the good matches as per Lowe's ratio test.
            good = []
            for m,n in matches:
                if m.distance < Dist*n.distance:
                    good.append(m)
            row2.append(len(good))

            #print(len(good))
        Data.append(row1)
        Data.append(row2)
        # Go on the next row of the scoreboard
        y1 = y1 + RowInterval

    Data = pd.DataFrame(Data)
    Data.columns = Names
    return(Data.idxmax(axis=1))

###############################################################################
# END Functions import
###############################################################################