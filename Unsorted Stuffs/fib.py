# O(n) time and space complexity
# Normally a fib sequence like this would have a O(2^n) time complexity and O(n) space complexity
# However, since we've implemented memoization by storing previous solutions into a dictionary, we can save time complexity by reusing those previous solutions



def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))