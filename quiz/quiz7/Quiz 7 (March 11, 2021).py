import pandas as pd
_ = inf = 999999  # inf


class Node(object):
    def __init__(self, vertex, edge):
        self.vertex = vertex
        self.edge = edge
        self.next = None


def distances(i, j, llist):
    head = llist[i]
    p = head.next
    while p:
        if p.vertex == j:
            return p.edge
        else:
            p = p.next
    return inf


def prim(llist):
    v_near=0
    total = 0
    n = len(llist)
    nearest = [0]*n
    distance = [-1]*n
    k = n-1
    for i in range(1, n):
        nearest[i] = 0
        distance[i] = distances(0, i, llist)
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
            if distances(j, v_near, llist) < distance[j]:
                distance[j] = distances(j, v_near, llist)
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
    vertex_llist = []
    pre = -1
    for r in range(len(data)):
        v = node1[r]
        if v != pre:
            head = Node(v, 0)  # edge for vertex itslef is set to 0
            vertex_llist.append(head)
            ajv = Node(node2[r], dis[r])
            head.next = ajv
            tail = ajv
        elif v == pre:
            curr = Node(node2[r], dis[r])
            tail.next = curr
            tail = curr
        pre = v
    print('The total distance in the minimum-spanning tree is:', prim(vertex_llist))