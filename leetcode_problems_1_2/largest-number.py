from typing import List


class Solution:
    # 문제에 적합한 비교 함수
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    # 삽입 정렬 구현
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            # str(j-1) + str(j) < str(j) + str(j - 1)일 때
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                # 스왑
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1
        # nums 리스트를 str로 바꾼 후 하나의 str로 변경
        # 그리고 00과 같은 숫자를 대비해 int형으로 변경 후 다시 str로
        return '0' if nums[0] == 0 else ''.join(map(str, nums))

# 람다에 사용 할 클래스
class LargerNumKey(str):
    # lt(less than)는 < 
    # le(less or equal)는 <=
    # eq(equal)는 ==
    # ne(not equal)는 !=
    # 매직 메소드에 해당
    # 코틀린 operator 관례에 해당
    # 참조 사이트 : https://kwonkyo.tistory.com/234
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


nums = [3,30,34,5,9]
solution = Solution()
print(solution.largestNumber(nums))