def check(string):
    return string == string[::-1]

def solution(s):
    answer = 0
    tmp = len(s)
    max_v = -1
    for i in range(tmp):
        for j in range(i,tmp+1):
            if check(s[i:j]):
                if max_v < len(s[i:j]):
                    max_v = len(s[i:j])
    return max_v