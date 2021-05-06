from collections import deque, defaultdict
# import google_functions
import program_execution
import command_strings
import logging


import sys, os, psutil

logging.basicConfig(level=logging.DEBUG)

mainNodes = []

class TreeNode():

    global mainNodes

    def __init__(self, name="", func=None, buzzwords=[], childNodes=[], freq = 0):
        self.buzzwords = buzzwords
        self.childNodes = childNodes
        self.func = func
        self.name = name
        self.parent = None
        self.freq = freq
        # the line below is problematic. Every time a node is created, it is added to the mainNodes list. We dont want that to happen. We only want to add it to the list if the node doesnt have a parent.
        # Fixed it in make_tree() func
        mainNodes.append(self)

    def add_child(self, child):
        child.parent = self
        self.childNodes.append(child)
        mainNodes.remove(child)

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
        # print(sys.getsizeof(self.name))
        if self.childNodes:
            for child in self.childNodes:
                child.print_tree()

    """
    STATUS:     COMPLETED
    Obj:        Create a tree from a dicitonary
    Method:     Take the dict and make a tree out of it.e
    Input:      dict d, TreeNode node
    """
def makeTree(d, node):
    for key, value in d.items():
        if isinstance(value, dict):
            newNode = TreeNode(key, value['command'], value["strings"], [], value['freq'])
            if node:
                node.add_child(newNode)
            makeTree(value, newNode)


    """
    NAME:       dfs(node, text)
    STATUS:     COMPLETED (for now)
    OBJ:        Use the input string to find appropriate command to execute
    METHOD:     1)  Traverse through the tree to find an appropriate node, then 
                    execute its command.
                2)  Then make sure that other nodes in the  stack are not 
                    checked, to save time.
                3)  Increase frequency of the node and its ancestors everytime
                    its command is used.
                4)  Organize the nodes according to their frequency every x
                    number of times.
                5)  Organize the most used functions into an array

    
    TODO:   1)  Add a function call after frequency incrementor to adjust the 
                sorting of the nodes within parent's childNodes array, then recurse upwards.
            2)  We also need to increase the freq var of the parent levels once 
                the command has been found and executed.

    CASE CHECKS:
        1)  An appropriate node exists in pos 0 (never gonna happen, root is 0)
        2)  The appropriate node doesnt exist
        3)  The appropriate node exists in the last pos
        4)  The appropriate node exists between 0 and n-1 pos

    OBJECTIONS:
        1)  Cant make everything just dfs or bfs. Need a combination of the
            two. Breadth first until just buzzwords found, then go only into that node's tree. Basically, breadth first restarts everytime buzzword check passes. Try clearing the stack????
    
        2)  Cant clear the stack, what if the command is not found, we
            should search other nodes.

        3)  Instead of creating a recountFrequency method, increasing only the
            current node's freq and its parent nodes' frequencies will be faster. Then its a matter of organizing the most used functions.

    POTENTIAL SOLUTION: 
        1)  Check that if the keywords of a level dont exists in the text,
            then, dont add its children to the stack, thereby skipping over its entire tree.
    """

def dfs(node, text):
    stack = deque()
    stack.append(node)

    # baseLayerAdded var exists to make sure that there are always nodes in the stack until the search ends or the function executes.
    baseLayerAdded = False
    buzzwordMatch = False
    # visited = set()

    # TODO implement array to store frequently used commands

    while stack:
        vertex = stack.pop()

        logging.info("vertex: " + vertex.name)

        if (not baseLayerAdded):
            baseLayerAdded = True
            for child in reversed(root.childNodes):
                stack.append(child)

        """
        HUGE PROBLEM: NOT ANYMORE
        THIS IS TRUE DFS. WE WANT LEVEL ORDER
        """

        for string in vertex.buzzwords:

            logging.info("Checking string: " + string)

            # if buzzword is in the input
            if string in text:

                """
                Problem: if there are more than one buzzwords detected, the nodes are added multiple times
                """
                if not buzzwordMatch:
                    buzzwordMatch = True
                    for child in reversed(vertex.childNodes):
                        stack.append(child)

                # if function exists, execute it, then increase freq for node and its parents
                if vertex.func:
                    vertex.func(text)
                    vertex.freq += 1
                    # root.freq += 1

                    # while we can keep going up
                    while vertex.parent:
                        vertex.parent.freq += 1

                        # if vertex is the first in the list, then we dont do anything, else
                        # check if its freq is higher than the node befor it.
                        if not vertex == vertex.parent.childNodes[0]:
                            vertexIndex = vertex.parent.childNodes.index(vertex)

                            # check if vertex's freq > previous sibling freq
                            # if yes, switch them
                            if vertex.freq > vertex.parent.childNodes[vertexIndex-1].freq:
                                vertex.parent.childNodes[vertexIndex], vertex.parent.childNodes[vertexIndex-1] = vertex.parent.childNodes[vertexIndex-1], vertex.parent.childNodes[vertexIndex]
                        vertex = vertex.parent

                    # if (root.freq % 11 == 0):
                    #     rebalance(root)
                    #     root.freq = 1

                    # Once the func has been found and executed, break loop
                    break

            if (not baseLayerAdded == True):
                for child in vertex.childNodes:
                    stack.append(child)

        else:
            continue

        break

    stack.clear()


if __name__ == "__main__":
    root = TreeNode("root", None, [], [], 0)
    makeTree(command_strings.command_strs, root)
    # root.print_tree()
    # print(type("execute chrome"))
    dfs(root, "search code")


if not __name__ == "__main__":
    makeTree(command_strings.command_strs, root)
    root.print_tree()