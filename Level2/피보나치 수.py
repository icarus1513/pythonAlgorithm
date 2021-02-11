def solution(n):
    answer = 0
    tmp = [0] * (n+1)
    tmp[1] = 1
    for i in range(2,n+1):
        tmp[i] = (tmp[i-1] + tmp[i-2])%1234567
    return tmp[n]