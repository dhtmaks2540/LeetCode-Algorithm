import itertools

# itertools - combinations를 활용
def combine(n, k):
    nums = [i for i in range(1, n + 1)]
    return list(map(list, list(itertools.combinations(nums, k))))


def combine(n, k):
    results = []

    def dfs(elements, start, k):
        print(start, k)
        if k == 0:
            results.append(elements[:])
            return

        # 자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return results


n = 4
k = 2
print(combine(n, k))