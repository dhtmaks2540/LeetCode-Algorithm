import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.StringBuilder

private lateinit var graph: Array<Array<Char>>

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    graph = Array(n) { Array(n) { ' ' } }

    fun star(x: Int, y: Int, n: Int, blank: Boolean) {
        if(blank) {
            for(i in x until x + n) {
                for(j in y until y + n) {
                    graph[i][j] = ' '
                }
            }
            return
        }

        if(n == 1) {
            graph[x][y] = '*'
            return
        }

        val size = n / 3
        var count = 0

        for(i in x until x + n step size) {
            for(j in y until y + n step size) {
                count++
                if(count == 5) {
                    star(i, j, size, true)
                } else {
                    star(i, j, size, false)
                }
            }
        }
    }

    star(0, 0, n, false)

    val sb = StringBuilder()
    for(i in 0 until n) {
        for(j in 0 until n) {
            sb.append(graph[i][j])
        }
        sb.append('\n')
    }
    print(sb)
}