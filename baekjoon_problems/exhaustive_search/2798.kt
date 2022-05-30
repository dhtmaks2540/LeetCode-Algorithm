package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val array = Array(n) { 0 }
    val st = StringTokenizer(readLine(), " ")
    repeat(n) { index ->
        array[index] = st.nextToken().toInt()
    }

    var minDiff = Int.MAX_VALUE
    var answer = 0

    for(i in 0 until n) {
        for(j in i + 1 until n) {
            for(k in j + 1 until n) {
                val sumValue = array[i] + array[j] + array[k]
                if(sumValue <= m && m - sumValue < minDiff) {
                    minDiff = m - sumValue
                    answer = sumValue
                }
            }
        }
    }

    println(answer)
}