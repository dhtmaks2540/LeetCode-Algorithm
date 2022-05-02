import com.sun.org.apache.xpath.internal.operations.Bool
import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

lateinit var graph: Array<Array<Int>>
lateinit var answer: Array<Int>

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()

    graph = Array<Array<Int>>(n) { Array<Int>(n) { 0 }}
    answer = Array(3) { 0 }

    for(i in 0 until n) {
        val stringTokenizer = StringTokenizer(br.readLine(), " ")
        for(j in 0 until n) {
            graph[i][j] = stringTokenizer.nextToken().toInt()
        }
    }

    divideAndConquer(0, 0, graph.size)
    for(value in answer) {
        println(value)
    }
}

fun divideAndConquer(x: Int, y: Int, size: Int) {
    if(checkNum(x, y, size)) {
        when(graph[x][y]) {
            -1 -> answer[0]++
            0 -> answer[1]++
            1 -> answer[2]++
        }
        return
    }

    val nextSize = size / 3

    divideAndConquer(x, y, nextSize)
    divideAndConquer(x, y + nextSize, nextSize)
    divideAndConquer(x, y + 2 * nextSize, nextSize)

    divideAndConquer(x + nextSize, y, nextSize)
    divideAndConquer(x + nextSize, y + nextSize, nextSize)
    divideAndConquer(x + nextSize, y + 2 * nextSize, nextSize)

    divideAndConquer(x + 2 * nextSize, y, nextSize)
    divideAndConquer(x + 2 * nextSize, y + nextSize, nextSize)
    divideAndConquer(x + 2 * nextSize, y + 2 * nextSize, nextSize)
}

fun checkNum(x: Int, y: Int, size: Int): Boolean {
    val firstNum = graph[x][y]

    for(i in 0 until size) {
        for(j in 0 until size) {
            if(graph[i + x][j + y] != firstNum) return false
        }
    }

    return true
}