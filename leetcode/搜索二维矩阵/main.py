"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

示例 1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

示例 2：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
"""


class Solution:
    """双重二分"""

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left1, right1 = 0, len(matrix)-1
        while left1 <= right1:
            mid1 = (left1+right1) // 2
            if matrix[mid1][len(matrix[mid1])-1] >= target and matrix[mid1][0] <= target:
                break
            elif matrix[mid1][len(matrix[mid1])-1] < target:
                left1 = mid1+1
            elif matrix[mid1][0] > target:
                right1 = mid1 - 1
        left2, right2 = 0, len(matrix[mid1])-1
        while left2 <= right2:
            mid2 = (left2+right2) // 2
            if matrix[mid1][mid2] == target:
                return True
            elif matrix[mid1][mid2] > target:
                right2 = mid2 - 1
            else:
                left2 = mid2 + 1
        return False
