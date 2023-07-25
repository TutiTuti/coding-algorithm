import sys
import pprint
sys.stdin = open("./input/input7.txt", "r")

win = 0
concave = [list(map(int, input().split())) for _ in range(19)]
# 이동 방향은 ➡ ⬇ ↘ ↙ 방향이다.
way_row = [0, 1, 1, 1]
way_col = [1, 0, 1, -1]

def check():
    pass

# 4 방향 모든 방향으로 5목을 탐색
for way in range(4):

    # 5목 성공,실패 여부가 나올 떄 까지 반복
    while True:
        pass

