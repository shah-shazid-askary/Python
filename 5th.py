def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

for i in range(1, 6):
    print(f"{i}! = {factorial(i)}")
