T = int(input())
for t in range(1, T+1):
    n = int(input())
    price = list(map(int,input().split()))
    stack = []
    ans = 0
    point = i = n-1
    while point != -1:
        # print('3',i)
        # print('1',stack)
        if price[point] >= price[i]:
            stack.append(price[i])
        if price[point] < price[i] or i == 0:
            if stack:
                for j in stack:
                    # print('2', price[point], j)
                    ans += price[point] - j
                stack.clear()
            point = i
        if i == -1:
            break
        i -= 1
    print(f'#{t}', ans)