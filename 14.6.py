import re


def collector(d1, d2, d3, slogaemoe1, slogaemoe2, summa):
    l = []
    for bukva in slogaemoe1:
        if bukva in d1:
            l.append(str(d1[bukva]))
        elif bukva in d2:
            l.append(str(d2[bukva]))
        elif bukva in d3:
            l.append(str(d3[bukva]))
        else:
            print("коллектор сломался")
    l.append("+")
    for bukva in slogaemoe2:
        if bukva in d1:
            l.append(str(d1[bukva]))
        elif bukva in d2:
            l.append(str(d2[bukva]))
        elif bukva in d3:
            l.append(str(d3[bukva]))
        else:
            print("коллектор сломался")
    l.append("=")
    for bukva in summa:
        if bukva in d1:
            l.append(str(d1[bukva]))
        elif bukva in d2:
            l.append(str(d2[bukva]))
        elif bukva in d3:
            l.append(str(d3[bukva]))
        else:
            print("коллектор сломался")
#    print("".join(l))
    return "".join(l)


def to_int(d, predp, word):
    ans = []
    for i in word:
        if i in d:
            ans.append(str(d[i]))
        elif i in predp:
            ans.append(str(predp[i]))
        else:
            print("problems with to_int", i, d, predp)
    return int("".join(ans))


def dict_sum(d1, d2, d3):
    #print(d1, d2, d3)
    d4 = {}
    for key, value in d1.items():
        d4[key] = value
    for key, value in d2.items():
        d4[key] = value
    for key, value in d3.items():
        d4[key] = value
    return d4


def full_in_d(seq, d):
    for i in seq:
        if i not in d:
            return False
    return True


