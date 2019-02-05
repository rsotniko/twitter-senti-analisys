import Analyzer


class Saver(object):

    def __init__(self, analis_res):
        self.data = analis_res

    def safe(self):
        print self.data
