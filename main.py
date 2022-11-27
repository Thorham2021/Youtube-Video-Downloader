from pytube import YouTube
import os
url=YouTube(str(input("Enter the url of the video: ")))
my_video=url
my_audio=url.streams.filter(only_audio=True).first()
print("Video Title: "+my_video.title)
my_video=my_video.streams.get_highest_resolution()
user_input=int(input("Type '1' to download only audio and '2' to download both audio and video as a single file: "))
destination=str(input("Enter full dir: "))
if user_input==2 :
    print("Downloading...")
    output_file=my_video.download(output_path=destination)
    base, ext=os.path.splitext(output_file)
    new_file=base+'.mp4'
    os.rename(output_file, new_file)
    print("DONE!!!\nFILE NAME: "+my_video.title+".mp4")
elif user_input==1 :
    print("Downloading...")
    output_file=my_audio.download(output_path=destination)
    base, ext=os.path.splitext(output_file)
    new_file=base+'.mp3'
    os.rename(output_file, new_file)
    print("DONE!!!\nFILE NAME: "+my_video.title+".mp3")
else :
    print("Process terminated!!!")