def analyze(seq1, seq2, ans, d):
    #global num1, num2
    was = []
    predpoloj = {}
    gypotheza = {}

    #выбор буквы наименьшего разряда
    if not full_in_d(seq1, d) and not full_in_d(seq2, d):
        for num1, i in enumerate(seq1[::-1]):
            if i not in d:
                break
        for num2, i in enumerate(seq2[::-1]):
            if i not in d:
                break
        mladshiy = seq1[-1 - num1] if num1 <= num2 else seq2[-1 - num2]

    #2ое слово разгадано
    elif not full_in_d(seq1, d) and full_in_d(seq2, d):
        for num1, i in enumerate(seq1[::-1]):
            if i not in d:
                break
        mladshiy = seq1[-1 - num1]

    #1ое слово разгадано
    elif full_in_d(seq1, d) and not full_in_d(seq2, d):
        for num1, i in enumerate(seq2[::-1]):
            if i not in d:
                break
        mladshiy = seq2[-1 - num1]

    else:
        print("2 полных слова в начале функции")
        exit()

    if mladshiy == seq1[0] or mladshiy == seq2[0] or mladshiy == ans[0]:
        was.append(0)

    #цикл
    while True:
        print("new iter", d, predpoloj, was)

        #подстановка цифры
        counter = 0
        while counter < 10:
            if counter not in was and counter not in d.values():
                predpoloj[mladshiy] = counter
                was.append(counter)
                break
            counter += 1
        else:
            print("return")
            return

        print("предположение", predpoloj)
        #проверка на нарушение суммы (смотрим длины хвостов)
        tail_ans = 0
        for lenght in range(len(ans)):
            if (ans[::-1])[lenght] in d or (ans[::-1])[lenght] in predpoloj:
                tail_ans += 1
            else:
                break

        if not full_in_d(seq1, dict_sum(d, predpoloj, {})) and not full_in_d(seq2, dict_sum(d, predpoloj, {})):
            tail = 0
            for lenght in range(dlina):
                if ((seq1[::-1])[lenght] in d or (seq1[::-1])[lenght] in predpoloj) and ((seq2[::-1])[lenght] in d or (seq2[::-1])[lenght] in predpoloj):
                    tail += 1
                else:
                    break

        # 1ое слово разгадано
        elif full_in_d(seq1, dict_sum(d, predpoloj, {})) and not full_in_d(seq2, dict_sum(d, predpoloj, {})):
            tail = 0
            for bukva in seq2[::-1]:
                if bukva in d or bukva in predpoloj:
                    tail += 1
                else:
                    break

        # 2ое слово разгадано
        elif not full_in_d(seq1, dict_sum(d, predpoloj, {})) and full_in_d(seq2, dict_sum(d, predpoloj, {})):
            tail = 0
            for bukva in seq1[::-1]:
                if bukva in d or bukva in predpoloj:
                    tail += 1
                else:
                    break

        else:
            print("2 полных слова длина хвоста")
            tail = len(seq1)
            #exit()

        cur_tail = min(tail, tail_ans)

        if tail == 0:
            print("рекурсивный вызов0")
            analyze(seq1, seq2, ans, dict_sum(d, predpoloj, gypotheza))
            continue



        #если нарушает - новый оборот
        if cur_tail > 0:
            if not full_in_d(seq1, dict_sum(d, predpoloj, {})) and not full_in_d(seq2, dict_sum(d, predpoloj, {})):
                if (to_int(d, predpoloj, seq1[-cur_tail:]) + to_int(d, predpoloj, seq2[-cur_tail:])) % 10 ** cur_tail != to_int(d, predpoloj, ans[-cur_tail:]):
                    print("нарушает сумму")
                    continue

            # 2ое слово разгадано
            elif not full_in_d(seq1, dict_sum(d, predpoloj, {})) and full_in_d(seq2, dict_sum(d, predpoloj, {})):
                if cur_tail >= len(seq2):
                    if (to_int(d, predpoloj, seq1[-cur_tail:]) + to_int(d, predpoloj, seq2)) % 10 ** cur_tail != to_int(d, predpoloj, ans[-cur_tail:]):
                        print("нарушает сумму")
                        continue
                else:
                    if (to_int(d, predpoloj, seq1[-cur_tail:]) + to_int(d, predpoloj, seq2[-cur_tail:])) % 10 ** cur_tail != to_int(d, predpoloj, ans[-cur_tail:]):
                        print("нарушает сумму")
                        continue

            else:
                print("2 полных слова в проверку суммы предположения", cur_tail, tail, d, predpoloj, (to_int(d, predpoloj, seq1[-cur_tail:]) + to_int(d, predpoloj, seq2)))
                if cur_tail >= len(seq2):
                    if (to_int(d, predpoloj, seq1[-cur_tail:]) + to_int(d, predpoloj, seq2)) % 10 ** cur_tail != to_int(d, predpoloj, ans[-cur_tail:]):
                        print("нарушает сумму")
                        continue
                else:
                    if (to_int(d, predpoloj, seq1[-cur_tail:]) + to_int(d, predpoloj, seq2[-cur_tail:])) % 10 ** cur_tail != to_int(d, predpoloj, ans[-cur_tail:]):
                        print("нарушает сумму")
                        continue
                #exit()

        if len(d) + len(predpoloj) + len(gypotheza) == alp_dlina:
            print("Here!", d, predpoloj, gypotheza)
            global_answer.append(collector(d, predpoloj, gypotheza, seq1, seq2, ans))
            gypotheza = {}
            continue

        #возможность гипотезы о сумме
        if tail > tail_ans:
            if not full_in_d(seq1, dict_sum(d, predpoloj, {})) and not full_in_d(seq2, dict_sum(d, predpoloj, {})):
                delta = (to_int(d, predpoloj, seq1[-tail_ans - 1:]) + to_int(d, predpoloj, seq2[-tail_ans - 1:])) % 10 ** tail // 10 ** tail_ans
                #gypotheza[ans[-tail_ans - 1]] = delta
                flag1 = 0
                for num, i in enumerate(ans[len(ans) - tail: len(ans) - tail_ans]):
                    if i not in gypotheza or (i in gypotheza and gypotheza[i] == int(str(delta)[num])):
                        gypotheza[i] = int(str(delta)[num])
                    else:
                        flag1 = 1
                        break
                if flag1:
                    gypotheza = {}
                    print("exit")
                    continue
                print("гипотеза", gypotheza)

            # 2ое слово разгадано
            elif not full_in_d(seq1, dict_sum(d, predpoloj, {})) and full_in_d(seq2, dict_sum(d, predpoloj, {})):
                if tail >= len(seq2):
                    delta = (to_int(d, predpoloj, seq1[-tail_ans - 1:]) + to_int(d, predpoloj, seq2)) % 10 ** tail // 10 ** tail_ans
                    #gypotheza[ans[-tail_ans - 1]] = delta
                    flag1 = 0
                    for num, i in enumerate(ans[len(ans) - tail: len(ans) - tail_ans]):
                        if i not in gypotheza or (i in gypotheza and gypotheza[i] == int(str(delta)[num])):
                            gypotheza[i] = int(str(delta)[num])
                        else:
                            flag1 = 1
                            break
                    if flag1:
                        gypotheza = {}
                        print("exit")
                        continue
                    print("гипотеза", gypotheza)
                else:
                    delta = (to_int(d, predpoloj, seq1[-tail_ans - 1:]) + to_int(d, predpoloj, seq2[-tail_ans - 1:])) % 10 ** tail // 10 ** tail_ans
                    #gypotheza[ans[-tail_ans - 1]] = delta
                    flag1 = 0
                    for num, i in enumerate(ans[len(ans) - tail: len(ans) - tail_ans]):
                        if i not in gypotheza or (i in gypotheza and gypotheza[i] == int(str(delta)[num])):
                            gypotheza[i] = int(str(delta)[num])
                        else:
                            flag1 = 1
                            break
                    if flag1:
                        gypotheza = {}
                        print("exit")
                        continue
                    print("гипотеза", gypotheza)
            else:
                print("2 полных слова в гипотезе")
                delta = (to_int(d, predpoloj, seq1) + to_int(d, predpoloj, seq2)) % 10 ** tail // 10 ** tail_ans

                flag1 = 0
                print("---", cur_tail, tail, ans[len(ans) - tail: len(ans) - tail_ans], delta, (to_int(d, predpoloj, seq1) + to_int(d, predpoloj, seq2)))
                for num, i in enumerate(ans[len(ans) - tail: len(ans) - tail_ans]):
                    if (i not in gypotheza or (i in gypotheza and gypotheza[i] == int(str(delta)[num]))) and int(str(delta)[num]) not in gypotheza.values():
                        gypotheza[i] = int(str(delta)[num])
                    else:
                        flag1 = 1
                        break
                if flag1:
                    gypotheza = {}
                    print("exit")
                    continue
                print("гипотеза", gypotheza)
                #exit()


        #проверка невозможности гипотезы о сумме
            flag = 0
            for key, value in gypotheza.items():
                if value in d.values() or value in predpoloj.values():
                    print("гипотеза невозможна", gypotheza)
                    gypotheza = {}
                    flag = 1
                    break
            if flag == 1:
                continue


        #Если ребус не разгадан
        if len(d) + len(predpoloj) + len(gypotheza) != alp_dlina:
            print("рекурсивный вызов", dict_sum(d, predpoloj, gypotheza))
            analyze(seq1, seq2, ans, dict_sum(d, predpoloj, gypotheza))
            gypotheza = {}

        #Если ребус разгадан
        else:
            print("Here!", d, predpoloj, gypotheza)
            global_answer.append(collector(d, predpoloj, gypotheza, seq1, seq2, ans))
            gypotheza = {}
            continue

global_answer = []
#a = input()
a = "АНДРЕЙ+ЖАННА=ДРУЖБА"
a = a.split("+")
a = [a[0]] + a[1].split("=")
dlina = max(len(a[0]), len(a[1]))

alp = {}
for item in "".join(a):
    if item not in alp:
        alp[item] = None
alp_dlina = len(alp)
inp = sorted([a[0],a[1]], key=lambda x: -len(x))
if max(len(a[0]), len(a[1])) == len(a[2]):
    analyze(*inp, a[2], {})
else:
    analyze(*inp, a[2], {a[2][0]: 1})

#print("success")
if inp == [a[0], a[1]]:
    for item in sorted(global_answer):
        item = item.split("+")
        item = [item[0]] + item[1].split("=")
        if int(item[0]) + int(item[1]) == int(item[2]):
            print(item[0] + "+" + item[1] + "=" + item[2])

else:
    for item in sorted(global_answer):
        item = item.split("+")
        item = [item[0]] + item[1].split("=")
        print(item[1] + "+" + item[0] + "=" + item[2])
