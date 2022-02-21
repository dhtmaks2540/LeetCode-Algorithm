from typing import List


class Solution:
    # 이진 탐색을 사용하여 문제 풀이, 시간복잡도는 row * (nlogn) -> O(nlogn)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])

        # Iterate row
        for i in range(row):
            # Binary Search
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

    # 투 포인터를 사용, 시간 복잡도는 row * column
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])

        for i in range(row):
            right = 0
            while right < column:
                if matrix[i][right] == target:
                    return True
                elif matrix[i][right] < target:
                    right += 1
                else:
                    break

        return False

    # 이진 탐색을 이용하여 첫 행의 맨 뒤에서부터 탐색
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
            if target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 아래로 이동
            if target > matrix[row][col]:
                row += 1
        
        return False

    # 파이썬 다운 방식
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)

matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
    ]
target = 5
solution = Solution()
print(solution.searchMatrix(matrix, target))