from flask import Flask, Response, render_template, request
from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import database
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
resp1_arr = []
resp2_arr = []
resp3_arr = []
resp4_arr = []
resp5_arr = []
results_arr = []

@app.route('/thankspage.html')
def thanks():
    url = request.url

    resp1_arr.append(url[url.index("question1=") + len("question1="):][1])
    resp2_arr.append(url[url.index("question2=") + len("question2="):][1])
    resp3_arr.append(url[url.index("question3=") + len("question3="):][1])
    resp4_arr.append(url[url.index("question4=") + len("question4="):][1])
    resp5_arr.append(url[url.index("question5=") + len("question5="):][1])
    # return resp1_arr[0]
    return render_template('thankspage.html')

@app.route('/results')
def process():
	avg = 0
	for resp in resp1_arr:
		avg = avg + int(resp)
	results_arr.append(float(avg) / len(resp1_arr))

	avg = 0
	for resp in resp2_arr:
		avg = avg + int(resp)
	results_arr.append(float(avg) / len(resp2_arr))

	avg = 0
	for resp in resp3_arr:
		avg = avg + int(resp)
	results_arr.append(float(avg) / len(resp3_arr))

	avg = 0
	for resp in resp4_arr:
		avg = avg + int(resp)
	results_arr.append(float(avg) / len(resp4_arr))

	avg = 0
	for resp in resp5_arr:
		avg = avg + int(resp)
	results_arr.append(float(avg) / len(resp5_arr))

	# a Python object (dict):
	x = {
	  "SurveyA": "I would come to Market Central more often if it was in full service (serving more food options) for longer each day.",
	  "Average ResultA": results_arr[0],
	  "SurveyB": "I go to Market Central less frequently because I don't like the food.",
	  "Average ResultB": results_arr[1],
	  "SurveyC": "Long wait times at 360 Degrees make me want to not get food there.",
	  "Average ResultC": results_arr[2],
	  "SurveyD": "I would go to Market Central more often if there were more Vegan/Vegetarian options.",
	  "Average ResultD": results_arr[3],
	  "SurveyE": "I find the food quality at Market Central to be inconsistent.",
	  "Average ResultE": results_arr[4],
	}

	# convert into JSON:
	y = json.dumps(x)

	# the result is a JSON string:
	return y

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)