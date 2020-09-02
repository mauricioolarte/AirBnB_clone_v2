#!/usr/bin/python3
""" this module starts a flask aplication """

from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db_sesion(error):
    storage.close()


@app.route('/cities_by_states')
def list_states():
    state_cities = {}
    query = storage.all(State)
    query_cities = storage.all(City)
    for state in query:
        cities = []
        for city in query_cities:
            if city.__dict__['state_id'] == state.__dict__['id']:
                cities.append((city.__dict__['id'], city.__dict__['name']))
        state_cities[state.__dict__['name']] = cities
    for key, value in state_cities.items():
        print("{}--{}".format(key, value))
    return (render_template('8-cities_by_states.html',
            query=query, query_cities=state_cities))


if __name__ == '__main__':
    app.run(debug=True)
