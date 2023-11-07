def find(n, v):
    global ans

    if v > M:              # M 보다 커지거나 0보다 작아진다면 return
        return
    elif v == M:                     # 값을 찾으면 ans 갱신
        ans = n
        return
    else:
        find(n+1, v*2)               # 2배
        find(n+1, int(str(v)+'1'))   # 끝에 1추가 해준다.


N, M = map(int, input().split())
ans = -1                             # 값을 못 찾으면 -1이 출력 된다.
find(1, N)
print(ans)