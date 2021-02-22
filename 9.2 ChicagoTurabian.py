from re import *


def analyze(n, b):
    if not(n and b):
        print(False)
        return

    n = n.groupdict()
    b = b.groupdict()

    if n["title"] == b["title"] and n["city"] == b["city"] and n["publisher"] == b["publisher"] and n["date"] == b["date"]:
        if b["author4"]:
            if n["author41"] == b["author11"] and n["author42"] == b["author12"]:
                print(True)
                return
            else:
                print(False)
                return

        elif b["author3"]:
            if b["author3"] == n["author3"] and b["author2"] == n["author2"] and n["author11"] == b["author11"] and n["author12"] == b["author12"]:
                print(True)
                return
            else:
                print(False)
                return

        elif b["author2"]:
            if b["author2"] == n["author22"] and n["author211"] == b["author11"] and n["author212"] == b["author12"]:
                print(True)
                return
            else:
                print(False)
                return

        else:
            if (n["author11"] == b["author11"] or n["author11"] == b["author11"] + ".") and n["author12"] == b["author12"]:
                print(True)
                return
            else:
                print(False)
                return

    else:
        print(False)
        return

prefix = r"\d+\.\s"
author = r"(?:" + r"(?P<author41>.+)\s(?P<author42>[^\s,]+)\set\sal\." + r"|" + r"(?P<author211>[^,]+)\s(?P<author212>\S+)\sand\s(?P<author22>[^,]+)" + r"|" + r"(?P<author11>[^,]+)\s(?P<author12>[^\s,]+)" + r"(?:(?:(?:,\s(?P<author3>.+),)?\sand\s(?P<author2>[^,]+)))?" + r")" + r",\s"
title = r"(?P<title>.+)\s\("
city = r"(?P<city>.+):\s"
publisher = r"(?P<publisher>.+),\s"
date = r"(?P<date>\d+)\),\s"
page = r"(?:(?:\d+|\d+–\d+))\."
Ntemplate = prefix + author + title + city + publisher + date + page

authorB = r"(?P<author12>\S+),\s(?P<author11>[^,]+)(?:,(?:\s(?P<author3>[^,]+),)?(?:\s(?P<author4>[^,]+),)*\sand\s(?P<author2>[^\d]+))?" + r"\.\s"
titleB = r"(?P<title>.+)\.\s"
cityB = r"(?P<city>.+):\s"
publisherB = r"(?P<publisher>.+),\s"
dateB = r"(?P<date>\d+)\."
Btemplate = authorB + titleB + cityB + publisherB + dateB

N, B = input(), input()

n = search(Ntemplate, N)
b = search(Btemplate, B)

analyze(n, b)
