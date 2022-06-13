import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val s = readLine()
    val values = IntArray(26)
    val prefixSum = Array(s.length + 1) { IntArray(26) }

    for(i in s.indices) {
        values[s[i] - 'a'] += 1
        prefixSum[i + 1] = values.copyOf()
    }

    val q = readLine().toInt()
    val sb = StringBuilder()

    repeat(q) { _ ->
        val st = StringTokenizer(readLine(), " ")
        val ch = st.nextToken().single()
        val start = st.nextToken().toInt()
        val end = st.nextToken().toInt()

        sb.append(prefixSum[end + 1][ch - 'a'] - prefixSum[start][ch - 'a']).append("\n")
    }

    println(sb)
}
