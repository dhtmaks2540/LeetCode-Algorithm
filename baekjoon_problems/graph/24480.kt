import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.collections.ArrayList

private var cnt = 0

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine(), " ")
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()
    val r = st.nextToken().toInt()

    val array = Array(n + 1) { ArrayList<Int>() }

    repeat(m) { _ ->
        st = StringTokenizer(readLine(), " ")
        val start = st.nextToken().toInt()
        val end = st.nextToken().toInt()
        array[start].add(end)
        array[end].add(start)
    }

    for(i in 1..n)
        array[i].sortDescending()

    val answer = IntArray(n + 1) { - 1 }
    val visited = BooleanArray(n + 1)

    fun dfs(node: Int) {
        answer[node] = cnt
        visited[node] = true
        cnt++

        for(nextNode in array[node]) {
            if(!visited[nextNode])
                dfs(nextNode)
        }
    }

    dfs(r)

    val sb = StringBuilder()

    for(num in 1..n) {
        if(answer[num] == -1)
            sb.append("0\n")
        else
            sb.append("${answer[num] + 1}\n")
    }

    println(sb.toString())
}