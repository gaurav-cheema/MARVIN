from collections import deque

mainNodes = []

class TreeNode():

    global mainNodes

    def __init__(self, name="", func=None, buzzwords=[], childNodes=[]):
        self.buzzwords = []
        self.childNodes = childNodes
        self.func = func
        self.name = name
        self.parent = None
        # the line below is problematic. Every time a node is created, it is added to the mainNodes list. We dont want that to happen. We only want to add it to the list if the node doesnt have a parent.
        # Fixed it in make_tree() func
        mainNodes.append(self)

    def add_child(self, child):
        child.parent = self
        self.childNodes.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.name)
        if self.childNodes:
            for child in self.childNodes:
                child.print_tree()


def check_tree(text):
    global mainNodes
    # Sorry about the arrow code lol
    for node in mainNodes:
        for i in node.buzzwords:
            if i in text:
                for child in node.childNodes:
                    for j in node.childNodes.buzzwords:
                        if j in text:
                            node.childNodes.func(text)
                            return True


def make_tree(someDict):
    if not isinstance(someDict, dict): return None

    currDict = someDict
    stack = deque()
    stack.append(currDict)

    if isinstance(currDict, dict):
        for key in currDict.keys():
            newNode = TreeNode(key, None, currDict[key]["buzzwords"],[])
            for key2 in currDict[key]:
                if isinstance(currDict[key][key2], list):
                    pass
                if isinstance(currDict[key][key2], dict):
                    newChild = TreeNode(key2, currDict[key][key2], currDict[key][key2]["strings"], [])
                    newNode.add_child(newChild)
                    mainNodes.pop()