import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val t = readLine().toInt()
    val sb = StringBuilder()

    repeat(t) { _ ->
        var st = StringTokenizer(readLine(), " ")
        val n = st.nextToken().toInt()
        val m = st.nextToken().toInt()

        val array = IntArray(n)
        st = StringTokenizer(readLine(), " ")

        for(i in 0 until n) {
            array[i] = st.nextToken().toInt()
        }

        val queue = ArrayDeque<IntArray>()
        val importanceArray = array.sortedArrayDescending()

        for(index in array.indices) {
            queue.add(intArrayOf(array[index], index))
        }

        var cnt = 0
        var index = 0

        while(queue.isNotEmpty()) {
            if(queue.peekFirst()[0] == importanceArray[index]) {
                cnt++
                index++
                val now = queue.pollFirst()

                if(now[1] == m) {
                    sb.append("$cnt\n")
                    break
                }
            } else
                queue.add(queue.pollFirst())
        }
    }

    println(sb.toString())
}