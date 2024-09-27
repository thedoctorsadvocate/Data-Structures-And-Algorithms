# Very similar to the fib, this will recursively call functions lessering the values each iteration
# We will also save time complexity by using memoization


def gridTravler(x, y, memo={}):
    m = str(x) + ',' + str(y)
    if m in memo:
        return memo[m]
    if x == 0 or y == 0:
        return 0
    if x == 1 or y == 1:
        return 1
    memo[m] = gridTravler(x - 1, y, memo) + gridTravler(y - 1, x, memo)
    return memo[m]

print(gridTravler(1, 1))
print(gridTravler(2, 3))
print(gridTravler(3, 2))
print(gridTravler(3, 3))
print(gridTravler(18, 18))