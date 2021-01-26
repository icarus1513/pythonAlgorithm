import heapq

def solution(scoville, K):
    answer = 0
    tmp = []
    for i in scoville:
        heapq.heappush(tmp,i)
    while tmp[0] < K:
        try:
            heapq.heappush(tmp,heapq.heappop(tmp)+(heapq.heappop(tmp)*2))
        except IndexError:
            return -1
        answer += 1
    return answer