from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        temp = []
        index = 0

        for i, char in enumerate(s):
            # spaces의 값과 비교하며 해당하는 인덱스이면 공백 추가
            if index < len(spaces) and spaces[index] == i:
                temp.append(" ")
                index += 1
            temp.append(char)

        return ''.join(temp)

s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]

solution = Solution()
print(solution.addSpaces(s, spaces))