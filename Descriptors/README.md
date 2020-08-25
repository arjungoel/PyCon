Author: Andy Fundinger
Talks - PyCaribbean 2016, PyGotham 2017, EuroPython, PyCascades, and PyTennesssee
Technologies - Flask, Celery, pycsvw, Redis, Jena, Hadoop, Perl, C/C++, JavaScript


Descriptors have not changed since python 2.2 version.



1. Quietly sitting between an instance(o) and an attribute(x) (.) serves as syntactic sugar in place of getattr(o, 'x'). In the simplest case this reduces further to o.__dict__['x'] 
2. It could be a class attribute.
3. It could also come from parent class.


__getattr__() is called when there is not a definition when an attribute is not defined on the instance
__setattr__() lets us say if we are setting a value we will call this
__getattribute__() actually calls __getattr__(). __getattribute__() is actually looking what is found in the class __dict__ before it decides what to do when it's resolving what's in the class __dict__.
