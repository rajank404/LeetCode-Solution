class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_copy = x
        result = 0

        while x > 0:
            digit = x % 10
            result = result * 10 +  digit
            x = x // 10
        if x_copy == result:
            return True
        return False
        

        