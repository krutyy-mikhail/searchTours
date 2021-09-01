import flask
from flask import render_template

from db import db

app = flask.Flask(__name__)


@app.route('/')
def index_view():
    all_tours = db.get_all_tours()
    return render_template('index.html', tours=all_tours)


@app.route('/departures/<departure>')
def departure_view(departure):
    tours_on_departure = db.get_tours_on_departure(departure)
    try:
        departure_desc = db.get_departure_desc(departure)
    except KeyError:
        flask.abort(404)
    try:
        min_price_tour = db.get_min_price_tour(tours_on_departure)
        max_price_tour = db.get_max_price_tour(tours_on_departure)
        min_night_tour = db.get_min_night_tour(tours_on_departure)
        max_night_tour = db.get_max_night_tour(tours_on_departure)
    except ValueError:
        flask.abort(404)

    return render_template('departure.html',
                           tours_on_departure=tours_on_departure,
                           departure=departure,
                           departure_desc=departure_desc,
                           min_price_tour=min_price_tour,
                           max_price_tour=max_price_tour,
                           min_night_tour=min_night_tour,
                           max_night_tour=max_night_tour,
                           )


@app.route('/tours/<int:tour_id>/')
def tour_view(tour_id):
    try:
        tour = db.get_tour(tour_id)
    except KeyError:
        flask.abort(404)
    str_departure = db.get_str_departure(tour);
    return render_template('tour.html',
                           tour=tour,
                           str_departure=str_departure
                           )


if __name__ == '__main__':
    app.run('127.0.0.1',8000)
