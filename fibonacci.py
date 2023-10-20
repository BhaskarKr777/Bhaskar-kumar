#for fibonacci series
def fibonacci(n):
    fib_series = [0, 1] 
    
    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2] 
        fib_series.append(next_term) 

    return fib_series

n = int(input("Enter the number of terms in the Fibonacci series: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(n)
    print("Fibonacci series with", n, "terms:")
    for number in result:
        print(number)
