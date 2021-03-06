# -*- coding: utf-8 -*-

from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_mail import Mail

from database import db
from users.models import User


# Create a tolbar object
debug_toolbar = DebugToolbarExtension()


# Create and setup a logger manager object
login_manager = LoginManager()
login_manager.login_view = 'users.views.login_view'


@login_manager.user_loader
def load_user(userid):
    return db.session.query(User).get(userid)


# Create a flask-mail object
mail = Mail()
