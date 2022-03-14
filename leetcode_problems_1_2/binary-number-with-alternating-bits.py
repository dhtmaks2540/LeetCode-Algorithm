# 101010과 같이 항상 인접한 비트가 서로 다른지
class Solution:
    """
    101010과 같이 차례대로 나오는지 확인하기 위해 비트연산을 활용
    첫 비트를 저장한 후 인덱스 값을 증가시키며 짝수, 홀수 인덱스에서의 비트를 비교
    짝수 인덱스는 첫 비트의 값과 같은지, 홀수 인덱스는 첫 비트의 값과 다른지 비교함
    """
    # 비트 연산을 활용
    def hasAlternatingBits(self, n: int) -> bool:
        # 첫 비트
        first_bit = n & 1
        index = 0

        while n:
            if index % 2 == 0:
                if n & 1 != first_bit:
                    return False
            else:
                if n & 1 == first_bit:
                    return False

            n >>= 1
            index += 1

        return True

    """
    https://leetcode.com/problems/binary-number-with-alternating-bits/discuss/108456/easy-python
    """
    def hasAlternatingBits(self, n: int) -> bool:
        # 이진수로 변경
        s = bin(n)

        # 00 또는 11이 s에 포함되어 있는지 확인
        return '00' not in s and '11' not in s
        
n = 7
solution = Solution()
print(solution.hasAlternatingBits(n))