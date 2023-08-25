def ladder(row, col):
    global arr
    next = [-1, 1]
    while row != 0:
        for i in range(2):
            if 0<= col+next[i]<100 and arr[row][col+next[i]] == 1:
                col = side(row, col, next[i])
                break
        row -= 1
    return col

def side(row, col, move):
    global arr
    while True:
        if 0<= col+move < 100 and arr[row][col+move] == 1:
            col += move
        else:
            return col


for _ in range(10):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    goal = 0
    for i in range(100):
        if arr[-1][i] == 2:
            goal = i
    print(f'#{T}', ladder(99, goal))