# Steps:
# Recursion -> Recursion +  DP -> Iterative DP -> Iterative DP Space Optimized

def ks(values, weights, capacity, index):
    if capacity <= 0 or index >= len(weights):
        return 0

    profit1 = 0
    if weights[index] <= capacity:
        profit1 = values[index] + ks(values, weights, capacity-weights[index], index+1)

    profit2 = ks(values, weights, capacity, index+1)

    return max(profit1, profit2)

def ksDP(values, weights, capacity, index, dp): # dp = (index, capacity)
    if capacity <= 0 or index >= len(weights):
        return 0

    if dp[index][capacity]:
        return dp[index][capacity]

    profit1 = 0
    if weights[index] <= capacity:
        profit1 = values[index] + ksDP(values, weights, capacity-weights[index], index+1, dp)

    profit2 = ksDP(values, weights, capacity, index+1, dp)

    dp[index][capacity] = max(profit1, profit2)
    return dp[index][capacity]

def ksItr(values, weights, capacity):
    if capacity <= 0 or len(weights) == 0 or len(weights) != len(values):
        return 0
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(weights))]

    # capacity = 0
    for i in range(len(weights)):
        dp[i][0] = 0
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # fill the dp array
    n = len(weights)

    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1 = 0
            if weights[i] <= c:
                profit1 = values[i] + dp[i-1][c-weights[i]]

            profit2 = dp[i-1][c]
            dp[i][c] = max(profit1, profit2)

    # final ans
    return dp[n-1][capacity]
