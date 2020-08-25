class MyObject:
    pass

# This is Old stuff but it is powerful


class Probe:
    def __getattr__(self, attr):
        ret = "__getattr__(%s)" % attr
        print("called __getattr__")
        if attr == 'r':
            return ret
        raise AttributeError

    def __setattr__(self, attr, value):
        print("called __setattr__")

    def __getattribute__(self, attr):
        print("__getattribute__(%s)" % attr)
        return 'Anyvar'


# 4. self.__class__.__getattr__(self, attr)
p = Probe()
print("print p before set", p.r, "called")

p.r = 3
print("print p after set", p.r, "access is direct")

# 5. self.__class__.__setattr__(self, value, attr)
p = Probe()
p.t = 3
print(p.__dict__)

# 6. self.__class__.__getattribute__(self, attr)
p = Probe()
print("print p before set", p.s)

p.s = "hello"
print("print p after set", p.s)


class ProbeND:
    def __get__(self, obj, type=None):
        ret = '__get__(%s,%s)' % (obj, type)


# 7. self.__class__.__dict__[attr].__get__(self,cls)
o = MyObject()
MyObject.z = ProbeND()  # adding to __class__.__dict__
print(o)
o.__dict__['z'] = None
print(o.z)
