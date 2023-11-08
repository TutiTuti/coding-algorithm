A, B = map(int, input().split())
ans = -1
cnt = 1
while B >= A:
    if A == B:
        ans = cnt
        break
    elif str(B)[-1] == '1':
        B = int(str(B)[:len(str(B))-1])
        cnt += 1
    elif B % 2 == 1:
        break
    else:
        B //= 2
        cnt += 1
print(ans)