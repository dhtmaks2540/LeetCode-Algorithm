import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.math.sqrt

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = 9999
    val array = Array(n + 1) { true }

    for(i in 2..(sqrt(n.toDouble()).toInt())) {
        if(array[i]) {
            var j = 2
            while(i * j <= n) {
                array[i * j] = false
                j++
            }
        }
    }

    fun toInt(values: CharArray): Int {
        var ret = 0
        for(value in values) {
            ret = ret * 10 + Character.getNumericValue(value)
        }

        return ret
    }

    fun bfs(visited: Array<Int>, start: Int) {
        val queue = ArrayDeque<Int>()
        queue.add(start)
        visited[start] = 0

        while(queue.isNotEmpty()) {
            val now = queue.pollFirst()

            for(i in 0 until 4) {
                val listNow = now.toString().toCharArray()

                for(j in 0..9) {
                    listNow[i] = Character.forDigit(j ,10)
                    val next = toInt(listNow)
                    if(next >= 1000 && array[next] && visited[next] == -1) {
                        visited[next] = visited[now] + 1
                        queue.add(next)
                    }
                }
            }
        }
    }

    val t = br.readLine().toInt()
    for(i in 0 until t) {
        val visited = Array(n + 1) { -1 }
        val (startNum, endNum) = br.readLine().split(" ").map { it.toInt() }
        bfs(visited, startNum)

        if(visited[endNum] != -1) println(visited[endNum])
        else println("Impossible")
    }
}