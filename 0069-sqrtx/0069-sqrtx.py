class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        h = x
        ans = 1
        while l <= h:
            mid = l+(h-l)//2
            temp = mid*mid
            if temp == x:
                return mid
            elif temp < x:
                l = mid + 1
                ans = mid
            else:
                h = mid - 1

        return ans
        