# AC
casenum = -1
with open("A-A-small-practice.in", 'rb') as fin:
    with open("A-small-practice.out", 'w') as  fout:
        try:
            for line in fin:
                if casenum == -1:
                    casenum = casenum + 1
                    continue
                casenum = casenum + 1
                line = line.strip("\n")
                flagX = 0
                flagY = 0
                X = ''
                for ch in line:
                    if flagX == 1:
                        X = X + '8'
                    if int(ch) % 2 == 1 and flagX == 0:
                        flagX = 1
                        X = X + str((int(ch) - 1))
                    if flagX == 0:
                        X = X + ch
                line = '0' + line
                Y = [0] * len(line)
                for i in range(len(line)):
                    if flagY == 1:
                        Y[i] = '0'
                    if line[i] == '9' and flagY == 0:
                        flagY = 1
                        j = i - 1
                        for j in range(i - 1, 0, -1):
                            if line[j] != '8':
                                break
                        Y[j] = str(int(line[j]) + 2)
                        for k in range(j + 1, i, 1):
                            Y[k] = '0'
                    elif int(line[i]) % 2 == 1 and flagY == 0:
                        Y[i] = int(line[i]) + 1
                        flagY = 1
                    if flagY == 0:
                        Y[i] = line[i]
                YY = ''
                for ch in Y:
                    YY = YY + str(ch)
                print('line ', line)
                print('X    ', X)
                print('Y    ', YY)
                fout.write("case #{}: {}\n".format(casenum, min(int(YY) - int(line), int(line) - int(X))))
                print(min(int(YY) - int(line), int(line) - int(X)))
        except Exception as e:
            print(e)
