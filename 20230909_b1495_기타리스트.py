N, S, M = map(int,input().split()) # Song_nums , Start_interval, max_interval
song = list(map(int,input().split())) # 노래 높낮이 차이
arr = [[0] * N for _ in range(M+1)] # N개의 곡을 M+1 높낮이 까지 다 저장할 수 있는 리스트

if 0<= S+song[0] <= M: # 첫번째 값 채워넣기 
    arr[S+song[0]][0] = 1

if 0<= S-song[0] < M:
    arr[S-song[0]][0] = 1

for i in range(1, N): # 두번째 노래 부터 반복문으로 넣기
    now = song[i] # 지금 노래의 높낮이 차이
    for j in range(M+1):
        if arr[j][i-1] == 1: # 전 노래의 높낮이를 찾았을 때
            if 0 <= j + now <= M: # 다음노래 높낮이를 더했을 때 높낮이 범위안에 든다면 1
                arr[j+now][i] = 1
            if 0 <= j - now <= M: # 다음노래 높낮이를 뺐을 때 높낮이 범위안에 든다면 1
                arr[j-now][i] = 1
                
flag = 1
for i in range(M,-1,-1): # M부터 0 까지 반복 -> 가장 높은 높낮이를 찾아야 하기 때문
    if arr[i][N-1] == 1: # 찾으면 출력하고 flag 바꾸고 break
        print(i)
        flag = 0
        break

if flag: # 못찾았으면 -1 
    print(-1)