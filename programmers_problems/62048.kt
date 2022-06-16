import kotlin.math.max
import kotlin.math.min

class Solution4 {
    fun solution(w: Int, h: Int): Long {
        val wL = w.toLong()
        val hL = h.toLong()

        return (wL * hL) - (wL + hL - gcd(wL, hL))
    }

    // 유클리드 호제법
    private fun gcd(a: Long, b: Long): Long {
        var big = max(a, b)
        var small = min(a, b)
        var remainder = 0L

        while(small != 0L) {
            remainder = big % small
            big = small
            small = remainder
        }

        return big
    }
}