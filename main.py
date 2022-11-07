from breadthfirst import Breadthfirst


def main():
    n = 3
    a = [[None] * n] * n
    for i in range(n):
        a[i] = input('please type in row {0}: ').format(i).split()

    goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
    Breadthfirst.breadthfirstsearch(a, goal)


if __name__ == '__main__':
    main()
