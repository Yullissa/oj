import re

while (True):
    nm = input().strip()
    mn = nm[::-1]
    saw1 = input().strip()
    saw2 = input().strip()
    pat1 = re.compile(r'(.*){}(.*)'.format(saw1))  # 用()表示1个组，2个组
    pat2 = re.compile(r'(.*){}(.*)'.format(saw2))
    # 只匹配最后一个一样的
    for1 = pat1.match(str(nm))
    bak1 = pat2.match(str(nm))
    for2 = pat1.match(str(mn))
    bak2 = pat2.match(str(mn))

    flag1 = 0
    flag2 = 0
    if (for1 and bak1):
        endfor1 = for1.end(1)
        grouplen = len(bak1.groups())
        startbak1 = bak1.start(grouplen)
        if (endfor1 < startbak1):
            flag1 = 1
    if (for2 and bak2):
        endfor2 = for2.end(1)
        grouplen = len(bak2.groups())
        startbak2 = bak2.start(grouplen)
        if (endfor2 < startbak2):
            flag2 = 1
    if (flag1 and flag2):
        print("both")
    elif (flag1):
        print("forward")
    elif (flag2):
        print("backward")
    else:
        print("invalid")
