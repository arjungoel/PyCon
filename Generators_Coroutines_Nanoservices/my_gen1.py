#!/usr/bin/env python3.9.0

def mygen():
    x = None
    # using walrus operator (PEP 572)
    while x := (yield x):   # exit the loop when we get `None` or an `empty value`
        x *= 5


g = mygen()
print(next(g))  # prime it
print(g.send(10))
