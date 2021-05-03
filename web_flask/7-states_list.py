#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import *
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from flask import Flask, render_template
classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception):
    """  """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ displays a HTML page with states """
    states = storage.all(classes["State"]).values()
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
