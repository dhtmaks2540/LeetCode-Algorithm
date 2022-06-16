"""
사라진 인형의 개수를 구하라

인형이 뽑히면 아래 칸부터 차곡차곡 쌓인다고 하였으므로 스택을 사용해서 이를 구현하면 된다.
따라서 연속되는 경우의 판단은 스택의 최상단에 있는 인형이 현재 뽑으려는 인형과 같은지로
판단하면 된다.

스택에 대한 개념을 아는지 물어보는 문제인듯하다.

"""

def solution(board, moves):
    answer = 0
    
    len_row = len(board)
    
    # 스택의 역할을 수행
    basket = []
    
    for move in moves:
        # 현재 row 순회
        for row in range(len_row):
            # 인형이 있다면
            if board[row][move - 1]:
                # 같은 모양의 인형이 있다면 인형 제거
                if basket and basket[-1] == board[row][move - 1]:
                    basket.pop()
                    answer += 2
                # 그렇지 않다면 바구니에 넣기
                else:
                    basket.append(board[row][move - 1])
            
                # 뽑기 처리
                board[row][move - 1] = 0
                break
                              
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))