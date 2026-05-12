class Solution:
    def reverse(self, x: int) -> int:
        int_min = -2**31
        int_max = 2**31 - 1
        result = 0
        n_isneg = x < 0
        if n_isneg:
            x = - x
        while x > 0:
            digit = x % 10
            result = result * 10 + digit
            x = x // 10
            if result > int_max or result < int_min:
                return 0
        if n_isneg:
            result = -result
        return result
		    
        