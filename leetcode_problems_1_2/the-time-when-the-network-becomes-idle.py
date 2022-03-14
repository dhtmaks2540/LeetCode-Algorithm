from typing import List
import collections
import heapq
from winsound import MessageBeep


class Solution:
    # 모든 데이터 서버가 메세지를 받는데 총 몇초가 걸렸는지
    # 메세지는 마스터 서버로 간 후 다시 돌려받는 시스템
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = collections.defaultdict(list)
        distance = collections.defaultdict(int)

        # 모든 거리는 1로 계산
        for a, b in edges:
            graph[a].append((b, 1))
            graph[b].append((a, 1))

        # 다익스트라 알고리즘
        # (거리, 정점)
        q = [(0, 0)]

        while q:
            dist, cur_node = heapq.heappop(q)

            # 이미 처리되었으면 패스
            if cur_node not in distance:
                distance[cur_node] = dist
                for v, w in graph[cur_node]:
                    alt = dist + w
                    heapq.heappush(q, (alt, v))

        visited = [False] * len(patience)
        message = collections.deque()
        time = 1

        # 시작 메세지
        for i in range(1, len(patience)):
            message.append(i)

        while message:
            print(time, message)
            for i in range(1, len(patience)):
                if not visited[i]:
                    if time % patience[i] == 0 and time < distance[i] * 2:
                        message.append(i)
                    elif time >= distance[i] * 2:
                        visited[i] = True
                        message.popleft()
                else:
                    continue

            time += 1
        
        return time
                    
    """
    https://leetcode.com/problems/the-time-when-the-network-becomes-idle/discuss/1524169/Python-Clean-BFS-Lots-Of-Comments-Easy-To-Follow
    
    1. 인접 리스트 생성
    2. 마스터 노드에서 데이터 노드로의 가장 짧은 거리(다익스트라 알고리즘)
    3. 마지막 재전송 시간이 언제인지, 그 후 서버에 도달하는 데 걸리는 시간을 계산

    """
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:    
        # 인접 리스트
        graph = collections.defaultdict(list)

        # 양방향 연결
        for source, target in edges:
            graph[source].append(target)
            graph[target].append(source)

        # BFS(데이터 노드에서 마스터노드로 가는 가장 짧은 거리)
        # 다익스트라 알고리즘
        distance = collections.defaultdict(int)
        # 거리, 시작점
        q = [(0, 0)]

        while q:
            curr_dist, curr_node = heapq.heappop(q)

            # 이미 처리되었다면 패스
            if curr_node not in distance:
                distance[curr_node] = curr_dist

                # 연결된 노드 확인
                for node in graph[curr_node]:
                    heapq.heappush(q, (curr_dist + 1, node))

        # 가장 짧은 거리를 사용해 계산
        ans = 0
        for index in range(1, len(patience)):
            resend_interval = patience[index]

            # 서버는 메세지를 마스터로 보낸 후 돌려받으면 요청을 중단
            shut_off_time = (distance[index] * 2)

            # shur_off_time - 1 == 마지막으로 서버가 재요청을 보낼 수 있는 시간
            last_second = shut_off_time - 1

            # Calculate the last time a packet is actually resent.
            last_resent_time = (last_second // resend_interval) * resend_interval

            # At the last resent time, the packet still must go through 2 more cycles to the master node and back
            last_packet_time = last_resent_time + shut_off_time

            ans = max(last_packet_time, ans)

        # Add + 1, the current answer is the last time the packet is received by the target server(still active).
        # we must return the first second the network is idle, therefore + 1
        return ans + 1

    """
    https://leetcode.com/problems/the-time-when-the-network-becomes-idle/discuss/1524181/BFS-%2B-Maths-C%2B%2B-Explanation
    """
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:    
        # 인접 리스트
        graph = collections.defaultdict(list)

        # 양방향 연결
        for source, target in edges:
            graph[source].append(target)
            graph[target].append(source)

        # BFS(데이터 노드에서 마스터노드로 가는 가장 짧은 거리)
        # 다익스트라 알고리즘
        distance = collections.defaultdict(int)
        # 거리, 시작점
        q = [(0, 0)]

        while q:
            curr_dist, curr_node = heapq.heappop(q)

            # 이미 처리되었다면 패스
            if curr_node not in distance:
                distance[curr_node] = curr_dist

                # 연결된 노드 확인
                for node in graph[curr_node]:
                    heapq.heappush(q, (curr_dist + 1, node))

        res = 0
        for i in range(1, len(patience)):
            extra_payload = (distance[i] * 2 - 1) // patience[i]
            # 첫 번째 메세지가 데이터 서버에 다시 도착하기 전의 추가 페이로드의 수
            # 데이터 서버는 첫 번째 메세지를 받기 전까지만 메세지를 보낼 수 있고
            # 첫 번째 메세지는 distance * 2에 도착하기 때문에 따라서 (time[i] * 2 - 1)

            last_out = extra_payload * patience[i] # 데이터 서버가 메세지를 마지막으로 보낸 시간
            last_in = last_out + distance[i] * 2 # 현재 데이터 서버의 결과

            res = max(res, last_in)

        # "res" 사간에 마지막 메세지가 데이터 서버 중 하나에 도착
        # 따라서 res + 1에 서버 간에 더 이상 메세지가 전달 X
        return res + 1

        


edges = [[0,1],[1,2]]
patience = [0,2,1]
solution = Solution()
print(solution.networkBecomesIdle(edges, patience))