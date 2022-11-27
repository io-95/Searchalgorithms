class Node:
    predecessor = None
    node = []
    h = 0

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

    def calc_h(self):
        counter = 1
        for i in range(len(self.node)):
            for j in range(len(self.node)):
                if self.node[i][j] != counter:
                    self.h += 1
                counter += 1

        # if the given node is the goal node then decrease by 1
        if self.h == 1:
            self.h -= 1
