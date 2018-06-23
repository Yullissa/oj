def divide(m, low, high):
    mid = int((low + high) / 2)
    if m < mid:
        if mid - low >= 5:
            return str(0) + divide(m, low, mid)
        else:
            return str(0)
    else:
        if high - mid >= 5:
            return str(1) + divide(m, mid, high)
        else:
            return str(1)


try:
    m = int(input().strip())
    print(divide(m, -90, 90))
except:
    pass
