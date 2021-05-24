import numpy as np
import pandas as pd
_ = inf = 999999  # inf


def prim(g):  # 输入距离矩阵
    v_near=0
    total = 0
    n = len(g)
    nearest = [0]*n
    distance = [-1]*n
    k = n-1
    for i in range(1, n):
        nearest[i] = 0
        distance[i] = g[0][i]
    print('Node', 'Node', 'Distance')
    while k > 0:
        min_value = inf
        for i in range(1, n):
            if 0 < distance[i] < min_value:
                min_value = distance[i]
                v_near = i
        print(nearest[v_near], v_near, distance[v_near])
        total = total + distance[v_near]
        for j in range(1, n):
            if g[j][v_near] < distance[j]:
                distance[j] = g[j][v_near]
                nearest[j] = v_near
        distance[v_near] = -1
        k = k-1
    return total


if __name__ == '__main__':
    data = pd.read_csv('Quiz6_Input_File.csv',
                       usecols=[0, 1, 2])
    node1 = data['NodeID'].values
    node2 = data['ConnectedNodeID'].values
    dis = data['Distance'].values
    n = data['NodeID'].values[-1] + 1
    aj = [[_] * n for x in range(n)]
    for r in range(len(data)):
        aj[node1[r]][node2[r]] = dis[r]
    print('The total distance in the minimum-spanning tree is:', prim(aj))