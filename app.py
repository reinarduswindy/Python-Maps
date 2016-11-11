#!flask/bin/python
import json
from flask import Flask
from flask import Response
import handler

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/get_direction/<string:origin>/<string:destination>/', defaults={'mode' : None})
@app.route('/get_direction/<string:origin>/<string:destination>/<string:mode>', methods=['GET'])
def get_direction(origin, destination, mode):
	res = handler.GetDirection(origin, destination, mode)
	if len(res) == 0:
		abort(404)
	return Response(json.dumps(res),  mimetype='application/json')

@app.route('/test/<string:name>', methods=['GET'])
def test(name):
	res = handler.Test(name)
	if len(res) == 0:
		abort(404)
	return Response(json.dumps(res), mimetype='application/json')

@app.route('/test_get/<string:origin>/<string:destination>/<string:angle>', methods=['GET'])
def get_step(origin, destination, angle):
	res = handler.GetStep(origin, destination, angle)
	if len(res) == 0:
		abort(404)
	return Response(json.dumps(res), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)