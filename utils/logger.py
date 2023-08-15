import sys


class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'w')
        self.callbacks = [(sys.stdout.write, '\n'), (self.file.write, '\n')]

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def log(self, message):
        for callback, end in self.callbacks:
            callback(message + end)
        self.file.flush()

    def close(self):
        self.file.close()


default = Logger('logs.txt')
