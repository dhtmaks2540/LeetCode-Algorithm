"""
주어진 array의 i부터 j 인덱스까지의 수를 정렬한 후 k번째 숫자를 출력하라

주어진 array의 길이는 최대 100개이고, commands의 최대 길이는 50이하이다. 따라서
최대 길이로 매번 주어지더라고 O(commands의 길이 * (array의 길이 * log array의 길이))이므로
충분하게 풀이할 수 있다. 문제는 command를 순회하며 현재 command의 i부터 j까지 배열을 자르고 정렬한 
후 k번째의 숫자를 출력하면 풀이할 수 있다.

정렬을 사용할 수 있는지 묻는 문제인듯하다. 

"""

def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        
        # i ~ j번째까지의 리스트 정렬
        temp_array = sorted(array[i - 1 : j])
        answer.append(temp_array[k - 1])
    
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))