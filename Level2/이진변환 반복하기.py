from collections import Counter
def solution(s):
    tmp, cnt = 0,0
    while s != "1":
        cnt += 1
        tmp += Counter(s)['0']
        s = str(bin(int(Counter(s)['1']))).replace("0b","")
    return [cnt,tmp]