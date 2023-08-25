
for t in range (10):
    T = int(input())
    str1 = input()
    str2 = input()
    m = len(str1)
    n = len(str2)
    k = len(''.join(str2.split(str1)))
    p =((n-k)//m)
    print(f'#{T} {p}')