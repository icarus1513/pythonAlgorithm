def solution(s):
    answer = ''
    tmp = list(map(int,s.split()))
    tmp.sort()
    answer = '{} {}'.format(tmp[0],tmp[-1])
    print(answer)
    return answer