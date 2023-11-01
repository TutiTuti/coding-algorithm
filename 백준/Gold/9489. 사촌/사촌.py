while True:
    N, K = map(int, input().split())

		# 0 0 들어오면 스탑
    if (N, K) == (0, 0):
        break

    arr = list(map(int, input().split()))

		# parent의 idx = node번호
		# parent의 값 = idx에 해당하는 node의 부모 idx
    parent = [0] * N

		# 0번째 원소는 root노드이므로 부모가 X => -1로 초기화
    parent[0] = -1

		# 부모 idx를 카운팅할 변수
    idx = -1
		# 0번째 원소는 root노드이므로 1번 원소부터 확인
    for i in range(1, N):
				# 값이 K인 원소는 target (=K 노드)
        if arr[i] == K:
            target = i

				# 앞의 원소와의 값 차이가 1보다 크다면 부모 노드가 다름
				# idx += 1 
        if arr[i] != arr[i-1] + 1:
            idx += 1

        parent[i] = idx

    ans = 0
    for j in range(1, N):
        if parent[j] != parent[target] and parent[parent[j]] == parent[parent[target]]:
            ans += 1

    print(ans)