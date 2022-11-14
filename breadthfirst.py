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
            #list is saved in list have to be solved! For example multiple return values
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
        positionZero = []

        for i in range(len(currentNode.node)):
            for j in range(len(currentNode.node)):
                if currentNode.node[i][j] == 0:
                    positionZero.append(i)
                    positionZero.append(j)

        if positionZero[0] == 0 and positionZero[1] == 0:
            newNode1 = Node(currentNode.node, currentNode)
            newNode1.node[0][0], newNode1.node[0][1] = newNode1.node[0][1], newNode1.node[0][0]
            newNode2 = Node(currentNode.node, currentNode)
            newNode2.node[0][0], newNode2.node[1][0] = newNode2.node[1][0], newNode2.node[0][0]
            
            return newNode1, newNode2
        if positionZero[0] == 0 and positionZero[1] == 1:
            newNode1 = Node(currentNode.node, currentNode)
            newNode1.node[0][1], newNode1.node[0][0] = newNode1.node[0][0], newNode1.node[0][1]
            newNode2 = Node(currentNode.node, currentNode)
            newNode2.node[0][1], newNode2.node[0][2] = newNode2.node[0][2], newNode2.node[0][1]
            newNode3 = Node(currentNode.node, currentNode)
            newNode3.node[0][1], newNode3.node[1][1] = newNode3.node[1][1], newNode3.node[0][1]
            
            return newNode1, newNode2, newNode3

        if positionZero[0] == 0 and positionZero[1] == 2:
            newNode1 = Node(currentNode.node, currentNode)
            newNode1.node[0][2], newNode1.node[0][1] = newNode1.node[0][1], newNode1.node[0][2]
            newNode2 = Node(currentNode.node, currentNode)
            newNode2.node[0][2], newNode2.node[1][2] = newNode2.node[1][2], newNode2.node[0][2]

            return newNode1, newNode2
        if positionZero[0] == 1 and positionZero[1] == 0:
            newNode1 = Node(currentNode.node, currentNode)
            newNode1.node[1][0], newNode1.node[0][0] = newNode1.node[0][0], newNode1.node[1][0]
            newNode2 = Node(currentNode.node, currentNode)
            newNode2.node[1][0], newNode2.node[1][1] = newNode2.node[1][1], newNode2.node[1][0]
            newNode3 = Node(currentNode.node, currentNode)
            newNode3.node[1][0], newNode3.node[2][0] = newNode3.node[2][0], newNode3.node[1][0]
            
            return newNode1, newNode2, newNode3
        if positionZero[0] == 1 and positionZero[1] == 1:
            newNode1 = Node(currentNode.node, currentNode)
            newNode1.node[1][1], newNode1.node[0][1] = newNode1.node[0][1], newNode1.node[1][1]
            newNode2 = Node(currentNode.node, currentNode)
            newNode2.node[1][1], newNode2.node[1][0] = newNode2.node[1][0], newNode2.node[1][1]
            newNode3 = Node(currentNode.node, currentNode)
            newNode3.node[1][1], newNode3.node[1][2] = newNode3.node[1][2], newNode3.node[1][1]
            newNode4 = Node(currentNode.node, currentNode)
            newNode4.node[1][1], newNode4.node[2][1] = newNode4.node[2][1], newNode4.node[1][1]
         
            return newNode1, newNode2, newNode3, newNode4
        if positionZero[0] == 1 and positionZero[1] == 2:
            newNode1 = Node(currentNode.node, currentNode)
            newNode1.node[1][2], newNode1.node[0][2] = newNode1.node[0][2], newNode1.node[1][2]
            newNode2 = Node(currentNode.node, currentNode)
            newNode2.node[1][2], newNode2.node[1][1] = newNode2.node[1][1], newNode2.node[1][2]
            newNode3 = Node(currentNode.node, currentNode)
            newNode3.node[1][2], newNode3.node[2][2] = newNode3.node[2][2], newNode3.node[1][2]
            
            return newNode1, newNode2, newNode3
        if positionZero[0] == 2 and positionZero[1] == 0:
            newNode1 = Node(currentNode.node, currentNode)
            newNode1.node[2][0], newNode1.node[1][0] = newNode1.node[1][0], newNode1.node[2][0]
            newNode2 = Node(currentNode.node, currentNode)
            newNode2.node[2][0], newNode2.node[2][1] = newNode2.node[2][1], newNode2.node[2][0]
            
            return newNode1, newNode2
        if positionZero[0] == 2 and positionZero[1] == 1:
            newNode1 = Node(currentNode.node, currentNode)
            newNode1.node[2][1], newNode1.node[2][0] = newNode1.node[2][0], newNode1.node[2][1]
            newNode2 = Node(currentNode.node, currentNode)
            newNode2.node[2][1], newNode2.node[1][1] = newNode2.node[1][1], newNode2.node[2][1]
            newNode3 = Node(currentNode.node, currentNode)
            newNode3.node[2][1], newNode3.node[2][2] = newNode3.node[2][2], newNode3.node[2][1]
            
            return newNode1, newNode2, newNode3
        if positionZero[0] == 2 and positionZero[1] == 2:
            newNode1 = Node(currentNode.node, currentNode)
            newNode1.node[2][2], newNode1.node[2][1] = newNode1.node[2][1], newNode1.node[2][2]
            newNode2 = Node(currentNode.node, currentNode)
            newNode2.node[2][2], newNode2.node[1][2] = newNode2.node[1][2], newNode2.node[2][2]
            
            return newNode1, newNode2

