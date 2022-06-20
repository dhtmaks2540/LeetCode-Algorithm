import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val st = StringTokenizer(readLine(), " ")
    val n = st.nextToken().toInt()
    val k = st.nextToken().toInt()
    val queue = ArrayDeque<Int>()
    val answer = IntArray(n)

    for(i in 1..n) {
        queue.add(i)
    }

    var cnt = 0
    var index = 0
    while(queue.isNotEmpty()) {
        cnt++

        if(cnt == k) {
            cnt = 0
            answer[index++] = queue.pollFirst()
        } else {
            queue.add(queue.pollFirst())
        }
    }

    println(answer.joinToString(prefix = "<", postfix = ">", separator = ", "))
}