###############################################################################

# Main Video analysis program
# Benjamin Vittrant & Pierre Boileau for metaraven
# 10/2020

###############################################################################

# Import libraries
exec(open('Scripts/Prog/Modules.py').read())

###############################################################################
# Functions
###############################################################################

# Import a bunch of useful function
exec(open('Scripts/Prog/Functions.py').read())

###############################################################################
# Main features (Need to be arg passed at a moment)
###############################################################################

current_date = date.today()
current_date = current_date.strftime("%d-%m-%Y")
current_time = datetime.now()
current_time = current_time.strftime("%H-%M-%S")
DateTime = current_date+"_"+current_time

# User = "Pierre"
User = "Tryptobob"
# Path to video
PathToVideo = '..\\Data\\Users\\'+User+'\\Videos\\10-22_EUW1-4905012650_01.webm'
# Id for the file
IdVideo = PathToVideo.split("\\")[len(PathToVideo.split("\\"))-1].split(".")[0]

# Loads video replay
print("Start converting webm video to another format")
vidcap = cv2.VideoCapture(convert(PathToVideo))
print("End conversion webm video to another format")
print("###")

# Threshold for the function
Thres = 50 # cv2.threshold(TmpImg,Thres,255,cv2.THRESH_BINARY)
Thres100 = 100 
ThresTime = 140 # Need to be different than the others functions

# Saves video framecount and FPS
totalFramecount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
totalFramecount
fps = int(vidcap.get(cv2.CAP_PROP_FPS))
print("Your video has ",totalFramecount, "frames and is initially runing at ",fps," FPS")
print("###")

# Initialization of time and frameCount
frameCountStart = 5
FrameIncrement = 4
STOP = totalFramecount
#MODULO = 10 # Go in the video recognition script to set frame writting and save to picture

###############################################################################
# Main part : Video analysis frame by frame
###############################################################################

# Import video analysis part
exec(open('Scripts/Prog/Metanalytics_video_recognition_replay.py').read())

###############################################################################
# Data Processing
###############################################################################

# Data processing part
exec(open('Scripts/Prog/Metanalytics_Data_processing.py').read())

###############################################################################
# END
###############################################################################