from itertools import count
from typing import List
import collections

"""
세 개의 integer array에서 적어도 두 개의 integer array에 포함되는 숫자를 반환하라

접근방법

해시 테이블 또는 해시 맵은 키를 값에 매핑할 수 있는 구조이다. 자바에서 해시 테이틀과 해시 맵은 모두
컬렉션의 Map 인터페이스를 구현한 클래스이며, Key와 Value를 이용하여 값을 저장하는 구조이다.
다만, HashTable은 동기화를 지원하므로 멀티 스레드 환경에서 사용할 수 있어서 put, get과 같은 주요 
메소드에 synchronized 키워드가 선언되어 있다.

HashMap은 동기화를 지원하지 않으므로 멀티 스레드 환경에는 적합하지 않다.

해시 테이블을 통해 이 문제에 접근한 이유는 세 개의 array의 값을 키로하여 그 개수를 파악하고
그 개수를 사용해서 두 개 이상의 array에서 나왔는지 판단할 수 있기 때문이다. 즉, 가장 큰 점은
해당 값을 키로하여 값을 저장하기 위해서 해시 테이블을 사용했다. 또한 이를 위해 set을 사용해 원소의
중복을 제거한 후 해시 테이블을 사용하였다.

사람들의 정답 중 가장 빨랐던 것은 set을 이용해 중복을 제거한 후 비트 연산자(&, |)을 사용하여 
중복을 뽑아내는 방식으로 문제를 풀이하는 것이 좋은 것 같다. 중요한 점은 비트 연산자는 list에는 사용할 수 없고
문제에서 set의 원소인 int 불변 객체에 사용 가능하다.
"""

class Solution:
    # 해시테이블을 사용하여 문제 풀이
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # 중복을 제거하기 위해서 set으로
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)

        counter = collections.defaultdict(int)

        # 세 개의 nums iterate
        for num in nums1:
            counter[num] += 1

        for num in nums2:
            counter[num] += 1

        for num in nums3:
            counter[num] += 1

        # 2번 이상이 나왔을 경우 두 개의 array에는 포함된다는 의미이므로 아래와 같이 반환
        return [key for key, value in counter.items() if value >= 2]

    # 해시테이블을 사용하여 접근
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        answer = set()

        # nums1에 있는 값이 nums2 또는 nums3에도 있는지
        for num in set(nums1):
            if num in nums2 or num in nums3:
                answer.add(num)

        # nums2에 있는 값이 nums1 또는 nums3에도 있는지
        for num in set(nums2):
            if num in nums1 or num in nums3:
                answer.add(num)

        return list(answer)

    """
    https://leetcode.com/problems/two-out-of-three/discuss/1516174/Python-one-line-simple-solution
    """

    # 비트 연산자를 사용하여 접근
    # 두 개의 set에 비트 연산자 &를 사용하면 중복되는 값만 보여주고,
    # 두 개의 set에 비트 연산자 |를 사용하면 두 리스트 원소를 모두 한곳에 모아 보여준다.
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # nums1과 nums2에 있거나 nums2와 nums3에 있거나 nums1이나 nums3에 있는 값
	    return set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums1) & set(nums3)
    

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
# nums1 = [3,1]
# nums2 = [2,3]
# nums3 = [1,2]
solution = Solution()
print(solution.twoOutOfThree(nums1, nums2, nums3))