import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toLong()
    val k = readLine().toInt()

    var left = 1L
    var right = k.toLong()

    while(left < right) {
        val mid = left + (right - left) / 2
        var count = 0L

        for(i in 1..n) {
            count += min(mid / i, n)
        }

        if(k <= count) {
            right = mid
        } else {
            left = mid + 1
        }
    }

    println(left)
}