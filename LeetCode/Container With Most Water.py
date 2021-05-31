class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        i = 0
        r = len(height) - 1
        while (i < r):
            answer = max(answer, min(height[i], height[r]) * (r - i))
            if height[i] < height[r]:
                i += 1
            else:
                r -= 1

        return answer
