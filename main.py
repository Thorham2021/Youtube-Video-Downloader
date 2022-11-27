from pytube import YouTube
import os
import shutil
url=input("Enter the url of the video: ")
my_video=YouTube(url)
print("Video Title: "+my_video.title)
my_video = my_video.streams.get_highest_resolution()
user_input=input("Do you want to continue (Y/N): ")
if user_input=="Y" or user_input=="y" :
    print("Downloading...")
    my_video.download()
    print("DONE!!!\nFILE DETAILS ↓")
    print("File is located in the dir: "+os.getcwd()+"\\")
    print("File name: "+my_video.title)
else :
    print("Process terminated!!!")
