import heapq


def solution(jobs):
    ea = len(jobs)
    totalTime = 0
    n = 0
    heapq.heapify(jobs)
    wating = []
    while jobs or wating:
        while jobs and jobs[0][0] <= n:
            tmp = heapq.heappop(jobs)
            heapq.heappush(wating, (tmp[1], tmp[0]))
        if wating:
            tmp = heapq.heappop(wating)
            totalTime += n - tmp[1] + tmp[0]
            n += tmp[0]
        else:
            n = jobs[0][0]
    return totalTime//ea