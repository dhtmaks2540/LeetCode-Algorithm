import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.max

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val strA = '0' + readLine()
    val strB = '0' + readLine()

    val dp = Array(1001) { IntArray(1001) }

    for(i in strA.indices) {
        for(j in strB.indices) {
            if(i == 0 || j == 0)
                dp[i][j] = 0
            else if(strA[i] == strB[j])
                dp[i][j] = dp[i - 1][j - 1] + 1
            else
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        }
    }

    println(dp[strA.length - 1][strB.length - 1])
}