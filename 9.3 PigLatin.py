from re import *


notletter = compile(r"([^a-zA-Z']+)")
sogl = compile(r"[^aouieAOUIE]+")
soglglasn = compile(r"([^aouie]+)([aouie]+.*)")
glasnsoglslasn = compile(r"[aouie][^aouie]*[aouie]")
glasnsogld = compile(r"([aouie][^aouie]*)(.+)")
glasnsogl = compile(r"([aouie][^aouie]*)")


def analyze(a):
    ans = []
    for item in notletter.split(a):
        if item:
            if notletter.search(item):
                ans.append(item)
            else:
                if sogl.match(item):
                    if item[0].isupper():
                        tmp = soglglasn.sub(r"\2\1ay", item.lower())
                        ans.append(tmp[0].upper() + tmp[1:])
                    else:
                        ans.append(soglglasn.sub(r"\2\1ay", item))
                else:
                    if item[0].isupper():
                        item = item.lower()
                        if glasnsoglslasn.search(item):
                            tmp = glasnsogld.sub(r"\2\1ay", item)
                            ans.append(tmp[0].upper() + tmp[1:])
                        else:
                            tmp = glasnsogl.sub(r"\1yay", item)
                            ans.append(tmp[0].upper() + tmp[1:])
                    else:
                        if glasnsoglslasn.search(item):
                            ans.append(glasnsogld.sub(r"\2\1ay", item))
                        else:
                            ans.append(glasnsogl.sub(r"\1yay", item))
    return "".join(ans)


a = input()
while a:
    print(analyze(a))
    a = input()
