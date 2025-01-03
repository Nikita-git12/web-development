#Fibonacci Series with Recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 10
print([fibonacci_recursive(i) for i in range(n)])


#Fibonacci Series with Memoization
def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

n = 10
print([fibonacci_memo(i) for i in range(n)])


#Fibonacci Series with Tabulation
def fibonacci_tabulation(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

n = 10
print([fibonacci_tabulation(i) for i in range(n)])


#Fibonacci Series with Space Optimization
def fibonacci_optimized(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = 10
print([fibonacci_optimized(i) for i in range(n)])

#Fibonacci Numbers Modulo
def fibonacci_mod(n, mod):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % mod
    return b

n = 10
mod = 1000000007
print([fibonacci_mod(i, mod) for i in range(n)])
