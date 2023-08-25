q = int(input())
for t in range(1,q+1):
    N = int(input())
    route = []
    for i in range(N):
        a, b = map(int, input().split())
        route.append([a,b])
    P = int(input())
    station = []
    for i in range(P):
        c = int(input())
        station.append(c)
    ans = ''
    for s in station:
        count = 0
        for r in route:
            if r[0] <= s <= r[1]:
                count += 1
        ans += str(count)+' '
    print(f'#{t} {ans}')