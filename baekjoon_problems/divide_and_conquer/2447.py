"""
주어진 패턴과 같은 별을 출력하라

문제를 보고 규칙을 찾다 보니 3의 패턴(위 3개, 중간 2개, 아래 3개)의 패턴이 반복된다는 것을 파악했다.
따라서 문제가 3의 제곱수로 나오므로 이를 사용해서 재귀적으로 풀이하려고 시도했는데 
방법이 떠오르지 않아서 풀이하지 못했다... ㅠ
분할정복은 분할, 정복, 조합의 과정으로 이루어져 있는데 해당 문제는 병합정렬과 같이 다시
조합할 필요가 없으므로 분할, 정복의 과정만 가지면 된다. 그리고 규칙을(가운데는 n/3 * n/3 크기의 공백,
나머지는 n/3으로 채우기) 찾았으므로 이를 사용해서 9등분으로 분할하고, 분할을 더이상 못한다면
정복(해당 위치에 별을 채우든 공백을 채우든)하는 방법을 생각하자!!

문제의 규칙은 한 block에서 가운데 부분은 공백이라는 것이다.
예를 들어 N = 3일 때, 2차원 배열이 선언되었다고 가정하고 공백은 arr[1][1]이다.
이는 (0,0), (0,1), (0,2), (1,0) 까지 별을 출력하다가 별 출력이 4번 이루어지면
그다음 블럭은 반드시 공백이라는 것이다.

이를 사용해서 재귀적으로 풀면 N = 27일 때 우선 9개의 블럭으로 구분한다.
그리고 공백인 구간을 만족한다면(5번째) 그 구간은 공백으로 채우고 
공백 구간이 아닌 블럭은 재귀호출을 하면 된다.

그러면 N = 9 일 때로 넘어갈 것이고, 또 앞선 함수와 같이 9개의 블럭으로 나누고
공백 구간은 공백 문자로 채우고 공백이 아닌 구간을 다시 재귀 호출을 하는 것이다.

그러면 N = 3 일 때로 넘어갈 것이고, 위와 같은 과정을 반복하면 결국 N = 1 일 때가 온다.
여기서 더 못 쪼깨기 때문에 해당 구역의 배열을 공백 또는 별로 채우면 되는 것이다.

https://st-lab.tistory.com/95

"""
def solution1():
    N = int(input())

    # 별을 저장하기 위한 2차원 리스트
    graph = [[0] * N for _ in range(N)]

    def star(x, y, n, blank):
        # 공백칸이라면(정복)
        if blank:
            for i in range(x, x + n):
                for j in range(y, y + n):
                    graph[i][j] = ' '
            
            return
        
        # 더이상 쪼갤 수 없는 블록일 때(정복)
        if n == 1:
            graph[x][y] = '*'
            return
        
        """
        N = 27 일 경우 한 블록의 사이즈는 9이고,
        N = 9 일 경우 한 블록의 사이즈는 3이듯
        해당 블록의 한 칸을 담을 변수를 의미 size
        
        count는 별 출력 누적 합을 의미하는 변수
        """
        
        size = n // 3
        count = 0
        
        # 9칸으로 구성(분할)
        for i in range(x, x + n, size):
            for j in range(y, y + n, size):
                count += 1
                if count == 5: # 공백 칸일 경우
                    star(i, j, size, True)
                else:
                    star(i, j, size, False)
                    
    star(0, 0, N, False)

    for values in graph:
        for value in values:
            print(value, end="")
        print()

# https://cotak.tistory.com/38

"""
해당 방법은 정답으로 나오는 구간을 3등분한 후, 재귀를 통해서 이를 더해나가는 과정이다.
예를 들어 3이 들어온다면 ['*']을 리턴받은 후 윗 줄은 이를 3 곱한 '***',
아랫 줄은 이를 한번 더하고, LEN // 3 만큼의 공백, 그리고 다시 한번 더한 '* *',
마지막 줄은 이를 3 곱한 '***' 이 리턴된다.

9가 들어온다면 재귀호출되서 LEN이 3에 해당하는 ['***', '* *', '***']의 값을 사용해서
위와 같은 과정을 똑같이 수행하면 된다.

"""

def solution3():
    import sys
    sys.setrecursionlimit(10**6)
    
    def append_star(LEN):
        if LEN == 1:
            return ['*']
        
        stars = append_star(LEN // 3)
        L = []
        
        # 윗줄
        for s in stars:
            L.append(s*3)
        # 중간줄
        for s in stars:
            L.append(s + ' ' * (LEN // 3) + s)
        # 마지막 줄
        for s in stars:
            L.append(s * 3)
        return L
    
    n = int(sys.stdin.readline().strip())
    print('\n'.join(append_star(n)))
    
solution3()