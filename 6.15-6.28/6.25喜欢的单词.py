import traceback
import re

try:
    n = input()
    pat1 = re.compile('[A-Z]+')
    pat2 = re.compile('.*(.)(\\1).*')
    pat3 = re.compile('.*(.).*(.)(.*\\1)(.*\\2).*')
    print(pat3.match(n))
    if pat1.match(n) and not pat2.match(n) and not pat3.match(n):
        print("Likes")
    else:
        print("Dislikes")
except:
    traceback.print_exc()
    pass