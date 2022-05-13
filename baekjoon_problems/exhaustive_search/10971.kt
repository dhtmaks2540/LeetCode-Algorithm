import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.math.min

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val graph = Array<Array<Int>>(n) { Array(n) { 0 } }
    for(i in 0 until n) {
        val st = StringTokenizer(br.readLine(), " ")
        for(j in 0 until n) {
            graph[i][j] = st.nextToken().toInt()
        }
    }
    val visited = Array<Boolean> (n) { false }

    var minPrice = Int.MAX_VALUE

    fun dfs(start: Int, y: Int, sumPrice: Int, cnt: Int) {
        if(cnt == n && start == y) {
            minPrice = min(minPrice, sumPrice)
            return
        }

        var tempPrice = sumPrice

        for(x in 0 until n) {
            if(graph[y][x] == 0) continue

            if(!visited[y]) {
                visited[y] = true
                tempPrice += graph[y][x]

                if(tempPrice <= minPrice) {
                    dfs(start, x, tempPrice, cnt + 1)
                }

                visited[y] = false
                tempPrice -= graph[y][x]
            }
        }
    }

    for(i in 0 until n) {
        dfs(i, i, 0, 0)
    }

    if(minPrice == Int.MAX_VALUE) println(0)
    else println(minPrice)
}