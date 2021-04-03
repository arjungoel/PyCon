#!/usr/bin/env python3.9.0

def mygen():
    x = None
    while True:
        ''' it contradicts the statement that `yield` is a statement and it returns something to us. But here, yield has been used as an expression
        something that has a value that is returned to us '''
        x = yield x
        x *= 5


g = mygen()
print(next(g))  # prime it
print(g.send(10))
