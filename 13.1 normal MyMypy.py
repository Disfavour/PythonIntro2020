from types import FunctionType
from functools import wraps
import inspect
import re


pref = re.compile(r"__")


def analyze(d):
    for name, item in d.items():
        if item[1].kind == item[1].POSITIONAL_OR_KEYWORD:
            print("POSITIONAL_OR_KEYWORD", name, item)
            if not isinstance(item[0], item[1].annotation):
                raise TypeError(f"Type mismatch: {name}")

    for name, item in d.items():
        if item[1].kind == item[1].KEYWORD_ONLY:
            #print("KEYWORD_ONLY", name, item)
            if not isinstance(item[0], item[1].annotation):
                raise TypeError(f"Type mismatch: {name}")

    for name, item in d.items():
        if item[1].kind == item[1].VAR_POSITIONAL:
            #print("VAR_POSITIONAL", name, item)

            for i in item[0]:
                if not isinstance(i, item[1].annotation):
                    raise TypeError(f"Type mismatch: {name}")

            #if not isinstance(item[0], item[1].annotation):
            #    raise TypeError(f"Type mismatch: {name}")

    for name, item in d.items():
        if item[1].kind == item[1].VAR_KEYWORD:
            #print("VAR_KEYWORD", name, item)

            for i in item[0].values():
                if not isinstance(i, item[1].annotation):
                    raise TypeError(f"Type mismatch: {name}")

            #if not isinstance(item[0], item[1].annotation):
            #    raise TypeError(f"Type mismatch: {name}")


def checker(fun, name):
    @wraps(fun)
    def newf(self, *args, **kwargs):
        sig_obj = inspect.signature(fun)
        bind_obj = sig_obj.bind(self, *args, **kwargs)
        print(sig_obj)
        print(bind_obj)

        d = {}

        for key, value in bind_obj.arguments.items():
            #print(key, value, sig_obj.parameters[key])
            #print(sig_obj.parameters[key].annotation)
            if sig_obj.parameters[key].annotation is not sig_obj.empty:
                d[key] = [value, sig_obj.parameters[key]]

        #print(d)
        analyze(d)



        if sig_obj.return_annotation != sig_obj.empty:
            if not isinstance(fun(self, *args, **kwargs), sig_obj.return_annotation):
                raise TypeError(f"Type mismatch: return")

        return fun(self, *args, **kwargs)
    return newf


class checked(type):
    def __init__(self, name, parents, ns):
        for attr, obj in vars(self).items():
            if isinstance(obj, FunctionType) and not pref.match(attr):
                setattr(self, attr, checker(obj, attr))
        return super().__init__(name, parents, ns)


class E(metaclass=checked):
    def __init__(self, var: int):
        self.var = var if var % 2 else str(var)

    def mix(self, val: int, opt) -> int:
        return self.var * val + opt

    def al(self, c: int, d: int = 1, *e: int, f: int = 1, **g: int):
        return self.var * d


e1, e2 = E(1), E(2)
code = """
e1.al(1, f="E", d="1")
"""
"""
e1.al(1, d="E", f="1")
e1.al(1, e="E")
e1.al(1, g="E")
"""

for c in code.strip().split("\n"):
    try:
        res = eval(c)
    except TypeError as E:
        res = E
    print(f"Run: {c}\nGot: {res}")