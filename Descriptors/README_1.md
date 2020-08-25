__setattr__ is built into python and allows us to customize the storage of different attributes on a class. This is called whenever we try to set an instance variable and it's going to take the instance object itself, the attribute name that we are trying to set and thenthe value we are trying to set for this attribute.

__setattr__(self, attr, value)

property is actually implemented as a descriptor however it is an astraction that doesn't provide anything that a descriptor could.
