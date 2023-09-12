N = int(input())
nums = list(map(int,input().split()))
# 진홍스 알고리즘  나머지 (0,0), (1,2), (2,1) 이 인접할 때 합 %3 이 0이 나온다. 
#> 0, 0 만 피하면 된다.
d1 = [] # %3 했을 때 나머지가 1인 숫자들의 리스트
d2 = [] # %3 했을 때 나머지가 2인 숫자들의 리스트
d0 = [] # %3 했을 때 나머지가 0인 숫자들의 리스트

for i in range(N): # 나머지를 구하고 해당하는 리스트에 넣어준다.
    if nums[i] % 3 == 1:
        d1.append(nums[i])
    elif nums[i] % 3 == 2:
        d2.append(nums[i])
    else:
        d0.append(nums[i])


ans = [] # 정답을 담을 리스트

# 나머지0이 없는데 1,2 둘다 있을 때 or 0 개수가 너무 많을 때 or 0리스트에만 숫자가 있을 때
if (len(d0) == 0 and d1 and d2) or (len(d1)+len(d2) < len(d0)-1) or (not d1 and not d2):
    print(-1) # -1 출력
else:
    arr1 = [] # 0과 2를 담을 리스트 
    while d0 and d2: # 리스트 2개다 존재할 떄 진행
        arr1.append(d0.pop(-1)) 
        arr1.append(d2.pop(-1))
    while (d2): # d2가 남아있을 수도 있으니 
        arr1.append(d2.pop()) # 다 더해준다.


    arr2 = [] # 0과 1을 담을 리스트
    while d0 and d1:
        arr2.append(d0.pop(-1))
        arr2.append(d1.pop(-1))
    while d1: # d1이 남아있다면
        arr2.append(d1.pop())
    ans = arr2 + arr1 # 구한 순서 반대로 리스트를 합한다.

    while d0: # 만약 0 1 0 1 0 1 0 2 0 2 0 2 0 모양이라면 마지막 0을 더해줘야 한다.
        ans.append(d0.pop())

    print(*ans) # 만든 ans 출력