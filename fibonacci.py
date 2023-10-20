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

# Input the number of terms you want in the Fibonacci sequence
n = int(input("Enter the number of Fibonacci terms: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(n)
    print("Fibonacci sequence up to", n, "terms:")
    print(result)
