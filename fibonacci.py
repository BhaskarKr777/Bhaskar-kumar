def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib

n = int(input("Enter number:- "))

if n <= 0:
    print("Enter positive number.")
else:
    result = fibonacci(n)
    print("Fibonacci number of ", n, "terms:")
    print(result)
