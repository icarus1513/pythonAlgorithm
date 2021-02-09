def solution(nums):
    answer = 0
    size = len(nums) / 2
    cnt = 1
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            cnt += 1

    if size <= cnt:
        answer = size
    else:
        answer = cnt

    return answer