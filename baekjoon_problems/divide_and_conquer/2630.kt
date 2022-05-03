import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

var blueColors = 0
var whiteColors = 0

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

    divideAndConquer(0, 0, n, graph)
    println(whiteColors)
    println(blueColors)
}

fun checkColor(x: Int, y: Int, size: Int, graph: Array<Array<Int>>): Boolean {
    val newColor = graph[x][y]

    for(i in 0 until size) {
        for(j in 0 until size) {
            if(graph[i + x][j + y] != newColor) {
                return false
            }
        }
    }

    return true
}

fun divideAndConquer(x: Int, y: Int, size: Int, graph: Array<Array<Int>>) {
    if(checkColor(x, y, size, graph)) {
        when(graph[x][y]) {
            1 -> blueColors++
            0 -> whiteColors++
        }
        return
    }

    val newSize = size / 2

    // 4등분으로 분할
    divideAndConquer(x, y, newSize, graph)
    divideAndConquer(x, y + newSize, newSize, graph)

    divideAndConquer(x + newSize, y, newSize, graph)
    divideAndConquer(x + newSize, y + newSize, newSize, graph)
}