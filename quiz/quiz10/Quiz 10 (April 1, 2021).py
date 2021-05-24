def knapsack(w, p, W):
    n = len(w)
    max_profit = [0]
    best_set = [[]]
    include = ['no']*n

    def _promising(i, profit, weight):
        if weight >= W:
            return False
        else:
            total_weight = weight
            bound = profit
            j = i+1

            while j < n:
                if total_weight + w[j] <= W:
                    total_weight = total_weight + w[j]
                    bound = bound + p[j]
                else:
                    break
                j = j+1
            if j < n:
                bound = bound + (W - total_weight)*p[j]/w[j]
            return bound > max_profit[0]

    def _knapsack(i, profit, weight):
        if(weight <= W) & (profit > max_profit[0]):
            max_profit[0] = profit
            best_set[0] = include[:]
        if _promising(i, profit, weight):
            include[i+1] = 'yes'
            _knapsack(i+1, profit + p[i+1], weight + w[i+1])
            include[i+1] = 'no'
            _knapsack(i + 1, profit, weight)
    _knapsack(-1, 0, 0)
    return max_profit[0], best_set[0]


if __name__ == '__main__':
    max_profit,best_set=knapsack([2, 5, 7, 3, 1], [20, 30, 35, 12, 3], 9)
    print('Max profit is:', max_profit)
    print('The best set for each item:', best_set)