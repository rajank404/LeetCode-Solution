class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # M - 1 == using the XOR operation 

        ans = 0
        for i in range(len(nums)):
            ans = ans ^ nums[i]
        return ans

        # M - 2 == also solve by using the concept of dictionary

        