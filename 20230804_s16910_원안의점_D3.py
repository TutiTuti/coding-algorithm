T = int(input())
for t in range(1, T+1):
    n = int(input())
    ans = 0
    for i in range(-n,n+1):
        for j in range(-n, n+1):
            if i**2 + j**2 <= n**2:
                ans +=1
    print(f'#{t} {ans}')