def solution(s):
    answer = ''
    s_len = len(s)
    if s_len % 2 == 0:
        mid = (int)(s_len / 2) - 1
        answer = s[mid:mid+2]
    elif s_len % 2 == 1 :
        mid = (int)(s_len / 2)
        answer = s[mid]
    return answer