from typing import List
import bisect

class Solution:
    """
    접근방법
    
    아이들에게 나누어 줄 수 있는 쿠키의 수를 최대로 하기 위해서 크기가 작은 쿠키를
    greedy factor가 작은 아이에게 먼저 나누어주는 방법을 선택
    
    따라서 쿠키와 아이들을 모두 오름차순으로 정렬 후
    cookie를 iterate하며 현재 쿠키 사이즈가 greedy factor를 만족하면 결과변수 증가,
    아니면 다음 쿠키로 넘어가는 방식으로 문제를 풀이하였다.
    
    그리디 알고리즘으로 분류한 이유는 현재의 상황에서 가장 작은 쿠키를 나누어주고 이후의 상황은 
    상관하지 않기에 그리디 알고리즘으로 분류했다고 생각한다.
    """
    # 두 리스트를 모두 오름차순으로 정렬한 후 
    # 쿠키의 크기가 작은 
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 결과 변수
        count = index = 0
        n = len(g)
        
        # 정렬
        g.sort()
        s.sort()
        
        for cookie in s:
            if cookie >= g[index]:
                count += 1
                index += 1
                
            if index > n - 1:
                break
            
        return count
    
    # 책의 그리디 알고리즘 풀이
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child_i = cookie_j = 0
        # 만족하지 못할 때까지 그리디 진행
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
            
        return child_i
    
    # 책의 이진 검색 풀이
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
        
g = [1,2]
s = [1,2,3]
solution = Solution()
print(solution.findContentChildren(g, s))