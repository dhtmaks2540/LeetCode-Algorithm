from typing import List


class Solution:
    # 첫 바이트를 기준으로 판별
    def validUtf8(self, data: List[int]) -> bool:
        # 문자 바이트 만큼 10으로 시작 판별
        def check(size):
            for i in range(start + 1, start + size + 1):
                # i의 값이 리스트의 사이즈를 넘거나 10으로 시작하지 않는다면
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            # 첫 바이트 기준 총 문자 바이트 판별
            first = data[start]
            # 3개의 바이트 체크
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            # 2개의 바이트 체크
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            # 1개의 바이트 체크
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            # 0은 체크할 게 없음
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True

solution = Solution()
data = [197,130,1]

solution.validUtf8(data)