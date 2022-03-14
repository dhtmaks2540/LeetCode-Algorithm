import collections
from typing import List

# T의 모든 글자를 포함하는 minimum s의 substring
class Solution:
    # 브루드 포스로 접근 -> Time Limit Exceed
    def minWindow(self, s: str, t: str) -> str:
        def contains(s_substr_lst: List, t_lst: List):
            for t_elem in t_lst:
                if t_elem in s_substr_lst:
                    s_substr_lst.remove(t_elem)
                else:
                    return False
            
            return True

        if not s or not t:
            return ''

        window_size = len(t)

        for size in range(window_size, len(s) + 1):
            for left in range(len(s) - size + 1):
                s_substr = s[left:left + size]
                if contains(list(s_substr), list(t)):
                    return s_substr

        return ''

    # 투 포인터, 슬라이딩 윈도우로 최적화
    def minWindow(self, s: str, t: str) -> str:
        # 필요한 문자 각각의 개수
        need = collections.Counter(t)
        # 팔요한 문자의 전체 개수
        missing = len(t)
        left = start = end = 0

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단(더 줄일 수 있는지)
            if missing == 0:
                # 필요없는 문자를 가지고 있는지 판단(음수면 쓸모없는 문자)
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                # update window
                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1

        return s[start:end]

    # 투 포인터, 슬라이딩 윈도우 활용
    def minWindow(s, t):
        need = collections.Counter(t)            #hash table to store char frequency
        missing = len(t)                         #total number of chars we care
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):          #index j from 1
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:                     #match all chars
                while i < j and need[s[i]] < 0:  #remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
                missing += 1                     #we missed this first char, so add missing by 1
                if end == 0 or j-i < end-start:  #update window
                    start, end = i, j
                i += 1                           #update i to start+1 for next window
        return s[start:end]


    # Counter를 활용
    def minWindow(self, s: str, t: str) -> str:
        t_count = collections.Counter(t)
        current_count = collections.Counter()

        start = float('-inf')
        end = float('-inf')

        left = 0
        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            current_count[char] += 1

            # AND 연산 결과로 왼쪽 포인터 이동 판단
            while current_count & t_count == t_count:
                if right - left < end - start:
                    start, end = left, right

                current_count[s[left]] -= 1
                left += 1

        return s[start:end] if end - start <= len(s) else ""

s = "ADOBECODEBANC"
t = "ABC"
solution = Solution()
print(solution.minWindow(s, t))