import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.StringBuilder

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val graph = Array(n) { Array (2 * n) { ' '} }

    fun recursive(x: Int, y: Int, size: Int) {
        if(size == 3) {
            graph[x][y] = '*'

            graph[x + 1][y - 1] = '*'
            graph[x + 1][y + 1] = '*'

            for(i in -2 until 3) {
                graph[x + 2][y + i] = '*'
            }
            return
        }

        val nextSize = size / 2

        recursive(x, y, nextSize)
        recursive(x + nextSize, y - nextSize, nextSize)
        recursive(x + nextSize, y + nextSize, nextSize)
    }

    recursive(0, n - 1, n)

    val sb = StringBuilder()

    for(values in graph) {
        for(value in values) {
            sb.append(value)
        }
        sb.append('\n')
    }
    println(sb)
}