# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask.ext.admin import Admin


def create_app(config='config.ini'):
    app = Flask(__name__)
    if os.path.exists(config):
        app.config.from_pyfile(config)
    else:
        raise 'No posee archivo de configuracion'

    register_blueprints(app)
    return app


def register_blueprints(app):
    from views import supervisor
    admin = Admin(app, 'Falcon-Admin', template_mode='bootstrap3')
    for config in app.config["SUPERVISOR"]:
        supervisor.init_app(admin, config)

app = create_app()

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], host=app.config['HOST'],
            port=app.config['PORT'])
