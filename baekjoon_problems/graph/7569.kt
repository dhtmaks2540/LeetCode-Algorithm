import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine(), " ")
    val m = st.nextToken().toInt()
    val n = st.nextToken().toInt()
    val h = st.nextToken().toInt()

    val graph = Array(h) { Array(n) { IntArray(m) } }
    repeat(h) { i ->
        repeat(n) { j ->
            st = StringTokenizer(readLine(), " ")
            repeat(m) { k ->
                graph[i][j][k] = st.nextToken().toInt()
            }
        }
    }

    val dxyz = arrayOf(Triple(0,0,-1),Triple(0,0,1),Triple(0,1,0),Triple(0,-1,0),Triple(1,0,0),Triple(-1,0,0))
    var answer = 0
    val queue = ArrayDeque<Triple<Int,Int,Int>>()

    repeat(h) { i ->
        repeat(n) { j ->
            repeat(m) { k ->
                if(graph[i][j][k] == 1)
                    queue.add(Triple(i, j, k))
            }
        }
    }

    while(queue.isNotEmpty()) {
        for(i in queue.indices) {
            val triple = queue.pollFirst()
            val nowX = triple.first
            val nowY = triple.second
            val nowZ = triple.third

            for(index in dxyz.indices) {
                val nextX = dxyz[index].first + nowX
                val nextY = dxyz[index].second + nowY
                val nextZ = dxyz[index].third + nowZ

                if(nextX in 0 until h && nextY in 0 until n && nextZ in 0 until m) {
                    if(graph[nextX][nextY][nextZ] == 0) {
                        graph[nextX][nextY][nextZ] = 1
                        queue.add(Triple(nextX, nextY, nextZ))
                    }
                }
            }
        }

        answer++
    }

    if(checkRipe(graph)) {
        println(answer - 1)
    } else {
        println(-1)
    }
}

private fun checkRipe(graph: Array<Array<IntArray>>): Boolean {
    for(i in graph.indices) {
        for(j in graph[0].indices) {
            for(k in graph[0][0].indices) {
                if(graph[i][j][k] == 0)
                    return false
            }
        }
    }

    return true
}