
q = map(int, input().split())
sum = 0
for i in q:
    sum += (i * i)
print(sum % 10)