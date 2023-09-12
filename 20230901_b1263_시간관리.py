N = int(input()) # 해야할 일의 수 N

workTime = [] # 일 작업시간, 마감시간 을 넣을 리스트

for i in range(N): # 일의 수 만큼 반복
    work = list(map(int,input().split())) # 일 작업시간, 마감시간을 입력받는다.

    workTime.append(work)   # 리스트에 넣기

workTime.sort(key= lambda x:(-x[1], x[0])) # 마감시간을 기준으로 내림차순 정렬 같은 수는 걸리는 시간 오름차순 정렬 한다.

ans = workTime[0][1]    # 시작시간 ans를 가장 늦은 마감시간으로 초기화.

for i in range(N):

    if workTime[i][1] < ans:    # 만약 마감시간이 시작시간보다 작다면
        ans = workTime[i][1]    # 시작시간을 마감시간으로 바꿔준다.

    ans -= workTime[i][0]   # 시작시간에서 작업시간을 빼준다.

if ans < 0: # 시작시간이 음수가 된다면.
    ans = -1    # 시작시간을 -1로 변경

print(ans)  # 시작시간 출력