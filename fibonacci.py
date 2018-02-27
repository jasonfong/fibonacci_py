class FibonacciError(BaseException):
    pass


def fibonacci(n):
    if not isinstance(n, int):
        raise FibonacciError("Not an integer")
    if n < 0:
        raise FibonacciError("Negative value")

    hist = [None] * (n+1)
    return fibonacci_helper(n, hist)


def fibonacci_helper(n, hist):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if not hist[n]:
        hist[n] = fibonacci_helper(n-2, hist) + fibonacci_helper(n-1, hist)

    return hist[n]
