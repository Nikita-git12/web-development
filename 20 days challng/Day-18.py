#LCS Using Tabulation (Bottom-Up Approach)
def lcs_tabulation(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS (Tabulation):", lcs_tabulation(X, Y))


#LCS Using Memoization (Top-Down Approach)
def lcs_memoization(X, Y, m, n, memo):
    if m == 0 or n == 0:
        return 0
    if memo[m][n] is not None:
        return memo[m][n]

    if X[m - 1] == Y[n - 1]:
        memo[m][n] = 1 + lcs_memoization(X, Y, m - 1, n - 1, memo)
    else:
        memo[m][n] = max(lcs_memoization(X, Y, m - 1, n, memo), lcs_memoization(X, Y, m, n - 1, memo))

    return memo[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
m, n = len(X), len(Y)
memo = [[None] * (n + 1) for _ in range(m + 1)]
print("Length of LCS (Memoization):", lcs_memoization(X, Y, m, n, memo))


#Print LCS Using Tabulation
def print_lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

X = "AGGTAB"
Y = "GXTXAYB"
print("LCS String:", print_lcs(X, Y))

#Space-Optimized LCS (For Length Only)
def lcs_space_optimized(X, Y):
    m, n = len(X), len(Y)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, [0] * (n + 1)

    return prev[n]

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS (Space Optimized):", lcs_space_optimized(X, Y))
