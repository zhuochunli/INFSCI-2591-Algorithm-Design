def backtrack(first, curr):
    if len(curr) == k:
        result.append(curr[:])
        return
    for i in range(first, x):
        curr.append(set[i])
        backtrack(i + 1, curr)
        curr.pop()


if __name__ == '__main__':
    n = [3, 5, 7]
    for x in n:
        set = list(range(1, x+1))
        result = []
        for k in range(x+1):
            backtrack(0, [])
        print(result)
        print('total subset count:', len(result))