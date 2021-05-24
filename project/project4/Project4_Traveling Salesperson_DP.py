import pandas as pd
_ = inf = 999999  # inf

# To test whether the i-th position of a decimal number x is 1 or not: (((x >> (i - 1) ) & 1) == 1
# 5 = 101, (((5 >> (2 - 1) ) & 1)==1, False
# dp[0][{1,3}]=dp[0][101]=dp[0][5]; dp[0][{1,2,3}]=dp[0][111]=dp[0][7]


def tsp2(matrix):  # assume the start node is node 0
    n = len(matrix)
    dp = [[_]*(2**(n-1)) for x in range(n)]  # dp matrix, n x 2^(n-1), use binary to represent all subsets
    for i in range(n):  # fill in the first column dp[][0]
        dp[i][0] = matrix[i][0]  # from node i to start node directly, without passing any other node

    for j in range(1, 2**(n-1)):  # fill in the other columns except dp[][0] in dp
        for i in range(n):  # for every row
            if i != 0 and ((j >> (i-1)) & 1) == 1:  # if already reached node.Eg: dp[1][{1,3}], no w[3][1]+dp[1][{1}]
                continue
            for k in range(1, n):  # try every other nodes, see whether can go to node k first
                if ((j >> (k-1)) & 1) == 0:  # can't reach node k first
                    continue
                # dp[0][{1, 2, 3}] = min{C01 + dp[1][{2, 3}] ，C02 + dp[2][{1, 3}] ，C03 + dp[3][{1, 2}]}
                if dp[i][j] > matrix[i][k] + dp[k][j ^ (1 << (k-1))]:
                    dp[i][j] = matrix[i][k] + dp[k][j ^ (1 << (k-1))]
        print(2**(n-1)-j)
    return dp[0][2**(n-1)-1]


def tsp1(array):  # assume the start node is node 0
    dp = [[_]*(2**(n-1)) for x in range(n)]  # dp matrix, n x 2^(n-1), use binary to represent all subsets
    for i in range(n):  # fill in the first column dp[][0]
        if i == 0:  # array doesn't store matrix[i][i]
            dp[0][0] = inf
        else:
            dp[i][0] = array[int((i*(i-1))/2+0)]  # from node i to start node, without passing any other nodes

    for j in range(1, 2**(n-1)):  # fill in the other columns except dp[][0] in dp
        for i in range(n):  # for every row
            if i != 0 and ((j >> (i-1)) & 1) == 1:  # if already reached node.Eg: dp[1][{1,3}], no w[3][1]+dp[1][{1}]
                continue
            for k in range(1, n):  # try every other nodes, see whether can go to node k first
                if ((j >> (k-1)) & 1) == 0:  # can't reach node k first
                    continue
                if i == k:
                    dis = inf
                elif i < k:
                    dis = array[int((k*(k-1))/2+i)]
                else: dis = array[int((i*(i-1))/2+k)]
                # dp[0][{1, 2, 3}] = min{C01 + dp[1][{2, 3}] ，C02 + dp[2][{1, 3}] ，C03 + dp[3][{1, 2}]}
                if dp[i][j] > dis + dp[k][j ^ (1 << (k-1))]:
                    dp[i][j] = dis + dp[k][j ^ (1 << (k-1))]
        print(2**(n-1)-j)
    return dp[0][2**(n-1)-1]


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
    # aj=[[inf,10,15,inf],[10,inf,35,25],[15,35,inf,30],[inf,25,30,inf]]
    # aj=[10,15,35,inf,25,30]
    print('The minimum distance is:', tsp2(aj2))
    print('The minimum distance is:', tsp1(aj1))