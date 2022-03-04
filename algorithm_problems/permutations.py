import itertools

# itertools - permutations를 활용한 순열
def permute(nums):
    return list(map(list, itertools.permutations(nums)))

def permute(nums):
    result = []
    prev_elements = []

    def dfs(elements):
        # 리프 노드일 때 결과 추가
        if len(elements) == 0:
            # 참조가 아닌 값을 복사하는 식으로
            result.append(prev_elements[:])

        # 순열 생성 재귀 호출
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return result
        

nums = [1,2,3]
print(permute(nums))