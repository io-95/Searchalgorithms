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
        positions = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        counter = 1

        for i in range(len(self.node)):
            for j in range(len(self.node)):
                if self.node[i][j] != counter and self.node[i][j] != 0:
                    currentValue = self.node[i][j]
                    x = positions[currentValue - 1][0]
                    y = positions[currentValue - 1][1]

                    dist = abs(x - i) + abs(y - j)
                    self.h += dist
                counter += 1

    def calc_f(self):
        return self.g + self.h

    def __lt__(self, other):
        return self.calc_f() < other.calc_f()
