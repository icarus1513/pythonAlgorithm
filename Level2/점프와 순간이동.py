def solution(n):
    ans = 0
    cnt = 0
    while True:
        if n == 1:
            cnt += 1
            break
        elif n % 2 == 0:
            n = n/2
        else :
            n = (n-1)/2
            cnt += 1
    return cnt