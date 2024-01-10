def fibonacci_of(n):
    if n in {0, 1}:  
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  

fibonacci_values = [fibonacci_of(n) for n in range(5)]
print(fibonacci_values)

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
    
    # series.py

def sum_series(n, first=0, second=1):
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)
