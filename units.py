class Generic:
    def __init__(self, name, range, hp, inv = None):
        self.name = name
        self.range = range
        self.hp = hp
        self.inv = inv or {}

class Infantry(Generic):
    def __init__(self, name, range, hp, inv = None):
        super().__init__(name, range, hp, inv)

class Mobile(Generic):
    def __init__(self, name, range, hp, inv = None):
        super().__init__(name, range, hp, inv)
