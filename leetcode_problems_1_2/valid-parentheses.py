def isValid(s):
    # 스택 역할을 수행할 리스트
    stack = []
    # 딕셔너리(매칭용)
    table = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for char in s:
        # (, {, [ 라면
        if char not in table:
            stack.append(char)
        # 스택이 비어있거나 매칭되는 값이 아니라면
        elif not stack or table[char] != stack.pop():
            return False
    
    return len(stack) == 0

print(isValid("()"))