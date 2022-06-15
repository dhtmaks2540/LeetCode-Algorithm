import kotlin.math.abs

class Solution2 {
    fun solution(numbers: IntArray, hand: String): String {
        val answer = StringBuilder()
        
        val keyMap = hashMapOf(
            '1' to Pair(0, 0), '2' to Pair(0, 1), '3' to Pair(0, 2),
            '4' to Pair(1, 0), '5' to Pair(1, 1), '6' to Pair(1, 2),
            '7' to Pair(2, 0), '8' to Pair(2, 1), '9' to Pair(2, 2),
            '*' to Pair(3, 0), '0' to Pair(3, 1), '#' to Pair(3, 2)
        )
        
        val left = intArrayOf(1,4,7)
        val right = intArrayOf(3,6,9)
        var lhand = '*'
        var rhand = '#'
        
        for(num in numbers) {
            if(num in left) {
                answer.append('L')
                lhand = num.digitToChar()
            } else if(num in right) {
                answer.append('R')
                rhand = num.digitToChar()
            } else {
                val curPos = keyMap[num.digitToChar()]
                val lPos = keyMap[lhand]
                val rPos = keyMap[rhand]
                val lDist = abs(curPos!!.first - lPos!!.first) + abs(curPos.second - lPos.second)
                val rDist = abs(curPos.first - rPos!!.first) + abs(curPos.second - rPos.second)

                if(lDist < rDist) {
                    answer.append('L')
                    lhand = num.digitToChar()
                } else if(lDist > rDist) {
                    answer.append('R')
                    rhand = num.digitToChar()
                } else {
                    if(hand == "left") {
                        answer.append('L')
                        lhand = num.digitToChar()
                    } else {
                        answer.append('R')
                        rhand = num.digitToChar()
                    }
                }
            }
        }
        
        return answer.toString()
    }
}