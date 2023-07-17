''' 문제 1961 문제
N x N 행렬이 주어질 때,
시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.
입력							출력
10							#1
3							741 987 369
123							852 654 258
456							963 321 147
789							#2
6							872686 679398 558496
6 9 4 7 0 5					952899 979157 069877
8 9 9 2 6 5					317594 487722 724799
6 8 5 4 9 8					997427 894586 495713
2 2 7 7 8 4					778960 562998 998259
7 5 1 9 7 9					694855 507496 686278
8 9 3 9 7 6
…							…
'''

''' input 파일 가져오기 코딩 '''
import sys
inputversion = "0"
sys.stdin = open(".\input\input"+inputversion+".txt", "r")



for T in range(int(input())):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    arr90 = [ [0]*n for _ in range(n) ]
    arr180 = [ [0]*n for _ in range(n) ]
    arr270 = [ [0]*n for _ in range(n) ]
    for i in range(n):
        for k in range(n):
            #90도
            arr90[i][n-1-k] = arr[k][i]
            #180도
            arr180[n-1-i][n-1-k] = arr[i][k]
            #270도
            arr270[n-1-k][i] = arr[i][k]

    print("#{}".format(T+1))
    for i in range(n):
        a90 = a180 = a270 = ""
        for k in range(n):
            a90 = a90 + str(arr90[i][k])
            a180 = a180 + str(arr180[i][k])
            a270 = a270 + str(arr270[i][k])
        print(a90,a180,a270)