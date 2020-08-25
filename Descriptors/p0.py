# 1. self.__dict__[key]

class MyObject:
    pass


o = MyObject()
o.__dict__['x'] = 3
print(o.__dict__)
print(o.x)

###################################################################################################################################################################

# 2. self.__class__.__dict__[key]


class BaseObject:
    pass


class MyObject(BaseObject):
    pass


o = MyObject()
MyObject.y = 4
print(o.__class__.__dict__)
print(o.y)

#######################################################################################################################################################################

# 3. self.__class__{BaseClasses}__dict__[key]

o = MyObject()
BaseObject.t = 4
print(o.__class__.__dict__)
print(o.__class__.__bases__[0].__dict__)
print(o.t)
