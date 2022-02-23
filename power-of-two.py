class Solution:
    # 2의 제곱근인지 판별
    def isPowerOfTwo(self, n: int) -> bool:
        # exit condition(0이하이면 제곱근 X)
        if n <= 0:
            return False

        while n:
            if n != 1 and n % 2 != 0:
                return False

            n //= 2

        return True

    """
    https://leetcode.com/problems/power-of-two/discuss/1638707/PythonC%2B%2BJava-Detailly-Explain-Why-n-and-n-1-Works-oror-1-Line-oror-100-Faster-oror-Easy
    
    form of every power of two likes 0b1000....0

    1 = 0b1
    2 = 0b10
    4 = 0b100
    8 = 0b1000

    so pow(2, n) & (pow(2, n) - 1) == 0 (bit의 값이 1인 개수를 파악하는 문제에서도 이를 이용하여 풀이가능)
    for example, num = 4 = 0b100
    4 - 1 = 3 = 0b11
    4 & 3 = 0b100 & 0b11 = 0

    if n is not a power of two then n & n -1 != 0
    if m is not a power of two, then the binary form of m contains more than one
    for example, m = 6 = 0b110
    6 - 1 = 5 = 0b101
    6 & 5 = 4 = 0b100 > 0
    """
    def isPowerOfTwo(self, n: int) -> bool:
        # n이 양수인지 먼저 파악
        return n and not (n & n - 1)

n = 5
solution = Solution()
print(solution.isPowerOfTwo(n))