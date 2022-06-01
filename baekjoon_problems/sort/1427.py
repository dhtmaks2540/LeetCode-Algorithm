"""
수가 주어지면 각 자리수를 내림차순으로 정렬하라

최대 10자리밖에 되지 않으므로 주어진 숫자를 리스트로 변경한 후, 정렬을 통해 풀이할 수 있다.
"""

nums = list(map(int, input()))
nums.sort(reverse = True)
for num in nums:
    print(num, end="")