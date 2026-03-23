class Solution:
    def rotate(self, arr: List[int], d: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        d = d % n
        i = 0
        j = n - d - 1
        while i < j:
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 1
            j = j - 1
        i = n - d
        j = n-1
        while i < j:
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 1
            j = j - 1
        i = 0
        j = n - 1
        while i < j:
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 1
            j = j - 1
        return arr
        