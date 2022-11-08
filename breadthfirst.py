import collections
from node import Node

class Breadthfirst:

    @staticmethod
    def breadthfirstsearch(nodelist, goal):
        newNodes = []
        for node in nodelist:
            isGoal = Breadthfirst.goalreached(node, goal)
            if isGoal:
                print('goal reached')
                return node
            

    @staticmethod
    def goalreached(aNode, goal):
        res = [x for x in aNode.node + goal if x not in aNode.node or x not in goal]
        if len(res) == 0:
            return True

