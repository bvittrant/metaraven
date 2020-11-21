###############################################################################
# Main script for video analysis
###############################################################################

# Data output - Futur list of list of frames infos
DataVideo = []

for frameCount in range(frameCountStart,totalFramecount,FrameIncrement):
# Main loop in which DataVideo is populated, frame by frame
    print("Working on frame ", frameCount)
    # Loads the current frame
    vidcap.set(cv2.CAP_PROP_POS_FRAMES,frameCount)
    tmp,img = vidcap.read()
    # If image is none because anything
    if img is None:
        continue
    # On the first frame collect champions names (Can we do it on the last frame to avoid repeat if condition ?)
    # Maybe some probleme with dead champion at the end
    if frameCount == frameCountStart:
        ChampsNames = GetScoreBoardChampions(img,'..\\Data\\Images\\Champions\\ChampionSquareAssets\\',48,61)

    # Check the current game time and if we get back just skip the frame
    # Sometime with openCV this sheet happend.
    InfoTime = GetInfoReplayTime(img,ThresTime)
    
    # treat info on the frame and append it to a row then append the row to a list to create list of list
    # MiniMapInfo = GetInfoFromMiniMap(img)
    Row = [User, frameCount, InfoTime[0], InfoTime[1],GetRedGoldTotal(img,Thres100),GetBlueGoldTotal(img,Thres100), GetRedKill(img,Thres), GetBlueKill(img,Thres), GetRedTowerKill(img,Thres100), GetBlueTowerKill(img,Thres100)]
    Row = Row + GetPlayerLife(img, Thres) + GetPlayerSubLifeBar(img, Thres)
    Row = Row + GetScoreBoardGold(img,Thres) + GetScoreBoardKDA(img, Thres) + GetScoreBoardMinions(img, Thres) + GetScoreBoardWards(img, Thres)
    Row = Row + [ChampsNames[0],ChampsNames[2],ChampsNames[4],ChampsNames[6],ChampsNames[8],ChampsNames[1],ChampsNames[3],ChampsNames[5],ChampsNames[7],ChampsNames[9]]
    DataVideo.append(Row)

    # Comment if no need to optimize
    #if frameCount % MODULO == 0:
    #    PathToImg = "..\\Data\\Users\\"+User+"\\Images\\image"+str(f"{frameCount:06d}")+".jpg"
    #    cv2.imwrite(PathToImg, img)
    
    # Iteration
    frameCount = frameCount + FrameIncrement
    # To remove after final code
    if frameCount >= STOP:
        break

# Close video to avoid any problem and memory leak
vidcap.release()
cv2.destroyAllWindows()
# Remove new video format to keep storage
os.remove(PathToVideo+".avi")