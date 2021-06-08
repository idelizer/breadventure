"""Models for bread baking journal."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User():
    """A user."""

    __tablename__ = "users"


class Recipe():
    """A recipe."""
    pass


def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
