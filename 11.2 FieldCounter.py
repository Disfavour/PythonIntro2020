from re import *

def Stat(*args):
    if len(args) == 1:
        klas = args[0]

        for key in tuple(vars(klas)):
            if match(r"_", key) is None and not callable(getattr(klas, key)):
            #    print("key", key)
                setattr(klas, "_read_" + key, 0)
                setattr(klas, "_write_" + key, 0)

        def my_getattr(self, name):

            try:
                exec("self." + "_read_" + name + "+= 1")
            #    if match(r"_", name) is None:
            #        print("setattr", name)
            except:
                pass

            return object.__getattribute__(self, name)


        def my_setattr(self, name, value):
            #if match(r"_", name) is None:
            #    print("setattr", name)

            try:
                exec("self." + "_write_" + name + "+= 1")
            except:
                pass

            object.__setattr__(self, name, value)

        klas.__getattribute__ = my_getattr
        klas.__setattr__ = my_setattr

        return klas

    elif len(args) == 2:
        obj = args[0]
        pole = args[1]
        #print(pole, "_read_" + pole)
        try:
            return getattr(obj, "_read_" + pole), getattr(obj, "_write_" + pole)
        except AttributeError:
            return (0, 0)
