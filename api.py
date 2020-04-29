import flask
import csv
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

LINEUP = []

with open('static/EDC_Lineups_2019.csv', newline="") as csvfile:
    reader = csv.reader(csvfile)




@app.route('/', methods=['GET'])
def home():
    return "<h1>Info App</h1><p>This site is for the info EDC API</p>"

@app.route('/api/v1/resources/artists/all', methods=['GET'])
def api_all():
    return jsonify(LINEUP)

@app.route('/api/v1/resources/artists', methods=['GET'])
def api_id():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for artist in LINEUP:
        results.append(artist)


    return jsonify(results);

if __name__ == '__name__':
    app.run()