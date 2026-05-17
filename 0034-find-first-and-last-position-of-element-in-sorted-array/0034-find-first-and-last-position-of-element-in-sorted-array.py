class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:

        l = 0
        h = len(arr)-1
        first = -1
        while l <= h:
            mid = l + (h-l)//2
            if arr[mid] == target:
                first = mid
                h = mid - 1
            elif arr[mid] > target:
                h = mid - 1
            else:
                l = mid + 1


        l = 0
        h = len(arr)-1
        last = -1
        while l <= h:
            mid = l + (h-l)//2
            if arr[mid] == target:
                last = mid
                l = mid + 1
            elif arr[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        if last == -1:
            return [-1,-1]
        else:
            return [first,last]

        

        
     
        
        