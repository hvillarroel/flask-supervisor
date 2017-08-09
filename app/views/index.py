# -*- coding: utf-8 -*-
from flask import redirect, Blueprint


page = Blueprint('index', __name__)


def initialize_app(app):
    app.register_blueprint(page)


@page.route('/')
def index():
    return redirect('/admin')
