# 8방향 문제에 맞춰서 딕셔너리로 만들어주기
movement = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1),
}

king_loc, stone_loc, move = map(str, input().split())
# 파이썬 리스트 = 0,0이 왼쪽 위 하지만 체스판은 0,0이 왼쪽 아래에 해당 하므로 상하 반전을 해줘야함
kr = 8 - int(king_loc[1])
kc = ord(king_loc[0])-65
sr = 8 - int(stone_loc[1])
sc = ord(stone_loc[0])-65
# print(kr, kc, sr, sc)
for _ in range(int(move)): # 움직이는 횟수 만큼 반복
    m = input()
    dr, dc  = movement[m]
    move_kr = kr + dr
    move_kc = kc + dc

    if not 0 <= move_kr < 8 or not 0 <= move_kc < 8:
        continue
    if move_kr == sr and move_kc == sc:
        move_sr = sr + dr
        move_sc = sc + dc
        if 0 <= move_sr < 8 and 0 <= move_sc < 8:
            sr = move_sr
            sc = move_sc
        else:
            # 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.
            continue
    kr = move_kr
    kc = move_kc

kr = str(8-kr)
kc = chr(kc+65)

sr = str(8-sr)
sc = chr(sc+65)

print(kc+kr)
print(sc+sr)