import os
import logging

#############
# Functions #
#############

def video_checker(): # using a function because testing lool
    logging.info("Function video_checker running")
    if os.path.isfile("./video"):
        logging.info("Video file found")
        return True
    else:
        logging.info("Video file not found")
        return False

def download():
    logging.info("download function running")
    logging.warning("If install.sh was not run then the installer will crash")
    os.system("yt-dlp -o video https://www.youtube.com/watch?v=FtutLA63Cp8") #Using yt-dlp to download Bad-Apple video
    logging.info("Download finished")
    
    


logging.info("framer.py has started running")
logging.info("Displaying welcome messege")
print("Welcome to the Bad-Apple installer!")
logging.info("Displayed welcome messege")
logging.info("Checking if video exists")
if video_checker():
    logging.info("All clear")
else:
    logging.warning("Video not found! Downloading...")
    print("Video not found! Downloading!")
    download()
logging.info("Running ffmpeg command!")
os.system("ffmpeg -i video -vf fps=15 img/output%06d.png")
logging.info("Frames created! Exiting!")
