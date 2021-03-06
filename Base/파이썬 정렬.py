a = [(1,2),(0,1),(5,1)]

c = sorted(a, key = lambda x : x[0])

## set 사용

a = {1,3,5}
b = {1,2,5}

i = a & b # a와 b의 교집합
u = a | b # a와 b의 합집합

d = a - b # a와 b의 차집합
