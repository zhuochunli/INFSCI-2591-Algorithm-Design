import pandas as pd
_ = inf = 999999  # inf


def tsp2(matrix):
    def get_complement(s1, s2):  # get the set of s2-s1, return a list
        s = []
        for item in s2:
            if item not in s1:
                s.append(item)
        return s

    def length(path):  # return the length of a path
        sum = 0
        for i in range(len(path)-1):
            sum = sum+matrix[path[i]][path[i+1]]
        return sum

    def min_bound(queue):  # find the node with the smallest bound
        min = inf
        min_index = 0
        for item_index in range(len(queue)):
            if queue[item_index][2] < min:
                min = queue[item_index][2]
                min_index = item_index
        return min_index

    def bound(path):
        b1 = length(path)
        others_point = get_complement(path, all_nodes)
        b2 = min([matrix[path[-1]][j] for j in others_point])
        b3 = 0
        for i in others_point:
            s = []
            for j in others_point:
                if i != j:
                    s.append(matrix[i][j])
            b3 = b3 + min(min(s), matrix[i][0])
        return b1 + b2 + b3

    all_nodes = list(range(n))
    pq = [[0, [0], bound([0])]]  # a queue[level, path, bound]
    opttour = []  # the optimal path
    minlen = inf  # the minimum length
    while pq:
        min_bound_index = min_bound(pq)
        level1, path1, bound1 = pq[min_bound_index]
        pq.pop(min_bound_index)  # find the node with smallest bound and pop it
        if bound1 < minlen:  # if this node is promising
            level2 = level1+1  # expand the node, next level
            for i in range(1, n):  # generate all its children, except the start node 0
                if i not in path1:
                    path2 = path1+[i]
                    if level2 == n-2:  # already reach the leaf, the final node is determined
                        path2.extend(get_complement(path2, all_nodes))  # put [the last remaining node] at the end
                        path2.append(0)  # then put start node at the end
                        if length(path2) < minlen:
                            minlen = length(path2)
                            opttour = path2
                    else:
                        if bound(path2) < minlen:  # if has not reached the leaf and the node is promising, in queue
                            pq.append([level2, path2, bound(path2)])

    return opttour, minlen


def tsp1(array):
    def get_complement(s1, s2):  # get the set of s2-s1, return a list
        s = []
        for item in s2:
            if item not in s1:
                s.append(item)
        return s

    def distance(m, n):  # return the distance between node m and node n
        if m == n:
            return inf
        elif m < n:
            return array[int((n*(n-1))/2+m)]
        else:
            return array[int((m*(m-1))/2+n)]

    def length(path):  # return the length of a path
        sum = 0
        for i in range(len(path)-1):
            sum = sum+distance(path[i], path[i+1])
        return sum

    def min_bound(queue):  # find the node with the smallest bound
        min = inf
        min_index = 0
        for item_index in range(len(queue)):
            if queue[item_index][2] < min:
                min = queue[item_index][2]
                min_index = item_index
        return min_index

    def bound(path):
        b1 = length(path)
        others_point = get_complement(path, all_nodes)
        b2 = min([distance(path[-1], j) for j in others_point])
        b3 = 0
        for i in others_point:
            s = []
            for j in others_point:
                if i != j:
                    s.append(distance(i, j))
            b3 = b3 + min(min(s), distance(i, 0))
        return b1 + b2 + b3

    all_nodes = list(range(n))
    pq = [[0, [0], bound([0])]]  # a queue[level, path, bound]
    opttour = []  # the optimal path
    minlen = inf  # the minimum length
    while pq:
        min_bound_index = min_bound(pq)
        level1, path1, bound1 = pq[min_bound_index]
        pq.pop(min_bound_index)  # find the node with smallest bound and pop it
        if bound1 < minlen:  # if this node is promising
            level2 = level1+1  # expand the node, next level
            for i in range(1, n):  # generate all its children, except the start node 0
                if i not in path1:
                    path2 = path1+[i]
                    if level2 == n-2:  # already reach the leaf, the final node is determined
                        path2.extend(get_complement(path2, all_nodes))  # put [the last remaining node] at the end
                        path2.append(0)  # then put start node at the end
                        if length(path2) < minlen:
                            minlen = length(path2)
                            opttour = path2
                    else:
                        if bound(path2) < minlen:  # if has not reached the leaf and the node is promising, in queue
                            pq.append([level2, path2, bound(path2)])

    return opttour, minlen


if __name__ == '__main__':
    data = pd.read_csv('E:/学习资料/Pitt/algorithm/project/project4/Project 4_Problem 2_InputData.csv',
                       usecols=[0, 1, 2])
    node1 = data['NodeID'].values
    node2 = data['ConnectedNodeID'].values
    dis = data['Distance'].values
    n = data['NodeID'].values[-1] + 1
    aj1 = [_]*(int((n*(n-1))/2))
    aj2 = [[_] * n for x in range(n)]
    for r in range(len(data)):
        aj2[node1[r]][node2[r]] = dis[r]
        if node1[r] > node2[r]:
            aj1[int((node1[r]*(node1[r]-1))/2+node2[r])] = dis[r]
    shortest_path, min_len = tsp1(aj1)
    # shortest_path, min_len = tsp2(aj2)
    print('The shortest path is:', shortest_path)
    print('The minimum distance is:', min_len)