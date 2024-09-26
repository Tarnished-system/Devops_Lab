from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt=YouTube(url)
        streams=yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream=streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!\nNice work, my G")
    except Exception as e:
        print(e)   
url="https://youtu.be/snxa63taOHc?si=PTzS3uYPMpQDWPq3"
save_path="C:\Users\krish\Downloads"

download_video(url,save_path)