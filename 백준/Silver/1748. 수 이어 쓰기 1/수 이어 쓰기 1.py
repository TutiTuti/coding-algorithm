N = int(input())
ans = 0
dept = 0
while N:
    # print(10**dept)
    if N // (10**dept) > 9:
        # print('@@', 9*(10**dept)*(dept+1))
        ans += 9*(10**dept)*(dept+1)
    else:
        ans += (N-((10**dept) - 1)) * (dept+1)
        break
    dept += 1
    # N = int(N/10)
print(ans)