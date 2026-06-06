class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened_list = []
        for x in matrix:
            flattened_list += x
        left = 0
        n = len(flattened_list)
        right = n-1
        while left<=right:
            mid = left + (right-left) // 2
            if flattened_list[mid] == target:
                return True
            elif flattened_list[mid] > target:
                right=mid-1
            else:
                left = mid+1
        return False
        