class Node:
    predecessor = None
    node = []
    h = 0
    g = 0

    # Constructor
    def __init__(self, node, predecessor, g):

        self.node = node
        self.predecessor = predecessor
        self.g = g

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
                if self.node[i][j] != counter and self.node[i][j] != 0:
                    self.h += 1
                counter += 1


    def calc_f(self):
        return self.g + self.h

    def __lt__(self, other):
        return self.calc_f() < other.calc_f()
