
def fibonacci_of(n):
    if n in {0, 1}:
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

def sum_series(n, first=0, second=1):
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)


def test_fibonacci():
    assert fibonacci_of(0) == 0
    assert fibonacci_of(1) == 1
    assert fibonacci_of(2) == 1
    assert fibonacci_of(3) == 2
    assert fibonacci_of(4) == 3

def test_lucas():
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7

def test_sum_series():
    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(2) == 1
    assert sum_series(3) == 2
    assert sum_series(4) == 3

if __name__ == "__main__":
    test_fibonacci()
    test_lucas()
    test_sum_series()
    print("All tests passed!")
