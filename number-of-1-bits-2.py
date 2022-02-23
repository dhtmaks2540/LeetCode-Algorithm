class Solution:
    # 비트연산 활용
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(32):
            bit = (n >> i) & 1
            if bit == 1:
                count += 1
        
        return count

    # bin 함수와 count 함수 활용
    def hammingWeight(self, n: int) -> int:
        # return bin(n ^ 0).count('1')
        return bin(n).count('1')

    # 비트연산 활용
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            # 1을 뺀 값과 AND 연산 횟수 측정
            # 1을 뺀 값과 ANd 연산을 수행할 때마다 비트가 1씩 빠진다.
            n &= n - 1
            count += 1

        return count