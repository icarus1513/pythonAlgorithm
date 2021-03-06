import heapq


def solution(A, B):
    answer = 0
    if min(A) > max(B):
        return 0
    A.sort(reverse=True)
    B = [-i for i in B]
    heapq.heapify(B)

    count = 0
    for i in A:
        if i >= abs(B[0]):
            continue
        else:
            heapq.heappop(B)
            count += 1
    return count

    return answer