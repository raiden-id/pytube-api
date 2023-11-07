
from flask import jsonify
from app.helpers import Search_video, Stream_video
from app import app

import json
baseurl = app.config['YT_URL']

def search_data(q):
  basedata = baseurl + q
  #return jsonify({'author':'Konan','results':jsx})

def video_id(data):
  basedata = baseurl + data
  
  results = Stream_video(basedata)
  return jsonify({'author':'Konan','results':results})
  
  
   # else: return jsonify({'author':'konan','status':False})

