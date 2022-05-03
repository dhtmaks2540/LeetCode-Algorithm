import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.collections.ArrayList

private lateinit var graph: Array<CharArray>
private lateinit var answer: ArrayList<String>

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    graph = Array(n) { br.readLine().toCharArray() }
    answer = ArrayList()

    divideAndConquer(0, 0, n)

    for(value in answer) {
        print(value)
    }
}

private fun checkColor(x: Int, y: Int, size: Int): Boolean {
    val nowColor = graph[x][y]

    for(i in 0 until size) {
        for(j in 0 until size) {
            if(nowColor != graph[i + x][j + y])
                return false
        }
    }
    return true
}

private fun divideAndConquer(x: Int, y: Int, size: Int) {
    if(checkColor(x, y, size)) {
        when(graph[x][y]) {
            '1' -> answer.add("1")
            '0' -> answer.add("0")
        }
        return
    }

    val newSize = size / 2

    // 분할 시작
    answer.add("(")

    divideAndConquer(x, y, newSize)
    divideAndConquer(x, y + newSize, newSize)

    divideAndConquer(x + newSize, y, newSize)
    divideAndConquer(x + newSize, y + newSize, newSize)

    // 분할 끝
    answer.add(")")
}