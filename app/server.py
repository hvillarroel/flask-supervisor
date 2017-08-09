# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_admin import Admin


def create_app(config_file='config.ini'):
    app = Flask(__name__)
    app.secret_key = 'NP97AP1WxF7Ypmtni0C14wdDJNVKuwyQ/rMpIecPUO4='
    config = os.path.join(os.getcwd(), config_file)
    if os.path.exists(config):
        app.config.from_pyfile(config)
    else:
        raise 'Not found config.ini'

    register_blueprints(app)
    return app


def register_blueprints(app):
    from app.views import index, supervisor
    admin = Admin(app, 'Admin', template_mode='bootstrap3')
    index.initialize_app(app)
    for config in app.config["SUPERVISOR"]:
        supervisor.init_app(admin, config)

app = create_app()

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], host=app.config['HOST'],
            port=app.config['PORT'])
