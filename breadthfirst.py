import collections
from node import Node

class Breadthfirst:

    @staticmethod
    def breadthfirstsearch(nodelist, goal):
        newNodes = []
        for node in nodelist:
            if Breadthfirst.goalreached(node, goal):
                print('goal reached')
                return node
            newNodes.append(predecessor(node))
            if len(newNodes) > 0:
                return breadthfirstsearch(newNodes, goal)
            else
                print('no solution')
                return None

    @staticmethod
    def goalreached(aNode, goal):
        res = [x for x in aNode.node + goal if x not in aNode.node or x not in goal]
        if len(res) == 0:
            return True

    @staticmethod
    def predecessor(currentNode):
        
