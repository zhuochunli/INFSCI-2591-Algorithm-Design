import numpy as np


def multiplication(x, y):
    a=str(abs(x))
    b=str(abs(y))
    ans = [-1]*(len(a)+len(b))
    carry = 0
    rect = np.zeros((len(b), len(a), 2), int)
    for i in range(len(a)-1, -1, -1):
        for j in range(len(b)-1, -1, -1):
                tmp = int(a[i])*int(b[j])
                rect[j][i][0] = tmp / 10
                rect[j][i][1] = tmp % 10

    for m in range(len(a)+len(b)-1, -1, -1):
        tmp = carry
        for i in range(len(a) - 1, -1, -1):
            for j in range(len(b) - 1, -1, -1):
                for k in range(1, -1, -1):
                    if i+j+k == m:
                        tmp = tmp + rect[j][i][k]
                    carry = tmp // 10
                    ans[m] = tmp % 10

    if (x > 0 and y < 0) or (x < 0 and y > 0):
        print('-', end='')
        for num in ans:
            print(num, end='', sep='')
    else:
        for num in ans:
            print(num, end='', sep='')
    print()


if __name__ == '__main__':
    multiplication(7000, 7294)
    multiplication(25, 5038385)
    multiplication(-59724, 783)
    multiplication(8516, -82147953548159344)
    multiplication(45952456856498465985, 98654651986546519856)
    multiplication(-45952456856498465985, -98654651986546519856)