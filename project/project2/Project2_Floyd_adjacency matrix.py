import pandas as pd
import time
import os
import psutil

_ = inf = 999999  # inf


def floyd(matrix):
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    parents[i][j] = parents[k][j]


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
    data = pd.read_csv('Project2_Input_Files/Project2_Input_File9.csv',
                       usecols=[0, 1, 2])
    node1 = data['NodeID'].values
    node2 = data['ConnectedNodeID'].values
    dis = data['Distance'].values
    n = data['NodeID'].values[-1] + 1
    aj = [[_] * n for x in range(n)]
    parents = [[x] * n for x in range(n)]
    for r in range(len(data)):
        aj[node1[r]][node2[r]] = dis[r]
    floyd(aj)
    # print_path(197, 27, parents)
    # print_path(65, 280, parents)
    # print_path(187,68, parents)
    end_t = time.process_time()
    total = end_t-start_t
    print('Time use:', '%.2f' % total, 's')
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0] / 2. ** 20
    print('Memory use:', '%.2f' % memoryUse, 'MB')