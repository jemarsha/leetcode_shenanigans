import sys

#dynamic programming way
def min_change_dynamic(coins, m, V):
    table = [V] * (V + 1)

    table[0] = 0

    # table = [0 for i in range(V + 1)]

    # Base case (If given value V is 0)
    # table[0] = 0

    # Initialize all table values as Infinite
    # for i in range(1, V + 1):
    #   table[i] = sys.maxsize
    for i in range(1, V + 1):

        for j in range(m):

            if (coins[j] <= i):
                print(coins[j])
                sub = table[i - coins[j]]

                if (sub != V and sub + 1 < table[i]):
                    table[i] = (sub + 1)

    return table[V]

#REcursive way
def coin_change(coins, amount: int):
    """Function for generating coin change."""
    if amount < 1:
        return 0
    return coin_change_recur(coins, amount, [0]*amount)


def coin_change_recur(coins, rem, count):
    if rem < 0:
        return -1
    if rem == 0:
        return 0
    if count[rem - 1] != 0:
        return count[rem - 1]
    min_val = float("inf")
    for coin in coins:
        res = coin_change_recur(coins, rem - coin, count)
        if res >= 0 and res < min_val:
            min_val = 1 + res
    if min_val == float("inf"):
        count[rem - 1] = -1
    else:
        count[rem - 1] = min_val
    return count[rem - 1]