class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        high, low = 0, row - 1
        targetRow = -1
        while high <= low:
            mid = high + (low - high) // 2
            if target > matrix[mid][-1]:
                high = mid + 1
            elif target < matrix[mid][0]:
                low = mid - 1
            else:
                targetRow = mid
                break
        if targetRow == -1:
            return False

        l, r = 0, col - 1
        while l <= r:
            mid = l + (r - l)//2
            if target > matrix[targetRow][mid]:
                l = mid + 1
            elif target < matrix[targetRow][mid]:
                r = mid - 1
            else:
                return True

        return False