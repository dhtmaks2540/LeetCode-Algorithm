class Solution:
    # 비트연산을 활용하여 풀이
    def reverseBits(self, n: int) -> int:
        reverse_n = ""
        
        # iterate 32-bit
        for i in range(32):
            # use '&' operation to divide this number is 0 or 1
            bit = (n >> i) & 1

            if bit == 0:
                reverse_n += '0'
            else:
                reverse_n += '1'

        # change binary number to octal number
        return int(reverse_n, 2)

    """
    https://leetcode.com/problems/reverse-bits/discuss/54738/Sharing-my-2ms-Java-Solution-with-Explanation
    """
    def reverseBits(self, n: int) -> int:
        if n == 0: return 0

        result = 0

        # n을 거꾸로 iterate 하면서 해당 digit의 bit 검사
        for i in range(32):
            # move bit
            result <<= 1
            # 해당 자릿수의 비트와 1을 &한 연산이 1이라면 -> result 1 증가
            if n & 1 == 1: result += 1
            # move bit
            n >>= 1

        return result