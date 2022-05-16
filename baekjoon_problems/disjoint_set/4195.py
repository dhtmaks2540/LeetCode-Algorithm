"""
https://jaimemin.tistory.com/771

Union-Find를 사용해서 서로소를 판별한 후 현재 해당 친구들이 속한 서로소 집합의 개수를 출력하는
방법을 풀이하려고 했으나 서로소 집합의 원소의 개수를 판별하는 방법을 생각해내지 못했다...
해답을 보면 루트를 찾는 함수는 똑같지만 집합을 합치는 Union 과정에서 조금 다르다. 원래 Union-Find는
루트 노드의 집합만을 리스트로 사용했지만 이 문제는 해당 집합의 원소의 개수도 저장하기 위해서
size라는 리스트도 하나 추가한다. 그리고 union 할 때 사이즈가 더 큰 집합으로 작은 집합이 들어가도록
풀이하면서 단지 루트 노드만 변경하는 것이 아니라 size 리스트도 합쳐주는 방식으로 코드를 짠다.

그리고 지금까지는 노드가 숫자로 주어져서 리스트의 인덱스를 사용해서 노드를 지정할 수 있었다.
하지만 이 문제는 문자열로 주어지기 때문에 map<String, Int>(파이썬은 딕셔너리)을 선언해서
이름과 인덱스를 기록하고 이를 통해 원래의 문제와 똑같이 인덱스를 이용해서 노드를 접근한다.

응용을 해야하기에 이미 만들어져있는 함수를 변경하고 사이즈 리스트를 추가하는 등의 방식으로
넓게 생각해야 하는데 단지 함수는 그대로 사용하고 사이클이 존재하는지 등의 이미 풀었던 방식으로만
풀려고 하는 것 같다... 알고리즘은 방법이 무궁무진하니 이것저것 생각해보자. 특히 이 문제는
서로소 집합의 개수가 필요하므로 서로소 집합의 개수 리스트를 추가하는 것과 같이 문제에 필요한
리스트를 사용하는 방법을 고민해보자
"""

import sys

MAX_VALUE = 200000 + 1

# 루트 찾는 함수
def find_parent(parent, node):
    if node == parent[node]:
        return node
    
    # 현재 노드가 집합의 루트가 아니라면
    # 재귀 호출하여 업데이트
    parent[node] = find_parent(parent, parent[node])
        
    return parent[node]

# 집합을 합치는 함수
def union_parent(parent, node1, node2):
    # a가 속한 루트를 찾음
    node1 = find_parent(parent, node1)
    # b가 속한 루트를 찾음
    node2 = find_parent(parent, node2)
    
    # 같은 집합이 아니라면
    if node1 != node2:
        # 크기가 더 큰 집합으로 작은 집합이 들어감
        if size[node1] < size[node2]:
            node1, node2 = node2, node1
            
        parent[node2] = node1 # node2 집합이 node1에 합쳐짐
        size[node1] += size[node2] # node1의 집합 크기가 커짐
        size[node2] = 0 # node2가 node1에 흡수되므로
        
# 테스트 케이스
T = int(sys.stdin.readline().strip())

for _ in range(T):
    # 친구 관계의 수
    F = int(sys.stdin.readline().strip())
    # 부모 노드
    parent = [0] * MAX_VALUE
    # 해당 집합의 원소의 개수
    size = [0] * MAX_VALUE
    name_dic = dict()
    idx = 1
    
    # 초기화
    for i in range(MAX_VALUE):
        parent[i] = i
        size[i] = 1
    
    for i in range(F):
        person1, person2 = sys.stdin.readline().strip().split(" ")
        
        # 새로 나온 이름이라면 인덱스 부여
        if person1 not in name_dic:
            name_dic[person1] = idx
            idx += 1
            
        if person2 not in name_dic:
            name_dic[person2] = idx
            idx += 1
            
        # 루트 찾기
        person1_parent = find_parent(parent, name_dic[person1])
        person2_parent = find_parent(parent, name_dic[person2])
        
        # 같은 집합 내에 있다면
        if person1_parent == person2_parent:
            print(max(size[person1_parent], size[person2_parent]))
        # 다른 집합이라면 합친 후 최댓값 출력
        else:
            union_parent(parent, name_dic[person1], name_dic[person2])
            print(max(size[person1_parent], size[person2_parent]))
    