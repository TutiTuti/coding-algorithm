N = int(input())
arr = [0] * 1_000_001 # N의 숫자 제한이 1,000,000 까지 있으니까 1000001로 만들어야 한다.
arr[0] = 0 # 0번은 0
arr[1] = 1 # 1번은 1
for i in range(2, 1_000_001): # 2부터 반복
    arr[i] =  (arr[i-1] + arr[i-2]) % 1_000_000_000 # F(n) = F(n-1) + F(n-2)

ans = 0 # 기본값 0
if N > 0: # 양수면 1
    ans = 1
elif N < 0: # 음수일 때 짝수면 -1 홀수면 1
    if N % 2 == 0:
        ans = -1
    else:
        ans = 1

print(ans)
print(arr[abs(N)])