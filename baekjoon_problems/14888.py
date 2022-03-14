"""
접근방법

재귀적으로 문제를 풀었다.
우선, 연산자의 개수를 모두 파악한 후 계산하기 전에 해당 연산자의 개수에서 1을 빼고
재귀함수로 그 정보를 넘겨주고 다시 연산자를 1추가해주면 아래에서 다시 사용될 수 있기 때문이다.

재귀 구조를 배울 수 있는 대표적인 예시문제같다.
"""

# 수의 개수
N = int(input())
# 숫자
nums = list(map(int, input().split()))
# 연산자
ope = list(map(int, input().split()))
# 결과 변수
result = []

def recursive_oper(index, ope, num):
    if index > N - 1:
        result.append(num)
        return
    
    if ope[0] != 0:
        ope[0] -= 1
        recursive_oper(index+1, ope, num + nums[index])
        ope[0] += 1
    if ope[1] != 0:
        ope[1] -= 1
        recursive_oper(index+1, ope, num - nums[index])
        ope[1] += 1
    if ope[2] != 0:
        ope[2] -= 1
        recursive_oper(index+1, ope, num * nums[index])
        ope[2] += 1
    if ope[3] != 0:
        ope[3] -= 1
        recursive_oper(index+1, ope, int(num / nums[index]))
        ope[3] += 1

recursive_oper(1, ope, nums[0])
print(max(result))
print(min(result))

# # 수의 개수
# N = int(input())
# # 숫자
# nums = list(map(int, input().split()))
# # 연산자
# add, sub, mul, div = map(int, input().split())
# # 최댓값
# max_result = -int(1e9)
# # 최솟값
# min_result = int(1e9)

# def dfs(i, now):
#     global max_result, min_result, add, sub, mul, div

#     if i == N:
#         max_result = max(max_result, now)
#         min_result = min(min_result, now)
#     else:
#         # 각 연산에 대해 재귀적으로 수행
#         if add > 0:
#             add -= 1
#             dfs(i + 1, now + nums[i])
#             add += 1
#         if sub > 0:
#             sub -= 1
#             dfs(i + 1, now - nums[i])
#             sub += 1
#         if mul > 0:
#             mul -= 1
#             dfs(i + 1, now * nums[i])
#             mul += 1
#         if div > 0:
#             div -= 1
#             dfs(i + 1, int(now / nums[i]))
#             div += 1

# dfs(1, nums[0])

# print(max_result)
# print(min_result)