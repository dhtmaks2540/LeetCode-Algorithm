
"""
https://leetcode.com/problems/smallest-value-of-the-rearranged-number/discuss/1748511/Sort-and-Swap

* If negative : sort descending, excluding the sign.
* if positive : sort ascending
  * Find first non-zero number
  * swap it with the first number
"""
class Solution:
    def smallestNumber(self, num: int) -> int:
        # 문자여롤 변경 후 음수라면 음수라면 내림차순, 양수라면 오름차순
        s = sorted(str(abs(num)), reverse = num < 0)
        # next 함수는 이터레이션에서 해당하는 조건에 맞는 다음 값을 가져오거나 
        # default 값을 반환
        # 양수라면 0이 제일 앞에 있기에 처음으로 0이 아닌 수와 변경하기 위해서 사용
        non_zero = next((i for i, n in enumerate(s) if n != '0'), 0)
        # 위치 변경
        s[0], s[non_zero] = s[non_zero], s[0]
        # 음수는 -를 추가하기 위해서
        return int(''.join(s)) * (1 if num >= 0 else -1)

    """
    https://leetcode.com/problems/smallest-value-of-the-rearranged-number/discuss/1748527/Python-Easy-and-Concise-with-Explanation
    
    if negative : 오름차순으로 정렬한 후 뒤에서부터 반환
    if positive : 첫 번째 숫자와 첫 번째 0이 아닌 숫자를 변경
    """
    def smallestNumber(self, num: int) -> int:
        s = sorted(str(abs(num)))
        if num <= 0:
            return -int(''.join(s[::-1]))
        i = next(i for i,a in enumerate(s) if a > '0')
        s[i], s[0] = s[0], s[i]
        return int(''.join(s))

num = 310
solution = Solution()
print(solution.smallestNumber(num))