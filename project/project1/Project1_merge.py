def merge(sub1, sub2):
    m = min(len(sub1), len(sub2))
    if len(sub2) > len(sub1):
        array = sub1+sub2
    else:
        array = sub2+sub1
    n = len(array)
    aux = [0]*m
    for i in range(0, m):
        aux[i] = array[i]
    l = 0
    r = m
    for k in range(0, n):
        if l >= m:
            break
        elif r >= n:
            array[k] = aux[l]
            l = l+1
        elif array[r] < aux[l]:
            array[k] = array[r]
            r = r+1
        else:
            array[k] = aux[l]
            l = l+1
    print(array)


if __name__ == '__main__':
    merge([], [3, 7, 9])
    merge([2, 7, 9], [1])
    merge([1, 7, 10, 15], [3, 8, 12, 18])
    merge([1, 3, 5, 5, 15, 18, 21], [5, 5, 6, 8, 10, 12, 16, 17, 17, 20, 25, 28])