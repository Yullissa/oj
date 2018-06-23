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
        pat1 = re.compile(r'(.*){}(.*){}(.*)'.format(saw1,saw2))

        flag1 = pat1.match(nm)
        flag2 = pat1.match(mn)
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
