import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val t = readLine().toInt()
    val sb = StringBuilder()
    val dxy = arrayOf(Pair(-1, 0), Pair(1, 0), Pair(0, -1), Pair(0, 1))

    fun dfs(graph: Array<IntArray>, m: Int, n: Int, x: Int, y: Int) {
        graph[x][y] = 2

        for(i in 0 until 4) {
            val nextX = x + dxy[i].first
            val nextY = y + dxy[i].second

            if(nextX in 0 until n && nextY in 0 until m && graph[nextX][nextY] == 1)
                dfs(graph, m, n, nextX, nextY)
        }
    }

    repeat(t) { _ ->
        var st = StringTokenizer(readLine(), " ")
        val m = st.nextToken().toInt()
        val n = st.nextToken().toInt()
        val k = st.nextToken().toInt()

        val graph = Array(n) { IntArray(m) }
        repeat(k) { _ ->
            st = StringTokenizer(readLine(), " ")
            val col = st.nextToken().toInt()
            val row = st.nextToken().toInt()
            graph[row][col] = 1
        }

        var answer = 0

        for(x in 0 until n) {
            for(y in 0 until m) {
                if(graph[x][y] == 1) {
                    answer++
                    dfs(graph, m, n, x, y)
                }
            }
        }

        sb.append("$answer\n")
    }

    println(sb.toString())
}