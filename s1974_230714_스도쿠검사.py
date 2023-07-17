'''
스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
※ 규칙
같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고( 가로, 세로) ,
3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
3 X 3 크기 9개가 정사각형으로 붙어있는 모양세

겹치는 수가 없을 경우 1 그렇지 않을 경우 0을 출력한다. ex > "#1 1"  #테스트번호 정답
입력 값
1. 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
2. 다음 줄부터 각 테스트 케이스가 주어진다.
3. 테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다
'''

''' input 파일 가져오기 코딩 '''
import sys
inputversion = "3"
sys.stdin = open(".\input\input"+inputversion+".txt", "r")

# box안의 값이 규칙에 맞는지 검증하는 함수
def box(arr, x, y):
    # 0이 9개 있는 리스트 boxpass 초기화
    boxpass = [0]*9
    #박스의 x좌표 3개를 반복
    for i in range(3):
        #박스의 y좌표 3개를 반복
        for j in range(3):
            #박스좌표의 값을 boxpass 인덱스로 하여 값을 1로 변경
            boxpass[arr[x+i][y+j] -1]=1
    #boxpass값이 모두 1이라면 True 아니라면 False 반환
    return (True if sum(boxpass)==9 else False)

#  i번째 x축이 규칙에 맞는지 검증하는 함수
def sum_x(arr, i):
    # 0이 9개 있는 리스트 xpass 초기화
    xpass = [0]*9
    # x축의 값 9개를 반복
    for k in range(9):
        #x축의 값들을 인덱스로 값을 1로 바꿔줌
        xpass[arr[i][k]-1] = 1
    # 리스트값 합이 9면 True 아니면 False 반환
    return (True if sum(xpass)==9 else False)

# i번째 y축이 규칙에 맞는지 검증하는 함수
def sum_y(arr, i):
    ypass = [0]*9
    for k in range(9):
        ypass[arr[k][i]-1] = 1
    return (True if sum(ypass)==9 else False)


# 퍼즐 개수 T를 입력받아 T회 반복
for T in range(int(input())):
    # 스도쿠 9 X 9 크기의 리스트를 입력받는다.
    sudoku = [list(map(int,input().split())) for _ in range(9)]
    # 현재 스도쿠의 결과를 True라고 초기화한다.
    flag = True
    # 박스 첫 번째 칸의 x좌표  0,3,6 반복
    for i in range(0,9,3):
        #flag가 True일 떄  
        if flag:
            # 박스 첫 번째 칸의 y좌표 0,3,6 반복
            for j in range(0,9,3):
                # box(sudoku, im j) 함수의 결과값이 False일 때
                if not box(sudoku,i, j):
                    #flag를 False로 변경
                    flag = False
                    # (30) for문 나가기
                    break
    # box 검증을 통과하면 flag값은 True
    if flag:
        # 9개의 줄을 반복한다
        for i in range(9):
            # flag값이 True
            if flag:
                # i번째 x축 합 검증 sum_x() y축 합 검증 sum_y() 중에 False가 있다면
                if not sum_x(sudoku,i) or not sum_y(sudoku,i):
                    flag=False
                    break
    print(f"#{T+1} {1 if flag==True else 0}")

