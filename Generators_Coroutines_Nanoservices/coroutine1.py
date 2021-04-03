import hashlib


def md5_gen():
    output = None

    while s := (yield output):
        m = hashlib.md5()  # md5 object
        m.update(s.encode())  # converting string into bytes
        output = m.hexdigest()


g = md5_gen()
""" it's going to run through the first yield that first yield is on the right-side of the assignment not on the left-side so the right-side is 
returned to us then it's waiting for us then we send the second thing is then going into the assignment and go into the while so the first thing
is actually never seen by the `while` """
print(g.send(None))  # prime it

print(g.send("hello"))
print(g.send("world"))

print(g.send(None))   # stop the service
