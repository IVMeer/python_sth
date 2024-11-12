def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# n = 10
# print(fibonacci(n))
for i in range(10):
    print(fibonacci(i), end=' ')