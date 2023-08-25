def check_line(index, ver):
    check = [0]*10
    if ver:
        for i in range(9):
            check[arr[index][i]] = 1

    else:
        for i in range(9):
            check[arr[i][index]] = 1

    if sum(check) != 9:
        return 1
    return 0

def check_square(r,c):
    check = [0]*10
    for i in range(3):
        for j in range(3):
            check[arr[r+i][c+j]] = 1

    if sum(check) != 9:
        return 1
    return 0



T = int(input())
for t in range(1, T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]

    flag = 1
    for i in range(9):
        if check_line(i,0):
            flag = 0
            break;
        if check_line(i,1):
            flag = 0
            break
    if flag:
        for i in range(0,9,3):
            if flag:
                for j in range(0,9,3):
                    if check_square(i,j):
                        flag = 0
                        break
    print(f'#{t} {flag}')