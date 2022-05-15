import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))

    fun bfs(start: Int, target: Int, visited: Array<Boolean>): String {
        val queue = ArrayDeque<Pair<Int, String>>()
        queue.add(Pair(start, ""))
        visited[start] = true

        while(queue.isNotEmpty()) {
            val (now, path) = queue.pollFirst()

            if(now == target)
                return path

            val dResult = (now * 2) % 10000
            if(!visited[dResult]) {
                visited[dResult] = true
                queue.add(Pair(dResult, path + 'D'))
            }

            val sResult = if(now - 1 < 0) 9999 else now - 1
            if(!visited[sResult]) {
                visited[sResult] = true
                queue.add(Pair(sResult, path + 'S'))
            }

            val lResult = (now % 1000) * 10 + (now / 1000)
            if(!visited[lResult]) {
                visited[lResult] = true
                queue.add(Pair(lResult, path + 'L'))
            }

            val rResult = (now % 10) * 1000 + (now / 10)
            if(!visited[rResult]) {
                visited[rResult] = true
                queue.add(Pair(rResult, path + 'R'))
            }
        }

        return ""
    }

    val t = br.readLine().toInt()

    for(i in 0 until t) {
        val (startNum, endNum) = br.readLine().split(" ").map { it.toInt() }
        val visited = Array(10000) {false}
        val path = bfs(startNum, endNum, visited)
        println(path)
    }
}