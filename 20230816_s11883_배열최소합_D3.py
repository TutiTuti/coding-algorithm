def find(d, b, s):
    global minx
    if s > minx:
        return
    
    if N == d:
        if minx > sum(B):
            minx = sum(B)
# min < s 가지치기 해야함 why? 한번 N==d 되고나서 min이 갱신되서 큰 거  거를 수 있기 떄문 ..하하하하하하
    else:
        for i in range(N):
            if i not in b:
                B[d] = arr[d][i]
                c = b[:]
                c.append(i)
                find(d+1, c, s+arr[d][i])



T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [ list(map(int, input().split())) for _ in range(N)]
    B = [0]*N
    minx = 987654321
    find(0, [], 0)
    print(f'#{t}', minx)