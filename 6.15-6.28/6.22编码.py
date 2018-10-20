import traceback

try:
    instr = list(input())
    arr = [1 + 25 + 25 * 25 + 25 * 25 * 25, 1 + 25 + 25 * 25, 1 + 25, 1]
    k = 0
    index = -1
    while (k<len(instr)):
        index += (ord(instr[k]) - ord('a')) * arr[k] + 1
        k += 1
    print(index)
except:
    traceback.print_exc()
    pass
