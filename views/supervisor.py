# -*- coding: utf-8 -*-
from flask import request, url_for, redirect, flash
from flask.ext.admin import expose, BaseView
from supervisor import Supervisor


def init_app(admin, data):
    view = SupervisorView(
        name=data['NAME'],
        endpoint=data["ID"],
        config=data
    )
    admin.add_view(view)


class SupervisorView(BaseView):

    can_start = True
    can_stop = True
    can_restart = True
    can_start_all = True
    can_restart_all = True
    can_stop_all = True
    can_restart_supervisor = True
    can_stop_supervisor = True

    def __init__(self, **data):
        self.config = data['config']
        del data['config']
        super(SupervisorView, self).__init__(**data)
        self.init_connection()

    def init_connection(self):
        self.conn = Supervisor(
            host=self.config['HOST'],
            port=self.config['PORT'],
            user=self.config['USER'],
            password=self.config['PASSWORD']
        )

    @expose('/')
    def index(self):
        try:
            list_processes = self.conn.get_all_process_info()
        except Exception as e:
            print(e)
            list_processes = []
            flash("PROBLEM IN CONNECTION", 'error')

        return self.render('supervisor.html', list_processes=list_processes)

    @expose('/start_all_processes')
    def start_all_processes(self):
        self.conn.start_all_processes()
        return redirect(url_for('.index'))

    @expose('/stop_all_processes')
    def stop_all_processes(self):
        self.conn.stop_all_processes()
        return redirect(url_for('.index'))

    @expose('/restart_all_processes')
    def restart_all_processes(self):
        return '{}'

    @expose('/restart_supervisor')
    def restart_supervisor(self):
        self.conn.restart()
        return redirect(url_for('.index'))

    @expose('/stop_supervisor')
    def stop_supervisor(self):
        self.conn.shutdown()
        return redirect(url_for('.index'))

    @expose('/start_process')
    def start_process(self):
        name = request.values.get('id')
        self.conn.start_process(name)
        return redirect(url_for('.index'))

    @expose('/stop_process')
    def stop_process(self):
        name = request.values.get('id')
        self.conn.stop_process(name)
        return redirect(url_for('.index'))

    @expose('/restart_process')
    def restart_process(self):
        name = request.values.get('id')
        self.conn.restart_process(name)
        return redirect(url_for('.index'))

    @expose('/get_log')
    def get_log(self):
        try:
            name = request.values.get('id')
            html = self.conn.get_log_process(name, 0, 1500)
            return html.replace("\n", "<br>")
        except Exception as e:
            print(e)
            return "PROBLEM WITH METHOD OF LOG"

        return '{}'

    states = {
        0: {
            "name": "STOPPED",
            "class": "",
            "style": ""
        },
        10: {
            "name": "STARTING",
            "class": "",
            "style": ""
        },
        20: {
            "name": "RUNNING",
            "class": "",
            "style": "color: green;"
        },
        30: {
            "name": "BACKOFF",
            "class": "",
            "style": ""
        },
        40: {
            "name": "STOPPING",
            "class": "",
            "style": ""
        },
        100: {
            "name": "EXITED",
            "class": "",
            "style": ""
        },
        200: {
            "name": "FATAL",
            "class": "",
            "style": ""
        },
        1000: {
            "name": "UNKNOWN",
            "class": "",
            "style": ""
        },
    }
