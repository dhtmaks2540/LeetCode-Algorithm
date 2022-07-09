import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.min
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val t = readLine().toInt()
    val sb = StringBuilder()

    repeat(t) { _ ->
        val k = readLine().toInt()
        val sumArray = IntArray(k + 1)
        val dp = Array(k + 1) { IntArray(k + 1) }
        val st = StringTokenizer(readLine(), " ")

        for(i in 1..k) {
            sumArray[i] = sumArray[i - 1] + st.nextToken().toInt()
        }

        for(i in 1..k) {
            for(j in 1..k-i) {
                dp[j][i + j] = Int.MAX_VALUE
                for(k in j until i + j) {
                    dp[j][i + j] = min(dp[j][i + j], dp[j][k] + dp[k + 1][i + j] + sumArray[i + j] - sumArray[j - 1])
                }
            }
        }

        sb.append("${dp[1][k]}\n")
    }

    println(sb.toString())
}