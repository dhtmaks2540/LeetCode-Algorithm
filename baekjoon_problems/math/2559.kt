import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.math.max

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine(), " ")
    val n = st.nextToken().toInt()
    val k = st.nextToken().toInt()

    val array = IntArray(n)
    st = StringTokenizer(readLine(), " ")
    repeat(n) { index ->
        array[index] = st.nextToken().toInt()
    }

    val prefixSum = IntArray(n + 1)
    var sumValue = 0
    var maxSum = Int.MIN_VALUE

    repeat(n) { index ->
        sumValue += array[index]
        prefixSum[index + 1] = sumValue
    }

    for(i in k..n) {
        maxSum = max(maxSum, prefixSum[i] - prefixSum[i - k])
    }

    println(maxSum)
}
