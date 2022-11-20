class Node:

    predecessor = None
    node = []

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
