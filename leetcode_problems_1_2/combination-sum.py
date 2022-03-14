def combinationSum(candidates, target):
    result = []

    def dfs(elements, target):
        if sum(elements) == target:
            temp = sorted(elements)
            if temp not in result:
                result.append(temp[:])
        elif sum(elements) > target:
            return
        # 값이 작을 때
        else:
            for i in range(len(candidates)):
                elements.append(candidates[i])
                dfs(elements, target)
                elements.pop()

    dfs([], target)
    return result


def combinationSum(candidates, target):
    result = []
    
    # csum - target에서 현재 인덱스의 값을 빼는 변수
    # index - 현재 위치 
    # path - 경로
    def dfs(csum, index, path):
        # 종료 조건
        if csum < 0:
            return
        # 만족 조건
        if csum == 0:
            result.append(path)
            return

        # 자신부터 하위 원소까지의 나열 재귀 호출
        # 만약 순열로 접근하였으면 인덱스를 0으로 지정하여 항상 첫 번째 값부터 탐색하도록
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
