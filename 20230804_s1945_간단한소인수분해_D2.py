T = int(input())
for t in range(1, T+1):
    num = int(input())
    list_num = [2,3,5,7,11]
    ans = [0]*5

    while num != 1:
        for i in range(5):
            if num % list_num[i] == 0:
                ans[i] += 1
                num //= list_num[i]
    print(f'#{t}', *ans)