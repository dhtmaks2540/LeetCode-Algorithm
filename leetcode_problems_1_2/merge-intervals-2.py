from typing import List


class Solution:
    # 정렬로 수행
    # 시간 복잡도 : O(nlogn)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        # 예외처리
        if len(intervals) == 1:
            return intervals

        # 정렬 수행
        intervals.sort(key=lambda interval: interval[0])

        # interval
        temp = intervals[0]

        for i in range(1, len(intervals)):
            # prev interval 사이에 들어간다면
            if temp[0] <= intervals[i][0] <= temp[1]:
                # interval 갱신
                temp = [temp[0], max(intervals[i][1], temp[1])]
            else:
                result.append(temp)
                temp = intervals[i]

            # 마지막 원소라면
            if i == len(intervals) - 1:
                result.append(temp)

        return result

    # 정렬하여 병합
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        # 첫 번째 원소를 기준으로 정렬 수행
        for i in sorted(intervals, key=lambda x: x[0]):
            # 기록된 값이 있고 현재 값의 시작점이 가장 최근 기록된 값의 범위 안에 들어갈 때 갱신
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            # 범위에 들어가지 않는다면 그냥 추가
            else:
                # 콤나는 중첩 리스트로 만들어주는 역할, a += [b]와 같은 역할
                merged += i,

        return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
solution = Solution()
print(solution.merge(intervals))