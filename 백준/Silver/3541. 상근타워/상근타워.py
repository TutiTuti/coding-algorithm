import sys
import math 
n, m = map(int, sys.stdin.readline().split())
elevators = []
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    elevators.append((a,b))


tmp = []

for elevator in elevators:
    current = 0
    lcm = math.lcm(elevator[0], elevator[1])
    k =( n % (lcm //elevator[0] + lcm //elevator[1])) + lcm //elevator[0] + lcm //elevator[1]

    for j in range(k):
        if current > elevator[1] : 
            current -= elevator[1]
        else :
            current += elevator[0]

    tmp.append(current)

print(min(tmp))