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


def dijkstra_all_shortestPath(llist, start, end=-1):
    length = len(llist)
    min_len = []
    temp_array = []
    for v in range(length):
        min_len.append(distance(start, v, llist))
        temp_array.append(distance(start, v, llist))
    temp_array[start] = inf
    already_traversal = [start]
    path_parent = [start] * length
    while len(already_traversal) < length:
        i = temp_array.index(min(temp_array))
        temp_array[i] = inf
        if end != -1 and i == end:  # if user specifies the start and end, then print the shortest path between them
            print_path(start, end, path_parent)
        already_traversal.append(i)
        for j in range(length):
            if j not in already_traversal:
                if (min_len[i] + distance(i, j, llist)) < min_len[j]:
                    min_len[j] = temp_array[j] = min_len[i] + distance(i, j, llist)
                    path_parent[j] = i
    return min_len   # min_dis stores the length of shortest path from start node to each other nodes


def print_path(start, end, path_parent):
    path = []
    path.append(str(end))
    k = end
    while path_parent[k] != start:
        path.append(str(path_parent[k]))
        k = path_parent[k]
    path.append(str(start))
    path.reverse()
    print('From '+str(start)+' to '+str(end) + ':', '->'.join(path))


if __name__ == '__main__':
    start_t = time.process_time()
    data = pd.read_csv('Project2_Input_Files/Project2_Input_File10.csv',
                       usecols=[0, 1, 2])
    node1 = data['NodeID'].values
    node2 = data['ConnectedNodeID'].values
    dis = data['Distance'].values
    n = data['NodeID'].values[-1] + 1
    vertex_llist = []
    pre = -1
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
    # dijkstra_all_shortestPath(vertex_llist, 197, 27)
    # dijkstra_all_shortestPath(vertex_llist, 65, 280)
    # dijkstra_all_shortestPath(vertex_llist, 187, 68)
    for node in range(n):
        dijkstra_all_shortestPath(vertex_llist, node)
    end_t = time.process_time()
    total = end_t-start_t
    print('Time use:', '%.2f' % total, 's')
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0] / 2. ** 20
    print('Memory use:', '%.2f' % memoryUse, 'MB')