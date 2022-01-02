from typing import List


class Solution:
    # 투 포인터 
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        # 왼쪽 포인터, 오른쪽 포인터
        left, right = 0, len(height) - 1
        # 왼쪽 최댓값, 오른쪽 최댓값
        left_max, right_max = height[left], height[right]

        # 최대지점(중간)에서 만나기 전까지
        while left < right:
            # 최댓값 갱신
            left_max, right_max = max(height[left], left_max),\
                max(height[right], right_max)

            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

    # 스택 활용
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
            
            stack.append(i)
        return volume

    

height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()
print(solution.trap(height))