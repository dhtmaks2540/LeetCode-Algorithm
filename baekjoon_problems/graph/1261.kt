import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (M, N) = br.readLine().split(" ").map { it.toInt() }
    val graph = Array(N) { IntArray(M) }

    repeat(N) { idx ->
        val line = br.readLine()
        line.forEachIndexed { index, char ->
            graph[idx][index] = char.toString().toInt()
        }
    }

    val visited = Array(N) { Array(M) { false } }
    val directionXY = arrayListOf(Pair(-1, 0), Pair(1, 0), Pair(0, -1), Pair(0, 1))

    val comp = { a: Int, b: Int ->
        when {
            a < b -> -1
            a > b -> 1
            else -> 0
        }
    }

    val priorityQueue = PriorityQueue<Triple<Int, Int, Int>> { a, b ->
        if(a.first != b.first) {
            comp(a.first, b.first)
        } else {
            if(a.second != b.second) {
                comp(a.second, b.second)
            } else {
                comp(a.third, b.third)
            }
        }
    }

    visited[0][0] = true
    priorityQueue.add(Triple(0, 0, 0))

    while(priorityQueue.isNotEmpty()) {
        val (cnt, row, col) = priorityQueue.poll()

        for(i in 0 until 4) {
            val nextRow = row + directionXY[i].first
            val nextCol = col + directionXY[i].second

            if(nextRow in 0 until N && nextCol in 0 until M && !visited[nextRow][nextCol]) {
                visited[nextRow][nextCol] = true
                if(graph[nextRow][nextCol] == 1) graph[nextRow][nextCol] = cnt + 1
                else graph[nextRow][nextCol] = cnt

                priorityQueue.add((Triple(graph[nextRow][nextCol], nextRow, nextCol)))
            }
        }
    }

    println(graph[N - 1][M - 1])
}