def find(n, m):
    global ans
    if n != M and m == len(chickengood):
        return
    if n == M:
        # print('check')
        tmptotal = 0
        for i in housegood:
            tmp = 1e9
            for j in choice:
                dis = abs(i[0] - j[0]) + abs(i[1] - j[1])
                tmp = min(tmp, dis)
            tmptotal += tmp
        ans = min(ans, tmptotal)
        # print(ans)

    else:
        choice.append(chickengood[m])
        find(n+1, m+1)
        choice.pop()
        find(n, m+1)


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

chickengood = []
housegood = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            housegood.append([i, j])
        elif maps[i][j] == 2:
            chickengood.append([i, j])
ans = 1e9
# print('chicken',chickengood)
# print('house', housegood)
choice = []
find(0, 0)
print(ans)