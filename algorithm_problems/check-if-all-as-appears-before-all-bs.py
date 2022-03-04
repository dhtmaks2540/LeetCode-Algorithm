import collections

class Solution:
    # 딕셔너리 사용하여 접근
    def checkString(self, s: str) -> bool:
        freq = collections.defaultdict(int)

        for char in s:
            # a인 경우에 b의 값이 0이 아니라면
            # a가 모두 처리되기전에 b가 나온 경우이므로
            # False 리턴
            if char == 'a':
                if freq['b'] != 0:
                    return False
                else:
                    freq['a'] += 1
            else:
                freq['b'] += 1

        return True

    # 파이썬 다운 방식
    def checkString(self, s: str) -> bool:
        # ba가 있다면 b가 나온 후 a가 나온 경우이므로 False / 아니면 전부 정상
        return "ba" not in s

s = "abab"
solution = Solution()
print(solution.checkString(s))