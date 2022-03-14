from typing import List

# 0 point에서 시작해서 matrix에서 얻을 수 있는 point를 최대로 하라.
# point를 얻기 위해서 각 행에서 하나의 cell을 선택해야한다.
# 다만 인접한 row(r, r+1)에 있어서 (r, c1), (r + 1, c2)의 point를 더할 때 abs(c1 - c2)를 빼야한다.
class Solution:
    """
    처음접근

    현재 matrix에서 각 row의 point중 최댓값을 획득하여 반환하라기에 값을 기록하기 위해서 DP로 문제를 접근함
    다만, 현재 인덱스에서 최대로 획득할 수 있는 포인트는 단지 이전 row point중 최댓값이 아닌
    현재 인덱스와 이전 row의 인덱스의 차를 빼고 계산해야 하기에 for문을 총 세 번 사용해서 접근함
    당연히 시간 복잡도가 O(n*3)이기에 시간 초과가 뜸

    문제의 풀이를 잘못 생각함.
    """

    # DP를 이용하여 문제풀이
    # 현재 위치에서 
    def maxPoints(self, points: List[List[int]]) -> int:
        row = len(points)
        column = len(points[0])
        dp = [[0] * column for _ in range(row)]

        # 첫 번째 행을 초기화(값과 인덱스를 기록)
        for i in range(column):
            dp[0][i] = (points[0][i], i)

        for i in range(1, row):
            for j in range(column):
                max_value = 0
                for k in range(column):
                    value, index = dp[i-1][k]
                    max_value = max(max_value, value - abs(index - j))
                dp[i][j] = (max(points[i][j], points[i][j] + max_value), j)

        max_value = 0

        for i in range(row):
            max_value = max(dp[i])

        return max_value[0]

    """"
    https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344908/C%2B%2BJavaPython-3-DP-Explanation-with-pictures-O(MN)-Time-O(N)-Space
    
    풀이방법

    위와 같은 경우는 현재의 위치에서 매번 인덱스에 대해서 값을 계산하기에 O(n*3)에 달하는 시간복잡도가 발생
    그것을 해결하기 위해 왼쪽부터 값을 접근하는 lft와 오른쪽부터 값을 접근하는 rgt를 사용하여 DP를 풀이
    
    우선, 이전의 값은 풀었다고 가정하여 prev라는 변수에 현재 row(x + 1)의 이전의 row(x)를 저장
    lft(left)의 첫 번째 인덱스는 더 작은 값이 없기에 prev[0]를 통해 접근할 수 밖에 없다.
    그 이후의 인덱스는 현재의 인덱스 값(prev[i]) 그대로 가져오던가 이전의 값(lft[i - 1])에서 
    인덱스의 차이에 따른 -1을 한 값 중 최댓값을 가져와야 한다.
    
    즉, lft[i] = max(prev[i] - lft[i - 1] - 1)에 해당한다.
    그 이후의 값들도 똑같은 점화식을 가지고 사용하는데 더 이전의 값들은 생각하지 않나면
    DP의 기본적인 개념 중 하나로 이미 계산을 했기에(예를들어 lft[2]를 계산할 때 lft[0]의 값은 lft[1]을 계산할 때 계산됨)
    단지 이전의 인덱스 값을 가져와서 비교해주면 된다.

    오른쪽도 왼쪽과 마찬가지 개념으로 오른쪽 인덱스(n-1)부터 0번 인덱스까지 계산해주면 된다.
    rgt[n-1]은 prev[n-1] 값 그대로 가져오고
    rgt[n-2]는 현재의 값(prev[n - 2]) 또는 rgt[n - 1] - 1 중 최댓값을 기록하면 되는 것이다.

    이와같이 현재 row의 lft와 rgt가 모두 계산되었다면
    현재 row(x + 1)의 값은 현재 row의 cell의 값을 더하고 lft 또는 rgt의 값 중 최댓값을 더해주면 된다.

    """

    # DP로 문제를 접근
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        # 예외처리
        if m == 1: return max(points[0])
        if n == 1: return sum(sum(x) for x in points)

        # the maximum value from the left
        # 왼쪽부터 계산
        def left(arr):
            lft = [arr[0]] + [0] * (n - 1)
            # 첫 번째 인덱스부터 마지막 인덱스까지 최댓값 생성
            for i in range(1, n): lft[i] = max(lft[i - 1] - 1, arr[i])
            return lft

        # the maximum value from the right
        # 오른쪽부터 계산
        def right(arr):
            rgt = [0] * (n - 1) + [arr[-1]]
            # 마지막 인덱스부터 첫 번째 인덱스까지 최댓값 생성
            for i in range(n - 2, -1, -1): rgt[i] = max(rgt[i + 1] - 1, arr[i])
            return rgt

        # pre 변수
        pre = points[0]
        for i in range(m - 1):
            lft, rgt, cur = left(pre), right(pre), [0] * n
            # 한 행을 방문하며
            for j in range(n):
                # 현재 행의 최댓값 = 현재 행의 point + left[j]와 rgt[j]의 최댓값
                cur[j] = points[i + 1][j] + max(lft[j], rgt[j])
            # update cur as pre
            pre = cur[:]

        return max(pre)        
        
points = [[1,2,3],[1,5,1],[3,1,1]]
solution = Solution()
print(solution.maxPoints(points))