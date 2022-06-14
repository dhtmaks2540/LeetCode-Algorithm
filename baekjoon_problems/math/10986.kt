import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine(), " ")
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()

    val modCnt = LongArray(m)
    var sumValue = 0

    st = StringTokenizer(readLine(), " ")

    repeat(n) { _ ->
        sumValue = (sumValue + st.nextToken().toInt()) % m
        modCnt[sumValue]++
    }

    var answer = modCnt[0]
    repeat(m) { index ->
        answer += (modCnt[index] * (modCnt[index] - 1)) / 2
    }

    println(answer)
}