def queens(i):
    if promising(i):
        if i==n-1:
            global solutions
            solutions = solutions+1
        else:
            for j in range(n):
                col[i+1]=j
                queens(i+1)


def promising(i):
    k=0
    switch=True
    while k<i and switch:
        if col[i] == col[k] or abs(col[i]-col[k])==i-k:
            switch=False
        k=k+1
    return switch


if __name__ == '__main__':
    test=[4,8,10,12]
    for n in test:
        solutions=0
        col=[-1]*n
        queens(-1)
        print(solutions)