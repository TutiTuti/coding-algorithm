T = int(input())
for t in range (1, T+1):
    str1 = input()
    str2 = input()
    ans = {}
    max =0
    for i in str1:
        ans[i] = 0
    for i in str2:
        if ans.get(i, -1) != -1:
            ans[i] += 1
            if ans[i] > max:
                max = ans[i]
    print(f'#{t} {max}')