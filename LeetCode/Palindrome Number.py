class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            word = str(x)
            if word == word[::-1]:
                return True
            return False

