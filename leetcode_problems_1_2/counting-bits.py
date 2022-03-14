from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        def find_one(number):
            count = 0

            # 0이 아닌 동안
            while number:
                # n & n - 1은 1의 개수를 파악할 수 있음
                # for example 4 = 0b100, 4 - 1 = 3 = 0b011
                # 0b100 & 0b011 = 0b0
                # 5 = 0b101, 5 - 1 = 4 = 0b100
                # 0b101 % 0b100 = 0b100
                number &= number - 1
                count += 1

            return count

        for i in range(len(result)):
            count = find_one(i)

            result[i] = count

        return result

n = 5
solution = Solution()
print(solution.countBits(n))