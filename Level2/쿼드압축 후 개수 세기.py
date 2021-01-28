from itertools import chain


def zip(arr):
    arr_len = len(arr)
    unit = arr_len // 2
    arr_sum = sum(chain(*arr))

    if arr_len == 1:
        return [arr[0][0]]
    elif arr_sum == arr_len * arr_len:
        return [1]
    elif arr_sum == 0:
        return [0]
    arr1, arr2, arr3, arr4 = (
        [ar[0:unit] for ar in arr[0:unit]],
        [ar[unit:] for ar in arr[0:unit]],
        [ar[0:unit] for ar in arr[unit:]],
        [ar[unit:] for ar in arr[unit:]],
    )
    result = zip(arr1) + zip(arr2) + zip(arr3) + zip(arr4)
    return list(chain(result))


def solution(arr):
    answer = []
    answer = zip(arr)

    return [answer.count(0), answer.count(1)]