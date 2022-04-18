"""
쇠막대기와 레이저 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 쇠막대기의 총 개수를 구하라

리스트를 사용해서 괄호를 저장하고, 문제의 조건에 맞게 코드를 구현하는 방식으로 문제 풀이를 했다.
현재 괄호를 받아서 레이저인지, 막대인지를 판단해야 하기에 괄호를 계속 리스트에 저장하는 방식으로
풀이해야겠다고 생각했다. 따라서 괄호를 리스트에 저장하며 레이저인지, 막대기인지 분기하며
현재 막대의 개수와 총 막대의 개수 변수를 사용해 정답을 도출하였다.
"""

def solution1():
    # 쇠막대기
    array = list(input())
    # 총 막대의 개수
    answer = 0
    # 현재 막대의 개수
    temp = 0
    stack = []

    # 괄호 iteration
    for index, x in enumerate(array):
        # 열린 괄호
        if x == '(':
            # 다음에 올 괄호가 레이저가 아니라면
            if array[index + 1] == '(':
                # 현재 막대의 개수 증가
                temp += 1
                answer += 1
            stack.append('(')
        # 닫힌 괄호
        elif x == ')':
            # 마지막에 들어간 값이 열린 괄호라면 레이저
            if stack[-1] == '(':
                answer += temp
            # 마지막에 들어간 값이 닫힌 괄호라면 막대기 제거
            else:
                temp -= 1
                
            stack.append(')')
            
    print(answer)

# https://inuplace.tistory.com/844
def solution2():
    # 괄호
    array = list(input())
    answer = 0
    stack = []
    
    for i in range(len(array)):
        # 열린 괄호일 경우
        if array[i] == '(':
            stack.append('(')
        # 닫힌 괄호일 경우
        else:
            # 레이저라면
            if array[i - 1] == '(':
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer += 1
                
    print(answer)

solution2()