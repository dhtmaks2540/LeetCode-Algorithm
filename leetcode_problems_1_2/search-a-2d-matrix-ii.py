from typing import List

import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 행을 나타내는 인덱스
        i = 0

        while i <= len(matrix) - 1:
            left = 0
            right = len(matrix[0]) - 1
            while left <= right:
                mid = left + (right - left) // 2

                if matrix[i][mid] > target:
                    right = mid - 1
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    return True
            i += 1
        return False

    # 첫 행의 맨 뒤에서 탐색
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 예외 처리
        if not matrix:
            return False

        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 오른쪽으로 이동
            elif target > matrix[row][col]:
                row += 1
        return False

    # 파이썬 다운 방식
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

solution = Solution()
print(solution.searchMatrix(matrix, target))