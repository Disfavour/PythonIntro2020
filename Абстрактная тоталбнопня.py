a = input().strip().split()
b = bytes.fromhex(input())

Dict = {(): "ПABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИЙКЛМНЕОРСТУФХЦЧШЩЫЭЮЯ()[]+-*/%;.,>=<\"!:".encode('koi8-r')}
List = [[i, j] for i in a for j in a if i != j]


def bytes_analys(str2, code):
	str1 = str2
	cur = tuple(reversed(code))
	for i in range(0,len(cur),2):
		try:
			str1 = str1.decode(cur[i]).encode(cur[i+1])
		except:
			return None
	str1 = str1.decode('koi8-r')
	if str1[:4] == "ПРОЦ":
		return str1
	else:
		return None


def analys(param, Dict, List):
	for item in List:
		for key in tuple(Dict.keys()):
			value = Dict[key]
			if len(key) == param * 2:
				try:
					tmp = value.decode(item[0]).encode(item[1])
				except UnicodeDecodeError:
					pass
				except UnicodeEncodeError:
					pass
				else:
					Dict[tuple(list(key) + item)] = tmp
					if tmp[:1] == b[:1]:
						B = bytes_analys(b, tuple(list(key) + item))
						if B:
							print(B)
							return
	analys(param + 1, Dict, List)
	return


analys(0, Dict, List)
