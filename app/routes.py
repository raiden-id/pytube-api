from app import app
from app.controllers import video_id,search_data

@app.route('/')
def home():
        return "hai, konan is here!"

@app.route('/api/video_id/<string:data>')
def get_data_from_id(data):
    return video_id(data)

@app.route('/api/search/<string:query>')
def get_data_search(query):
	return search_data(query)

