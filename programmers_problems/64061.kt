import java.util.*

class Solution {
    fun solution(board: Array<IntArray>, moves: IntArray): Int {
        var answer = 0

        val lenRow = board.size
        val basket = Stack<Int>()

        for(move in moves) {
            for(row in 0 until lenRow) {
                if(board[row][move - 1] != 0) {
                    if(basket.isNotEmpty() && basket.lastElement() == board[row][move - 1]) {
                        basket.pop()
                        answer += 2
                    } else {
                        basket.add(board[row][move - 1])
                    }

                    board[row][move - 1] = 0
                    break
                }
            }
        }

        return answer
    }
}