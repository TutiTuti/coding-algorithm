S, E = map(str, input().split())
res = 0
if len(S) != len(E):
    print(res)
else:
    for i in range(len(S)):
        if S[i] == E[i]:
            if S[i] == '8':
                res += 1
        else:
            break
    print(res)