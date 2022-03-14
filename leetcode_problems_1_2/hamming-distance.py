class Solution:
    # XOR를 활용(같으면 False, 다르면 True를 반환)
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR 연산 후 이진수로 변경
        xor_value = bin(x ^ y)
        
        result = 0

        for char in xor_value:
            # 1이 들어있다면, 즉 값이 다르다면
            if char == '1':
                result += 1

        return result

solution = Solution()

x, y = 3, 1
print(solution.hammingDistance(x, y))