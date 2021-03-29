from collections import Counter

ex = Counter("Hello world")
##{'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

ex.most_common()
##[('l',3)]

ex.update("Hello world")
##{'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1} * 2

## subtract 각 요소들을 빼기
## elements 카운터 숫자만큼 요소 반환