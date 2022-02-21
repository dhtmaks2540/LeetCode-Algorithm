from typing import List

# 각 행은 왼쪽에서 오른쪽으로 오름 차순
# 각 행의 첫 번째 숫자는 이전 행의 마지막 숫자보다 더 크다
class Solution
    # 조건을 활용하여 첫 행의 맨 뒤에서부터 탐색(투 포인터..)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        column = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and column >= 0:
            if matrix[row][column] == target:
                return True
            # target보다 크면 왼쪽으로 이동
            elif matrix[row][column] > target:
                column -= 1
            # target보다 작으면 아래로 이동
            else:
                row += 1

        return False

    # 이진탐색을 활용하여 풀이
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, column = len(matrix), len(matrix[0])

        for i in range(row):
            left, right = 0, column - 1

            while left <= right:
                mid = left + (right - left) // 2

                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        return False

    """
    https://leetcode.com/problems/search-a-2d-matrix/discuss/26220/Don't-treat-it-as-a-2D-matrix-just-treat-it-as-a-sorted-list
    
    현재 행의 첫 번째 열이 마지막 행의 마지막 열의 값보다 크므로 생각해보면 길게 쭉 펼쳐진 sorted list라 생각하면 편하다.
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # exit condition
        if not matrix:
            return False

        # Binary Search
        left, rows, cols = 0, len(matrix), len(matrix[0])
        right = rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid // cols][mid % cols] == target:
                return True
            elif matrix[mid // cols][mid % cols] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

            
matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
    ]
target = 13
solution = Solution()
print(solution.searchMatrix(matrix, target))