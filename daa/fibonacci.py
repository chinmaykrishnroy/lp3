# Iterative approach to print Fibonacci sequence up to n
def fibonacci_iterative(n: int):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        dp = [0] * n
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp

# Recursive approach to print Fibonacci sequence up to n
def fibonacci_recursive(n):
    cache = {1: 0, 2: 1}
    result = []
    for i in range(1, n+1):
        result.append(helper(i, cache))
    return result

def helper(n: int, cache):
    if n in cache:
        return cache[n]
    else:
        cache[n] = helper(n - 1, cache) + helper(n - 2, cache)
        return cache[n]

# Input from the user
n = int(input("Enter value of n (to print Fibonacci sequence up to n): "))
print(f"Fibonacci Sequence (Iterative): {fibonacci_iterative(n)}")
print(f"Fibonacci Sequence (Recursive): {fibonacci_recursive(n)}")
