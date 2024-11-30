import time


def fib_loop(n):
    fib1 = 1
    fib2 = 1

    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2

def fib_array(n):
    fib1 = 1
    fib2 = 1
    container = []

    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        
        # Запись в массив
        container.append(fib2)

        i = i + 1
    return container

def fib_recursive(n):
    if n in (1, 2):
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

