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


@app.route('/states/<id>')
@app.route('/states')
def list_states(id=""):
    state_cities = {}
    query = storage.all(State)
    print("este es {}".format(id))
    if id:
        q_state = []
        for state in query:
            if state.__dict__['id'] == id:
                q_state.append(state)
        query_cities = storage.all(City)
        for state in q_state:
            if state.__dict__['id'] == id:
                cities = []
                for city in query_cities:
                    if city.__dict__['state_id'] == state.__dict__['id']:
                        cities.append((city.__dict__['id'],
                                       city.__dict__['name']))
                state_cities[state.__dict__['name']] = cities
        return (render_template('9-states.html',
                query=q_state, query_cities=state_cities, id=id))
    else:
        return (render_template('7-states_list.html', query=query))


if __name__ == '__main__':
    app.run(debug=True)
