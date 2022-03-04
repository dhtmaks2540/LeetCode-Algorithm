# 슬라이딩 윈도우와 투 포인터를 사용
def lengthOfLongestSubstring(s):
    # 딕셔너리
    used = {}
    # 최대 길이 변수, 왼쪽 포인터
    max_length = start = 0
    # index는 오른쪽 포인터
    for index, char in enumerate(s):
        # 이미 등장했던 문자라면 'start' 위치 갱신
        if char in used and start <= used[char]:
            start = used[char] + 1
        else: #최대 부분 문자열 길이 갱신
            max_length = max(max_length, index - start + 1)

        # 현재 문자의 위치 삽입
        used[char] = index

    return max_length
    
s = "pwwkew"
print(lengthOfLongestSubstring(s))