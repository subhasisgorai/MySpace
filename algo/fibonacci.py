

def fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fibonacci(n - 1)
        return (a + b, a)


def fibonacci_series():
    a = 0
    b = 1
    while True:
        yield a
        future = a + b
        a = b
        b = future


if __name__ == '__main__':
    print fibonacci(6)
    
    fibonacci_series = fibonacci_series()
    for i in range(10):
        print next(fibonacci_series),
