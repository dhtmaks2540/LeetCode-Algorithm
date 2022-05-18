import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (R, C) = br.readLine().split(" ").map { it.toInt() }
    val graph = Array(R) { CharArray(C) }
    repeat(R) {
        graph[it] = br.readLine().toCharArray()
    }

    val moveDxy = arrayOf(Pair(-1, 0), Pair(1, 0), Pair(0, -1), Pair(0, 1))

    var answer = 0
    val visited = BooleanArray(26)
    visited[graph[0][0] - 'A'] = true

    fun dfs(row: Int, col: Int, cnt: Int) {
        answer = maxOf(answer, cnt)

        for(i in 0 until 4) {
            val nextRow = row + moveDxy[i].first
            val nextCol = col + moveDxy[i].second

            if(nextRow in 0 until R && nextCol in 0 until C
                && !visited[graph[nextRow][nextCol] - 'A']) {
                visited[graph[nextRow][nextCol] - 'A'] = true
                dfs(nextRow, nextCol, cnt + 1)
                visited[graph[nextRow][nextCol] - 'A'] = false
            }
        }
    }

    dfs(0, 0, 1)
    print(answer)
}