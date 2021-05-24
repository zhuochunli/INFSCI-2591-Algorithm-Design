import pandas as pd
import time
import os
import psutil

_ = inf = 999999  # inf


def dijkstra_all_shortestPath(matrix, start, end=-1):
    length = len(matrix)
    min_len = []
    temp_array = []
    min_len.extend(matrix[start])
    temp_array.extend(matrix[start])
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
                if (min_len[i] + matrix[i][j]) < min_len[j]:
                    min_len[j] = temp_array[j] = min_len[i] + matrix[i][j]
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
    data = pd.read_csv('Project2_Input_Files/Project2_Input_File3.csv',
                       usecols=[0, 1, 2])
    node1 = data['NodeID'].values
    node2 = data['ConnectedNodeID'].values
    dis = data['Distance'].values
    n = data['NodeID'].values[-1] + 1
    aj = [[_] * n for x in range(n)]
    for r in range(len(data)):
        aj[node1[r]][node2[r]] = dis[r]
    # dijkstra_all_shortestPath(aj, 197, 27)
    # dijkstra_all_shortestPath(aj, 65, 280)
    # dijkstra_all_shortestPath(aj, 187, 68)
    for node in range(n):
        dijkstra_all_shortestPath(aj, node)
    end_t = time.process_time()
    total = end_t-start_t
    print('Time use:', '%.2f' % total, 's')
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0] / 2. ** 20
    print('Memory use:', '%.2f' % memoryUse, 'MB')
