#storing solutions of sub-problems to solve original problem

#memoization - caching and reusing previously computed resluts

#eg find the fibonacci number at a particular index of the sequence

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    else:
        return fibonacci(n - 1) + fibonacci(n -2)

#this is a naive solution recurively calculates each number in the sequence from scratch O(n^2)!!

memo = {0:0, 1:1}

def fibonacci_memoization(n):
    if n in memo.keys():
        return memo[n]
    
    else:
        memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
        return memo[n]

#Tabulation: bottom up approach

def fibonacci_tabulation(n):
    if n == 0:
        return n

    #pre-initalize array
    f = [0] * (n + 1) #to the length of n
    f[1] = 1  # sets index 1 to 1 bc above array is [0, 0 ...n]

    for i in range(2, n + 1):
        f[i] = f[i -1] + f[i -2]
    return f[n]
