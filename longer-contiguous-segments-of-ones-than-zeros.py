# 연속된 1의 max 길이가 연속된 0의 max 길이보다 긴지 아닌지
class Solution:
    """
    현재 값을 분기하여 1과 0의 빈도수를 체크, 그리고 그 값을 가지고 max 빈도수를 저장
    """
    def checkZeroOnes(self, s: str) -> bool:
        zero_max_freq = one_max_freq = sum_one_freq = sum_zero_freq = 0

        for num in map(int, s):
            # 현재 값이 1인 경우
            if num == 1:
                sum_one_freq += 1
                sum_zero_freq = 0
                one_max_freq = max(one_max_freq, sum_one_freq)
            # 현재 값이 0인 경우
            else:
                sum_zero_freq += 1
                sum_one_freq = 0
                zero_max_freq = max(zero_max_freq, sum_zero_freq)
            
        return one_max_freq > zero_max_freq

s = "110100010"
solution = Solution()
print(solution.checkZeroOnes(s))