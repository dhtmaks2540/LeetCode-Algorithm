import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.math.max

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val array = Array(n) { IntArray(2) }
    repeat(n) { row ->
        val st = StringTokenizer(readLine(), " ")
        repeat(2) { col ->
            array[row][col] = st.nextToken().toInt()
        }
    }

    array.sortWith(compareBy { o1 ->
        o1[0]
    })

    val dp = IntArray(n)

    for(i in 0 until n) {
        dp[i] = 1
        for(j in 0 until i) {
            if(array[i][1] > array[j][1])
                dp[i] = max(dp[i], dp[j] + 1)
        }
    }

    println(n - dp.maxOrNull()!!)
}