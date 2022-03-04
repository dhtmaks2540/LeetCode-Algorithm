# 오름차순으로 정렬한 후 앞에서 부터 쌍을 지어서 가져가
# 합하면 그게 최대 값에 해당
def arrayPairSum(nums):
    sum = 0
    # 정렬 수행
    nums.sort()
    # 순서쌍
    pair = []

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum

# 짝수 번째 값 계산
# 정렬한 후 min값을 계산할 때 항상 작은 것은 짝수이므로
def arrayPairSum(nums):
    sum = 0
    # 정렬 수행
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n

    return sum

# 파이썬 방식
def arrayPairSum(nums):
    # 정렬된 리스트에서 짝수 값만을 가져와 sum
    return sum(sorted(nums)[::2])

nums = [1,4,3,2]
print(arrayPairSum(nums))