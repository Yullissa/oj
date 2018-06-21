# coding=utf-8

import re
import sys

while (True):
    # try 很重要！！！！！！！！！不然非法输入会报错！！！！！！！！！！！！
    try:
        nm = input().strip()
        saw1 = input().strip()
        saw2 = input().strip()
        # 语法糖，切片，字符串反转
        mn = nm[::-1]
        pathlen = len(nm)
        for1 = nm.split(saw1)
        for2 = mn.split(saw1)
        bak1 = nm.split(saw2)
        bak2 = mn.split(saw2)

        flag1 = 0
        flag2 = 0
        if (for1[0] != pathlen) and (bak1[0] != pathlen):
            endfor1 = len(for1[0])
            startbak1 = pathlen - len(bak1[-1])-len(saw2)
            if (endfor1 < startbak1):
                flag1 = 1
        if (for2[0] != pathlen) and (bak2[0] != pathlen):
            endfor2 = len(for2[0])
            startbak2 = pathlen - len(bak2[-1]) - len(saw2)
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
    except:
        break
