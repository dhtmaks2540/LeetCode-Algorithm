import itertools

"""
주어진 숫자 리스트에서 세 수의 합이 소수인지를 판별하라.

숫자의 총 개수는 50이하이고, 각 원소의 1000 이하의 자연수이므로 모두 1000씩 나오게 되면 최대 3,000이고
이 이하의 숫자를 소수 판별을 해주면 된다. 이는 에라토스테네스의 체를 통해 미리 3000까지의 소수를 판별한 후,
조합을 통해 세 수를 뽑아 합한 후 이 값이 소수인지 판별해주는 방식으로 풀이할 수 있다.

에라토스테네스의 체와 조합을 사용할 수 있는지 묻는 문제인듯하다.

"""

def solution(nums):
    answer = 0

    # 에라토스테네스의 체를 사용하여 소수 판별
    MAX_NUM = 3000
    prime_nums = [True] * (MAX_NUM + 1)

    for i in range(2, int(MAX_NUM**0.5) + 1):
        if prime_nums[i]:
            j = 2
            while i * j <= MAX_NUM:
                prime_nums[i * j] = False
                j += 1
    
    for nums in list(itertools.combinations(nums, 3)):
        if prime_nums[sum(nums)]:
            print(nums)
            answer += 1

    return answer

nums = [1,2,7,6,4]
print(solution(nums))