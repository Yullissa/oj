# -*- coding:UTF8 -*-
import re
import traceback

try:
    n = input()
    pattern = re.compile(r'\d+')  # 查找数字
    result1 = list(map(int,pattern.findall(n)))
    result1.sort(reverse=True)
    print(result1[0])
except:
    traceback.print_exc()
    pass