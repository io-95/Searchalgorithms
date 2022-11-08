import collections
from node import Node

class Breadthfirst:
    @staticmethod
    def breadthfirstsearch(nodelist, goal):
        newNodes = []
        for node in nodelist:
            res = [x for x in node.node + goal if x not in node.node or x not in goal]
            if len(res) == 0:
                print('goal reached')
                return node

    def goalreached(self):
        pass
