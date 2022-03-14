class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

    # 비트 연산을 활용
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # 1을 뺀 값과 AND 연산 횟수 측정
            n &= n - 1
            count += 1
        return count

"""
임시 변수를 사용하지 않고 변수 스왑

1. 덧셈, 뺄셈 이용
x, y = 9, 4
x = x + y # 13
y = x - y # 9
x = x - y # 4

2. XOR 이용
x, y = 9, 4 # 1001, 0100
x = x ^ y # 1001 ^ 0100 = 1101(13)
y = x ^ y # 1101 ^ 0100 = 1001(9)
x = x ^ y # 1101 ^ 1001 = 0100(4)


"""

n = 0b00000000000000000000000000001011

solution = Solution()
print(solution.hammingWeight(n))