class Tree():

    def __init__(self):
        self.buzzwords = []
        self.childNodes = []
        self.func = None
        self.name = ""

    def addChild(self, child):
        self.childNodes.append(child)