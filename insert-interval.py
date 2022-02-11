from typing import List


class Solution:
    # 정렬하여 병합
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # newInterval 추가
        intervals.append(newInterval)
        # 정렬 수행
        intervals.sort(key= lambda interval: interval[0])
        # 결과변수
        result = []

        for interval in intervals:
            # 현재 interval의 시작 시간이 가장 최근에 기록된 interval의 끝나는 시간안에 들어가면
            if result and interval[0] <= result[-1][1]:
                # 갱신
                result[-1][1] = max(result[-1][1], interval[1])
            # 그렇지 않다면
            else:
                # 추가
                # ,로 인해서 result += [interval]과 같음
                result += interval,

        return result

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
solution = Solution()
print(solution.insert(intervals, newInterval))