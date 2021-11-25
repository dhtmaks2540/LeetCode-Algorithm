# 브루드 포스
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# in을 이용한 탐색
def twoSum(nums, target):
    for i, n in enumerate(nums):
        # 첫 번째 값을 뺀 값
        complement = target - n

        # 그 값이 나머지 숫자에서 존재한다면
        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i+1)]


# 첫 번째 수를 뺀 결과 키 조회
def twoSum(nums, target):
    # 딕셔너리 선언
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


# 딕셔너리 조회 구조 개선
def twoSum(nums, target):
    # 딕셔너리 선언
    nums_map = {}
    # 하나의 for문으로 통합
    for i, num in enumerate(nums):
        # 첫 번째 수를 뺀 결과가 존재한다면
        if target - num in nums_map:
            return [nums_map[target - num], i]
        # 값 대입
        nums_map[num] = i

# 투 포인터 이용
# 투 포인터로 풀려면 정렬이 필요한데 그렇게 되면 인덱스가 망가지기에
# 해당 문제에서는 불가능
def twoSum(nums, target):
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        if nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]

input = [2,7,11,15]
target = 9

print(twoSum(input, target))