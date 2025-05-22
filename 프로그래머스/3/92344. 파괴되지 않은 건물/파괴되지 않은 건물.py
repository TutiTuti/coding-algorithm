def solution(board, skill):
    answer = 0
    lst = list([0] * (len(board[0]) + 1) for _ in range(len(board) + 1))

    for i in skill:
        s_type, r1, c1, r2, c2, v = i
        if s_type == 1:
            v = -v
        lst[r1][c1] += v
        lst[r1][c2 + 1] += -v
        lst[r2 + 1][c1] += -v
        lst[r2 + 1][c2 + 1] += v

    for r in range(len(board)):
        for c in range(1, len(board[0])):
            lst[r][c] += lst[r][c - 1]

    for r in range(1, len(board)):
        for c in range(len(board[0])):
            lst[r][c] += lst[r - 1][c]

    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += lst[r][c]
            if board[r][c] > 0:
                answer += 1

    return answer