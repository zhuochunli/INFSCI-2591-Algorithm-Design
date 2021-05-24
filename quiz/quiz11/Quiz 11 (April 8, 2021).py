def knapsack3(w, p, w_max):
    n = len(w)
    max_profit = 0
    number_visit = 1  # the number of nodes before finding the optimal solution

    def insert(s):  # s = [level, profit, weight, bound_value]
        m = len(queue)

        def _insert(low, high):
            if high >= low:
                mid = int((low+high)/2)
                if s[3] <= queue[mid][3]:
                    _insert(mid+1, high)
                else:
                    _insert(low, mid-1)
            else:
                queue.insert(low, s)
        _insert(0, m-1)

    def bound(lev, prof, wei):
        if wei >= w_max:
            return 0
        else:
            expect_profit = prof
            j = lev + 1
            total_weight = wei
            while j < n:
                if total_weight + w[j] <= w_max:
                    total_weight = total_weight + w[j]
                    expect_profit = expect_profit + p[j]
                    j += 1
                else:
                    break
            if j < n:
                expect_profit = expect_profit + (w_max - total_weight)*p[j]/w[j]
            return expect_profit

    queue = [[-1, 0, 0, bound(-1, 0, 0)]]  # initial a queue with root. level, profit, weight, bound
    while queue:
        if queue[0][3] > max_profit:   # queue[0][3] means bound
            number_visit = number_visit+2  # visit all its children, 2
            level1 = queue[0][0] + 1
            profit1 = queue[0][1] + p[level1]  # lchild: pick the next item
            weight1 = queue[0][2] + w[level1]
            bound_value1 = bound(level1, profit1, weight1)
            if (profit1 > max_profit) & (weight1 <= w_max):
                max_profit = profit1
            profit2 = queue[0][1]  # rchild: doesn't pick the next item
            weight2 = queue[0][2]
            bound_value2 = bound(level1, profit2, weight2)
            del queue[0]  # pop out the parent node
            if bound_value1 > max_profit:
                insert([level1, profit1, weight1, bound_value1])
            if bound_value2 > max_profit:
                insert([level1, profit2, weight2, bound_value2])
        else:
            del queue[0]

    return max_profit, number_visit


if __name__ == '__main__':
    max_profit, number_nodes = knapsack3([2, 5, 7, 3, 1], [20, 30, 35, 12, 3], 13)
    print('The max profit is:', max_profit)
    print('The number of nodes it visits before finding the optimal solution:', number_nodes)