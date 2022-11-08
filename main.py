from breadthfirst import Breadthfirst


def main():
    n = 3
    a = []

    for i in range(n):
        a.append([int(j) for j in input().split()])
    
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    Breadthfirst.breadthfirstsearch(a, goal)


if __name__ == '__main__':
    main()
