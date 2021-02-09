def solution(n):
    answer = 0
    for i in range(1,n+1):
        nsum = 0
        for j in range(i,n+1):
            nsum += j
            if nsum == n:
                answer+= 1
                break
            elif nsum > n:
                break
    return answer