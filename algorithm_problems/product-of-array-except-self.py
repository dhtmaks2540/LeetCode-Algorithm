# 왼쪽 곱셈 결과와 오른쪽 값을 차례대로 갑하기
def productExceptSelf(nums):
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) -1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return out

nums = [1,2,3,4]
print(productExceptSelf(nums))