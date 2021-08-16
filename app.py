import flask
from flask import render_template

import data


app = flask.Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/departures/<departure>')
def departure(departure):
    return render_template('departure.html')


@app.route('/tours/<id>')
def tour(id):
    return render_template('tour.html')


@app.route('/data/')
def all_tours():
    return render_template('tours.html', tours=data.tours)


@app.route('/data/departures/<departure>')
def tours_on_departure(departure):
    tours_on_departure = {}

    for tour in data.tours:
        print(data.tours[tour])
        if data.tours[tour]['departure'] == departure:
            tours_on_departure[tour] = data.tours[tour]

    return render_template('tours_on_departure.html', tours_on_departure=tours_on_departure, departure=data.departures[departure])


@app.route('/data/tours/<int:id>')
def tour_desc(id):
    return render_template('tour_desc.html', tour=data.tours[id])


if __name__ == '__main__':
    app.run()
