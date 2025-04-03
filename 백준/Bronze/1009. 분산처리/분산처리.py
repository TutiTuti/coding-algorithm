num_dict = {  # 일의 자릿수 규칙 딕셔너리에 대입
    0: [0],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}

t = int(input())
for x in range(t):
    a, b = map(int, input().split())
    c = a % 10 
    d = len(num_dict[c])
    e = (b-1) % d
    f = num_dict[c][e]
    if(f == 0):
        f = 10
    print(f)
