# def cntOne(n):
#     cnt = 0
#     while True:
#         if n % 2 != 0:
#             cnt += 1
#         n = n / 2
#         if n == 2 or n == 1:
#             cnt += 1
#             break
#     return cnt
# def solution(n):
#     cnt  = cntOne(n)
#     n += 1
#     while True:
#         if cnt == cntOne(n):
#             break
#         n += 1
#     answer = n
#     return answer

def solution(n):
    c = bin(n).count('1')
    for m in range(n+1,1000001):
        if bin(m).count('1') == c:
            return m
