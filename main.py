#Module imports
from flask import Flask
from flask import render_template, jsonify, request
from tagPredictor import getTags
from flask_cors import CORS

# Creates a Flask application, named app
app = Flask(__name__)
cors = CORS(app)

# Route to get text summary
@app.route('/api/getRecommendedTags', methods=['POST'])
def api_all():
	question = request.json['question']
	getTags(question)
	print(question)
	return jsonify(question)


# Run the application
if __name__ == "__main__":
	app.run(debug=True)