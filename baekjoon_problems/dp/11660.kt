import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine(), " ")
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()

    val graph = Array(n) { LongArray(n) }
    val dp = Array(n + 1) { LongArray(n + 1) }

    for(i in 0 until n) {
        st = StringTokenizer(readLine(), " ")
        for(j in 0 until n) {
            graph[i][j] = st.nextToken().toLong()
        }
    }

    for(i in 1..n) {
        for(j in 1..n) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + graph[i - 1][j - 1]
        }
    }

    val sb = StringBuilder()

    repeat(m) { _ ->
        st = StringTokenizer(readLine(), " ")
        val x1 = st.nextToken().toInt()
        val y1 = st.nextToken().toInt()
        val x2 = st.nextToken().toInt()
        val y2 = st.nextToken().toInt()
        sb.append("${dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]}\n")
    }

    println(sb)
}