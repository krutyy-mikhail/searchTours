from db import data


def get_all_tours():
    return data.tours


def get_tour(tour_id):
    return data.tours[tour_id]


def get_str_departure(tour):
    return data.departures[tour["departure"]]


def get_tours_on_departure(departure):
    tours_on_departure = {key: value for key, value in data.tours.items() if value['departure'] == departure}

    return tours_on_departure


def _get_values_on_field(data, field):
    return (obj[field] for obj in data.values())


def get_min_price_tour(tours_on_departure):
    return min(_get_values_on_field(tours_on_departure, 'price'))


def get_max_price_tour(tours_on_departure):
    return max(_get_values_on_field(tours_on_departure, 'price'))


def get_min_night_tour(tours_on_departure):
    return min(_get_values_on_field(tours_on_departure, 'nights'))


def get_max_night_tour(tours_on_departure):
    return max(_get_values_on_field(tours_on_departure, 'nights'))


def get_departure_desc(departure):
    return data.departures[departure]
