#!/usr/bin/python3
""" this module starts a flask aplication """

from models import storage
from models.state import State
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db_sesion(error):
    storage.close()


@app.route('/states_list')
def list_states():
    query = storage.all(State)
    return (render_template('7-states_list.html', query=query))


if __name__ == '__main__':
    app.run(debug=True)
