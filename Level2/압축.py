from string import ascii_uppercase


def lzw(w, dic, msg):
    idx = dic.index(w)
    if msg:
        dic.append(w + msg[0])

    return idx + 1, dic


def solution(msg):
    answer = []
    dict = list(ascii_uppercase)

    while msg:
        tmp = ''
        idx = 0
        for i in range(1, len(msg) + 1):
            if msg[:i] in dict:
                tmp = msg[:i]
                idx = i
            else:
                break
        msg = msg[idx:]
        ans, dict = lzw(tmp, dict, msg)
        answer.append(ans)
    return answer