def solution(brown, yellow):
    answer = []
    area = brown + yellow
    width = 0
    height = 0
    print(int(area ** 0.5))
    for h in range(3, int(area ** 0.5) + 1):
        if area % h == 0:
            if (h - 2) * ((area / h) - 2) == yellow:
                height = h
                width = area // h
    return [width, height]