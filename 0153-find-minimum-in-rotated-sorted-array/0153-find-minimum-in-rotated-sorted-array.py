class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        ans = 100000
        while l <= h:
            mid = l + (h-l)//2
            if nums[l] <= nums[mid]:
                ans = min(ans,nums[l])
                l = mid + 1
            elif nums[mid] <= nums[h]:
                ans = min(ans,nums[mid])
                h = mid - 1
        return ans
        