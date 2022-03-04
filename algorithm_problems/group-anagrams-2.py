from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)

        for str in strs:
            # 정렬
            temp = sorted(str)
            # 정렬한 값을 키값으로
            dict["".join(temp)].append(str)

        return [value for value in dict.values()]

strs = ["eat","tea","tan","ate","nat","bat"]

solution = Solution()
print(solution.groupAnagrams(strs))