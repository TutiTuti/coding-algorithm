N = int(input())
lst = list(map(int, input().split()))
s = []

for i in range(N):

    while s:
        t = s.pop()
        if lst[t] > lst[i]:
            s.append(t)
            s.append(i)
            print(t+1, end=" ")
            break
    if not s:
        s.append(i)
        print(0, end=" ")