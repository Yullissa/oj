#
import operator


def splitS(s):
    i = 0
    index = len(s)
    for ch in s:
        if (ch in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
            index = i
            break
        i = i + 1
    if (index == len(s)):
        return s, 0
    return s[0:index], int(s[index:])


# def splitP(s):
#     idx = len(s)
#     for i in s:
#         if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             idx = s.index(i)
#             break
#     if idx == len(s):
#         return s, 0
#     return s[:idx], int(s[idx:])


def cmpP(a, b):
    if (a[0] > b[0]):
        return 1
    if (a[0] == b[0]):
        return a[1] - b[1]
    else:
        return -1


if __name__ == '__main__':
    T = int(raw_input())
    slist = []
    for _ in range(T):
        s = raw_input()
        n, v = splitS(s)
        slist.append([n, v, s])
    slist.sort(key=operator.itemgetter(0, 1))
    # slist.sort(cmp=cmpP)
    for item in slist:
        print(item[2])
