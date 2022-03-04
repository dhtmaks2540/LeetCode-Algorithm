import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.defaultdict(int)
        temp = []
        result = []

        for char in s:
            counts[char] += 1

        for x, i in counts.items():
            temp.append((i, x))

        # 정렬수행
        temp.sort(reverse=True)

        for count, x in temp:
            for i in range(count):
                result.append(x)

        return "".join(result)

    def frequencySort(self, s):
        """
        :type str: str
        :rtype: str
        """
        counts = collections.Counter(s).most_common()

        return "".join([char * times for char, times in counts])
        
s = "tree"
solution = Solution()
print(solution.frequencySort(s))