from node import Node
import copy


class Iterativedeepening:

    @staticmethod
    def iterativeDeepening(node, goal):
        barrier = 0
        while True:
            if Iterativedeepening.depthfirstsearch(node, goal, 0, barrier):
                print('goal reached')
                return
            barrier = barrier + 1
        print('no solution found')

    @staticmethod
    def depthfirstsearch(node, goal, depth, barrier):
        if Iterativedeepening.goalreached(node.node, goal):
            print('goal reached!')
            node.shownode(node)
            return True

        newNodes = Iterativedeepening.successor(node)
        length = len(newNodes)
        i = 0
        while i < length and depth < barrier:
            if Iterativedeepening.depthfirstsearch(newNodes[0], goal, depth+1, barrier):
                return True
            del newNodes[0]
            i +=1
        return False

    @staticmethod
    def goalreached(aNode, goal):
        res = [x for x in aNode + goal if x not in aNode or x not in goal]
        if len(res) == 0:
            return True

    @staticmethod
    def successor(currentNode):
        positionZero = []

        for i in range(len(currentNode.node)):
            for j in range(len(currentNode.node)):
                if currentNode.node[i][j] == 0:
                    positionZero.append(i)
                    positionZero.append(j)

        if positionZero[0] == 0 and positionZero[1] == 0:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode1.node[0][0], newNode1.node[0][1] = newNode1.node[0][1], newNode1.node[0][0]
            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode2.node[0][0], newNode2.node[1][0] = newNode2.node[1][0], newNode2.node[0][0]
            return [newNode1, newNode2]

        if positionZero[0] == 0 and positionZero[1] == 1:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode1.node[0][1], newNode1.node[0][0] = newNode1.node[0][0], newNode1.node[0][1]
            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode2.node[0][1], newNode2.node[0][2] = newNode2.node[0][2], newNode2.node[0][1]
            newNode3 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode3.node[0][1], newNode3.node[1][1] = newNode3.node[1][1], newNode3.node[0][1]
            return [newNode1, newNode2, newNode3]

        if positionZero[0] == 0 and positionZero[1] == 2:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode1.node[0][2], newNode1.node[0][1] = newNode1.node[0][1], newNode1.node[0][2]
            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode2.node[0][2], newNode2.node[1][2] = newNode2.node[1][2], newNode2.node[0][2]
            return [newNode1, newNode2]

        if positionZero[0] == 1 and positionZero[1] == 0:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode1.node[1][0], newNode1.node[0][0] = newNode1.node[0][0], newNode1.node[1][0]
            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode2.node[1][0], newNode2.node[1][1] = newNode2.node[1][1], newNode2.node[1][0]
            newNode3 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode3.node[1][0], newNode3.node[2][0] = newNode3.node[2][0], newNode3.node[1][0]
            return [newNode1, newNode2, newNode3]

        if positionZero[0] == 1 and positionZero[1] == 1:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode1.node[1][1], newNode1.node[0][1] = newNode1.node[0][1], newNode1.node[1][1]
            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode2.node[1][1], newNode2.node[1][0] = newNode2.node[1][0], newNode2.node[1][1]
            newNode3 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode3.node[1][1], newNode3.node[1][2] = newNode3.node[1][2], newNode3.node[1][1]
            newNode4 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode4.node[1][1], newNode4.node[2][1] = newNode4.node[2][1], newNode4.node[1][1]
            return [newNode1, newNode2, newNode3, newNode4]

        if positionZero[0] == 1 and positionZero[1] == 2:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode1.node[1][2], newNode1.node[0][2] = newNode1.node[0][2], newNode1.node[1][2]
            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode2.node[1][2], newNode2.node[1][1] = newNode2.node[1][1], newNode2.node[1][2]
            newNode3 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode3.node[1][2], newNode3.node[2][2] = newNode3.node[2][2], newNode3.node[1][2]
            return [newNode1, newNode2, newNode3]

        if positionZero[0] == 2 and positionZero[1] == 0:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode1.node[2][0], newNode1.node[1][0] = newNode1.node[1][0], newNode1.node[2][0]
            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode2.node[2][0], newNode2.node[2][1] = newNode2.node[2][1], newNode2.node[2][0]
            return [newNode1, newNode2]

        if positionZero[0] == 2 and positionZero[1] == 1:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode1.node[2][1], newNode1.node[2][0] = newNode1.node[2][0], newNode1.node[2][1]
            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode2.node[2][1], newNode2.node[1][1] = newNode2.node[1][1], newNode2.node[2][1]
            newNode3 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode3.node[2][1], newNode3.node[2][2] = newNode3.node[2][2], newNode3.node[2][1]
            return [newNode1, newNode2, newNode3]

        if positionZero[0] == 2 and positionZero[1] == 2:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode1.node[2][2], newNode1.node[2][1] = newNode1.node[2][1], newNode1.node[2][2]
            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode)
            newNode2.node[2][2], newNode2.node[1][2] = newNode2.node[1][2], newNode2.node[2][2]
            return [newNode1, newNode2]
