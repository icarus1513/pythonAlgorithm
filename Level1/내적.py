def solution(a, b):
    answer = 1234567890
    arr = []
    for i in range(len(a)):
        tmp1 = int(a[i])
        tmp2 = int(b[i])
        arr.append(tmp1 * tmp2)

    answer = sum(arr)
    return answer