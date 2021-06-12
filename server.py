"""Server for bread journal app."""

from flask import (Flask, render_template, request, redirect, flash, session)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "bread_dev"
app.jinja_env.undefined = StrictUndefined

# routes go here

@app.route('/')
def homepage():
    """View homepage."""

    # has login boxes



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)