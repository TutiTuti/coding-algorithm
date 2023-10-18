arrow = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서

def move_back(r, c, d):
    return r + arrow[d][0] * (-1), c + arrow[d][1] * (-1)

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cleaned_count = 0

while True:
    # 1. 현재 위치를 청소한다.
    if arr[r][c] == 0:
        arr[r][c] = 2  # 청소 완료
        cleaned_count += 1

    # 2. 현재 위치에서 청소할 수 있는 칸 탐색
    found = False
    for _ in range(4):
        nd = (d + 3) % 4  # 현재 방향에서 왼쪽 방향 (반시계 방향으로 변경)
        nni, nnj = r + arrow[nd][0], c + arrow[nd][1]
        if 0 <= nni < N and 0 <= nnj < M and arr[nni][nnj] == 0:
            # 왼쪽 방향에 아직 청소하지 않은 공간이 존재
            r, c, d = nni, nnj, nd
            found = True
            break

        # 왼쪽 방향에 청소할 공간이 없으면 방향만 변경
        d = nd

    if not found:
        # 네 방향 모두 청소할 공간이 없는 경우
        nni, nnj = move_back(r, c, d)
        if 0 <= nni < N and 0 <= nnj < M and arr[nni][nnj] != 1:
            # 후진 가능하면 후진
            r, c = nni, nnj
        else:
            # 후진이 불가능하면 종료
            break

print(cleaned_count)
