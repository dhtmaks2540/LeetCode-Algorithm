from typing import List
import collections

class Solution:
    # 브루드 포스로 접근
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] + words[j] == (words[i] + words[j])[::-1]:
                    result.append([i, j])

                if words[j] + words[i] == (words[j] + words[i])[::-1]:
                    result.append([j, i])

        return result

# 트라이를 저장할 노드
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []

"""
1. 끝까지 탐색했을 때 word_id가 있는 경우
2. 끝까지 탐색했을 때 palindrome_word_ids가 있는 경우
3. 탐색 중간에 word_id가 있고 나머지 문자가 팰린드롬인 경우
"""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 자바의 static과 비슷
    @staticmethod
    def is_palindrome(word):
        return word[::] == word[::-1]

    # 단어 삽입
    def insert(self, index, word):
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index, word):
        result = []
        node = self.root

        while word:
            # 판별 로직 - 3
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        # 판별 로직 - 1
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 판별 로직 - 2
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results

"""
https://leetcode.com/problems/palindrome-pairs/discuss/79210/The-Easy-to-unserstand-JAVA-Solution

There are several cases to be considered that isPalindrome(s1 + s2)

Case1 : If s1 is a blank string, then for any string that is palindrome s2, s1+s2 and s2+s1 are palindrome.
Case1 : s1이 빈 문자열이고, s2가 팰린드롬이라면 s1+s2와 s2+s1은 팰린드롬

Case2 : If s2 is the reversing string of s1, then s1+s2 and s2+s1 are palindrome.
Case2 : 만약 s2가 s1을 뒤집은 문자라면, s1+s2와 s2+s1은 팰린드롬

Case 3 : If s1[0:cut] is palindrome and there exists s2 is the reversing string of s1[cut+1:] , then s2+s1 is palindrome.
Case 3 : 만약 s1[0:cut]이 팰린드롬이고, s2가 s1[cur+1:]을 뒤집은 문자라면, s2+s1는 팰린드롬

Case 4 : Similiar to case3. If s1[cut+1: ] is palindrome and there exists s2 is the reversing string of s1[0:cut] , then s1+s2 is palindrome.
Case 4 : case3와 비슷하게 s1[cut+1:]이 팰린드롬이고 s2가 s1[0:cut]을 뒤집은 문자라면 s1+s2는 팰린드롬
"""

class Solution:
    def palindromePairs(self, words):
    
        if not words: return []
        
        isPalindrome = lambda x: x == x[::-1]
        
        d = {}
        for i in range(len(words)):
            d[words[i]] = i
        
        res = []
        
        # If "" in words, add all palindrome words into res
        if "" in d:
            blankIndex = d[""]
            for i in range(len(words)):
                if i != blankIndex and isPalindrome(words[i]):
                    res.append([blankIndex, i])
                    res.append([i, blankIndex])
        
        # For every word in words, if word[::-1] is also in words, then [word, word[::-1]] makes a palindrome pair
        for i in range(len(words)):
            revWord = words[i][::-1]
            if revWord in d and d[revWord] != i:
                res.append([i, d[revWord]])
        
        # If s1[:cut] is a palindrome, and s1[cut:][::-1] in d, then (s2, s1) is a palindrome pair. If s1[cut:] is a palindrome and s1[cut:][::-1] in d, then (s1, s2) is a palindrome pair.
        for i in range(len(words)):
            cur_word = words[i]
            for cut in range(1, len(cur_word)):
                cut_l = cur_word[:cut]
                cut_r = cur_word[cut:]
                rev_cut_l = cut_l[::-1]
                rev_cut_r = cut_r[::-1]
                
                if isPalindrome(cut_l):
                    if rev_cut_r in d and rev_cut_r != i:
                        res.append([d[rev_cut_r], i])
                
                if isPalindrome(cut_r):
                    if rev_cut_l in d and rev_cut_l != i:
                        res.append([i, d[rev_cut_l]])
        return res

words = ["abcd","dcba","lls","s","sssll"]
solution = Solution()
print(solution.palindromePairs(words))