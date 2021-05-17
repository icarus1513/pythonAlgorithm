class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        median = 0
        length = len(nums)
        if length % 2 == 0:
            print(nums)
            median = (nums[int(length / 2) - 1] + nums[int(length / 2)]) / 2
        else:
            median = nums[int(length / 2)]
        return median
