m = int(input())
s = 1
e = 2
flag = True
while e < 100_000:
    g = (e*e) - (s*s)
    if g == m:
        flag = False
        print(e)
    if g > m:
        s += 1
    else:
        e += 1
if flag:
    print(-1)