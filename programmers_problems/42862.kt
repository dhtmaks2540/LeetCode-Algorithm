class Solution {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        val lostCheck = BooleanArray(n + 1)
        val reserveCheck = BooleanArray(n + 1)

        lost.forEach { num ->
            lostCheck[num] = true
        }

        reserve.forEach { num ->
            reserveCheck[num] = true
            if(reserveCheck[num] && lostCheck[num]) {
                reserveCheck[num] = false
                lostCheck[num] = false
            }
        }

        for(i in 1..n) {
            if(reserveCheck[i]) {
                if(i - 1 in 1..n && lostCheck[i - 1])
                    lostCheck[i - 1] = false
                else if(i + 1 in 1..n && lostCheck[i + 1])
                    lostCheck[i + 1] = false
            }
        }

        var answer = n

        for(i in 1..n) {
            if(lostCheck[i])
                answer--
        }

        return answer
    }
}