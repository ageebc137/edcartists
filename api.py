import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

artists = [
    {'name': 'Martin Garrix'},
    {'name': 'Jonas Blue'},
    {'name': 'Diplo'}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Info App</h1><p>This site is for the info EDC API</p>"

@app.route('/api/v1/resources/artists/all', methods=['GET'])
def api_all():
    return jsonify(artists)

@app.route('/api/v1/resources/artists', methods=['GET'])
def api_id():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)


    return jsonify(results);

app.run()