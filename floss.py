__version__ = 'dev'


class Floss:
    def __init__(self, lst):
        self.value = lst

    def have(self, val):
        return Floss([i for i in self.value if val in i])

    def starts(self, val):
        return Floss([i for i in self.value if val == i[:len(val)]])

    def condition(self, key):
        return Floss([i for i in self.value if key(i)])

    def end(self):
        return self.value
