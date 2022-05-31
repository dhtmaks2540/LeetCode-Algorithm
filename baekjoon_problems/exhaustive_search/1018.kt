import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

private var minCnt = Int.MAX_VALUE

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    fun find(x: Int, y: Int, graph: Array<BooleanArray>) {
        val endX = x + 8
        val endY = y + 8
        var cnt = 0

        var color = graph[x][y]

        for(i in x until endX) {
            for(j in y until endY) {
                if(graph[i][j] != color) cnt++

                color = !color
            }
            color = !color
        }

        cnt = min(cnt, 64 - cnt)
        minCnt = min(cnt, minCnt)
    }

    val (N, M) = readLine().split(" ").map { it.toInt() }
    val graph = Array(N) { BooleanArray(M) { false } }

    for(i in 0 until N) {
        val data = readLine().toCharArray()
        for(j in 0 until M) {
            graph[i][j] = data[j] == 'W'
        }
    }

    val nRow = N - 7
    val mCol = M - 7

    for(i in 0 until nRow) {
        for(j in 0 until mCol) {
            find(i, j, graph)
        }
    }

    println(minCnt)
}