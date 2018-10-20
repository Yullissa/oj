import traceback
import sys

need = []
for line in sys.stdin:
    need.extend(line.split())
need = set(need)
print(len(need))

