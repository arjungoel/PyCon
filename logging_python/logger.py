class Logger(Filterer):
    def __init__(self, name, level=NOTSET):
        Filterer.__init__(self)
        self.name = name
        self.level = _checkLevel(level)
        self.parent = None
        self.propagate = True
        self.handlers = []
        self.disabled = False


class Filterer(object):
    def __init__(self):
        self.filters = []


'''
You don't need to create this class explicitly. The handler will do that for you. Also tries to figure out:-
        - thread ID and name
        - PID and process name
        - Level Name
        - filename and module
'''


class LogRecord(object):
    def __init__(self, name, level, pathname, lineno,
                 msg, args, exc_info, func=None, sinfo=None, **kwargs):
