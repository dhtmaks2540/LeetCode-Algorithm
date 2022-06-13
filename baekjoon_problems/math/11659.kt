import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine(), " ")
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()

    val array = IntArray(n)
    st = StringTokenizer(readLine(), " ")
    repeat(n) { index ->
        array[index] = st.nextToken().toInt()
    }

    val prefixSum = IntArray(n + 1)
    var sumValue = 0

    for(i in 0 until n) {
        sumValue += array[i]
        prefixSum[i + 1] = sumValue
    }

    val sb = StringBuilder()

    for(i in 0 until m) {
        st = StringTokenizer(readLine(), " ")
        val i = st.nextToken().toInt()
        val j = st.nextToken().toInt()
        sb.append(prefixSum[j] - prefixSum[i - 1]).append("\n")
    }

    println(sb)
}