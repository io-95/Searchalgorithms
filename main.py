import breadthfirst

def main():
    n = 3
    a = [[None]*n]*n
    for i in range(n):
        a[i] = input('please type in row {0}: ').format(i)

    print(a)

if __name__ == '__main__':
    main()
