from flask import Flask, request
import requests
import json
app = Flask(__name__)

# ------------Route to index page
@app.route('/', methods = ['POST', 'GET'])
def index():
	stri = request.args['digits'][1]
	a = senti_for_digit(stri)
	if a!= '':
		#-------------Storing the elastic search
		url = "http://a00439258e0e04a2d4cc8018c794738d.us-east-1.aws.found.io:9200/ind/typ/"
		dat = {}
		dat['emotion'] = a
		payload = json.dumps(dat)
		#payload = '{"emotion" : '+a+'}'
		headers = {'Content-Type':'application/json'}
		requests.post(url, data=payload, headers=headers)
			#curl -XPOST http://a00439258e0e04a2d4cc8018c794738d.us-east-1.aws.found.io:9200/ind/typ/ -d '{"emotion" :' + a +'}'
	else:
		return None
	return 'Done'
#_---------------Function to map each user input to respective emotions and pass it on to server	
def senti_for_digit(digit):
	if digit == "1":
		return "happy"
	elif digit == "2":
		return "sad"
	elif digit == "3":
		return "angry"
	else:
		return False

if __name__ == "__main__":
	app.run(debug=True)

