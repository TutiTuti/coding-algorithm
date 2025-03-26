
# 동남서북 방향전환 고려
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# 홍준이 위치
now = [0, 0]
# 홍준이 방향
loc = 1
# 이동 좌표
moveX = [0]
moveY = [0]

N = int(input())
move = list(map(str, input()))


def moveL():
    global loc
    loc = (loc - 1 + 4) % 4


def moveR():
    global loc
    loc = (loc + 1) % 4


def moveF(now, moveX, moveY, loc):
    now[0] += dx[loc]
    now[1] += dy[loc]
    moveX.append(now[0])
    moveY.append(now[1])

switch_dict = {
    "L": lambda: moveL(),
    "R": lambda: moveR(),
    "F": lambda: moveF(now, moveX, moveY,  loc)
}

for act in move:
    switch_dict.get(act, lambda: None)()

difX = (max(moveX) - min(moveX)) + 1
difY = (max(moveY) - min(moveY)) + 1
answer = [["#"] * difX for _ in range(difY)]
mark = [abs(min(moveX)), abs(min(moveY))]


for i in range(len(moveX)):
    answer[moveY[i] + mark[1]][moveX[i] + mark[0]] = "."

for i in answer:
    print("".join(i))