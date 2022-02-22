class Solution:
    # xor를 활용
    def hammingDistance(self, x: int, y: int) -> int:
        # xor를 수행하면 서로 다른 비트에 대해서만 True(1)이 반환
        xor_num = x ^ y
        xor_num = bin(xor_num)

        ans = 0

        for i in range(2, len(xor_num)):
            if xor_num[i] == '1':
                ans += 1

        return ans

    # xor를 활용하는 깔끔한 코드
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

x = 3
y = 1
solution = Solution()
print(solution.hammingDistance(x, y))