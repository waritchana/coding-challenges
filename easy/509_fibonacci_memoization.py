def fib(n: int) -> int:
    saved_fib = {}
    def recursion_fib (n):
        if n in saved_fib:
            return saved_fib[n]
        if n == 0 or n == 1:
            fib = n
        else:
            fib = recursion_fib(n-1) + recursion_fib(n-2)
        saved_fib[n] = fib
        return fib

    return recursion_fib(n)


print("Fibonacci of 4 is", fib(4))
