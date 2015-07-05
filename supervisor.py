from xmlrpc import client


class Supervisor:

    def __init__(self, host='localhost', port=9001, user=None, password=None):
        if user:
            url = "http://%(user)s:%(password)s@%(host)s:%(port)s" % locals()
        else:
            url = "http://%(host)s:%(port)s" % locals()
        self.url = url
        self.con = client.ServerProxy(url)
        self.supervisor = self.con.supervisor

    def get_state(self):
        return self.supervisor.getState()

    def list_methods(self):
        return self.system.listMethods()

    def get_api_version(self):
        return self.supervisor.getAPIVersion()

    def get_supervidor_version(self):
        return self.supervisor.getSupervidorVersion()

    def get_pid(self):
        return self.supervisor.getPID()

    def shutdown(self):
        return self.supervisor.shutdown()

    def restart(self):
        return self.supervisor.restart()

    def get_all_process_info(self):
        return self.supervisor.getAllProcessInfo()

    def get_process_info(self, name):
        return self.supervisor.getProcessInfo(name)

    def start_process(self, name, wait=True):
        return self.supervisor.startProcess(name, wait)

    def start_all_processes(self, wait=True):
        return self.supervisor.startAllProcesses(wait)

    def start_process_group(self, name, wait=True):
        return self.supervisor.startProcessGroup(name, wait)

    def stop_process(self, name, wait=True):
        return self.supervisor.stopProcess(name, wait)

    def stop_all_processes(self, wait=True):
        return self.supervisor.stopAllProcesses(wait)

    def stop_process_group(self, name, wait=True):
        return self.supervisor.stopProcessGroup(name, wait)

    def restart_process(self, name, wait=True):
        process = self.get_process_info(name)
        if process.get('state', 0) == 20:
            if self.stop_process(name, wait):
                return self.start_process(name, wait)

    def get_log_process(self, name, offset=0, lenght=5000):
        return self.supervisor.readProcessStdoutLog(name, offset, lenght)
