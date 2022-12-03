from node import Node
import copy
import bisect

class A_star:

    @staticmethod
    def heuristicSearch(start, goal):
        nodelist = [start]

        while True:
            if len(nodelist) == 0:
                print('no solution found')
                return
            node = nodelist[0]
            del nodelist[0]
            if A_star.goalreached(node.node, goal):
                print('goal reached!')
                node.shownode(node)
                return
            successor = A_star.successor(node)
            A_star.sortin(successor, nodelist)

    @staticmethod
    def goalreached(aNode, goal):
        for i in range(3):
            for j in range(3):
                if aNode[i][j] != goal[i][j]:
                    return False

        return True

    @staticmethod
    def sortin(successor, nodelist):
        for node in successor:
            bisect.insort(nodelist, node)

    @staticmethod
    def cycleCheck(node):
        if node.predecessor.predecessor is None:
            return True

        res = [x for x in node.node + node.predecessor.predecessor.node if x not in node.node or x not in node.predecessor.predecessor.node]
        if len(res) == 0:
            return False
        else:
            return True

    @staticmethod
    def successor(currentNode):
        positionZero = []

        for i in range(len(currentNode.node)):
            for j in range(len(currentNode.node)):
                if currentNode.node[i][j] == 0:
                    positionZero.append(i)
                    positionZero.append(j)
                    break

        returnValue = []

        if positionZero[0] == 0 and positionZero[1] == 0:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode1.node[0][0], newNode1.node[0][1] = newNode1.node[0][1], newNode1.node[0][0]
            Node.calc_h(newNode1)
            if A_star.cycleCheck(newNode1):
                returnValue.append(newNode1)

            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode2.node[0][0], newNode2.node[1][0] = newNode2.node[1][0], newNode2.node[0][0]
            Node.calc_h(newNode2)
            if A_star.cycleCheck(newNode2):
                returnValue.append(newNode2)

            return returnValue

        if positionZero[0] == 0 and positionZero[1] == 1:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode1.node[0][1], newNode1.node[0][0] = newNode1.node[0][0], newNode1.node[0][1]
            Node.calc_h(newNode1)
            if A_star.cycleCheck(newNode1):
                returnValue.append(newNode1)

            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode2.node[0][1], newNode2.node[0][2] = newNode2.node[0][2], newNode2.node[0][1]
            Node.calc_h(newNode2)
            if A_star.cycleCheck(newNode2):
                returnValue.append(newNode2)

            newNode3 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode3.node[0][1], newNode3.node[1][1] = newNode3.node[1][1], newNode3.node[0][1]
            Node.calc_h(newNode3)
            if A_star.cycleCheck(newNode3):
                returnValue.append(newNode3)

            return returnValue

        if positionZero[0] == 0 and positionZero[1] == 2:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode1.node[0][2], newNode1.node[0][1] = newNode1.node[0][1], newNode1.node[0][2]
            Node.calc_h(newNode1)
            if A_star.cycleCheck(newNode1):
                returnValue.append(newNode1)

            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode2.node[0][2], newNode2.node[1][2] = newNode2.node[1][2], newNode2.node[0][2]
            Node.calc_h(newNode2)
            if A_star.cycleCheck(newNode2):
                returnValue.append(newNode2)

            return returnValue

        if positionZero[0] == 1 and positionZero[1] == 0:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode1.node[1][0], newNode1.node[0][0] = newNode1.node[0][0], newNode1.node[1][0]
            Node.calc_h(newNode1)
            if A_star.cycleCheck(newNode1):
                returnValue.append(newNode1)

            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode2.node[1][0], newNode2.node[1][1] = newNode2.node[1][1], newNode2.node[1][0]
            Node.calc_h(newNode2)
            if A_star.cycleCheck(newNode2):
                returnValue.append(newNode2)

            newNode3 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode3.node[1][0], newNode3.node[2][0] = newNode3.node[2][0], newNode3.node[1][0]
            Node.calc_h(newNode3)
            if A_star.cycleCheck(newNode3):
                returnValue.append(newNode3)

            return returnValue

        if positionZero[0] == 1 and positionZero[1] == 1:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode1.node[1][1], newNode1.node[0][1] = newNode1.node[0][1], newNode1.node[1][1]
            Node.calc_h(newNode1)
            if A_star.cycleCheck(newNode1):
                returnValue.append(newNode1)

            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode2.node[1][1], newNode2.node[1][0] = newNode2.node[1][0], newNode2.node[1][1]
            Node.calc_h(newNode2)
            if A_star.cycleCheck(newNode2):
                returnValue.append(newNode2)

            newNode3 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode3.node[1][1], newNode3.node[1][2] = newNode3.node[1][2], newNode3.node[1][1]
            Node.calc_h(newNode3)
            if A_star.cycleCheck(newNode3):
                returnValue.append(newNode3)

            newNode4 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode4.node[1][1], newNode4.node[2][1] = newNode4.node[2][1], newNode4.node[1][1]
            Node.calc_h(newNode4)
            if A_star.cycleCheck(newNode4):
                returnValue.append(newNode4)

            return returnValue

        if positionZero[0] == 1 and positionZero[1] == 2:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode1.node[1][2], newNode1.node[0][2] = newNode1.node[0][2], newNode1.node[1][2]
            Node.calc_h(newNode1)
            if A_star.cycleCheck(newNode1):
                returnValue.append(newNode1)

            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode2.node[1][2], newNode2.node[1][1] = newNode2.node[1][1], newNode2.node[1][2]
            Node.calc_h(newNode2)
            if A_star.cycleCheck(newNode2):
                returnValue.append(newNode2)
            newNode3 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode3.node[1][2], newNode3.node[2][2] = newNode3.node[2][2], newNode3.node[1][2]
            Node.calc_h(newNode3)
            if A_star.cycleCheck(newNode3):
                returnValue.append(newNode3)

            return returnValue

        if positionZero[0] == 2 and positionZero[1] == 0:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode1.node[2][0], newNode1.node[1][0] = newNode1.node[1][0], newNode1.node[2][0]
            Node.calc_h(newNode1)
            if A_star.cycleCheck(newNode1):
                returnValue.append(newNode1)

            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode2.node[2][0], newNode2.node[2][1] = newNode2.node[2][1], newNode2.node[2][0]
            Node.calc_h(newNode2)
            if A_star.cycleCheck(newNode2):
                returnValue.append(newNode2)

            return returnValue

        if positionZero[0] == 2 and positionZero[1] == 1:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode1.node[2][1], newNode1.node[2][0] = newNode1.node[2][0], newNode1.node[2][1]
            Node.calc_h(newNode1)
            if A_star.cycleCheck(newNode1):
                returnValue.append(newNode1)

            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode2.node[2][1], newNode2.node[1][1] = newNode2.node[1][1], newNode2.node[2][1]
            Node.calc_h(newNode2)
            if A_star.cycleCheck(newNode2):
                returnValue.append(newNode2)

            newNode3 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode3.node[2][1], newNode3.node[2][2] = newNode3.node[2][2], newNode3.node[2][1]
            Node.calc_h(newNode3)
            if A_star.cycleCheck(newNode3):
                returnValue.append(newNode3)

            return returnValue

        if positionZero[0] == 2 and positionZero[1] == 2:
            newNode1 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode1.node[2][2], newNode1.node[2][1] = newNode1.node[2][1], newNode1.node[2][2]
            Node.calc_h(newNode1)
            if A_star.cycleCheck(newNode1):
                returnValue.append(newNode1)

            newNode2 = Node(copy.deepcopy(currentNode.node), currentNode, currentNode.g+1)
            newNode2.node[2][2], newNode2.node[1][2] = newNode2.node[1][2], newNode2.node[2][2]
            Node.calc_h(newNode2)
            if A_star.cycleCheck(newNode2):
                returnValue.append(newNode2)

            return returnValue
