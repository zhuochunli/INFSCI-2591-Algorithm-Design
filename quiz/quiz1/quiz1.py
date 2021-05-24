def get_three(s):
    x = list(set(s))
    n = len(x)
    if n < 3:
        return[]
    else:
        results = []
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    result = [x[i], x[j], x[k]]
                    results.append(result)
        return results


if __name__ == '__main__':
    l1={1, 2, 3, 4}
    l2={7, 3}
    l3={4, 1, 7, 4, 3, 9, 1, 5}
    print('l1:', get_three(l1))
    print('l2:', get_three(l2))
    ans = get_three(l3)     #result of l3 is so long that we'd better split it in two lines to show
    print('l3:', ans[:15])
    print('l3:', ans[15:])