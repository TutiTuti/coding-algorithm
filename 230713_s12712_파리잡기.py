'''
N X N 배열 안의 숫자는 해당 영역에 존재하는 파리의 수를 의미한다.
파리 스프레이를 한 번만 뿌려 최대한 많은 파리를 잡을려고 한다.
스프레이는 +형태 or x형태로 분사된다. 스프레이르 M의 세기로 분사하면 중심 칸부터 각 방향으로 M칸의 파리를 잡을 수 있다.
뿌려진 일부가 영역을 벗어나도 상관없다. 한번에 잡을 수 있는 최대 파리수를 출력하라.

입력
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
다음 N 줄에 걸쳐 N x N 배열이 주어진다.
'''


''' input 파일 가져오기 코딩 '''
import sys
inputversion = "4"
sys.stdin = open(".\input\input"+inputversion+".txt", "r")

#  스프레이 +형태노줄 중심부터 각옆 1칸의 좌표들
px = [1,0,-1,0]
py = [0,1,0,-1]
#  스프레이 x형태노줄 중심부터 각옆 1칸의 좌표들
cx = [1,1,-1,-1]
cy = [-1,1,1,-1]
# TestCase 수를 입력받아 수만큼 반복
for T in range(int(input())):
    #배열의 크기 n , 스프레이 세기 m 을 입력받는다.
    n, m = map(int,input().split())
    # n X n 배열을 입력받는다.
    arr = [list(map(int,input().split()))for _ in range(n)]
    #최대값 ans를 0으로 초기화
    ans = 0
    # n x n 칸 반복
    for i in range(n):
        for j in range(n):
            #스프레이가 분사되는 중심값 설정
            plus_result = arr[i][j]
            cross_result = arr[i][j]
            #분사되는 4 방향을 반복
            for k in range(4):
                #한 방향을 중심부터 중심을 제외하고 m세기 까지 반복
                for w in range(1,m):
                    # 중심좌표에서 px[]방향 x m세기를 더해서 퍼지는 좌표를 구한다.
                    p_x,p_y = i+(px[k]*w), j+(py[k]*w)
                    c_x,c_y = i+(cx[k]*w), j+(cy[k]*w)
                    #구한 좌표가 n x n 배열 범위안에 있으면 plus_result에 값을 더해준다.
                    plus_result += (arr[p_x][p_y] if (0<=p_x<n) and (0<=p_y<n) else 0)
                    cross_result += (arr[c_x][c_y] if (0<=c_x<n) and (0<=c_y<n) else 0)
            # 기존 ans값 plus_result값, cross_result 값중 큰 값을 result로 설정한다.
            ans = max(ans, plus_result, cross_result)
    # 반복이 끝나면 테스트케이스 번호 잡은 파리수를 출력한다.
    print(f"#{T+1} {ans}")