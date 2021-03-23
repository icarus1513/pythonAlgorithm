import heapq


def solution(n, works):
    for i in range(len(works)):
        works[i] *= -1

    heapq.heapify(works)

    for i in range(n):
        m = heapq.heappop(works)
        if m >= 0:
            break
        m += 1
        heapq.heappush(works, m)

    answer = 0
    for i in range(len(works)):
        answer += pow(works[i] * -1, 2)

    return answer