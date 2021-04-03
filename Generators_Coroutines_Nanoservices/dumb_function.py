# dumbest python function
import dis


def myfunc():
    return 1
    return 2
    return 3


print(myfunc())

dis.dis(myfunc)

# "return" means: stop the function, and return a value
# "pylint" warns us that the final lines are unreachable
# Even Python's byte compiler ignores the final two lines
