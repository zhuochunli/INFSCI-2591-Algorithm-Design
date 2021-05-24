import pandas as pd
import numpy as np
import os
import psutil
_ = inf = 999999  # inf


class Node(object):
    def __init__(self, vertex, edge):
        self.vertex = vertex
        self.edge = edge
        self.next = None


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
    # using linked-list
    vertex_llist = []
    pre = -1
    for r in range(len(data1)):
        v = data1['NodeID'].values[r]
        if v != pre:
            head = Node(v, 0)  # edge for vertex itslef is set to 0
            vertex_llist.append(head)
            ajv = Node(data1['ConnectedNodeID'].values[r], distance1[r])
            head.next = ajv
            tail = ajv
        elif v == pre:
            curr = Node(data1['ConnectedNodeID'].values[r], distance1[r])
            tail.next = curr
            tail = curr
        pre = v
    n1 = len(vertex_llist)
    for r in range(len(data2)):
        v = coord.index(coordinate2[r])
        if v != pre and v >= n1:
            head = Node(v, 0)  # edge for vertex itslef is set to 0
            vertex_llist.append(head)
            tmp = np.where(data2['NodeID'].values == data2['ConnectedNodeID'].values[r])
            ajv = Node(coord.index(coordinate2[tmp[0][0]]), distance2[r])
            head.next = ajv
            tail = ajv
        elif v == pre:
            tmp = np.where(data2['NodeID'].values == data2['ConnectedNodeID'].values[r])
            curr = Node(coord.index(coordinate2[tmp[0][0]]), distance2[r])
            tail.next = curr
            tail = curr
        else:  # if the vertex is already in vertex_llist
            for node in vertex_llist:
                if node.vertex == v:
                    tail = node
                    break
            while tail.next:
                tail = tail.next
            tmp = np.where(data2['NodeID'].values == data2['ConnectedNodeID'].values[r])
            curr = Node(coord.index(coordinate2[tmp[0][0]]), distance2[r])
            tail.next = curr
            tail = curr
        pre = v

    print(aj, vertex_llist)
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0] / 2. ** 20
    print('Memory use:', '%.2f' % memoryUse, 'MB')