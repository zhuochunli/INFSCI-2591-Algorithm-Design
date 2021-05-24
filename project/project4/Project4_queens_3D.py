import numpy as np


def queens_3d(queen, i, j, k):
    if promising(queen, i, j, k):
        if queen == n:
            tmp = np.zeros((n, n, n),dtype=int)
            for q in range(1, n+1):
                tmp[queens[q][0]][queens[q][1]][queens[q][2]] = 1
            tmp = tmp.tolist()
            if tmp not in results:
                results.append(tmp)
            # global solutions
            # solutions = solutions+1

        else:
            queen = queen + 1
            for z in range(k, n):
                for x in range(n):
                    for y in range(n):
                        queens[queen] = [x, y, z]
                        queens_3d(queen, x, y, z)


def promising(queen, x, y, z):
    for q in range(1, queen):
        i, j, k = queens[q][0], queens[q][1], queens[q][2]
        if z == k:  # The two queens are in the same layer
            if x == i or y == j or abs(x-i) == abs(y-j):
                return False
        else:  # The two queens are in different layers
            if x == i and y == j:
                return False
            elif abs(x-i) == abs(z-k) or abs(y-j) == abs(z-k):
                return False

    return True


if __name__ == '__main__':
    test = [2, 3, 4, 5]
    for n in test:
        solutions = 0
        queens = np.zeros((n+1, 3), dtype=int)   # store x,y,z of the n-th queen
        results = []
        queens_3d(0, 0, 0, 0)
        print('The number of legal queen configurations for queen={} is:'.format(n), len(results))