from typing import List
import collections

"""
i != j 일 때, arr[i] == 2 * arr[j]인 경우가 있는지 반환

접근방법

arr의 값을 기록하기 위해서 해시 테이블을 사용했다.
이때, 정렬을 수행하지 않고 해시 테이블을 접근하며 만약 현재의 값 * 2나 현재의 값 / 2가 
해시 테이블에 존재한다면 arr[i] * 2가 arr[j]에 해당한다는 뜻이므로 그 경우 True를 반환하도록 풀이

해시 테이블을 사용한 이유는 key, value 형식으로 값을 저장하기 위함과
in 키워드를 사용해 해당 값의 존재 여부를 판단하기 위해서 사용
"""

class Solution:
    # 해시 테이블을 사용하여 key, value 형식으로 기록
    def checkIfExist(self, arr: List[int]) -> bool:
        dic = {}

        # array iterate
        for num in arr:
            # 절반으로 나누거나 두배를 곱한 값이 해시 테이블에 있다면
            if num * 2 in dic.keys() or num / 2 in dic.keys():
                # return True
                return True

            # insert key, value in hash table
            dic[num] = num

        # not array[i] * 2 in hash table
        return False

    # hashset을 사용해서 문제 풀이
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for num in arr:
            if num * 2 in seen or num / 2 in seen:
                return True

            seen.add(num)

        return False

arr = [3,1,7,11]
arr = [10,2,5,3]
arr = [-20,8,-6,-14,0,-19,14,4]
arr = [-2,0,10,-19,4,6,-8]
solution = Solution()
print(solution.checkIfExist(arr))