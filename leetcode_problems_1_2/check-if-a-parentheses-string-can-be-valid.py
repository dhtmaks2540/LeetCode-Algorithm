class Solution:
    """
    https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/discuss/1646582/Python3-Java-C%2B%2B-Counting-Brackets-O(n)

    * Count of variable brackets is maintained using tot
    * Count of fixed open brackets is maintained using op
    * Count of fixed closed brackets is maintained using cl
    * 첫 반복에서는 closed 괄호 - ")"가 너무 많은지 확인
    * 그 후의 반복에서는 open 괄호 -"("가 너무 많은지 확인

    """
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)

        # 예외처리(홀수이면 패스)
        if n % 2 == 1: return False

        # tot -> 괄호의 총 갯수, op -> open, cl -> closed
        tot = op = cl = 0

        # 뒤에서 부터
        # 첫 반복에서는 closed 괄호 - ")"가 너무 많은지 확인
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0': tot += 1
            elif s[i] == '(': op += 1
            elif s[i] == ')': cl += 1
            if tot - op + cl < 0: return False
        tot = op = cl = 0
        # 그 후의 반복에서는 open 괄호 -"("가 너무 많은지 확인
        for i in range(len(s)):
            if locked[i] == '0': tot += 1
            elif s[i] == '(': op += 1
            elif s[i] == ')': cl += 1
            if tot + op - cl < 0: return False

        return True
        

    """
    https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/discuss/1646594/Left-to-right-and-right-to-left
    """
    def canBeValid(self, s: str, locked: str) -> bool:
        def validate(s: str, locked: str, op: str) -> bool:
            bal, wild = 0, 0
            for i in range(len(s)):
                if locked[i] == "1":
                    bal += 1 if s[i] == op else -1
                # locked가 0이라면 wild += 1
                else:
                    wild += 1
                if wild + bal < 0:
                    return False
            return bal <= wild
        return len(s) % 2 == 0 and validate(s, locked, '(') and validate(s[::-1], locked[::-1], ')')


s = "()()"
locked = "0000"
solution = Solution()
print(solution.canBeValid(s, locked))