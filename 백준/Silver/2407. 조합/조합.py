n, m = list(map(int, input().split()))

def factorial(n):
    if (n <= 1): return 1
    return n * factorial(n-1)

print(int(factorial(n) // (factorial(m) * factorial(n - m))))