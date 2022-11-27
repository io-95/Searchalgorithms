from a_star import A_star
from node import Node

def main():
    n = 3
    a = []

    for i in range(n):
        a.append([int(j) for j in input('type in row {}(space after every digit please): '.format(i)).split()])

    firstnode = Node(a.copy(), None)
    Node.calc_h(firstnode)

    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    A_star.heuristicSearch(firstnode, goal)


if __name__ == '__main__':
    main()
