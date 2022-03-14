from typing import List
import collections

import sys

class Solution:
    """
    https://leetcode.com/problems/brick-wall/discuss/788421/Python-3-%2B-Dictionary-Explanation
    """
    def leastBricks(self, wall: List[List[int]]) -> int:
        # 값을 누적할 딕셔너리
        brickEndpointsToCount = {}
        
    
        for bricks in wall:
			# Initialise brickEndpoint to 0, i.e. the left-most point of the wall.
            # 벽돌의 EndPoint를 0으로 초기화, 왼쪽부터 누적될 값
            brickEndpoint = 0
            
			# Ignore the very last brick for each row since their endpoints are always the right-most part of the wall.
            # 오른쪽 끝 EndPoint를 제외한 나머지 벽돌을 이터레이션하며
            for i in range(len(bricks) - 1):
                brick = bricks[i]
				# Update the brickEndpoint by adding the length of the current brick in the row.
                # 행의 현재 벽돌의 길이를 EndPoint에 더하여 업데이트하면서
                brickEndpoint += brick
                
				# We've seen this endpoint before, so increment the count.
                # 딕셔너리에 EndPoint가 있다면, 즉 이전에 본 값이라면 count + 1 증가
                if brickEndpoint in brickEndpointsToCount:
                    brickEndpointsToCount[brickEndpoint] += 1
				# This brickEndpoint hasn't been seen before, so initialise the count to 1.
                # 본적이 없다면 1로 초기화
                else:
                    brickEndpointsToCount[brickEndpoint] = 1
        
        # 값만 가져오기
		# Use this assignment to shorten the ternary operator in the return statement.
        counts = brickEndpointsToCount.values()
        print(counts)

		# 벽의 길이에서 최대 EndPoint, 즉 가장 많이 나온 EndPoint를 빼면 가장 적은 벽돌을 뛰어넘을것이기 때문에 이와 같이 계산
		# The solution is the number of rows of bricks (i.e. len(wall)) minus the maximum of the number of rows you can avoid by cutting through a certain brickEndpoint.
        return len(wall) - (max(counts) if counts else 0)

    # 위의 풀이법을 defaultdict를 사용하여 개선
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d = collections.defaultdict(int)
        for bricks in wall:
            brickEndPoint = 0
            for brick in bricks[:-1]:
                brickEndPoint += brick
                d[brickEndPoint] += 1
        # print len(wall), d
        return len(wall)-max(d.values() or [0])

wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
solution = Solution()
print(solution.leastBricks(wall))
