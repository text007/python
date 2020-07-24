
class Rocm(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.parhs = {}

    def go(self, direction):
        return self.parhs.get(direction, None)

    def add_paths(self, paths):
        self.parhs.update(paths)
