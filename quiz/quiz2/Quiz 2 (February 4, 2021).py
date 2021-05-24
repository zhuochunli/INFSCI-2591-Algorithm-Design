def transform(table):
    num = []
    for i in table:
        for j in i:
            num.append(j)
    return num


def location(low, high, x, s):
    if low > high:
        return 0
    else:
        mid = (low+high)//2
        if x == s[mid]:
            return mid
        elif x < s[mid]:
            return location(low, mid-1, x, s)
        else:
            return location(mid+1, high, x, s)


def output(index, table):
    if index == 0:
        print('Not found!')   # or print('[]')
    else:
        n = len(table)
        m = len(table[0])
        print('[', index//m, ',', index % m, ']')   #print('[', index//m+1, ',', index % m+1, ']')

#This function outputs the index of value in the original table(both rows and columns start from 0)
#if it needs to output the index of value in math definition(both rows and columns start from 1), just add 1 to both row,column


if __name__ == '__main__':
    table1 = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    table2 = [[2, 4, 9, 14, 14, 15, 18],
              [21, 27, 31, 35, 42, 45, 50],
              [54, 59, 64, 69, 82, 84, 84]]
    table3 = [[3, 15, 21, 24, 83, 87, 88, 93],
              [178, 319, 541, 669, 770, 793, 848, 970],
              [1439, 1546, 1853, 2124, 2234, 2459, 2518, 2978],
              [3111, 3406, 3490, 3669, 3796, 3936, 4112, 4776],
              [5277, 5667, 6067, 6555, 7890, 8056, 8234, 9968]]
    s1 = transform(table1)
    s2 = transform(table2)
    s3 = transform(table3)
    output(location(0, len(s1)-1, 8, s1), table1)
    output(location(0, len(s2) - 1, 45, s2), table2)
    output(location(0, len(s3) - 1, 2356, s3), table3)