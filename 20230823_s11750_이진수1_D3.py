T = int(input())
for t in range(1, T+1):
    n, m = input().split()
    list_n = []
    flag = 1
    for i in range(int(n)):
        if m[i].isdigit():
            tmp = int(m[i])
            tmp2 = ''
            while tmp:
                tmp2 += str(tmp%2)
                tmp//=2
            while len(tmp2) != 4:
                tmp2 += '0'
            list_n.append(tmp2)
        else:
            tmp = (ord(m[i])-55)
            tmp2 = ''
            while tmp:
                tmp2 += str(tmp%2)
                tmp//=2
            while len(tmp2) != 4:
                tmp2 += '0'
            list_n.append(tmp2)

    print(f'#{t} ',end='')

    for i in list_n:
        for j in range(3,-1,-1):
            print(i[j], end='')
    print()