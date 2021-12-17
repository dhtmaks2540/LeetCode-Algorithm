from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 결과용 변수
        merged = []
        # 첫 번째 키를 기준으로 정렬
        for i in sorted(intervals, key=lambda x: x[0]):
            # 다음 아이템의 시작 값이 이전 아이템의 끝 값 이하라면(즉, 겹친다면)
            if merged and i[0] <= merged[-1][1]:
                # 이전 아이템의 끝 값을
                # 이전 아이템의 끝 값과 다음 아이템의 끝 값중 더 큰 값으로 교체
                merged[-1][1] = max(merged[-1][1], i[1])
            # 겹치지 않는다면 단지 추가
            else:
                merged += i,
        return merged
          
intervals = [[1,3],[2,6],[8,10],[15,18]]
solution = Solution()
solution.merge(intervals)