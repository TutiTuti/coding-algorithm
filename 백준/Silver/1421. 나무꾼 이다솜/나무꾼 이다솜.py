N, C, W = map(int, input().split())
woods = []
for _ in range(N):
    wood = int(input())
    woods.append(wood)
ans = 0
for i in range(1, max(woods)+1):
    tmp = 0
    for j in woods:
        woodsCnt =0
        woodCutCost = 0
        if j % i == 0:
            woodCutCost += ((j//i)-1) * C
        else:
            woodCutCost += (j // i) * C
        woodsCnt += j//i
        if (W*woodsCnt*i) - woodCutCost > 0:
            tmp+= (W*woodsCnt*i) - woodCutCost

    ans = max(ans, tmp)
print(ans)