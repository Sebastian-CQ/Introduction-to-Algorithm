import time
import numpy as np


def anagramSolution(S1, S2):
    alist = list(S2)
    pos_1 = 0
    go_on = True
    while pos_1 < len(S1) and go_on:
        pos_2 = 0
        found = False
        while pos_2 < len(S2) and not found:
            if S1[pos_1] == alist[pos_2]:
                found = True
            else:
                pos_2 += 1
        if found:
            alist[pos_2] = None
        else:
            go_on = False
        pos_1 += 1
    return go_on


def anagramSolution2(S1, S2):
    list_a = list(S1)
    list_b = list(S2)
    list_a.sort()
    list_b.sort()

    matchs = True
    for i in range(len(list_a)):
        if list_a[i] != list_b[i]:
            matchs = False

    return matchs


def anagramSolution3(S1, S2):
    C1 = [0] * 26
    C2 = [0] * 26
    alist = list(S1)
    blist = list(S2)
    for i in range(len(S1)):
        C1[ord(alist[i]) - ord('a')] = C1[ord(alist[i]) - ord('a')] + 1
        C2[ord(alist[i]) - ord('a')] = C2[ord(alist[i]) - ord('a')] + 1
    match = False
    if C1 == C2:
        match = True

    return match


print(anagramSolution('python', 'typhon'))
print(anagramSolution2('python', 'typhon'))
print(anagramSolution3('python', 'typhon'))

