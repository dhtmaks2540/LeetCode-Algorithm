def subsets(nums):
    # 결과용 변수
    result = []

    # elements - 값을 담을 변수
    # index - 자신을 제외한 값을 가져오기 위한 인덱스
    # k - 개수를 측정하기 위한 변수
    def dfs(elements, index, k):
        # k가 nums의 크기보다 커진다면 return
        if k > len(nums):
            return

        # k가 nums의 크기보다 작다면 
        if k <= len(nums):
            result.append(elements[:])

        for i in range(index, len(nums)):
            elements.append(nums[i])
            dfs(elements, i + 1, k + 1)
            elements.pop()

    dfs([], 0, 0)

    return result


def subsets(nums):
    result = []

    def dfs(index, path):
        # 매번 결과 추가
        result.append(path)

        # 경로를 만들면서 dfs
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result

nums = [1,2,3]
print(subsets(nums))