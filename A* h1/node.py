class Node:
    predecessor = None
    node = []
    h = None

    # Constructor
    def __init__(self, node, predecessor):

        self.node = node
        self.predecessor = predecessor

    def shownode(self, node):
        while node:
            for i in range(3):
                print(node.node[i])
            node = node.predecessor
            print("\n")

    def calc_h(self, node):
        for i in range(len(node.node)):
            if node.node[i] == i + 1:
                self.h += 1

        # if the given node is the goal node then decrease by 1
        if self.h == 1:
            self.h -= 1
