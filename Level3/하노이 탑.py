def hanoi(n, start, end,tmp,answer):
    if n == 1:
        answer.append([start,end])
        return
    hanoi(n-1, start, tmp, end,answer)
    answer.append([start,end])
    hanoi(n-1, tmp, end,start,answer)
def solution(n):
    answer = []
    hanoi(n,1,3,2,answer)
    return answer