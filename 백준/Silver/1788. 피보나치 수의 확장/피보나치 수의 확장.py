N = int(input())
lst = [0] * 1_000_001

lst[0] = 0
lst[1] = 1

for i in range(2, abs(N) + 1):
    lst[i] = (lst[i - 1] + lst[i - 2]) % 1_000_000_000

if N == 0:
    print(0)
elif N > 0:
    print(1)
else:
    if abs(N) % 2 == 0:
        print(-1)
    else:
        print(1)

print(lst[abs(N)])