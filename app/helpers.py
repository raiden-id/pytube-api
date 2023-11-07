from flask import jsonify
from pytube import YouTube
from pytube import Search as Cari

def Stream_video(data):
  yt = YouTube(data)
  #filter video only
  yt.streams.filter(file_extension='mp4')
  stream = yt.streams.get_by_itag(22)
  
  # filter audio only
  yt.streams.filter(only_audio=True) #yt.streams.filter(file_extension='mp4')
  audio = yt.streams.get_by_itag(251) #stream = yt.streams.get_by_itag(22)
  
  data_all = {
    'channel':yt.author, 
    'judul':yt.title, 
    'views':yt.views, 
    'stream':{
      "mp3":audio.url, 
      "mp4":stream.url, 
      }
  }
  return data_all
  
  
def Search_video(data):
  yt = Cari(data)
  return None
  