from collections import UserString

class SubString(UserString):
    def __sub__(self, other):
        d = {}
        #f = other.data if type(other) == SubString else other
        if type(other) == SubString:
            f = other.data
        else:
            f = other

        for item in f:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        ans = []
        for item in self.data:
            if item in d and d[item] > 0:
                d[item] -= 1
            else:
                ans.append(item)
        return self.__class__("".join(ans))

del UserString
#print(SubString("qwertyerty")-SubString("ttttr"))