class Prototype(object):
    def __init__(self, construct0, construct1):
        self.construct0 = construct0
        self.construct1 = construct1

    def __repr__(self) -> str:
        return f"Prototype({self.construct0}, {self.construct1})"