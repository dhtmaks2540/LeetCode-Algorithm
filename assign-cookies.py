from typing import List

import bisect


class Solution:
    # 그리디 알고리즘을 사용하여 풀이
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 사람이 없거나 쿠키가 없으면
        if not g or not s:
            return 0

        # 정렬 수행
        g.sort(reverse = True)
        s.sort()      

        # 결과 변수
        result = 0

        for value in g:
            if s and value <= s[-1]:
                result += 1
                s.pop()

        return result

    # 그리디 알고리즘을 사용하여 풀이
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i = cookie_j = 0
        # 만족하지 못할 때까지 그리디 진행
        # 앞에서부터 진행(작은 값부터)
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j +=1

        return child_i

    # 이진 검색을 활용
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        for i in s:
            # 이진 검색으로 더 큰 인덱스 탐색
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1

        return result
    
g = [1,2,3]
s = [3]
solution = Solution()
print(solution.findContentChildren(g, s))