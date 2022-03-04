def dailyTemperatures(temperatures):
    # 결과 저장용
    result = [0] * len(temperatures)
    # 스택
    stack = []

    # 이터레이터하며
    for i, temperature in enumerate(temperatures):
        # 스택에 값이 존재하는 동안
        while stack:
            # 위에서부터 차례대로 빼기
            index, temp = stack.pop()
            # 작은 값이 존재한다면
            if temp < temperature:
                value = i - index
                result[index] = value
            # 존재하지 않는다면
            else:
                stack.append((index, temp))
                break
        
        stack.append((i, temperature))

    return result

# 스택을 이용한 풀이
def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []

    for i, cur in enumerate(temperatures):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer
        
temperatures = [30,40,50,60]
print(dailyTemperatures(temperatures))
