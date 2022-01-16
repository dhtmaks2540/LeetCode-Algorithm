from typing import List
import collections

class Solution:
    # 딕셔너리를 사용해서 접근
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dict = {}
        # 딕셔너리로 변경
        for root in dictionary:
            dict[root] = root
        
        sentence = sentence.split(" ")

        for index, sen in enumerate(sentence):
            # 한 단어의 길이만큼 이터레이션
            for i in range(len(sen)):
                temp = sen[:i + 1]
                # 값이 dict에 있다면
                if temp in dict:
                    # 변경 후 break
                    sentence[index] = dict[temp]
                    break

        return " ".join(sentence)

    """
    https://leetcode.com/problems/replace-words/discuss/105755/Python-Straightforward-with-Explanation-(Prefix-hash-Trie-solutions)
    """
    # prefix를 직접 검사
    def replaceWords(self, roots, sentence):
        rootset = set(roots)

        def replace(word):
            for i in range(1, len(word)):
                # 있으면 리턴
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))

    # trie 사용
    def replaceWords(self, roots, sentence):
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        END = True
        for root in roots:
            cur = trie
            for letter in root:
                cur = cur[letter]
            cur[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                # 글자가 없다면 break
                if letter not in cur: break
                cur = cur[letter]
                if END in cur:
                    return cur[END]
            return word

        return " ".join(map(replace, sentence.split()))

dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"

solution = Solution()
print(solution.replaceWords(dictionary, sentence))