import numpy as np


def complete(g):
    flag = 1
    n = len(g)
    for i in range(n):
        for j in range(n):
            if g[i][j] == 0 and j != i:
                flag = 0
                break
    if flag == 0:
        print('Not Complete')
    else:
        print('Complete')


def DFS(g, cur_vert):
    global visited_list
    visited_list[cur_vert] = 1
    w = []
    for i in range(len(g)):
        if g[cur_vert][i] == 1 and visited_list[i] == 0:
            w.append(i)
    if len(w) != 0:
        for i in range(len(w)):
            a = w[i]
            if visited_list[a] == 0:
                DFS(g, a)


def connect(g):
    DFS(g, 0)
    for v in range(len(g)):
        if visited_list[v]==0:
            return False
    return True


def degree(g):
    n=len(g)
    vertex = ['A','B','C','D','E','F','G']
    for x in range(n):
        indegree = 0
        outdegree = 0
        for i in range(n):
            if g[i][x]==1:
                indegree=indegree+1
        for j in range(n):
            if g[x][j]==1:
                outdegree=outdegree+1
        print('Node {}: in-degree:{}, out-degree:{}, total degree:{}'.format(vertex[x],indegree,outdegree,indegree+outdegree))


if __name__ == '__main__':
    file = open('graph4.txt', 'r')
    list = file.read().split(sep=',')
    n = int(len(list) ** 0.5)
    g = np.asarray(list,int)
    g = g.reshape(n,n)
    # g = [[0] * n for x in range(n)]
    # p = 0
    # for i in range(n):
    #     for j in range(n):
    #         g[i][j] = int(list[p])
    #         p = p+1
    visited_list = [0] * n
    if connect(g):
        print('Connected')
    else:
        print('Not Connected')
    complete(g)
    degree(g)