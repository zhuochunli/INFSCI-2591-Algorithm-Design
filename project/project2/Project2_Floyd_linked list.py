import pandas as pd
import time
import os
import psutil

_ = inf = 999999  # inf


class Node(object):
    def __init__(self, vertex, edge):
        self.vertex = vertex
        self.edge = edge
        self.next = None


def distance(i, j, llist):
    head = llist[i]
    p = head.next
    while p:
        if p.vertex == j:
            return p.edge
        else:
            p = p.next
    return inf


def floyd(llist):
    n = len(llist)
    graph = [[_] * n for x in range(n)]
    for i in range(n):
        for j in range(n):
            graph[i][j] = distance(i, j, llist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    parents[i][j] = parents[k][j]
    return graph


def print_path(start, end, path_parent):
    path = []
    path.append(str(end))
    k = end
    while path_parent[start][k] != start:
        path.append(str(path_parent[start][k]))
        k = path_parent[start][k]
    path.append(str(start))
    path.reverse()
    print('From '+str(start)+' to '+str(end) + ':', '->'.join(path))


if __name__ == '__main__':
    start_t = time.process_time()
    data = pd.read_csv('Project2_Input_Files/Project2_Input_File1.csv',
                       usecols=[0, 1, 2])
    node1 = data['NodeID'].values
    node2 = data['ConnectedNodeID'].values
    dis = data['Distance'].values
    n = data['NodeID'].values[-1] + 1
    vertex_llist = []
    pre = -1
    parents = [[x] * n for x in range(n)]
    for r in range(len(data)):
        v = node1[r]
        if v != pre:
            head = Node(v, 0)  #edge for vertex itslef is set to 0
            vertex_llist.append(head)
            ajv = Node(node2[r],dis[r])
            head.next = ajv
            tail = ajv
        elif v == pre:
            curr = Node(node2[r], dis[r])
            tail.next = curr
            tail = curr
        pre = v
    floyd(vertex_llist)
    # print_path(197, 27, parents)
    # print_path(65, 280, parents)
    # print_path(187,68, parents)
    end_t = time.process_time()
    total = end_t - start_t
    print('Time use:', '%.2f' % total, 's')
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0] / 2. ** 20
    print('Memory use:', '%.2f' % memoryUse, 'MB')