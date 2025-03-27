import math;
n, m = map(int, input().split())
answer = 1_000_000 * 1_000_000


for _ in range(m):
    u, d = map(int, input().split())
    floor = 0
    lcm = math.lcm(u, d)
    k =( n % (lcm //u + lcm //d)) + lcm //u + lcm //d

    for _ in range(k):
        if floor > d:
            floor -= d
        else:
            floor += u
    answer = min(answer, floor)

print(answer)