def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


print("Fibonacci of 4 is", fib(4))
