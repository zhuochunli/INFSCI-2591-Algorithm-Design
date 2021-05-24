
def max_sum(c):
    if not c:
        print('The original list is empty! No sublist is found.')
        return 0

    max_now = -10000
    max_end = 0
    start = 0
    end = 0
    x = 0
    n = len(c)
    for i in range(0, n):
        max_end += c[i]
        if max_now < max_end:
            max_now = max_end
            start = x
            end = i
        if max_end < 0:
            max_end = 0
            x = i + 1

    print('discovered sublist:', c[start:end+1])
    print('sum is:', max_now)


if __name__ == '__main__':
    max_sum([])
    max_sum([1])
    max_sum([1, 2, 3, 4])
    max_sum([-7, -4, -2, -8])
    max_sum([-2, 3, 5, -7])
    max_sum([-2, -3, 4, -1, -2, 1, 5, -3])
    max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
