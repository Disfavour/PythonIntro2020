def find_end(string, substring, index):
    #print("find3", substring, string)
    return substring == "".join(string[index::index + 1])[:len(substring)]


def find_second(string, substring):
    #print("find2", substring, string)
    index = string.find(substring[0])
    if index >= 0:
        new_string = string[index + 1:]
        if find_end(new_string, substring[1:], index):
            return True
        else:
            return find_second(new_string, substring)
    else:
        return False


def find(string, substring):
    #print("find", substring, string)
    index = string.find(substring[0])
    if index >= 0:
        new_string = string[index + 1:]
        if find_second(new_string, substring[1:]):
            return True
        else:
            return find(new_string, substring)
    else:
        return False


string = input()
substring = input()
y = "YES"
n = "NO"

if len(substring) > len(string):
    print(n)
else:
    if len(substring) <= 1:
        if not len(substring):
            print(y)
        elif substring in string:
            print(y)
        else:
            print(n)
    else:
        if find(string, substring):
            print(y)
        else:
            print(n)
