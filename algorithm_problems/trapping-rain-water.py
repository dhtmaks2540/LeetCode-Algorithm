# 투 포인터 사용
def trap(height):
    if not height:
        return 0

    # 쌓인 물
    volume = 0
    # 왼쪽 포인트, 오른쪽 포인트
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    # 최대 지점에 도달하기 까지
    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    
    return volume

# 스택사용
def trap(height):
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우(현재 높이가 이전 높이보다 높을 때)
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()

            # 스택이 비었다면 while문 빠져나가기
            if not len(stack):
                break
            
            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters
        # 변곡점이 아닌 경우
        stack.append(i)

    return volume

input = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(input))