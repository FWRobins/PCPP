"""
Imagine you’ve been given a task to clean up the code of a system developed in Python – the code should be treated as legacy code;
the system was created by a group of volunteers who worked with no clear “clean coding” rules;
the system suffers from a problem: we don’t know in which order the classes are created, so it causes multiple dependency problems;
your task is to prepare a metaclass that is responsible for:
equipping all newly instantiated classes with time stamps, persisted in a class attribute named instantiation_time;
equipping all newly instantiated classes with the get_instantiation_time() method. The method should return the value of the class attribute instantiation_time.
* The metaclass should have its own class variable (a list) that contains a list of the names of the classes instantiated by the metaclass (tip: append the class name in the __new__ method).

Your metaclass should be used to create a few distinct legacy classes;
create objects based on the classes;
list the class names that are instantiated by your metaclass.
"""
import datetime

def get_instantiation_time(self):
    print(self.instantiation_time)

class time_meta(type):
    classes_instantiated = []
    def __new__(mcs, name, bases, dictionary):
        if 'instantiation_time' not in dictionary:
            dictionary['instantiation_time'] = datetime.datetime.now()
        dictionary['get_instantiation_time'] = get_instantiation_time
        mcs.classes_instantiated.append(name)
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj

class first_class(metaclass=time_meta):
    pass

class second_class(metaclass=time_meta):
    pass

class1 = first_class()
class1.get_instantiation_time()

class2 = second_class()
class2.get_instantiation_time()

class3 = first_class()
class3.get_instantiation_time()

print(time_meta.classes_instantiated)
