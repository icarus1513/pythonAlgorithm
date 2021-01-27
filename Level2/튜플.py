import re
## 정규 표현식 이용
def solution(s):
    answer = []
    tmp = s.split(',{')
    tmp.sort(key = len)
    for val in tmp :
        ##문자에서 숫자만 가져오는 정규표현식
        num = re.findall("\d+",val)
        for i in num:
            if int(i) not in answer :
                answer.append(int(i))
    return answer