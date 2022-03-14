from re import T
from typing import List


import heapq

class Solution:
    # Greedy와 우선순위 큐를 이용하여 풀이
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        q = []

        # 전체 시간
        total_time = 0
        # 결과변수
        count = 0

        # last_day로 courses 정렬
        courses.sort(key=lambda course: (course[1], course[0]))

        for duration, last_day in courses:
            # 총 시간과 현재 강의 시간을 더한 값이 종료일 이하라면
            if total_time + duration <= last_day:
                total_time += duration
                heapq.heappush(q, (-duration, last_day))
            else: # 종료일 초과일 때
                # 우선순위 큐에 들은 기간이 가장 큰 값이 현재의 기간보다 크다면
                while q and -q[0][0] > duration:
                    # 교체작업
                    now = heapq.heappop(q)
                    total_time += now[0]
                    heapq.heappush(q, (-duration, last_day))
                    total_time += duration
        
        # 우선순위 큐에 들어간 값만큼 count 증가
        while q:
            heapq.heappop(q)
            count += 1

        return count

    """
    https://leetcode.com/problems/course-schedule-iii/discuss/104847/Python-Straightforward-with-Explanation
    """
    
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        q = []
        start = 0
        # 끝나는 시간으로 정렬
        for duration, end in sorted(courses, key = lambda course: (course[1])):
            # 현재 시간 추가
            start += duration
            # 우선순위 큐에 추가
            heapq.heappush(q, -duration)
            # 총 시간이 끝나는 시간보다 크다면
            while start > end:
                # 가장 큰 값 빼기
                start += heapq.heappop(q)

        return len(q)

    """
    https://leetcode.com/problems/course-schedule-iii/discuss/1187509/Python-Greedy-dp-with-proof-explained
    """

    def scheduleCourse(self, courses):
        heap, time = [], 0
        # 끝나는 시간으로 정렬
        for t, end in sorted(courses, key=lambda x: x[1]):
            # 현재 시간 추가
            time += t
            # 우선순위 큐에 추가
            heapq.heappush(heap, -t)
            if time > end:
                # 총 시간이 끝나는 시간보다 크다면
                nt = heapq.heappop(heap)
                # 가장 큰 값 빼기
                time += nt
        return len(heap)
    

courses = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]
solution = Solution()
print(solution.scheduleCourse(courses))