import collections

# 트라이의 노드
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        # 단어의 끝 인덱스 체크
        self.word_id = -1
        # 팰린드롬 단어의 위치를 저장하는 리스트 변수
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 데코레이터(자바의 어노테이션에 해당)
    # 자바으 static 선언과 비슷
    # 팰린드롬 여부 판별
    @staticmethod
    def is_palindrome(word):
        return word[::] == word[::-1]

    # 단어 삽입
    def insert(self, index, word):
        node = self.root
        for i, char in enumerate(reversed(word)):
            """
            트라이 삽입 중 남아 있는 단어가 팰린드롬이라면,
            미리 팰린드롬 여부를 세팅
            """
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    # 단어 존재 판별 여부
    def search(self, index, word):
        result = []
        node = self.root

        while word:
            # 판별 로직
            """
            탐색 중간에 word_id가 있고
            나머지 문자가 팰린드롬인 경우
            """
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            # node.children에 글자가 없을 경우 return
            if not word[0] in node.children:
                return result
            # 자식 타고 내려가기
            node = node.children[word[0]]
            # 다음 글자로
            word = word[1:]

        # 판별 로직
        """
        끝나는 지점이 -1이 아니고 같은 인덱스가 아닌 경우
        결과 리스트에 추가하기
        """
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 판별 로직
        """
        끝까지 탐색했을 때 palindrome_word_ids가 있는 경우
        """
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result

class Solution:
    # 트라이를 사용한 판별
    def palindromePairs(self, words):
        trie = Trie()

        # 삽입
        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        # 검색
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results

    def palindromePairs(self, words):
        # 결과용 변수
        ans = []
        # 딕셔너리에 word를 거꾸로 셋팅하고 인덱스 넣기
        dict = {word[::-1]: i for i, word in enumerate(words)}

        # 이터레이션하며
        for i, word in enumerate(words):
            if "" in dict and dict[""] != i and word == word[::-1]:
                ans.append([i, dict[""]])

            # 두 번째 글자부터 문자의 길이까지
            for j in range(1, len(word) + 1):
                # j까지의 문자
                l = word[:j]
                # j부터의 문자
                r = word[j:]
                print(f"l : {l} / r : {r}")
                """
                왼쪽 문자열이 딕셔너리안에 있고
                인덱스가 다르며
                오른쪽 문자열이 팰린드롬이라면
                """
                if l in dict and dict[l] != i and r == r[::-1]:
                    ans.append([i, dict[l]])
                """
                오른쪽 문자열이 딕셔너리안에 있고
                인덱스가 다르며
                왼쪽 문자열이 팰린드롬이라면
                """
                if r in dict and dict[r] != i and l == l[::-1]:
                    ans.append([dict[r], i])

        return ans


solution = Solution()

words = ["d", "dcbbc", "bbcd", "cbcd", "cbbc", "dcbb"]
print(solution.palindromePairs(words))