import collections

# 재귀를 통해 풀이
def removeDuplicateLetters(s):
    # 집합으로 정렬
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        print(suffix)

        # 전체 집합과 접미사 집합이 일치할 때 분리 진행
        if set(s) == set(suffix):
            print(set(suffix))
            return char + self.removeDuplicateLetters(suffix.replace(char, ''))
    return ''

def removeDuplicateLetters(s):
    # Counter, set, stack
    # stack에는 사실 in 이라는 연산자가 존재하지 않기에
    # set을 선언하여 사용
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        # 이미 존재할 경우 패스
        if char in seen:
            continue
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)

s = "cbacdcbc"
removeDuplicateLetters(s)