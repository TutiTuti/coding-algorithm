n = int(input())
mp, mf, ms, mv = map(int, input().split())

ingredients = [list(map(int, input().split())) for _ in range(n)]

vstd = [0 for _ in range(n)]


answer = []
def start(w, cost, choice, p, f, s, v):

    if p >= mp and f >= mf and s >= ms and v >= mv:
        answer.append([cost, choice[:]])
        return
    for j in range(w, n):
        if not vstd[j]:
            vstd[j] = 1
            choice.append(j+1)
            start(j, cost+ingredients[j][4], choice, p + ingredients[j][0], f + ingredients[j][1], s + ingredients[j][2], v + ingredients[j][3])
            choice.pop()
            vstd[j] = 0
    return

for i in range(n):
    vstd[i] = 1
    start(i, ingredients[i][4], [i + 1], ingredients[i][0], ingredients[i][1], ingredients[i][2], ingredients[i][3])
    vstd[i] = 0

if answer:
    answer.sort(key=lambda x: x[0])
    print(answer[0][0])
    print(" ".join(map(str, answer[0][1])))
else:
    print(-1)