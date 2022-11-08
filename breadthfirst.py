import collections
from node import Node

class Breadthfirst:

    @staticmethod
    def breadthfirstsearch(nodelist, goal):
        newNodes = []
        for node in nodelist:
            if Breadthfirst.goalreached(node.node, goal):
                print('goal reached')
                return node
            newNodes.append(Breadthfirst.predecessor(node))
            
            if newNodes[0] != None:
                return Breadthfirst.breadthfirstsearch(newNodes, goal)
            else:
                print('no solution')
                return None

    @staticmethod
    def goalreached(aNode, goal):
        res = [x for x in aNode + goal if x not in aNode or x not in goal]
        if len(res) == 0:
            return True

    @staticmethod
    def predecessor(currentNode):
        for i in range(len(currentNode.node)):
	    	    print(currentNode.node[i])
