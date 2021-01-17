# from itertools import permutations
#
# def solution(numbers):
#     answer = ''
#     tmp = list(permutations(numbers,len(numbers)))
#     tmp_permute = [''.join(map(str,i)) for i in tmp]
#     answer = max(tmp_permute)
#     return answer
# 틀린 풀이

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))