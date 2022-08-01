import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.collections.ArrayList

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine(), " ")
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()
    val r = st.nextToken().toInt()

    val graph = Array<ArrayList<Int>>(n + 1) { ArrayList() }
    repeat(m) { _ ->
        st = StringTokenizer(readLine(), " ")
        val start = st.nextToken().toInt()
        val end = st.nextToken().toInt()
        graph[start].add(end)
        graph[end].add(start)
    }

    repeat(n) { i ->
        graph[i].sort()
    }

    val queue = ArrayDeque<Int>()
    val answer = IntArray(n + 1) { -1 }
    var rank = 1

    answer[r] = rank
    queue.add(r)

    while(queue.isNotEmpty()) {
        val nowNode = queue.pollFirst()

        for(nextNode in graph[nowNode]) {
            if(answer[nextNode] == -1) {
                answer[nextNode] = ++rank
                queue.add(nextNode)
            }
        }
    }

    val sb = StringBuilder()

    for(i in 1..n) {
        if(answer[i] == -1)
            sb.append("0\n")
        else
            sb.append("${answer[i]}\n")
    }

    println(sb.toString())
}