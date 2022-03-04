from typing import List
import collections

class Solution:
    # DFS와 대문자, 소문자 조건을 활용
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        len_s = len(s)

        def dfs(index, path):
            result.append(path[:])

            for i in range(index, len_s):
                temp = path[i]
                # 대문자라면
                if path[i].isupper():
                    path[i] = path[i].lower()
                    dfs(i + 1, path)
                # 소문자라면
                elif path[i].islower():
                    path[i] = path[i].upper()
                    dfs(i + 1, path)

                # 변경 후 원래 값 가져오기
                path[i] = temp

        dfs(0, list(s))
        return ["".join(value) for value in result]

    """
    https://leetcode.com/problems/letter-case-permutation/discuss/115509/Python-simple-solution-(7-lines)
    """

    # 조건문을 활용
    def letterCasePermutation(self, s: str) -> List[str]:
        res = ['']
        for ch in s:
            # 문자라면
            if ch.isalpha():
                # 리스트의 값들에 현재 문자의 대문자, 소문자를 추가
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                # 숫자이면 리스트에 값들에 숫자 추가
                res = [i+ch for i in res]

        return res

    """
    https://leetcode.com/problems/letter-case-permutation/discuss/115485/Java-Easy-BFS-DFS-solution-with-explanation
    """

    # BFS로 접근
    def letterCasePermutation(self, s: str) -> List[str]:
        # 큐 선언
        queue = collections.deque()
        queue.append(s)
        # 문자 이터레이션
        for i in range(len(s)):
            # 현재의 글자가 문자라면
            if s[i].isalpha():
                # 큐의 길이만큼
                for _ in range(len(queue), 0, -1):
                    s = queue.popleft()
                    # left, right
                    left, right = s[0:i], s[i+1:]
                    # 큐에 현재의 값에 소문자 또는 대문자를 적용하고 left, right를 더하여 추가
                    queue.append(left + s[i].lower() + right)
                    queue.append(left + s[i].upper() + right)

        return list(queue)

    # DFS로 접근
    def letterCasePermutation(self, s: str) -> List[str]:
        # 결과변수
        result = []
        # 소문자로 변경 후 리스트로 변환
        list_s = list(s.lower())

        def dfs(list_s, index):
            # 현재의 인덱스가 문자열의 길이와 같다면
            if index == len(list_s):
                # 결과변수에 넣고 리턴
                result.append("".join(list_s))
                return

            dfs(list_s, index + 1)
            # 현재의 글자가 알파벳이라면
            if list_s[index].isalpha():
                # 대문자로 변경 후 dfs
                list_s[index] = list_s[index].upper()
                dfs(list_s, index + 1)
                # 다시 돌아오기
                list_s[index] = list_s[index].lower()

        dfs(list_s, 0)
        return result


s = "3z4"
solution = Solution()
print(solution.letterCasePermutation(s))