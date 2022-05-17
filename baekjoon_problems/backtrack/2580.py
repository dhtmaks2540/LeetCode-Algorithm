"""
스도쿠판을 완성해서 출력하라

https://st-lab.tistory.com/119

백트래킹을 사용해 DFS를 기본적으로 사용하며 현재 숫자를 넣어도 될 경우 넣고 종료 조건으로는
행과 열이 모두 채워졌을경우 출력하도록 하였다. 수도쿠의 조건에 부합하는지는 코드를 잘 짰지만
백트래킹 코드 부분을 잘못짰는지 계속해서 오류가 났다... 또한 이 문제는 N-Queen과 굉장히 유사한 문제로
N-Queen 또한 이 문제와 마찬가지로 한 칸에 퀸을 놓고 유망하다면(놓아도 상관없다면) 다음 칸에 놓는다.
백트래킹은 기본적으로 이러한 방식으로 문제를 푼다!

이 문제에서 틀린 부분은 유망한지 판단한 후 유망하지 않다면 다시 반환하는 방식으로 풀이를 해야하는데
그 코드를 작성하지 않아서 계속해서 오류가 난듯하다. 즉, solution1()의 67, 68번째 줄을 작성하지 않아서
오류가 났다. 백트래킹은 조건에 부합하지 않는 경우 돌아가는 방식으로 풀이를 꼭 해야한다!
"""

def solution():
    import sys

    graph = []
    for i in range(9):
        graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))

    # 해당 칸에 숫자를 넣었을 경우 수도쿠의 조건에 부합하는지
    def check(y, x, num):
        # 가로로 체크
        for index in range(9):
            if graph[y][index] == num:
                return False
            
        # 세로로 체크
        for index in range(9):
            if graph[index][x] == num:
                return False
            
        # 정사각형 체크
        for i in range((y // 3) * 3, (y // 3) * 3 + 3):
            for j in range((x // 3) * 3, (x // 3) * 3 + 3):
                if graph[i][j] == num:
                    return False
                
        return True

    def dfs_sudoku(row, col):
        # 행이 다 채워졌을 경우 다음 행의 첫 번째 열부터 시작
        if col == 9:
            dfs_sudoku(row + 1, 0)
            return
        
        # 행과 열이 모두 채워졌을 경우 출력 후 종료
        if row == 9:
            for i in range(9):
                for j in range(9):
                    print(graph[i][j], end=" ")
                print()
            
            exit()
            
        # 해당 위치의 값이 0이라면 1에서 9까지의 수 중 가능한 수 탐색
        if graph[row][col] == 0:
            for i in range(1, 10):
                # 중복되지 않는지 검사
                if check(row, col, i):
                    graph[row][col] = i
                    # 다음 열 확인
                    dfs_sudoku(row, col + 1)
            
            # 현재 넣은 값이 중복된다면 값 원상복구 후 return    
            graph[row][col] = 0
            return
        
        # 현재 위치의 값이 0이 아닌 경우
        dfs_sudoku(row, col + 1)
        
    dfs_sudoku(0, 0)
    
def solution2():
    import sys

    graph = [[0] * 9 for _ in range(9)]
    zero_index = []
    for i in range(9):
        data = list(map(int, sys.stdin.readline().strip().split(" ")))
        for j in range(9):
            graph[i][j] = data[j]
            if graph[i][j] == 0:
                zero_index.append((i, j))

    # 해당 칸에 숫자를 넣었을 경우 수도쿠의 조건에 부합하는지
    def check(row, col, num):
        # 가로로 체크
        for index in range(9):
            if graph[row][index] == num:
                return False
            
        # 세로로 체크
        for index in range(9):
            if graph[index][col] == num:
                return False
            
        # 정사각형 체크
        for i in range((row // 3) * 3, (row // 3) * 3 + 3):
            for j in range((col // 3) * 3, (col // 3) * 3 + 3):
                if graph[i][j] == num:
                    return False
                
        return True
    
    def dfs_sudoku(index, cnt):
        if cnt == len(zero_index):
            for i in range(9):
                for j in range(9):
                    print(graph[i][j], end=" ")
                print()
                
        for i in range(index, len(zero_index)):
            row, col = zero_index[i]
            for j in range(1, 10):
                if check(row, col, j):
                    graph[row][col] = j
                    dfs_sudoku(index + 1, cnt + 1)
                    
            graph[row][col] = 0
            return
        
    dfs_sudoku(0, 0)
    
solution2()