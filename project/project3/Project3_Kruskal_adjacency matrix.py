import pandas as pd
import numpy as np
import os
import psutil
_ = inf = 999999  # inf


def edge(w):
    n = np.shape(w)[0]
    edge_list = []
    for i in range(n):
        for j in range(n):
            if i < j:
                edge_list.append((w[i][j], i, j))
    edge_list.sort()
    return edge_list


def kruskal(w):
    n = np.shape(w)[0]
    u = list(range(n))
    edge_list = edge(w)
    result = []
    sum = 0  # total distance

    def find(i):
        while u[i] != i:
            i = u[i]
        return i

    def merge(p, q):
        if p < q:
            u[q] = p
        else:
            u[p] = q

    j = 0
    print('Node', 'Node', 'Distance')
    while len(result) < n-1:
        (long, v_little, v_large) = edge_list[j]
        q = find(v_little)
        p = find(v_large)
        if q != p:
            merge(p, q)
            result.append(edge_list[j])
            print(v_little, v_large, long)
            sum = sum+long
        j = j + 1
    return sum


if __name__ == '__main__':
    coord = []  # distinct coordinates for every node
    name = []  # intersection_names
    data1 = pd.read_csv('E:/学习资料/Pitt/algorithm/project/project3/Project3_G1_Data.csv')
    coordinate1 = data1['Coordinates'].values
    distance1 = data1['Distance'].values
    name1 = data1['Intersection_Name'].values
    data2 = pd.read_csv('E:/学习资料/Pitt/algorithm/project/project3/Project3_G2_Data.csv')
    coordinate2 = data2['Coordinates'].values
    distance2 = data2['Distance'].values
    name2 = data2['Intersection_Name'].values
    for i in range(len(data1)):
        if coordinate1[i] not in coord:
            coord.append(coordinate1[i])
            name.append(name1[i])
    for j in range(len(data2)):
        if coordinate2[j] not in coord:
            coord.append(coordinate2[j])
            name.append(name2[j])
    n = len(coord)
    # using a two-dimensional array
    aj = [[_] * n for x in range(n)]
    for i in range(len(data1)):
        aj[data1['NodeID'].values[i]][data1['ConnectedNodeID'].values[i]] = distance1[i]
    for j in range(len(data2)):
        tmp = np.where(data2['NodeID'].values == data2['ConnectedNodeID'].values[j])
        aj[coord.index(coordinate2[j])][coord.index(coordinate2[tmp[0][0]])] = distance2[j]
    print('The total distance of the minimum-spanning tree is:', kruskal(aj))
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0] / 2. ** 20
    print('Memory use:', '%.2f' % memoryUse, 'MB')