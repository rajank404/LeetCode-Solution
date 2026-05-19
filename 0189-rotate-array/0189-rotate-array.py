class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        l = 0
        h = n-k-1
        while l < h:
            nums[l],nums[h] = nums[h],nums[l]
            l = l + 1
            h = h - 1
        l = n-k
        h = len(nums) - 1
        while l < h:
            nums[l],nums[h] = nums[h],nums[l]
            l = l + 1
            h = h - 1
        l = 0
        h = len(nums)-1
        while l < h:
            nums[l],nums[h] = nums[h],nums[l]
            l = l + 1
            h = h - 1
        return nums


        