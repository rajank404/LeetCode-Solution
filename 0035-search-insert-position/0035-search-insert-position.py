class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        l = 0
        h = len(arr)-1
        ans = len(arr)
        while l <= h:
            mid = l + (h-l)//2
            if arr[mid] >= target:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans
        