'''
N 세로 N만큼의 공간만 사용하여 진행하도록 하였다.
이 공간을 벗어나면 실격처리가 되므로 공간안에서 가장 빠른 길을 찾아야 한다.
이 공간에는 섬과 같은 지나갈 수 없는 장애물과, 주기적으로 사라졌다 나타나는 소용돌이 같은 장애물이 존재한다.
( 섬과 같은 장애물은 지도에서 1로 표시, 소용돌이 같은 장애물은 2로 표시 )
소용돌이는 생성되고 2초동안 유지되다가 1초동안 잠잠해진다.
예를들어, 0초에 생성된 소용돌이는 0초, 1초까지 유지되고 2초에 사라지게된다. 또한 3초, 4초에는 생성되고 5초에 사라진다.
(단 ,한번 통과한 소용돌이 위에서는 머물러 있을 수 있다 )
이런 바다에서 우승하려면 어떤 경로로 보내야 될까?

입력
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 수영장의 크기 N  ( 2<=N<=15 )
다음 N개의 줄의 i번째 줄에는 수영장의 모양이 공으로 구분되어 주어진다. ( 0 : 지나갈 수 있는 곳 , 1 : 장애물 , 2: 주기가 2초인 소용돌이)
다음으로 시작위치 A,B가 주어지고 ( 0<=A,B<=N-1)
마지막 줄에 도착위치 C, D가 주어진다 ( 0 <=C,D<=N-1) ( 도착점과 시작점은 소용돌이가 아니다 )
'''

''' input 파일 가져오기 코딩 '''
import sys
inputversion = "6"
sys.stdin = open(".\input\input"+inputversion+".txt", "r")

# move는 위 아래 왼쪽 오른쪽 제자리 순서
move_col = [0,0,-1,1,0] # y축을 의미
move_row = [1,-1,0,0,0] # x축을 의미

# ( 현재좌표 row, col ) ( 타겟좌표 row, col ) (현재 움직인 과정 )
def move_location(now_row, now_col, target_row, target_col, moving_list, time=0):
    next_col = 0
    next_row = 0
    for i in range(5):
        print("TT")
        next_row = now_row + move_row[i]
        next_col = now_col + move_col[i]



for T in range(int(input())):
    n = int(input())
    swim_area = [list(map(int,input().split())) for _ in range(n)]
    start_row, start_col = map(int,input().split())
    end_row, end_col = map(int,input().split())
    move_process = []
    move_process.append([start_col,start_row])
    move_process = move_location(start_row, start_col, end_row, end_col, move_process)




