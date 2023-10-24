import sys;
input = sys.stdin.readline
import heapq
def prim(s):
    c=0
    tmpans = 0
    Q = [[0, s]]
    vstd = [0]*(V+1)
    while c != V:
        weight, s = heapq.heappop(Q)
        if vstd[s]:
            continue
        vstd[s] = 1
        tmpans += weight
        c += 1
        for i in arr[s]:
            heapq.heappush(Q, i)
    return tmpans


V, E = map(int, input().split())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a].append([c, b])
    arr[b].append([c, a])
print(prim(1))
