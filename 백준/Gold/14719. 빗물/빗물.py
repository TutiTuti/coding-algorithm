# 실패코드 2
H, W = map(int, input().split())
arr=list(map(int, input().split()))
left=0
ans=0
tmp=0
for i in range(W):
    if arr[i] >= arr[left] or i == W-1: # arr[i]가 왼쪽 벽가 같거나 클 때 or 마지막 인덱스 일 때
        # print("Y")
       
        # print("min :", min(arr[i], arr[left]), i-left-1, tmp, min(arr[i], arr[left])*(i-left-1)-tmp)
        if i:
            ans += min(arr[i], arr[left])*(i-left-1)-tmp
        left=i
        tmp=0
    elif arr[i] < arr[left]: # left i보다 크다면 ..  >> 벽 작은 arr[i]가 나머지 중에 가장 큰 값일 수도 있음.
        # print("N")
        flag=False
        for j in range(i+1,W):
            # print("find big num",arr[i] ,j , arr[j])
            if arr[j] > arr[i]:
                flag=True
                break
        if flag:
            tmp += arr[i]
            # print("tmp :", tmp)
        else:
            ans += min(arr[i], arr[left])*(i-left-1)-tmp
            left=i
            tmp=0
print(ans)