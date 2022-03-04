import collections
import re
from typing import List
import operator

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 정규식을 사용
        # 문자열이 아닌것은 공백으로 치환
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
                
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 특수문자는 공백으로, 나머지는 그대로
        normalized_str = "".join([c.lower() if c.isalnum() else " " for c in paragraph])

        # 공백을 기준으로 나누기
        words = normalized_str.split()

        word_count = collections.defaultdict(int)
        banned_words = set(banned)

        # 단어가 밴 목록에 없다면 카운트추가
        for word in words:
            if word not in banned_words:
                word_count[word] += 1

        return max(word_count.items(), key=operator.itemgetter(1))[0]