"""
번호가 담긴 배열이 주어지고 해당 번호를 왼손으로 눌렀는지 오른손으로 눌렀는지 출력하라

해당 문제는 2차원 그래프 상에서 현재 위치에서 목표값까지의 거리를 측정하는 문제로 
아래의 solution은 BFS를 사용해서 탐색했다. 그리고 문제에서 주어진 조건에 맞게 구현만 잘하면
풀이할 수 있는 문제이다.

이 문제에서는 2차원 그래프 상에서 거리를 어떻게 측정하는지를 포인트로 잡으면 될 것 같다.

"""

import collections

# BFS를 사용해서 풀이
def solution(numbers, hand):
    answer = ''
    
    left = {
        1 : (0, 0),
        4 : (1, 0),
        7 : (2, 0)
    }
    
    right = {
        3 : (0, 2),
        6 : (1, 2),
        9 : (2, 2)
    }
    
    center = {
        2 : (0, 1),
        5 : (1, 1),
        8 : (2, 1),
        0 : (3, 1)
    }
    
    def check_distance(row, col, target):
        queue = collections.deque()
        cnt = 0
        
        # 동서남북
        dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # 방문을 확인하기 위한 리스트
        visited = [[False] * 3 for _ in range(4)]
        
        # 시작점 삽입 및 방문처리
        queue.append((row, col))
        visited[row][col] = True
        
        while queue:
            cnt += 1
            for _ in range(len(queue)):
                now_x, now_y = queue.popleft()
                # 현재 목표로 한 곳이라면
                if graph[now_x][now_y] == target:
                    return cnt
                for i in range(4):
                    next_x, next_y = now_x + dxy[i][0], now_y + dxy[i][1]
                    # 현재 좌표가 정상범위이며 방문하지 않았다면
                    if 0 <= next_x < 4 and 0 <= next_y < 3 and not visited[next_x][next_y]:
                        queue.append((next_x, next_y))
                        visited[next_x][next_y] = True

    # 번호판 그래프 그리기
    cnt = 1
    graph = [[0] * 3 for _ in range(4)]
    graph[3][0] = '*'
    graph[3][2] = '#'
    for i in range(3):
        for j in range(3):
            graph[i][j] = cnt
            cnt += 1
    
    left_hand_index = (3, 0)
    right_hand_index = (3, 2)
    
    for num in numbers:
        # 현재 숫자가 왼쪽에 있는 숫자라면
        if num in left:
            answer += 'L'
            left_hand_index = left[num]
        # 현재 숫자가 오른쪽에 있는 숫자라면
        elif num in right:
            answer += 'R'
            right_hand_index = right[num]
        # 2,5,8,0이라면
        else:
            left_dis = check_distance(left_hand_index[0], left_hand_index[1], num)
            right_dis = check_distance(right_hand_index[0], right_hand_index[1], num)
            # 왼쪽이 더 가깝다면
            if left_dis < right_dis:
                left_hand_index = center[num]
                answer += 'L'
            # 오른쪽이 더 가깝다면
            elif left_dis > right_dis:
                right_hand_index = center[num]
                answer += 'R'
            # 같다면 어느 손잡이인지에 따라서
            else:
                if hand == "right":
                    right_hand_index = center[num]
                    answer += 'R'
                else:
                    left_hand_index = center[num]
                    answer += 'L'
                    
    return answer

# BFS를 사용하지 않고 거리를 측정하여 풀이
def solution2(numbers, hand):
    answer = ''
    key_dict = {1 : (0, 0), 4 : (1, 0), 7 : (2, 0),
                3 : (0, 2), 6 : (1, 2), 9 : (2, 2),
                2 : (0, 1), 5 : (1, 1), 8 : (2, 1), 0 : (3, 1),
                '*':(3,0), '#':(3,2)}
    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    
    for num in numbers:
        if num in left:
            answer += 'L'
            lhand = num
        elif num in right:
            answer += 'R'
            rhand = num
        else:
            curPos = key_dict[num]
            lpos = key_dict[lhand]
            rpos = key_dict[rhand]
            ldist = abs(curPos[0] - lpos[0]) + abs(curPos[1] - lpos[1])
            rdist = abs(curPos[0] - rpos[0]) + abs(curPos[1] - rpos[1])
            
            if ldist < rdist:
                answer += 'L'
                lhand = num
            elif ldist > rdist:
                answer += 'R'
                rhand = num
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = num
                else:
                    answer += 'R'
                    rhand = num
                    
    return answer