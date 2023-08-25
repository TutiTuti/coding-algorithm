T = int(input())
for t in range (1, T+1):
    str1, str2 = map(str,input().split())
    i = ans = 0
    n = len(str1)
    m = len(str2)
    while i < n-m+1:
        flag = 1
        for j in range(m):
            if str1[i+j] != str2[j]:
                flag = 0
                break
        if flag:
            i += m-1
            ans += 1
                
        i+= 1
    print(f'#{t} {n-m*ans+ans}')