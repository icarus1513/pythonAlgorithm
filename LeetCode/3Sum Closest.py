from itertools import combinations
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # answer = 0
        # comb = list(combinations(nums,3))
        # tmp = set()
        # val = set()
        # for i in comb :
        #     tmp.add(sum(i) - target)
        # tmp = sorted(tmp, key = lambda x : abs(x))
        # answer = tmp[0] + target
        # return answer
        # 투 포인터 사용하기
        diff = float('inf')
        nums.sort()
        for idx, val in enumerate(nums):
            left, right = idx + 1, len(nums) - 1
            while left < right:
                tmp = val + nums[left] + nums[right]
                if abs(target - tmp) < abs(diff):
                    diff = target - tmp
                if tmp > target:
                    right -= 1
                else:
                    left += 1
            if diff == 0:
                break
        return target - diff