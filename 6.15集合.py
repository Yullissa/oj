# coding = utf-8
import sys

try:
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip().split(" ")
    c = sys.stdin.readline().strip().split(" ")
    print(" ".join(sorted(set(b + c), key=int)))
except Exception as e:
    print(e)

# 4 3
# 1 3 5 4
# 2 4 6

# 1 2 3 4 5 6