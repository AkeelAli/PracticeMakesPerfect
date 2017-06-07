# NOTES
# The rows are the coins used
# The subproblems are => with coin x or without coin x
# Return cell [-1][-1] for result sought
def num_combinations(change, coins):
    # init cache table
    #               0 1 2 3 4 ... change
    # coins 0     : 1 0 0 0 0 ... 0
    # coins 0,1   : 1 0 0 0 0 ... 0
    # coins 0,1,2 : 1 0 0 0 0 ... 0
    # ...
    #
    cache = [([1] + [0]*change) #single row
                for _ in range(len(coins))]
    
    for x in range(len(coins)):
        for y in range(1,change+1):
            combinations_without_last_coin = cache[x-1][y] if x != 0 else 0
            combinations_with_last_coin = cache[x][y-coins[x]]

            cache[x][y] = combinations_without_last_coin + \
                            combinations_with_last_coin

    #print cache

    return cache[-1][-1]

# NOTES
# recursive calls must loop over returned generator and yield each solution
def generate_combinations(change, coins, solution=[]):
    if change == 0:
        yield solution
    elif change < 0:
        pass
    elif coins == []:
        pass
    else:
        for s in generate_combinations(change, coins[:-1], solution):
            yield s
        for s in generate_combinations(change - coins[-1], coins, solution + [coins[-1]]):
            yield s
        

print num_combinations(12, [2,3,7])

for sol in generate_combinations(12, [2,3,7]):
    print sol
