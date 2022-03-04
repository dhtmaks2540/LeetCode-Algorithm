from typing import List


class Solution:
    # 브루드 포스로 접근
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)

        for i, num in enumerate(nums1):
            # 인덱스 값 구하기
            index = nums2.index(num)

            for num2 in nums2[index + 1:]:
                # 더 큰 값 찾으면 저장 후 break
                if num < num2:
                    result[i] = num2
                    break

        return result

    # O(n) 시간 복잡도를 가진 풀이
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st, d = [], {}
        for n in nums2:
            # 스택에 값이 있고 가장 마지막 값이 현재 값보다 작다면
            while st and st[-1] < n:
                # 딕셔너리에 저장
                # 즉, 딕셔너리에는 키보다 오른쪽에서 가장 가까운 더 큰값을 저장
                d[st.pop()] = n
            st.append(n)

        # 키에서 get해서 값 가져오고 default값은 -1로
        return [d.get(x, -1) for x in nums1]


nums1 = [4,1,2]
nums2 = [1,3,4,2]
solution = Solution()
print(solution.nextGreaterElement(nums1, nums2))