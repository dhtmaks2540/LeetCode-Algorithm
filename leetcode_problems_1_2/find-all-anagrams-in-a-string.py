from typing import List
import collections

class Solution:
    # 슬라이딩 윈도우와 정렬을 사용
    # 시간복잡도는 O(nlogn) -> 시간 초과
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []

        # 정렬 수행
        p = sorted(p)

        i = 0
        j = len(p)

        while j <= len(s):
            if sorted(s[i:j]) == p:
                result.append(i)
                i += 1
                j += 1
            

        return result

    """
    https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/1737985/Python3-SLIDING-WINDOW-%2B-HASH-TABLE-Explained
    
    Sliding Window + Hash Table 사용

    Sliding Window를 사용하여 인덱스를 한 칸씩 증가시키고
    Hash Table에 찾으려는 값을 기록한 후 비교하며 문제 풀이
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        counts, res, pL, sL = collections.defaultdict(int), [], len(p), len(s)

        # 예외처리
        if pL > sL: return []

        # p의 글자 빈도수 hashmap으로 기록
        for ch in p:
            counts[ch] += 1

        # p-1번째 글자까지 초기화
        for i in range(pL - 1):
            if s[i] in counts:
                counts[s[i]] -= 1

        # slide the window with stride 1
        for i in range(-1, sL - pL + 1):
            # 제외되는 인덱스
            if i > -1 and s[i] in counts:
                counts[s[i]] += 1
            # 추가되는 인덱스
            if i + pL < sL and s[i + pL] in counts:
                counts[s[i + pL]] -= 1

            # dict에 기록된 값이 모두 0이라면 anagram에 해당
            if all(v == 0 for v in counts.values()):
                res.append(i + 1)

        return res

    """
    https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/1738052/A-very-deep-EXPLANATION-oror-Solved-without-using-HashTable
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # x와 y가 같은지 비교
        def areSame(x, y):
            for i in range(len(x)):
                if x[i] != y[i]:
                    return False

            return True

        # 배열을 생성('a' ~ 'z' 까지 기록)
        def freq(s):
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
            
            return count

        result = []

        # 예외처리
        if len(p) > len(s):
            return result

        n = len(s) 
        m = len(p)

        count = freq(p)
        currentCount = freq(s[:m])

        # p 문자열의 길이 우선 검사
        if areSame(count, currentCount):
            result.append(0)

        # p문자열 이후로
        for i in range(m, n):
            # 제외되는 인덱스
            currentCount[ord(s[i-m]) - ord('a')] -= 1
            # 추가되는 인덱스
            currentCount[ord(s[i]) - ord('a')] += 1
            # 같은지 비교
            if areSame(count, currentCount):
                result.append(i-m + 1)

        return result
        

s = "cbaebabacd"
p = "abc"
# s = "abab"
# p = "ab"
solution = Solution()
print(solution.findAnagrams(s, p))