from typing import List
import collections

class Solution:
    """
    https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/discuss/1675343/Python3-Java-C%2B%2B-Counting-Mirror-Words-O(n)
    
    2 letter words can be of 2 types:

    1. Where both letters are same
    2. Where both letters are different
    
    * If we are able to find the mirror of a word, ans += 4
    * The variable unpaired is used to store the number of unpaired words with both letters same.
    * Unpaired here means a word that has not found its mirror word.
    * At the end if unpaired same letter words are > 0, we can use one of them as the center of the palindromic string.
    
    * 그 자체로 팰린드롬인 단어(aa)는 같은 값이 나오지 않는 이상 팰린드롬의 가운데로만 들어갈 수 있음
    * 따라서 unpaired라는 변수는 같은 값이 나오면 빼고 아니면 남기기 위해 사용하는 변수
    * 그 자체로 팰린드롬이 아닌 단어(ab)는 팰린드롬이 기록되었으면 갱신만 해주면 됨
    """
    
    # HashMap 사용
    def longestPalindrome(self, words: List[str]) -> int:
        m = collections.defaultdict(int)
        unpaired = ans = 0
        for word in words:
            # 그 단어 자체만으로 팰린드롬일 경우
            if word[0] == word[1]:
                # 기록된 값이 있으면(gg, gg 같은 경우)
                if m[word] > 0:
                    # 갱신
                    unpaired -= 1
                    m[word] -= 1
                    ans += 4
                else:
                    # 기록
                    m[word] += 1
                    unpaired += 1
            else:
                # 팰린드롬이 기록됐으면
                if m[word[::-1]] > 0:
                    # 갱신
                    ans += 4
                    m[word[::-1]] -= 1
                else:
                    # 기록
                    m[word] += 1
        # 그 자체로 팰린드롬인 단어가 있으면
        if unpaired > 0: ans += 2
        return ans
    
    # without HashMap
    def longestPalindrome(self, words: List[str]) -> int:
        # 2차원 배열
        counter, ans = [[0] * 26 for _ in range(26)], 0
        
        for word in words:
            a, b = ord(word[0]) - ord('a'), ord(word[1]) - ord('a')
            # 팰린드롬이 존재한다면
            if counter[b][a]:
                # 갱신
                ans += 4
                counter[b][a] -= 1
            else:
                # 기록
                counter[a][b] += 1
        # 그 자체로 팰린드롬인 단어 확인(하나만 기록 가능)
        for i in range(26):
            if counter[i][i]:
                ans += 2
                break
        
        return ans
                     
words = ["lc","cl","gg"]
solution = Solution()
print(solution.longestPalindrome(words))