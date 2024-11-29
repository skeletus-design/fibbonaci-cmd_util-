import time


def cicle(n):
    fib1 = 1
    fib2 = 1

    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1

    return fib2



def recr(n):
    if n in (1, 2):
        return 1
    return recr(n - 1) + recr(n - 2)

