T = int(input())
for t in range(1, T+1):


    stack = list(input().split())

    tmp = []
    top = -1

    flag = 0
    for i in stack:
        if i == '.':
            if len(tmp) != 1:
                flag = 1
            break

        if i not in '+-*/':
            tmp.append(i)
            top += 1
        else:
            if len(tmp) < 2:
                flag = 1
                break  # 오류 오류 오류
            a = int(tmp.pop(top))
            top -=1
            b = int(tmp.pop(top))
            top -=1
            if i == '+':
                tmp.append(a+b)
            elif i == '-':
                tmp.append(b-a)
            elif i == '*':
                tmp.append(a*b)
            elif i == '/':
                tmp.append(b//a)
            top += 1


    if flag:
        tmp[0] = 'error'
    print(f'#{t} {tmp[0]}')