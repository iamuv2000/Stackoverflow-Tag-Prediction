#Module imports
from flask import Flask
from flask import render_template, jsonify, request
from tagPredictor import getTags
from flask_cors import CORS

# Creates a Flask application, named app
app = Flask(__name__, static_folder='./client/build', static_url_path='/')
cors = CORS(app)


# Route to fetch frontend
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Route to get text summary
@app.route('/api/getRecommendedTags', methods=['POST'])
def api_all():
	question = []
	question.append(request.json['question'])
	print(question)
	tags = getTags(question)[0]
	return jsonify(tags)


# Run the application
if __name__ == "__main__":
	app.run(debug=True)