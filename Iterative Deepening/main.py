from iteativedeepening import Iterativedeepening
from node import Node

def main():
    n = 3
    a = []

    for i in range(n):
        a.append([int(j) for j in input('type in row {}(space after every digit please): '.format(i)).split()])

    firstnode = Node(a.copy(), None)
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    Iterativedeepening.iterativeDeepening(firstnode, goal)


if __name__ == '__main__':
    main()
