from re import *


dh = globals()
d = {}
base_mistake = compile(r'/{2,}|\*\*|[a-zA-Z0-9]\w*\(|\.|([^0-9A-Za-z_](\d)+[eE][+-]\d)') #([^0-9A-Za-z_](\d)+[eE][+-]\d)   \d[eE][+-]?\d
name_for_sub = compile(r"(?<!\w)([a-zA-Z_]\w*)")
name_for_match = compile(r"([a-zA-Z_]\w*)\s*=\s*(.*)")
splitting_match = compile(r"([a-zA-Z_]\w*)\s*=\s*(.*)")


def analyze(f):
    if match(r"#", f) is None:


        if base_mistake.search(f):
            print("Syntax error")
            return

        f = sub(r"/", r"//", f)
        #print(f)
        f = name_for_sub.sub(r"_c_\1", f)
        #print(f)



        if name_for_sub.fullmatch(f):
            try:
                print(eval(f, dh, d))
            except NameError:
                print("Name error")
                return
            else:
                return


        elif name_for_match.match(f):
            s = splitting_match.match(f)
            left = s.group(1)
            right = s.group(2)
            #print(left, right)

            try:
                right = eval(right, dh, d)
                #print(right)
            except NameError:
                print("Name error")
                return
            except SyntaxError:
                print("Syntax error")
            else:
                try:
                    exec(left + "=" + str(right), dh, d)
                except SyntaxError:
                    print("Syntax error")
                    return
                else:
                    return


        else:
            if search(r"=", f):
                print("Assignment error")
                return
            try:
                print(eval(f, dh, d))
            except NameError:
                print("Name error")
                return
            except SyntaxError:
                print("Syntax error")
                return
            except:
                print("Runtime error")
                return
            else:
                return




a = input()
while a:
    analyze(a)
    a = input()
