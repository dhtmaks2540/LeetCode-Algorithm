"""
세 개의 물통이 있는데 첫 번째 물통이 비어 있을 때, 세 번째 물통에 담겨있을 수 있는 물의 양을
모두 구하라

세 개의 물통을 두고 물을 옮겨가면서 확인하는 완전 탐색으로 풀이해야겠다고 생각했다. 완전 탐색을 
수행하기 위해서 BFS를 사용하였고, A와 B와 C 물통의 양을 큐에 삽입하고 추출하면서 한 통의 물이 들어있다면
이 통이 비거나 다른 통이 가득찰때까지 옮기고 그 값을 다시 큐에 삽입하는 방식으로 풀이하였다.
다만 BFS나 DFS는 방문을 확인하지 않을 경우 무한 루프에 빠지므로 이전에 방문했는지 확인이 필요한데
이 문제에서는 해시 테이블(딕셔너리)를 선언하고 A와 B와 C를 String 타입으로 합친 값을 키로 지정하여
이를 통해 방문을 확인하였다.
"""

def solution1():
    import sys
    import collections

    A, B, C = map(int, sys.stdin.readline().strip().split(" "))
    max_a, max_b, max_c = A, B, C
    # 정답변수(중복값 제거하기 위해 set으로)
    answer = set()
    # 방문 확인용 변수
    visited = dict()

    queue = collections.deque()
    queue.append((0, 0, C))
    visited[str(A) + str(B) + str(C)] = 0

    while queue:
        now_A, now_B, now_C = queue.popleft()
        temp_A, temp_B, temp_C = now_A, now_B, now_C
        
        # A 물통에 물이 0이라면 -> C 물통에 담긴 물의 양 기록
        if now_A == 0:
            answer.add(now_C)

        # C에 물이 있다면
        if now_C:
            # C에 물을 모두 붓거나 A가 가득 차기까지
            while now_C != 0 and now_A != max_a:
                now_C -= 1
                now_A += 1
            
            # 방문하지 않았다면 큐에 삽입 및 방문 처리
            if str(now_A) + str(now_B) + str(now_C) not in visited:
                queue.append((now_A, now_B, now_C))
                visited[str(now_A) + str(now_B) + str(now_C)] = 0
            
            # 값 되돌리기    
            now_A, now_C = temp_A, temp_C
            
            # C에 물을 모두 붓거나 B가 가득 차기까지
            while now_C != 0 and now_B != max_b:
                now_C -= 1
                now_B += 1
            
            # 방문하지 않았다면 큐에 삽입 및 방문 처리
            if str(now_A) + str(now_B) + str(now_C) not in visited:
                queue.append((now_A, now_B, now_C))
                visited[str(now_A) + str(now_B) + str(now_C)] = 0
            
            # 되돌리기
            now_B, now_C = temp_B, temp_C
            
        if now_B:
            while now_B != 0 and now_A != max_a:
                now_B -= 1
                now_A += 1
            
            if str(now_A) + str(now_B) + str(now_C) not in visited:
                queue.append((now_A, now_B, now_C))
                visited[str(now_A) + str(now_B) + str(now_C)] = 0
                
            now_A, now_B = temp_A, temp_B
            
            while now_B != 0 and now_C != max_c:
                now_B -= 1
                now_C += 1
                
            if str(now_A) + str(now_B) + str(now_C) not in visited:
                queue.append((now_A, now_B, now_C))
                visited[str(now_A) + str(now_B) + str(now_C)] = 0
                
            now_B, now_C = temp_B, temp_C
                
        if now_A:
            while now_A != 0 and now_C != max_c:
                now_A -= 1
                now_C += 1
                
            if str(now_A) + str(now_B) + str(now_C) not in visited:
                queue.append((now_A, now_B, now_C))
                visited[str(now_A) + str(now_B) + str(now_C)] = 0
                
            now_C, now_A = temp_C, temp_A
            
            while now_A != 0 and now_B != max_b:
                now_A -= 1
                now_B += 1
            
            if str(now_A) + str(now_B) + str(now_C) not in visited:
                queue.append((now_A, now_B, now_C))
                visited[str(now_A) + str(now_B) + str(now_C)] = 0
                
    answer = sorted(answer)
    for x in answer:
        print(x, end=" ")
        
# 3차원 배열로 방문 처리
def solution2():
    import sys
    import collections
    
    MAX_VALUE = 200 + 1
    visited = [[[False] * MAX_VALUE for _ in range(MAX_VALUE)] for _ in range(MAX_VALUE)]
    
    A, B, C = map(int, sys.stdin.readline().strip().split(" "))
    
    queue = collections.deque()
    queue.append((0, 0, C))
    answer = set()
    
    while queue:
        a, b, c = queue.popleft()
        
        if visited[a][b][c]: continue
        
        visited[a][b][c] = True
        # 조건 충족 시
        if a == 0:
            answer.add(c)
            
        # a -> b
        if a + b > B: # 넘치는지 확인
            queue.append((a + b - B, B, c))
        else:
            queue.append((0, a + b, c))
            
        # a -> c
        if a + c > C:
            queue.append((a + c - C, b, C))
        else:
            queue.append((0, b, a + c))
            
        # b -> a
        if b + a > A:
            queue.append((A, b + a - A, c))
        else:
            queue.append((a + b, 0, c))
            
        # b -> c
        if b + c > C:
            queue.append((a, b + c - C, C))
        else:
            queue.append((a, 0, b + c))
            
        # c -> a
        if c + a > A:
            queue.append((A, b, c + a - A))
        else:
            queue.append((c + a, b, 0))
            
        # c -> b
        if c + b > B:
            queue.append((a, B, c + b - B))
        else:
            queue.append((a, c + b, 0))
            
    for x in sorted(answer):
        print(x, end=" ")
        
solution2()