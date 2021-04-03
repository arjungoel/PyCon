import dis


def my_gen():
    yield 1
    yield 2
    yield 3


print(my_gen())

# The use of "yield" turns a regular function into a generator function.
# When python compiles your function, it notices the "yield" and tags the function as a generator function.
# Running a "generator function" returns a "generator".

dis.show_code(my_gen)

# show_code() is a function that summarizes all the hints that python leaves for itself in the function object.

g = my_gen()

print(g)
print(iter(g))  # generator is its own iterator (manual way)
