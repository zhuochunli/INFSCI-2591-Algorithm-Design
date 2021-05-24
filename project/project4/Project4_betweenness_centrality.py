import pandas as pd

_ = inf = 999999  # inf


def floyd(matrix):
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    parents[i][j] = parents[k][j]


def calculate_betweenness(path_parent, matrix):
    n = len(matrix)
    betweenness_centrality = [0]*n
    for start in range(n):
        for end in range(n):
            if start != end and matrix[start][end] < inf:
                betweenness_centrality[start] += 1
                betweenness_centrality[end] += 1
                k = end
                while path_parent[start][k] != start:
                    k = path_parent[start][k]
                    betweenness_centrality[k] += 1
    return betweenness_centrality


if __name__ == '__main__':
    data = pd.read_csv('E:/学习资料/Pitt/algorithm/project/project4/Project 4_Problem 1_InputData.csv',
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
    betweenness = calculate_betweenness(parents, aj)
    print('The top 20 betweenness centrality vertices in the road network are:')
    for i in range(20):
        max_node = betweenness.index(max(betweenness))
        print(max_node, end=',')
        betweenness[max_node] = -1