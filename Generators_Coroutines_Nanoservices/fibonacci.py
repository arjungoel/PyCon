def fib():
    first = 0
    second = 1

    while True:
        yield first
        first, second = second, first + second


g = fib()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print(list(fib())) # The call to "list" will wait to get StopIteration which won't happen ever
