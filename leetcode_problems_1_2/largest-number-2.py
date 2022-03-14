from typing import List


class Solution:
    # 문제에 적합한 비교 함수(삽입 정렬의 조건)
    # '30' + '9'와 '9' + '30' 중 어떤 것이 더 큰지 확인하기 위한 함수
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    # 삽입 정렬 구현
    def largestNumber(self, nums: List[int]) -> str:
        # 첫 번째 인덱스부터
        i = 1
        while i < len(nums):
            j = i
            # 이전의 인덱스까지 조건을 사용해 비교하며 해당하면
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                # 위치 변경
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1

            i += 1

        return str(int(''.join(map(str, nums))))

# 정렬 함수의 key를 람다로 지정하여 풀이
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

nums = [3,30,34,5,9]
solution = Solution()
print(solution.largestNumber(nums))